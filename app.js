I18N_ADD({
'zh-CN':{title:'配方库 · 本地推理配方',xh1:'什么模型 × 什么硬件 × 什么引擎 = 多快、多贵',xlead:'聚焦 3 万美元以内的本地推理方案。每条数据附来源与可信等级，未知字段一律显示「未见公开数据」。',ph:'搜索模型 / 硬件 / 引擎 / 量化…',allcat:'全部类别',c_text:'文字',c_image:'图像',c_va:'影音',alleng:'全部引擎',allmf:'全部模型系列',allhw:'全部硬件',alllv:'全部来源等级',anymem:'不限内存',f_cat:'类别',f_eng:'引擎',f_mf:'模型系列',f_hw:'硬件',f_mem:'显存/内存 ≤',f_lvl:'来源等级',filters:'筛选',clear:'清除全部',moretags:'更多标签',lesstags:'收起标签',show_n:'显示 {n} 条结果',sortby:'排序',so_fast:'速度最快',so_val:'性价比（$/tok/s）',so_cheap:'硬件最便宜',so_new:'最新',so_model:'模型 A–Z',v_table:'表格',v_cards:'卡片',l_off:'官方',l_mea:'实测',l_rel:'转述',l_cla:'宣称',budget:'预算 ≤',unk:'含成本未知',chh:'tok/s vs 硬件成本（文字模型，两项均已知）',lgh:'说明',lg1:'<b>美元/tok/s</b> = 硬件成本 ÷ 单流 tok/s，越低越划算',lg2:'成本取来源区间下限；多卡按张计价的行不自动折算（显示原文）',lg3:'来源等级：',lg4:'点击任意行查看详情、启动命令和来源；勾选多行可并排对比',lg5:'指标原文、硬件等字段保留来源原文',lg6:'显存/内存从硬件描述中读取（如「RTX 4090 24GB」「2× DGX Spark」）；设置内存筛选时，未写明内存的行不显示。只计显存/统一内存，用于卸载的系统内存不计入；未选硬件类型时，显存与统一内存按同等数值比较',lg7:'独立显卡的价格通常只含显卡；Mac、DGX Spark、迷你主机是整机价格。先用「价格口径」筛选，再按 $/tok/s 排序才是同类比较',f_cb:'价格口径',allcb:'全部价格口径',cb_gpu:'仅显卡（独立显卡）',cb_sys:'整机',kc_gpu:'仅显卡',kc_sys:'整机',al_view:'视图',al_close:'关闭',al_budget:'预算上限',al_tray:'对比栏',al_results:'结果',al_chart:'散点图：tok/s 与硬件成本',th_cat:'类别',th_model:'模型',th_quant:'量化/优化',th_eng:'引擎',th_hw:'硬件',th_metric:'指标原文',th_cost:'成本 $',th_ctx:'上下文',th_src:'来源',xfoot:'数据来自 X / GitHub / Reddit / 价格站整理',xfootd:' · 最新条目 {d}',tags:'标签',st_all:'条配方',st_text:'文字',st_img:'图像',st_va:'影音',st_cmd:'含启动命令',st_mea:'实测',count:'共 {n} 条（总 {t}）',xaxis:'硬件成本（USD，对数）',empty:'当前筛选无可绘制数据',noresult:'没有符合条件的配方。试试放宽筛选？',more:'再显示 {n} 条',d_quant:'量化/优化',d_mf:'模型系列',d_tags:'标签',d_eng:'引擎',d_orig:'原文：',d_hw:'硬件',d_mem:'显存/内存',d_perf:'性能',d_tok:'单流 tok/s',d_conc:'并发',d_ctx:'上下文',d_cost:'硬件成本',d_date:'日期',d_note:'来源说明',d_cmd:'启动命令',d_nocmd:'# 未见公开数据\n# 你跑过这个配置？欢迎提交 PR 补全启动命令',d_src:'来源',d_open:'打开来源 ↗',d_guide:'📘 运行指南',d_fix:'✎ 提交修正 / 补充',d_sup:'已被 {id} 取代',cmp:'对比',cmp_add:'加入对比',cmp_rm:'移出对比',cmp_go:'对比',cmp_h:'配方对比',cmp_copy:'复制链接',cmp_copied:'已复制 ✓',cmp_n:'已选 {n} / 4',cmp_max:'最多对比 4 条',cmp_need:'再选 1 条即可对比',cmp_best:'最佳',cmp_remove:'移除',cmp_note:'★ 只在官方/实测数值之间评选；带 † 的是转述或宣称的数值，不参与评选。价格口径不同（仅显卡 vs 整机）时不评选成本。',cmp_untr:'转述/宣称，未参与评选',pk_h:'🖥️ 我的机器能跑什么？',pk_p:'选择硬件、显存/内存和预算，查看装得下的实测配方，按速度排序。只计显存/统一内存，卸载到系统内存的部分不计入。',pk_open:'打开',pk_close:'收起',pk_fam:'硬件类型',pk_any:'不限',pk_mem:'显存 / 统一内存',pk_bud:'预算',pk_mea:'只看实测',pk_memopt:'≤ {n} GB',pk_anymem:'不限',pk_anybud:'不限',pk_n:'{n} 条匹配，按单流 tok/s 排序',pk_none:'没有匹配的配方。试试放宽内存或预算？',pk_all:'在配方库中按这些条件筛选（{n} 条）→',pk_diff:'配方库里的 {n} 条还会包括已被取代、没有 tok/s 数值或「自称」的行。',pk_note:'按原始 tok/s 排序，各行模型大小不同，小模型和 MoE 模型自然靠前。不选硬件类型时，显存与统一内存按同一数值比较。',pk_off:'另用系统内存卸载',pk_unk:'另有 {n} 条未写明内存，未计入。',pk_det:'详情',af_q:'搜索',af_max:'预算 ≤ ${n}',af_unk:'不含成本未知',af_mem:'≤ {n} GB'},
en:{title:'Explore · Awesome Local Inference Recipes',xh1:'Which model × which hardware × which engine = how fast, how much',xlead:'Local inference setups under $30k. Every row carries a source and a trust level; unknown fields show “no public data”.',ph:'Search model / hardware / engine / quant…',allcat:'All categories',c_text:'Text',c_image:'Image',c_va:'Video & audio',alleng:'All engines',allmf:'All model families',allhw:'All hardware',alllv:'All source levels',anymem:'Any memory',f_cat:'Category',f_eng:'Engine',f_mf:'Model family',f_hw:'Hardware',f_mem:'Memory ≤',f_lvl:'Source level',filters:'Filters',clear:'Clear all',moretags:'More tags',lesstags:'Fewer tags',show_n:'Show {n} results',sortby:'Sort by',so_fast:'Fastest first',so_val:'Best value ($/tok/s)',so_cheap:'Cheapest hardware',so_new:'Newest',so_model:'Model A–Z',v_table:'Table',v_cards:'Cards',l_off:'Official',l_mea:'Measured',l_rel:'Relayed',l_cla:'Claimed',budget:'Budget ≤',unk:'Include unknown cost',chh:'tok/s vs hardware cost (text models with both known)',lgh:'Notes',lg1:'<b>$/tok/s</b> = hardware cost ÷ single-stream tok/s; lower is better value',lg2:'Cost is the low end of the quoted range; per-card prices for multi-GPU rows are not multiplied (original text shown)',lg3:'Source levels: ',lg4:'Click any row for details, launch command and source; tick rows to compare them side by side',lg5:'Text fields are shown in English translation; numbers are unchanged from the source; the original wording is in the linked source',lg6:'Memory is read from the hardware text (e.g. “RTX 4090 24GB”, “2× DGX Spark”); rows that don\'t state it are left out when a memory filter is set. Only GPU / unified memory counts: system RAM used for offload is not included, and VRAM and unified memory are compared as equals unless you pick a hardware type',lg7:'Discrete-card prices are usually the card alone; Mac, DGX Spark and mini-PC prices are the whole machine. Use “Price basis” to rank $/tok/s like-for-like',f_cb:'Price basis',allcb:'Any price basis',cb_gpu:'GPU only (discrete cards)',cb_sys:'Whole system',kc_gpu:'GPU only',kc_sys:'whole system',al_view:'View',al_close:'Close',al_budget:'Budget',al_tray:'Compare tray',al_results:'Results',al_chart:'Scatter plot of tok/s against hardware cost',th_cat:'Type',th_model:'Model',th_quant:'Quant / opt.',th_eng:'Engine',th_hw:'Hardware',th_metric:'Metric',th_cost:'Cost $',th_ctx:'Context',th_src:'Source',xfoot:'Compiled from X / GitHub / Reddit / price sites',xfootd:' · newest entry {d}',tags:'Tags',st_all:'recipes',st_text:'text',st_img:'image',st_va:'video & audio',st_cmd:'with launch command',st_mea:'measured',count:'{n} shown ({t} total)',xaxis:'Hardware cost (USD, log scale)',empty:'Nothing to plot for this filter',noresult:'No recipes match. Try loosening the filters?',more:'Show {n} more',d_quant:'Quant / optimization',d_mf:'Model family',d_tags:'Tags',d_eng:'Engine',d_orig:'',d_hw:'Hardware',d_mem:'Memory',d_perf:'Performance',d_tok:'Single-stream tok/s',d_conc:'Concurrency',d_ctx:'Context',d_cost:'Hardware cost',d_date:'Date',d_note:'Source note',d_cmd:'Launch command',d_nocmd:'# no public data\n# Ran this setup? Send a PR with the launch command',d_src:'Source',d_open:'Open source ↗',d_guide:'📘 How-to guide',d_fix:'✎ Submit a fix / addition',d_sup:'superseded by {id}',cmp:'Compare',cmp_add:'Add to compare',cmp_rm:'Remove from compare',cmp_go:'Compare',cmp_h:'Compare recipes',cmp_copy:'Copy link',cmp_copied:'Copied ✓',cmp_n:'{n} of 4 selected',cmp_max:'You can compare up to 4',cmp_need:'Pick one more to compare',cmp_best:'best',cmp_remove:'Remove',cmp_note:'★ is awarded only among Official / Measured values; values marked † are relayed or claimed and not ranked. Cost isn\'t starred when the price bases differ (GPU only vs whole system).',cmp_untr:'relayed / claimed, not ranked',pk_h:'🖥️ What can my machine run?',pk_p:'Pick your hardware, memory and budget to see measured recipes that fit, fastest first. Only GPU / unified memory is counted; system RAM used for offload is not.',pk_open:'Open picker',pk_close:'Hide',pk_fam:'Hardware family',pk_any:'Any',pk_mem:'VRAM / unified memory',pk_bud:'Budget',pk_mea:'Measured only',pk_memopt:'≤ {n} GB',pk_anymem:'Any',pk_anybud:'Any',pk_n:'{n} matches, ranked by single-stream tok/s',pk_none:'Nothing matches. Try more memory or a higher budget?',pk_all:'Apply these filters in the explorer ({n} rows) →',pk_diff:'The explorer\'s {n} rows can also include superseded rows, rows without a tok/s figure and self-reported numbers.',pk_note:'Ranked by raw tok/s across different models, so small and MoE models rank high. With “Any” hardware, VRAM and unified memory are compared as if equal.',pk_off:'also offloads to system RAM',pk_unk:'{n} more row(s) without stated memory are left out.',pk_det:'Details',af_q:'search',af_max:'budget ≤ ${n}',af_unk:'no unknown cost',af_mem:'≤ {n} GB'},
ja:{title:'エクスプローラー · Awesome Local Inference Recipes',xh1:'どのモデル × どのハードウェア × どのエンジン = どれくらい速く、いくらか',xlead:'3 万ドル未満のローカル推論構成に絞ります。各行に出典と信頼レベルが付き、不明な欄は「公開データなし」と表示します。',ph:'モデル / ハードウェア / エンジン / 量子化を検索…',allcat:'すべてのカテゴリ',c_text:'テキスト',c_image:'画像',c_va:'動画・音声',alleng:'すべてのエンジン',allmf:'すべてのモデル系列',allhw:'すべてのハードウェア',alllv:'すべての出典レベル',anymem:'メモリ指定なし',f_cat:'カテゴリ',f_eng:'エンジン',f_mf:'モデル系列',f_hw:'ハードウェア',f_mem:'VRAM / メモリ ≤',f_lvl:'出典レベル',filters:'フィルタ',clear:'すべてクリア',moretags:'タグをさらに',lesstags:'タグを減らす',show_n:'{n} 件を表示',sortby:'並び替え',so_fast:'速度（速い順）',so_val:'コスパ（$/tok/s）',so_cheap:'価格（安い順）',so_new:'新しい順',so_model:'モデル A–Z',v_table:'表',v_cards:'カード',l_off:'公式',l_mea:'実測',l_rel:'伝聞',l_cla:'主張',budget:'予算 ≤',unk:'コスト不明を含む',chh:'tok/s とハードウェアコスト（両方分かるテキストモデル）',lgh:'凡例',lg1:'<b>$/tok/s</b> = ハードウェアコスト ÷ シングルストリーム tok/s。低いほどコスパが良い',lg2:'コストは出典レンジの下限。マルチ GPU で「1 枚あたり」と書かれた行は自動では掛けません（原文を表示）',lg3:'出典レベル：',lg4:'行をクリックすると詳細・起動コマンド・出典を表示。複数行にチェックを付けると並べて比較できます',lg5:'テキスト欄は英訳で表示。数値は出典のまま。原文はリンク先にあります',lg6:'メモリはハードウェア文言から読み取ります（例：「RTX 4090 24GB」「2× DGX Spark」）。メモリフィルタ指定時、メモリ未記載の行は除外。GPU / 統合メモリのみ。オフロード用システム RAM は含めません。ハードウェア種別未選択時は VRAM と統合メモリを同値として比較',lg7:'単体カード価格は多くの場合カードのみ。Mac、DGX Spark、ミニ PC は本体全体。「価格の基準」で揃えてから $/tok/s を比べてください',f_cb:'価格の基準',allcb:'価格基準は問わない',cb_gpu:'GPU のみ（単体カード）',cb_sys:'システム全体',kc_gpu:'GPU のみ',kc_sys:'システム全体',al_view:'表示',al_close:'閉じる',al_budget:'予算上限',al_tray:'比較トレイ',al_results:'結果',al_chart:'tok/s とハードウェアコストの散布図',th_cat:'カテゴリ',th_model:'モデル',th_quant:'量子化',th_eng:'エンジン',th_hw:'ハードウェア',th_metric:'指標',th_cost:'コスト $',th_ctx:'コンテキスト',th_src:'出典',count:'{n} 件表示（全 {t} 件）',empty:'このフィルタでは描画するデータがありません',noresult:'一致するレシピがありません。フィルタを緩めてください。',more:'さらに {n} 件',tags:'タグ',d_open:'出典を開く ↗',d_hw:'ハードウェア',d_eng:'エンジン',d_quant:'量子化',d_mf:'モデル系列',d_tok:'シングルストリーム tok/s',d_perf:'性能',d_cost:'ハードウェアコスト',d_ctx:'コンテキスト',d_mem:'メモリ',d_conc:'同時実行',d_cmd:'起動コマンド',d_nocmd:'# 公開データなし\n# この構成を実行しましたか？起動コマンドを PR で送ってください',d_src:'出典',d_date:'日付',d_note:'出典メモ',d_tags:'タグ',d_guide:'📘 手順ガイド',d_sup:'{id} に置き換え済み',d_orig:'',d_fix:'✎ 修正 / 追加を送る',cmp:'比較',cmp_add:'比較に追加',cmp_remove:'外す',cmp_rm:'比較から外す',cmp_h:'レシピ比較',cmp_n:'{n} / 4 件選択',cmp_max:'最大 4 件まで比較できます',cmp_need:'もう 1 件選ぶと比較できます',cmp_go:'比較を開く',cmp_copy:'リンクをコピー',cmp_copied:'コピー済み ✓',cmp_best:'最良',cmp_note:'★ は公式 / 実測の値だけを対象に付けます。† は伝聞または主張で、順位付けしません。価格の基準が違う（GPU のみ vs システム全体）ときはコストに星を付けません。',cmp_untr:'伝聞 / 主張（順位付け対象外）',st_all:'レシピ',st_text:'テキスト',st_img:'画像',st_va:'動画・音声',st_mea:'実測',st_cmd:'コマンドあり',xfoot:'X / GitHub / Reddit / 価格サイトから整理',xfootd:' · 最新エントリ {d}',pk_h:'🖥️ このマシンで何が動く？',pk_open:'構成ピッカーを開く',pk_close:'閉じる',pk_bud:'予算',pk_anybud:'予算は問わない',pk_mem:'GPU / 統合メモリ',pk_anymem:'メモリは問わない',pk_memopt:'≤ {n} GB',pk_fam:'ハードウェア系統',pk_any:'系統は問わない',pk_all:'エクスプローラーでこれらのフィルタを適用（{n} 件）→',pk_mea:'実測のみ',pk_off:'システム RAM にもオフロード',pk_unk:'メモリ未記載の行がさらに {n} 件あり、除外しています。',pk_det:'詳細',pk_p:'ハードウェア、メモリ、予算を選ぶと、収まる実測レシピを速度順に表示します。GPU / 統合メモリのみ数え、オフロード用システム RAM は含めません。',pk_n:'{n} 件一致、シングルストリーム tok/s 順',pk_none:'候補がありません。条件を緩めてください。',pk_note:'異なるモデルの生 tok/s で順位付けするため、小さいモデルや MoE が上位になりやすいです。ハードウェアが「問わない」のとき、VRAM と統合メモリは同値として比較します。',pk_diff:'エクスプローラーの {n} 件には、後継あり・tok/s なし・自己申告の行が含まれる場合があります。',af_q:'検索',af_max:'予算 ≤ ${n}',af_mem:'≤ {n} GB',af_unk:'不明コストを除く',xaxis:'ハードウェアコスト（USD、対数）'}
});
applyI18n();
let GUIDES=new Set();const GP=fetch('data/guides.json').then(r=>r.ok?r.json():[]).then(a=>{GUIDES=new Set(a)}).catch(()=>{});
const MET=r=>r.metric;
// Dataset placeholders stay as filter values; only their display text is translated.
const TE=x=>displayValue(x,LANG);
const NA=`<span class="na">${T('na')}</span>`,CAT={text:TC('text'),image:TC('image'),'video-audio':TC('video-audio')};
const esc=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const v=x=>x==null||x===''?NA:esc(x),KC=r=>r.kind?`<small class="kc">${T('kc_'+r.kind)}</small>`:'';let D=[],sk='tok_s',sd=-1;const $=id=>document.getElementById(id);
const LV=['官方','实测','转述','宣称'],MEA='实测',MEMS=[8,12,16,24,32,48,64,96,128,192,256,512],BUDS=[1000,2500,5000,7000,14000,30000];
const REPO='https://github.com/raytone-lab/awesome-local-inference-recipes';
const mobile=matchMedia('(max-width: 860px)');

