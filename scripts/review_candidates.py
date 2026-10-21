#!/usr/bin/env python3
"""人工审核候选配方。
  python3 scripts/review_candidates.py list [file]
  python3 scripts/review_candidates.py show <id>
  python3 scripts/review_candidates.py approve <id>   # 逐项提示补缺字段后写入 data/recipes.json
  python3 scripts/review_candidates.py reject <id> [原因]"""
from pathlib import Path
import glob, json, os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RECIPES = f"{ROOT}/data/recipes.json"
FIELDS = ["id","category","model","quant","engine","hardware","hardware_family","hardware_cost_text","hardware_cost_usd","metric","tok_s","concurrency","context","launch_command","source_url","source_note","source_level","date"]
def files(): return sorted(glob.glob(f"{ROOT}/data/candidates/*.json"))
def find(cid):
    for f in files():
        d = json.load(open(f))
        for c in d["candidates"]:
            if c["id"] == cid: return f, d, c
    sys.exit(f"未找到 {cid}")
def save(f, d): json.dump(d, open(f, "w"), ensure_ascii=False, indent=1)
def main():
    if len(sys.argv) < 2: sys.exit(__doc__)
    cmd = sys.argv[1]
    if cmd == "list":
        for f in ([sys.argv[2]] if len(sys.argv) > 2 else files()):
            for c in json.load(open(f))["candidates"]:
                print(f"[{c.get('status','pending'):8}] {c['extracted_confidence']:.2f} {c['id']}  tok/s={c['tok_s']}  hw={c['hardware']}  缺:{','.join(c['needs_review'])}")
    elif cmd == "show":
        print(json.dumps(find(sys.argv[2])[2], ensure_ascii=False, indent=1))
    elif cmd == "reject":
        f, d, c = find(sys.argv[2]); c["status"] = "rejected"; c["reject_reason"] = " ".join(sys.argv[3:]) or None; save(f, d); print("已拒绝")
    elif cmd == "approve":
        f, d, c = find(sys.argv[2])
        for line in c["raw_snippet"]: print("  >", line)
        rec = {}
        for k in FIELDS:
            cur = c.get(k)
            v = input(f"{k} [{cur}]: ").strip()
            v = cur if v == "" else (None if v == "-" else v)
            if k in ("tok_s", "hardware_cost_usd") and isinstance(v, str): v = float(v)
            rec[k] = v
        if not rec["hardware"] or not rec["tok_s"]: sys.exit("hardware 和 tok_s 必填，未写入")
        recipes = json.load(open(RECIPES))
        if any(r["id"] == rec["id"] for r in recipes): sys.exit("id 已存在")
        recipes.append(rec); Path(RECIPES).write_text(json.dumps(recipes, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        c["status"] = "approved"; save(f, d); print("已写入 recipes.json")
    else: sys.exit(__doc__)
if __name__ == "__main__": main()
