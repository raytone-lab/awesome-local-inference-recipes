#!/usr/bin/env python3
"""Read-only hardware detection. Prints one JSON object. Stdlib only. Sends nothing over the network."""
import json, os, platform, re, shutil, subprocess, sys

def run(cmd, timeout=15):
    if not shutil.which(cmd[0]): return None
    try: return subprocess.run(cmd, capture_output=True, text=True, timeout=timeout).stdout
    except Exception: return None

def nvidia():
    out = run(['nvidia-smi', '--query-gpu=name,memory.total,driver_version', '--format=csv,noheader,nounits'])
    gpus = []
    for line in (out or '').strip().splitlines():
        p = [x.strip() for x in line.split(',')]
        if len(p) >= 2:
            gpus.append({'vendor': 'nvidia', 'name': p[0], 'vram_gb': round(float(p[1]) / 1024, 1) if p[1].replace('.', '').isdigit() else None,
                         'driver': p[2] if len(p) > 2 else None})
    return gpus

def amd():
    out = run(['rocm-smi', '--showproductname', '--showmeminfo', 'vram', '--json'])
    gpus = []
    try:
        for k, v in json.loads(out or '{}').items():
            if not k.startswith('card'): continue
            name = v.get('Card Series') or v.get('Card SKU') or v.get('Card Model') or 'AMD GPU'
            tot = v.get('VRAM Total Memory (B)')
            gpus.append({'vendor': 'amd', 'name': name, 'vram_gb': round(int(tot) / 2**30, 1) if tot else None})
    except Exception: pass
    return gpus

def linux():
    d = {'os': 'linux'}
    for line in open('/proc/meminfo'):
        if line.startswith('MemTotal'): d['ram_gb'] = round(int(line.split()[1]) / 2**20, 1)
    cpu = run(['lscpu']) or ''
    m = re.search(r'Model name:\s*(.+)', cpu); d['cpu'] = m.group(1).strip() if m else platform.processor()
    d['gpus'] = nvidia() + amd()
    if not d['gpus']:
        pci = run(['lspci']) or ''
        found = [l.split(': ', 1)[-1] for l in pci.splitlines() if re.search(r'VGA|3D controller|Display controller', l)]
        # No vendor tool works: keep NVIDIA and AMD devices as GPUs with unknown VRAM
        d['gpus'] = [{'vendor': 'nvidia' if 'NVIDIA' in n else 'amd', 'name': n, 'vram_gb': None, 'from': 'lspci'}
                     for n in found if re.search(r'NVIDIA|AMD|ATI|Radeon', n)]
        d['gpus_pci_other'] = [n for n in found if not re.search(r'NVIDIA|AMD|ATI|Radeon', n)]
    if os.path.exists('/etc/dgx-release') or 'GB10' in json.dumps(d): d['dgx_spark'] = True
    d['wsl'] = 'microsoft' in platform.release().lower()
    return d

def mac():
    d = {'os': 'macos'}
    d['cpu'] = (run(['sysctl', '-n', 'machdep.cpu.brand_string']) or '').strip()
    mem = (run(['sysctl', '-n', 'hw.memsize']) or '0').strip()
    d['ram_gb'] = round(int(mem) / 2**30, 1) if mem.isdigit() else None
    d['unified_memory'] = 'Apple' in d['cpu'] or platform.machine() == 'arm64'
    sp = run(['system_profiler', 'SPDisplaysDataType', '-json'], 30) or '{}'
    gpus = []
    try:
        for g in json.loads(sp).get('SPDisplaysDataType', []):
            gpus.append({'vendor': 'apple', 'name': g.get('sppci_model'), 'cores': g.get('sppci_cores'),
                         'vram_gb': d['ram_gb'] if d['unified_memory'] else None})
    except Exception: pass
    d['gpus'] = gpus
    d['model'] = (run(['sysctl', '-n', 'hw.model']) or '').strip()
    return d

def windows():
    d = {'os': 'windows'}
    ps = ['powershell', '-NoProfile', '-Command']
    cpu = run(ps + ['(Get-CimInstance Win32_Processor | Select-Object -First 1).Name']) or ''
    d['cpu'] = cpu.strip()
    mem = (run(ps + ['(Get-CimInstance Win32_ComputerSystem).TotalPhysicalMemory']) or '0').strip()
    d['ram_gb'] = round(int(mem) / 2**30, 1) if mem.isdigit() else None
    d['gpus'] = nvidia()
    if not d['gpus']:  # AdapterRAM is capped at 4 GB; use only the name
        names = run(ps + ['Get-CimInstance Win32_VideoController | ForEach-Object { $_.Name }']) or ''
        d['gpus'] = [{'vendor': 'amd' if 'Radeon' in n else 'other', 'name': n.strip(), 'vram_gb': None} for n in names.splitlines() if n.strip()]
    return d

def main():
    s = platform.system()
    d = linux() if s == 'Linux' else mac() if s == 'Darwin' else windows() if s == 'Windows' else {'os': s.lower(), 'gpus': []}
    d['arch'] = platform.machine()
    d['tools'] = {t: bool(shutil.which(t)) for t in ['ollama', 'llama-server', 'vllm', 'docker', 'mlx_lm.generate']}
    d['unified_memory'] = d.get('unified_memory', False)
    text = json.dumps(d, indent=1, ensure_ascii=False) + '\n'
    if len(sys.argv) > 2 and sys.argv[1] == '--out':  # write UTF-8 directly; a shell redirect can change the encoding
        with open(sys.argv[2], 'w', encoding='utf-8') as f: f.write(text)
    sys.stdout.write(text)

if __name__ == '__main__': main()