// Accelerator memory (GB) read from the free-text hardware field; null when it can't be read unambiguously.
// Sums GPU / unified-memory parts joined with " + ", multiplies "N×", skips system RAM / CPU / disk parts; comparisons ("A / B", "A vs B") stay unknown.
const KNOWN=[[/RTX\s*5090/i,32],[/RTX\s*4090/i,24],[/RTX\s*3090/i,24],[/RTX\s*(5080|4080)/i,16],[/RTX\s*3060/i,12],[/7900\s*XTX/i,24],[/R9700/i,32],[/DGX Spark|GB10|AI TOP ATOM/i,128],[/RTX PRO 6000/i,96]];
function memGB(h){if(!h||/\s\/|\/\s|\svs\s/i.test(h))return null;
 let t=h.replace(/[（(][^）)]*[）)]/g,' '),sum=0,ok=false;
 for(const p of t.split(/\s\+/)){if(/RAM|DDR|内存|NVMe|SSD|Ryzen|Intel|i[579]-|\bTR\b|Threadripper|iGPU|Windows|^\s*[\d.]+\s*GB\s*$/i.test(p))continue;
  const n=+(p.match(/(\d+)\s*×/)||[])[1]||1,g=p.match(/(\d+(?:\.\d+)?)\s*G(?:B|iB)?(?![A-Za-z0-9])/);let x=g?+g[1]:null;
  if(x==null&&!/笔记本|Laptop/i.test(p))for(const [re,gb] of KNOWN)if(re.test(p)){x=gb;break}
  if(x==null)return null;sum+=n*x;ok=true}
 return ok?sum:null}

fetch('data/recipes.json').then(r=>r.json()).then(d=>{D=d.map(r=>({...localizeRecipe(r,LANG),cpt:r.tok_s&&r.hardware_cost_usd?Math.round(r.hardware_cost_usd/r.tok_s):null,mem:memGB(r.hardware),kind:costKind(r)}));
 const cnt=k=>{const c={};D.forEach(r=>c[r[k]]=(c[r[k]]||0)+1);return Object.entries(c).sort((a,b)=>b[1]-a[1]||a[0].localeCompare(b[0]))};
 for(const [id,k] of [['eng','engine'],['mf','model_family'],['fam','hardware_family']])cnt(k).forEach(([x,n])=>$(id).add(new Option(`${k=='hardware_family'?TF(x):TE(x)} (${n})`,x)));
 MEMS.forEach(m=>$('mem').add(new Option(T('af_mem',{n:m}),m)));
 const tc={};D.forEach(r=>r.tags.forEach(t=>tc[t]=(tc[t]||0)+1));
 $('chips').innerHTML=Object.entries(tc).sort((a,b)=>b[1]-a[1]).map(([t,n])=>`<button type="button" class="chip" aria-pressed="false" data-t="${esc(t)}">${esc(t)} <i>${n}</i></button>`).join('');
 $('chips').querySelectorAll('.chip').forEach(b=>b.onclick=()=>toggleTag(b.dataset.t));
 $('stats').innerHTML=[[D.length,T('st_all')],[D.filter(r=>r.source_level==MEA).length,T('st_mea')],[D.filter(r=>r.category=='text').length,T('st_text')],[D.filter(r=>r.category=='image').length,T('st_img')],[D.filter(r=>r.category=='video-audio').length,T('st_va')],[D.filter(r=>r.launch_command).length,T('st_cmd')]].map(([b,a])=>`<span class="stat"><b>${b}</b>${a}</span>`).join('');
 initPicker();
 const U=applyParams();render();
 if(U.cmp.length>=2)openCmp();else if(U.id&&D.some(r=>r.id==U.id))GP.then(()=>open(U.id));
 const nd=D.map(r=>r.date).filter(Boolean).sort().pop();if(nd)$('xd').textContent=T('xfootd',{d:nd});});

let TG=new Set(),CMP=[],VIEW=null,SHOW=30,OPEN=null;
try{VIEW=localStorage.getItem('view')}catch(e){}
function toggleTag(t){TG.has(t)?TG.delete(t):TG.add(t);SHOW=30;render()}
['q','cat','eng','mf','fam','mem','cb','lvl','budget','unk'].forEach(i=>$(i).addEventListener('input',()=>{SHOW=30;render()}));
const SORTS=['-tok_s','cpt','hardware_cost_usd','-date','model'];
$('sort').onchange=()=>{const s=$('sort').value;if(!s)return;sd=s[0]=='-'?-1:1;sk=s.replace(/^-/,'');render()};
document.querySelectorAll('th[data-k]>button').forEach(b=>b.onclick=()=>{const k=b.parentNode.dataset.k;sd=sk==k?-sd:(['tok_s','date'].includes(k)?-1:1);sk=k;render()});
document.querySelectorAll('.vt [data-v]').forEach(b=>b.onclick=()=>{VIEW=b.dataset.v;try{localStorage.setItem('view',VIEW)}catch(e){}render()});
const mode=()=>mobile.matches?'cards':(VIEW=='cards'?'cards':'table');
mobile.addEventListener('change',()=>{render();if(!mobile.matches)closeFilters()});
$('more').onclick=()=>{SHOW+=30;render()};
$('tagmore').onclick=()=>{const m=$('tagbox').classList.toggle('more');$('tagmore').textContent=T(m?'lesstags':'moretags')};

function sync(){const P=new URLSearchParams();const m={q:'q',cat:'cat',eng:'engine',mf:'family',fam:'fam',lvl:'level',mem:'mem',cb:'cost'};
 for(const [id,k] of Object.entries(m))if($(id).value)P.set(k,$(id).value);if(+$('budget').value<30000)P.set('max',$('budget').value);if(TG.size)P.set('tag',[...TG].join(','));
 if(!$('unk').checked)P.set('unk','0');
 const so=(sd<0?'-':'')+sk;if(so!='-tok_s')P.set('sort',so);
 if(VIEW)P.set('view',VIEW);if(CMP.length)P.set('cmp',CMP.join(','));if(OPEN)P.set('id',OPEN);
 if($('picker').open){P.set('pick','1');if(PK.fam)P.set('pfam',PK.fam);if(PK.mem)P.set('pmem',PK.mem);if(PK.max)P.set('pmax',PK.max);if(!PK.mea)P.set('pall','1')}
 const lg=new URLSearchParams(location.search).get('lang');if(lg)P.set('lang',lg);
 history.replaceState(null,'',location.pathname+(P.toString()?'?'+P.toString().replace(/%2C/g,','):'')+location.hash);
 document.querySelectorAll('#chips .chip').forEach(b=>{const on=TG.has(b.dataset.t);b.classList.toggle('on',on);b.setAttribute('aria-pressed',String(on))});}
const match=q=>r=>!q||[r.model,r.quant,r.engine,r.engine_note,r.hardware,r.metric,r.metric_en,r.model_family,...r.tags].join(' ').toLowerCase().includes(q);
function filt(){const q=$('q').value.toLowerCase().trim(),b=+$('budget').value,mm=+$('mem').value;$('bv').textContent='$'+b.toLocaleString();
 return D.filter(r=>match(q)(r)&&(!$('cat').value||r.category==$('cat').value)&&(!$('eng').value||r.engine==$('eng').value)&&(!$('fam').value||r.hardware_family==$('fam').value)&&(!$('mf').value||r.model_family==$('mf').value)&&[...TG].every(t=>r.tags.includes(t))&&(!$('lvl').value||(r.source_level==$('lvl').value&&!($('lvl').value==MEA&&selfReported(r))))&&(r.hardware_cost_usd==null?$('unk').checked:r.hardware_cost_usd<=b)&&(!mm||(r.mem!=null&&r.mem<=mm))&&(!$('cb').value||r.kind==$('cb').value));}
const cmpSort=(a,b)=>{const x=a[sk],y=b[sk];if(x==null&&y==null)return 0;if(x==null)return 1;if(y==null)return -1;return (typeof x=='string'?x.localeCompare(y):(x>y?1:x<y?-1:0))*sd};
function activeFilters(){const A=[],lab=id=>{const s=$(id);return s.options[s.selectedIndex].text.replace(/ \(\d+\)$/,'')};
 if($('q').value)A.push([`${T('af_q')}: “${$('q').value}”`,()=>$('q').value='']);
 for(const id of ['cat','eng','mf','fam','mem','cb','lvl'])if($(id).value)A.push([lab(id),()=>$(id).value='']);
 if(+$('budget').value<30000)A.push([T('af_max',{n:(+$('budget').value).toLocaleString()}),()=>$('budget').value=30000]);
 if(!$('unk').checked)A.push([T('af_unk'),()=>$('unk').checked=true]);
 TG.forEach(t=>A.push(['#'+t,()=>TG.delete(t)]));return A}
function render(){if(!D.length)return;sync();const L=filt().sort(cmpSort),M=mode();
 document.querySelectorAll('th[data-k]').forEach(t=>t.setAttribute('aria-sort',t.dataset.k==sk?(sd<0?'descending':'ascending'):'none'));
 const so=(sd<0?'-':'')+sk;$('sort').value=SORTS.includes(so)?so:'';
 document.querySelectorAll('.vt [data-v]').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.v==M)));
 const A=activeFilters();
 $('active').innerHTML=`<span class="count">${T('count',{n:L.length,t:D.length})}</span>`+A.map(([l],i)=>`<button type="button" class="af" data-i="${i}">${esc(l)} <span aria-hidden="true">✕</span></button>`).join('')+(A.length?`<button type="button" class="linkbtn" id="aclear">${T('clear')}</button>`:'');
 $('active').querySelectorAll('.af').forEach(b=>b.onclick=()=>{A[+b.dataset.i][1]();render()});if($('aclear'))$('aclear').onclick=clearAll;
 $('fcount').hidden=!A.length;$('fcount').textContent=A.length;$('fdone').textContent=T('show_n',{n:L.length});
 $('tw').hidden=M!='table';$('cards').hidden=M!='cards';
 if(!L.length){$('tb').innerHTML=`<tr><td colspan="11" class="empty">${T('noresult')}</td></tr>`;$('cards').innerHTML=`<p class="empty">${T('noresult')}</p>`;$('morew').hidden=true}
 else if(M=='table'){$('morew').hidden=true;$('tb').innerHTML=L.map(r=>`<tr data-id="${esc(r.id)}" tabindex="0"${CMP.includes(r.id)?' class="sel"':''}><td class="cmpc"><input type="checkbox" class="ck" data-id="${esc(r.id)}" aria-label="${T('cmp')}: ${esc(r.model)}"${CMP.includes(r.id)?' checked':''}></td><td><span class="mdl">${esc(r.model)}</span><br><span class="tag">${CAT[r.category]}</span> <span class="tag fam">${esc(TE(r.model_family))}</span> ${r.tags.map(t=>`<button type="button" class="tg" data-t="${esc(t)}">${esc(t)}</button>`).join('')}</td><td>${v(r.quant)}</td><td>${esc(TE(r.engine))}${r.engine_note?`<small class="na">${esc(r.engine_note)}</small>`:''}</td><td>${esc(r.hardware)}<br><span class="tag">${esc(TF(r.hardware_family))}</span></td><td class="n tok">${v(r.tok_s)}</td><td>${v(MET(r))}</td><td class="n">${r.hardware_cost_usd!=null?r.hardware_cost_usd.toLocaleString()+KC(r):v(r.hardware_cost_text)}</td><td class="n">${v(r.cpt)}</td><td>${v(r.context)}</td><td><span class="lv ${esc(r.source_level)}">${TL(r.source_level)}</span></td></tr>`).join('')}
 else{const S=L.slice(0,SHOW);$('cards').innerHTML=S.map(card).join('');$('morew').hidden=L.length<=SHOW;$('more').textContent=T('more',{n:Math.min(30,L.length-SHOW)})}
 bindRows();tagOverflow();if($('viz').open)chart(L);else LAST=L;updTray();}
function tagOverflow(){const c=$('chips'),b=$('tagbox');$('tagmore').hidden=!b.classList.contains('more')&&c.scrollHeight<=c.clientHeight+2}
function card(r){const sel=CMP.includes(r.id);return `<article class="rc${sel?' sel':''}" data-id="${esc(r.id)}"><div class="rc-top"><div><span class="lv ${esc(r.source_level)}">${TL(r.source_level)}</span> <span class="tag">${CAT[r.category]}</span></div>
<label class="cmpbox"><input type="checkbox" class="ck" data-id="${esc(r.id)}"${sel?' checked':''}> ${T('cmp')}</label></div>
<h3><button type="button" class="op">${esc(r.model)}</button></h3>
<div class="rc-k"><span><b>${r.tok_s!=null?esc(r.tok_s):'—'}</b><small>tok/s</small></span><span class="sec"><b>${r.hardware_cost_usd!=null?'$'+r.hardware_cost_usd.toLocaleString():'—'}</b><small>${r.kind?T('kc_'+r.kind):T('th_cost').replace(' $','')}</small></span>${r.cpt!=null?`<span class="sec"><b>$${r.cpt}</b><small>/ tok/s</small></span>`:''}</div>
<div class="sub">${esc(r.hardware)}</div><div class="sub">${esc(TE(r.engine))}${r.quant?' · '+esc(r.quant):''}</div>
${MET(r)?`<div class="met">${esc(MET(r))}</div>`:''}<div>${r.tags.map(t=>`<button type="button" class="tg" data-t="${esc(t)}">${esc(t)}</button>`).join('')}</div></article>`}
function bindRows(){
 document.querySelectorAll('#tb tr[data-id]').forEach(tr=>{tr.onclick=e=>{if(!e.target.closest('input,button'))open(tr.dataset.id)};tr.onkeydown=e=>{if(e.key=='Enter'&&e.target==tr)open(tr.dataset.id)}});
 document.querySelectorAll('#cards .rc').forEach(c=>c.onclick=e=>{if(!e.target.closest('input,label,.tg'))open(c.dataset.id)});
 document.querySelectorAll('#results .tg').forEach(g=>g.onclick=e=>{e.stopPropagation();toggleTag(g.dataset.t)});
 document.querySelectorAll('#results .ck').forEach(c=>c.onchange=()=>toggleCmp(c.dataset.id,c));}

// ---- chart: log-x cost, linear tok/s; shape + color encode source level ----
let LAST=[];$('viz').addEventListener('toggle',()=>{if($('viz').open)chart(LAST.length?LAST:filt())});
const SH={'官方':(x,y)=>`<rect x="${x-4.5}" y="${y-4.5}" width="9" height="9" rx="1.5"`,'实测':(x,y)=>`<circle cx="${x}" cy="${y}" r="5"`,'转述':(x,y)=>`<path d="M${x} ${y-6}L${x+5.5} ${y+4}H${x-5.5}Z"`,'宣称':(x,y)=>`<path d="M${x} ${y-6}L${x+6} ${y}L${x} ${y+6}L${x-6} ${y}Z"`};
$('lgk').innerHTML=LV.map(k=>`<span><svg viewBox="-7 -7 14 14">${SH[k](0,0)} class="s-${k}"/></svg>${TL(k)}</span>`).join('');
function chart(L){LAST=L;const P=L.filter(r=>r.tok_s&&r.hardware_cost_usd&&r.category=='text'),W=Math.max(300,Math.min(900,$('chartw').clientWidth||640)),H=W<500?260:320,m={l:44,r:12,t:12,b:40};
 const x0=Math.log(400),x1=Math.log(Math.max(30000,...P.map(p=>p.hardware_cost_usd))),ym=Math.max(50,...P.map(p=>p.tok_s))*1.08;
 const X=c=>m.l+(Math.log(Math.max(c,400))-x0)/(x1-x0)*(W-m.l-m.r),Y=t=>H-m.b-t/ym*(H-m.t-m.b);let s='';
 for(const c of (W<500?[500,1000,2500,5000,10000,30000]:[500,1000,2000,5000,10000,20000,30000]))s+=`<line class="gl" x1="${X(c)}" x2="${X(c)}" y1="${m.t}" y2="${H-m.b}"/><text x="${X(c)}" y="${H-m.b+16}" font-size="11" text-anchor="middle">$${c>=1000?c/1000+'k':c}</text>`;
 for(let i=0;i<=5;i++){const t=ym*i/5;s+=`<line class="gl" x1="${m.l}" x2="${W-m.r}" y1="${Y(t)}" y2="${Y(t)}"/><text x="${m.l-6}" y="${Y(t)+4}" font-size="11" text-anchor="end">${Math.round(t)}</text>`}
 s+=`<text x="${(W+m.l)/2}" y="${H-6}" font-size="12" text-anchor="middle">${T('xaxis')}</text><text x="12" y="${(H-m.b)/2}" font-size="12" transform="rotate(-90 12 ${(H-m.b)/2})" text-anchor="middle">tok/s</text>`;
 s+=P.map(p=>`${SH[p.source_level](+X(p.hardware_cost_usd).toFixed(1),+Y(p.tok_s).toFixed(1))} class="mk s-${esc(p.source_level)}" data-id="${esc(p.id)}" data-tip="${esc(`${p.model} · ${p.hardware} · ${p.tok_s} tok/s · $${p.hardware_cost_usd.toLocaleString()} · ${TL(p.source_level)}`)}"/>`).join('');
 $('chart').setAttribute('viewBox',`0 0 ${W} ${H}`);$('chart').innerHTML=s+(P.length?'':`<text x="${W/2}" y="${H/2}" text-anchor="middle">${T('empty')}</text>`);
 const tip=$('tip');document.querySelectorAll('#chart .mk').forEach(d=>{d.onclick=()=>open(d.dataset.id);
  d.onmouseenter=e=>{tip.textContent=d.dataset.tip;tip.classList.add('on')};d.onmousemove=e=>{tip.style.left=Math.min(innerWidth-290,e.clientX+12)+'px';tip.style.top=(e.clientY+14)+'px'};d.onmouseleave=()=>tip.classList.remove('on')});}
let rz;addEventListener('resize',()=>{clearTimeout(rz);rz=setTimeout(()=>{if($('viz').open)chart(LAST)},150)});

// ---- dialogs (detail drawer, compare panel, mobile filter sheet) ----
// RET = where focus returns when the layer closes; BACK = id whose Details was opened from the compare panel (closing the drawer goes back there)
let RET=null,BACK=null;
function showLayer(el,focus,keep){if(!keep)RET=document.activeElement;el.classList.add('open');$('mask').classList.add('open');document.body.style.overflow='hidden';(focus||el).focus()}
function hideAll(){
 if(BACK&&$('drawer').classList.contains('open')&&CMP.length>=2){const id=BACK;BACK=null;$('drawer').classList.remove('open');OPEN=null;renderCmp();$('cmp').classList.add('open');sync();
  ($('cmpb').querySelector(`button[data-a="o"][data-id="${CSS.escape(id)}"]`)||$('cx')).focus();return}
 BACK=null;const any=$('drawer').classList.contains('open')||$('cmp').classList.contains('open')||$('filters').classList.contains('open');
 $('drawer').classList.remove('open');$('cmp').classList.remove('open');closeFilters(true);$('mask').classList.remove('open');document.body.style.overflow='';
 if(OPEN){OPEN=null;sync()}if(any&&RET&&RET.focus){if(RET.disabled||!RET.offsetParent)($('q')||document.body).focus();else RET.focus()}}
function open(id){const r=D.find(x=>x.id==id);if(!r)return;OPEN=id;const inC=CMP.includes(id),fromCmp=$('cmp').classList.contains('open');BACK=fromCmp?id:null;
 $('dc').innerHTML=`<h2 id="dh">${esc(r.model)}</h2><p><span class="tag">${CAT[r.category]}</span> <span class="lv ${esc(r.source_level)}">${TL(r.source_level)}</span> <span class="tag">${esc(r.id)}</span>${r.superseded_by?` <span class="tag">${T('d_sup',{id:esc(r.superseded_by)})}</span>`:''}</p>
<div class="dacts"><button type="button" class="btn btn-sm${inC?' btn-p':''}" id="dcmp">${T(inC?'cmp_rm':'cmp_add')}</button><a class="btn btn-sm" href="${esc(r.source_url)}" target="_blank" rel="noopener">${T('d_open')}</a></div>
<dl><dt>${T('d_tok')}</dt><dd><b>${v(r.tok_s)}</b></dd><dt>${T('d_cost')}</dt><dd>${v(r.hardware_cost_text)}${KC(r)}</dd><dt>$/tok/s</dt><dd>${v(r.cpt)}</dd><dt>${T('d_quant')}</dt><dd>${v(r.quant)}</dd><dt>${T('d_mf')}</dt><dd>${esc(TE(r.model_family))}</dd><dt>${T('d_tags')}</dt><dd>${r.tags.map(t=>`<span class="tg">${esc(t)}</span>`).join('')||'—'}</dd><dt>${T('d_eng')}</dt><dd>${esc(TE(r.engine))}${r.engine_note?` (${T('d_orig')}${esc(r.engine_note)})`:''}</dd><dt>${T('d_hw')}</dt><dd>${esc(r.hardware)} (${esc(TF(r.hardware_family))})</dd><dt>${T('d_mem')}</dt><dd>${r.mem!=null?r.mem+' GB':NA}</dd><dt>${T('d_perf')}</dt><dd>${v(MET(r))}</dd><dt>${T('d_conc')}</dt><dd>${v(r.concurrency)}</dd><dt>${T('d_ctx')}</dt><dd>${v(r.context)}</dd><dt>${T('d_date')}</dt><dd>${v(r.date)}</dd><dt>${T('d_note')}</dt><dd>${v(r.source_note)}</dd></dl>
<h3>${T('d_cmd')}</h3>${r.launch_command?`<pre>${esc(r.launch_command)}</pre>`:`<pre>${esc(T('d_nocmd'))}</pre>`}
<h3>${T('d_src')}</h3><p><a href="${esc(r.source_url)}" target="_blank" rel="noopener" style="overflow-wrap:anywhere">${esc(r.source_url)}</a></p>${GUIDES.has(r.id)?`<p><a href="${REPO}/blob/main/recipes/${esc(r.id)}${LANG=='en'?'':'.'+LANG}.md" target="_blank" rel="noopener">${T('d_guide')}</a></p>`:""}<p><a href="submit.html">${T('d_fix')}</a></p>`;
 $('dcmp').onclick=()=>{toggleCmp(id);const c=CMP.includes(id);$('dcmp').textContent=T(c?'cmp_rm':'cmp_add');$('dcmp').classList.toggle('btn-p',c)};
 $('cmp').classList.remove('open');$('drawer').scrollTop=0;showLayer($('drawer'),$('x'),fromCmp||$('drawer').classList.contains('open'));sync()}
$('x').onclick=$('mask').onclick=$('cx').onclick=hideAll;
// Esc closes the top layer; Tab / Shift+Tab stay inside the open dialog
const FOC='a[href],button:not([disabled]),input:not([disabled]),select:not([disabled]),textarea,[tabindex]:not([tabindex="-1"])';
document.addEventListener('keydown',e=>{if(e.key=='Escape'){hideAll();return}if(e.key!='Tab')return;
 const d=['drawer','cmp','filters'].map($).find(x=>x.classList.contains('open'));if(!d)return;
 const F=[...d.querySelectorAll(FOC)].filter(x=>x.getClientRects().length);if(!F.length)return;const a=F[0],z=F[F.length-1],c=document.activeElement;
 if(!d.contains(c)){e.preventDefault();(e.shiftKey?z:a).focus()}else if(e.shiftKey&&c==a){e.preventDefault();z.focus()}else if(!e.shiftKey&&c==z){e.preventDefault();a.focus()}});

// ---- mobile filter sheet ----
// the filter panel is inline on desktop and only becomes a modal sheet while opened on mobile
function openFilters(){const f=$('filters');f.setAttribute('role','dialog');f.setAttribute('aria-modal','true');$('fbtn').setAttribute('aria-expanded','true');showLayer(f,$('fclose'))}
function closeFilters(silent){const f=$('filters');if(!f.classList.contains('open'))return;f.classList.remove('open');f.removeAttribute('role');f.removeAttribute('aria-modal');$('fbtn').setAttribute('aria-expanded','false');if(!silent){$('mask').classList.remove('open');document.body.style.overflow='';$('fbtn').focus()}}
$('fbtn').onclick=openFilters;$('fclose').onclick=$('fdone').onclick=()=>closeFilters();
function clearAll(){$('q').value='';for(const id of ['cat','eng','mf','fam','mem','cb','lvl'])$(id).value='';$('budget').value=30000;$('unk').checked=true;TG.clear();SHOW=30;render()}
$('fclear').onclick=clearAll;

// ---- compare (2–4 recipes, ?cmp=id1,id2) ----
function toggleCmp(id,box){const i=CMP.indexOf(id);if(i>=0)CMP.splice(i,1);else if(CMP.length>=4){if(box)box.checked=false;flash(T('cmp_max'));return}else CMP.push(id);
 document.querySelectorAll(`#results [data-id="${CSS.escape(id)}"]`).forEach(el=>{if(el.matches('tr,.rc'))el.classList.toggle('sel',CMP.includes(id));if(el.matches('.ck'))el.checked=CMP.includes(id)});
 updTray();sync();if($('cmp').classList.contains('open'))CMP.length?renderCmp():hideAll()}
function flash(msg){const t=$('tl');t.textContent=msg;setTimeout(updTray,1800)}
function updTray(){const on=CMP.length>0;$('tray').classList.toggle('on',on);document.body.classList.toggle('has-tray',on);
 $('tl').textContent=CMP.length<2?T('cmp_need'):T('cmp_n',{n:CMP.length});$('tgo').disabled=CMP.length<2;
 $('tchips').innerHTML=CMP.map(id=>{const r=D.find(x=>x.id==id);return r?`<span class="tchip"><span>${esc(r.model)}</span><button type="button" data-id="${esc(id)}" aria-label="${T('cmp_remove')}: ${esc(r.model)}">✕</button></span>`:''}).join('');
 $('tchips').querySelectorAll('button').forEach(b=>b.onclick=()=>toggleCmp(b.dataset.id))}
$('tgo').onclick=openCmp;$('tclear').onclick=()=>{[...CMP].forEach(id=>toggleCmp(id))};
function openCmp(){if(CMP.length<2)return;renderCmp();$('drawer').classList.remove('open');OPEN=null;showLayer($('cmp'),$('cx'));sync()}
function renderCmp(){const R=CMP.map(id=>D.find(x=>x.id==id)).filter(Boolean);
 // ★ only among Official / Measured speeds (others get †); cost ★ only when every priced column shares one price basis (GPU only vs whole system)
 const ok=r=>r.source_level==MEA||r.source_level=='官方',kinds=new Set(R.filter(r=>r.hardware_cost_usd!=null).map(r=>r.kind)),same=kinds.size==1&&!kinds.has(null);
 const best=(k,f,rs)=>{const xs=rs.map(r=>r[k]).filter(x=>x!=null);return xs.length>1?f(...xs):null},bt=best('tok_s',Math.max,R.filter(ok)),bc=same?best('cpt',Math.min,R.filter(ok)):null,bh=same?best('hardware_cost_usd',Math.min,R):null;
 const DG=`<sup class="untr" title="${T('cmp_untr')}">†</sup>`;
 const row=(lab,f,cls)=>`<tr><th scope="row">${lab}</th>${R.map(r=>`<td${cls?` class="${cls}"`:''}>${f(r)}</td>`).join('')}</tr>`,B=(x,b,s,r)=>x==null?NA:`<span${x===b&&(!r||ok(r))?` class="best" title="${T('cmp_best')}"`:''}>${s}</span>${r&&!ok(r)?DG:''}`;
 $('cmpb').innerHTML=`<table class="cmpt" style="min-width:${110+R.length*180}px"><thead><tr><th></th>${R.map(r=>`<th scope="col">${esc(r.model)}<small class="muted" style="display:block;font-weight:500;font-size:12px">${esc(r.hardware)} · ${esc(TE(r.engine))}</small><div class="rm"><button type="button" class="btn btn-sm" data-id="${esc(r.id)}" data-a="o">${T('pk_det')}</button> <button type="button" class="btn btn-sm btn-ghost" data-id="${esc(r.id)}" data-a="x">${T('cmp_remove')}</button></div></th>`).join('')}</tr></thead><tbody>
${row(T('d_tok'),r=>B(r.tok_s,bt,esc(r.tok_s),r),'big')}${row('$/tok/s',r=>B(r.cpt,bc,'$'+r.cpt,r))}${row(T('d_cost'),r=>r.hardware_cost_usd!=null?B(r.hardware_cost_usd,bh,'$'+r.hardware_cost_usd.toLocaleString())+KC(r)+(r.hardware_cost_text?`<small class="muted" style="display:block">${esc(r.hardware_cost_text)}</small>`:''):v(r.hardware_cost_text))}
${row(T('d_hw'),r=>`${esc(r.hardware)}<br><span class="tag">${esc(TF(r.hardware_family))}</span>`)}${row(T('d_mem'),r=>r.mem!=null?r.mem+' GB':NA)}${row(T('d_eng'),r=>esc(TE(r.engine)))}${row(T('d_quant'),r=>v(r.quant))}
${row(T('d_perf'),r=>v(MET(r)))}${row(T('d_ctx'),r=>v(r.context))}${row(T('d_conc'),r=>v(r.concurrency))}${row(T('th_src'),r=>`<span class="lv ${esc(r.source_level)}">${TL(r.source_level)}</span> <a href="${esc(r.source_url)}" target="_blank" rel="noopener">${T('d_open')}</a>`)}
${row(T('d_date'),r=>v(r.date))}${row(T('d_tags'),r=>r.tags.map(t=>`<span class="tg">${esc(t)}</span>`).join('')||'—')}${row(T('d_cmd'),r=>r.launch_command?`<pre>${esc(r.launch_command)}</pre>`:NA)}</tbody></table><p class="cmp-note">${T('cmp_note')}</p>`;
 $('cmpb').querySelectorAll('button[data-a]').forEach(b=>b.onclick=()=>b.dataset.a=='o'?open(b.dataset.id):toggleCmp(b.dataset.id))}
$('ccopy').onclick=()=>{const u=location.href,done=()=>{$('ccopy').textContent=T('cmp_copied');setTimeout(()=>$('ccopy').textContent=T('cmp_copy'),1600)};
 (navigator.clipboard?navigator.clipboard.writeText(u):Promise.reject()).then(done).catch(()=>{prompt(T('cmp_copy'),u)})};

// ---- "What can my machine run?" picker ----
const PK={fam:'',mem:0,max:0,mea:true};
function initPicker(){const fams=['',...new Set(D.map(r=>r.hardware_family))];
 $('pk_fam').innerHTML=fams.map(f=>`<button type="button" class="chip" data-f="${esc(f)}" aria-pressed="false">${f?esc(TF(f)):T('pk_any')}</button>`).join('');
 $('pk_fam').querySelectorAll('.chip').forEach(b=>b.onclick=()=>{PK.fam=b.dataset.f;pick()});
 $('pk_mem').innerHTML=`<option value="0">${T('pk_anymem')}</option>`+MEMS.map(m=>`<option value="${m}">${T('pk_memopt',{n:m})}</option>`).join('');
 $('pk_max').innerHTML=`<option value="0">${T('pk_anybud')}</option>`+BUDS.map(b=>`<option value="${b}">≤ $${b.toLocaleString()}</option>`).join('');
 $('pk_mem').onchange=()=>{PK.mem=+$('pk_mem').value;pick()};$('pk_max').onchange=()=>{PK.max=+$('pk_max').value;pick()};$('pk_mea').onchange=()=>{PK.mea=$('pk_mea').checked;pick()};
 $('picker').addEventListener('toggle',()=>{if($('picker').open)pick();else sync()})}
function pick(){$('pk_fam').querySelectorAll('.chip').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.f===PK.fam)));
 $('pk_mem').value=PK.mem;$('pk_max').value=PK.max;$('pk_mea').checked=PK.mea;
 // measured-only also drops self-reported (自称) rows, see selfReported in cost.js
 const base=D.filter(r=>r.category=='text'&&r.tok_s&&!r.superseded_by&&(!PK.mea||(r.source_level==MEA&&!selfReported(r)))&&(!PK.fam||r.hardware_family==PK.fam)&&(!PK.max||(r.hardware_cost_usd!=null&&r.hardware_cost_usd<=PK.max)));
 const R=base.filter(r=>!PK.mem||(r.mem!=null&&r.mem<=PK.mem)).sort((a,b)=>b.tok_s-a.tok_s),unk=PK.mem?base.filter(r=>r.mem==null).length:0;
 // what "Apply in the explorer" will show (same filters, but the explorer keeps superseded / no-tok/s / self-reported rows)
 const ex=D.filter(r=>r.category=='text'&&(!PK.fam||r.hardware_family==PK.fam)&&(!PK.mem||(r.mem!=null&&r.mem<=PK.mem))&&(!PK.max||(r.hardware_cost_usd!=null&&r.hardware_cost_usd<=PK.max))&&(!PK.mea||r.source_level==MEA)).length;
 const OFF=/RAM|DDR|内存|卸载|offload/i;
 $('pk_res').innerHTML=R.length?`<div class="pk-sum"><span>${T('pk_n',{n:R.length})}${unk?' · '+T('pk_unk',{n:unk}):''}${ex!=R.length?' · '+T('pk_diff',{n:ex}):''}</span><button type="button" class="btn btn-sm" id="pk_go">${T('pk_all',{n:ex})}</button></div><p class="pk-note">${T('pk_note')}</p><ol>`+R.slice(0,8).map((r,i)=>`<li class="pk-it"><span class="rk">#${i+1}</span><div><div class="ttl">${esc(r.model)}</div><div class="sub">${esc(r.hardware)}${r.mem!=null?` · ${r.mem} GB${OFF.test((r._src||r).hardware)?` <span class="kc in">${T('pk_off')}</span>`:''}`:''} · ${esc(TE(r.engine))}${r.quant?' · '+esc(r.quant):''}</div></div><div class="tok">${esc(r.tok_s)}<small>tok/s${r.hardware_cost_usd!=null?' · $'+r.hardware_cost_usd.toLocaleString():''}</small></div>
<div class="acts"><span class="lv ${esc(r.source_level)}">${TL(r.source_level)}</span><button type="button" class="btn btn-sm" data-o="${esc(r.id)}">${T('pk_det')}</button><button type="button" class="btn btn-sm${CMP.includes(r.id)?' btn-p':''}" data-c="${esc(r.id)}">${T(CMP.includes(r.id)?'cmp_rm':'cmp_add')}</button></div></li>`).join('')+'</ol>':`<p class="empty">${T('pk_none')}${unk?' '+T('pk_unk',{n:unk}):''}</p>`;
 $('pk_res').querySelectorAll('[data-o]').forEach(b=>b.onclick=()=>open(b.dataset.o));
 $('pk_res').querySelectorAll('[data-c]').forEach(b=>b.onclick=()=>{toggleCmp(b.dataset.c);pick()});
 if($('pk_go'))$('pk_go').onclick=()=>{clearAll();$('cat').value='text';$('fam').value=PK.fam;$('mem').value=PK.mem||'';if(PK.max){$('budget').value=PK.max;$('unk').checked=false}if(PK.mea)$('lvl').value=MEA;sk='tok_s';sd=-1;render();$('active').scrollIntoView({behavior:'smooth',block:'start'})};
 sync()}

// deep-link: explore.html?family=Qwen&tag=MoE,4bit&engine=llama.cpp&fam=Mac&cat=text&level=实测&max=3000&q=...&mem=24&cost=gpu|sys&sort=-tok_s&view=cards&cmp=a,b&id=x&pick=1&pfam=Mac&pmem=64&pmax=7000&pall=1
function applyParams(){const U=new URLSearchParams(location.search);if(U.get('max'))$('budget').value=U.get('max');
 for(const [id,k] of [['fam','fam'],['mf','family'],['eng','engine'],['cat','cat'],['lvl','level'],['mem','mem'],['cb','cost']])if(U.get(k))$(id).value=U.get(k);
 if(U.get('tag'))U.get('tag').split(',').filter(Boolean).forEach(t=>TG.add(t));if(U.get('q'))$('q').value=U.get('q');if(U.get('unk')=='0')$('unk').checked=false;
 const so=U.get('sort');if(so){sd=so[0]=='-'?-1:1;sk=so.replace(/^-/,'')}
 if(['table','cards'].includes(U.get('view')))VIEW=U.get('view');
 const cmp=(U.get('cmp')||'').split(',').filter(id=>D.some(r=>r.id==id)).slice(0,4);CMP.push(...cmp);
 if(U.get('pick')||U.get('pfam')||U.get('pmem')||U.get('pmax')||location.hash=='#picker'){PK.fam=U.get('pfam')||'';PK.mem=+U.get('pmem')||0;PK.max=+U.get('pmax')||0;PK.mea=U.get('pall')!='1';$('picker').open=true;pick()}
 if(!mobile.matches)$('viz').open=true;
 return {id:U.get('id'),cmp}}
