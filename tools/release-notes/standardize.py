#!/usr/bin/env python3
"""
Standardize release notes to style guide rule G-31. Formatting only; wording is never changed.

Usage (from the repository root):
  standardize.py <product|all> [report.csv]
Products: ARM, DataLoader, CodeScan, "CodeScan Self-Hosted", Vault, Guard, nCino, "IZ Suite", all

What it changes:
  * release headings  -> "## <Product> <version>"            (e.g. "## ARM 26.4.5")
  * release dates     -> "**Release date:** D Month YYYY"
  * section headings  -> New features / Enhancements / Fixes (CodeScan also New rules / Rule enhancements)
  * all headings      -> no bold, no <a href> anchors, no &#x20;, no "1." numbering
  * links to renamed headings, anywhere in the repo, are updated to the new anchors
Heading levels, page structure and every other line are left alone. Anything it can't
convert safely is listed in the report for a person to fix.
"""
import os, re, sys, csv, glob, subprocess, html
from urllib.parse import unquote
group=sys.argv[1]; REPORT=sys.argv[2] if len(sys.argv) > 2 else os.devnull
RN='release-notes/release-notes/'
GROUPS={
 'ARM':(sorted(glob.glob(RN+'arm-release-notes/**/*.md',recursive=True)),'ARM'),
 'DataLoader':([RN+'arm-release-notes-26.md'],'DataLoader'),
 'CodeScan':(sorted(glob.glob(RN+'codescan-release-notes/cloud-releases/**/*.md',recursive=True))+[RN+'codescan-release-notes/README.md'],'CodeScan'),
 'CodeScan Self-Hosted':(sorted(glob.glob(RN+'codescan-release-notes/on-premise-releases/**/*.md',recursive=True)),'CodeScan Self-Hosted'),
 'Vault':(sorted(glob.glob(RN+'vault-release-notes/*.md')),'AutoRABIT Vault'),  # Vault release notes always say AutoRABIT Vault
 'Guard':(sorted(glob.glob(RN+'guard/*.md'))+[RN+'guard.md'],'Guard'),
 'nCino':(sorted(glob.glob(RN+'ncino-release-notes/*.md')),'nCino'),
 'IZ Suite':(sorted(glob.glob(RN+'iz-suite-release-notes/*.md')),'IZ Suite'),
}
if group == 'all':
    import subprocess as _sp
    rc = 0
    for g in GROUPS:
        rc |= _sp.call([sys.executable, '-I', os.path.abspath(__file__), g, REPORT])
    sys.exit(rc)
if group not in GROUPS:
    sys.exit('Unknown product. Choose one of: ' + ', '.join(GROUPS) + ', all')
files,PRODUCT=GROUPS[group]; files=[f for f in files if os.path.exists(f)]
V=r'\d+(?:\.\d+)+'
MONTHS='january february march april may june july august september october november december'.split()
def month(s):
    s=s.lower()[:3]
    for i,m in enumerate(MONTHS):
        if m[:3]==s: return MONTHS[i].capitalize()
SECT={'new features':'New features','new feature':'New features','enhancements':'Enhancements','enhancement':'Enhancements',
      'improvements':'Enhancements','application enhancements':'Enhancements','other enhancements':'Enhancements',
      'bug fixes':'Fixes','bug fix':'Fixes','bugs fixed':'Fixes','bugs':'Fixes','fixes':'Fixes','new rules':'New rules','rule enhancements':'Rule enhancements'}
def slug(text):
    s=text.lower(); s=re.sub(r'[^a-z0-9 \-._]','',s); s=s.replace(' ','-')
    return ('id-'+s) if s[:1].isdigit() else s
def clean(h):
    ids=re.findall(r'<a href="#[^"]*" id="([^"]*)"></a>',h)
    t=re.sub(r'<a href="#[^"]*" id="[^"]*"></a>','',h)
    t=t.replace('**','').replace('&#x20;',' ').replace('\\[','[').replace('\\]',']')
    t=re.sub(r'\s+',' ',t).strip()
    return t,(ids[0] if ids else None)
report=[]
def release_heading(t,f):
    if re.match(r'(summary|integration|current|major|minor|prior)\b',t,re.I): return None
    m=re.search(V,t)
    if not m: return None
    if not re.search(r'release|^(arm|codescan|autorabit|vault|guard|ncino|iz suite|dataloader|data loader)\b|^v\.? ?\d',t,re.I): return None
    ms=list(re.finditer(V,t)); m=max(ms,key=lambda x:(x.group(0).count('.'),-x.start()))
    ver=m.group(0)
    rest=t[:m.start()]+' '+t[m.end():]
    prod=PRODUCT
    low=t.lower()
    if 'ncino' in low and re.search(r'data ?loader',low): prod='nCino + DataLoader'
    elif re.search(r'data ?loader',low):
        if re.search(r'data ?loader\s*(\+|&|and)\s*data ?loader pro',low): prod='DataLoader and DataLoader Pro'
        elif re.search(r'data ?loader pro',low): prod='DataLoader Pro'
        else: prod='DataLoader'
    suffix=[]
    ed=re.search(r'\b(eagle|tiger)\b\s*(?:edition)?\s*\(?\s*(?:v\.?\s*)?(\d+(?:\.\d+)?)?',rest,re.I)
    if ed:
        suffix.append(ed.group(1).capitalize()+(' '+ed.group(2) if ed.group(2) else ''))
        rest=rest[:ed.start()]+' '+rest[ed.end():]
    mon=re.search(r'\b(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*\.?\s+(\d{4})\b',rest,re.I)
    if mon:   # "Release Notes 24.0.1 Feb 2024" -> "CodeScan 24.0.1 (February 2024)"
        suffix.append(f'{month(mon.group(1))} {mon.group(2)}'); rest=rest[:mon.start()]+' '+rest[mon.end():]
    parens=re.findall(r'\(([^)]*)\)',rest)
    for p in parens:
        p2=p.strip()
        if p2 and not re.fullmatch(r'(v\.?\s*(\d+(\.\d+)*)?|on-prem|tiger edition|eagle edition)',p2,re.I): suffix.append(p2)
    rest=re.sub(r'\([^)]*\)','',rest)
    noise=r'\b(autorabit|arm|codescan|cloud|vault|guard|ncino|iz|suite|data ?loader|pro|release|releases|notes|self-hosted|on-premises|on-prem|edition|v)\b|[-–+&/.:()]|\band\b'
    left=re.sub(noise,' ',rest,flags=re.I).strip()
    if left:
        report.append(('skipped-heading',f,t)); return None
    return f'{prod} {ver}'+(f' ({", ".join(suffix)})' if suffix else '')
DATE=re.compile(r'^\s*\**\s*(?:release date\s*:?\s*\**\s*:?\s*\**\s*(?P<a>[^*\n]+?)\s*\**|(?P<b>[^*\n]+?)\s+release date\s*\**)\s*$',re.I)
def norm_date(s):
    s=s.strip().strip('*').strip()
    m=re.fullmatch(r'(\d{1,2})(?:st|nd|rd|th)?\s+([A-Za-z]+)\.?,?\s+(\d{4})',s) or None
    if m and month(m.group(2)): return f'{int(m.group(1))} {month(m.group(2))} {m.group(3)}'
    m=re.fullmatch(r'([A-Za-z]+)\.?\s+(\d{1,2})(?:st|nd|rd|th)?,?\s+(\d{4})',s)
    if m and month(m.group(1)): return f'{int(m.group(2))} {month(m.group(1))} {m.group(3)}'
anchor_maps={}
stats={'release_headings':0,'section_headings':0,'item_headings':0,'dates':0}
for f in files:
    lines=open(f,encoding='utf-8',newline='').read().split('\n'); out=[]; code=False; amap={}
    for ln in lines:
        if ln.lstrip().startswith('```'): code=not code
        m=re.match(r'^(#{2,6}) (.*)$',ln) if not code else None
        if m:
            lv,h=m.groups(); t,eid=clean(h); new=t
            rh=release_heading(t,f) if len(lv)<=3 else None
            if rh: new=rh; stats['release_headings']+=1
            elif t.lower().rstrip(':').strip() in SECT and len(lv) in (3,4):
                new=SECT[t.lower().rstrip(':').strip()]; stats['section_headings']+=1
            else:
                n2=re.sub(r'^\d+\.\s+','',t)
                if n2!=t: stats['item_headings']+=1
                new=n2
            newln=f'{lv} {new}'
            if newln!=ln:
                old_id=eid or slug(t); amap[old_id]=slug(new); amap.setdefault(slug(t),slug(new))
            out.append(newln); continue
        if not code and re.search(r'release date',ln,re.I):
            tail=''; core=ln.rstrip('\r')
            cr=ln[len(core):]
            while True:
                mm=re.search(r'(\\|<br>|&#x20;|\s)$',core)
                if not mm: break
                if mm.group(1) in ('\\','<br>') and not tail: tail=mm.group(1)
                core=core[:mm.start()]
            dm=DATE.match(core)
            if dm:
                d=norm_date(dm.group('a') or dm.group('b') or '')
                if d:
                    nl=f'**Release date:** {d}'+tail+cr
                    if nl!=ln: stats['dates']+=1
                    out.append(nl); continue
            report.append(('unparsed-date',f,ln.strip()))
        out.append(ln)
    new='\n'.join(out)
    if new!='\n'.join(lines): open(f,'w',encoding='utf-8',newline='').write(new)
    anchor_maps[f]={k:v for k,v in amap.items() if k!=v}
# update links that point at changed anchors in these files
allmd=[x for x in subprocess.run(['git','ls-files','*.md'],capture_output=True,text=True).stdout.split('\n') if x and not x.startswith(('autorabit-','explore-the-new-arm-ui.md','.gitbook/'))]
urlpath={f:(f[:-len('/README.md')] if f.endswith('/README.md') else f[:-3]) for f in anchor_maps}
links=0
for src in allmd:
    t=open(src,encoding='utf-8',newline='').read(); orig=t
    def fix(m):
        global links
        url,frag=m.group(1),m.group(2)
        if url.startswith('https://knowledgebase.autorabit.com/'):
            p=unquote(url.split('knowledgebase.autorabit.com/',1)[1]).strip('/')
            tgt=next((f for f,u in urlpath.items() if u==p),None)
        elif url.startswith('http'): return m.group(0)
        elif url=='' : tgt=src if src in anchor_maps else None
        else: tgt=os.path.normpath(os.path.join(os.path.dirname(src),unquote(url)))
        if tgt in anchor_maps and frag in anchor_maps[tgt]:
            links+=1; report.append(('link-updated',src,f'{url}#{frag} -> #{anchor_maps[tgt][frag]}'))
            return f'{url}#{anchor_maps[tgt][frag]}'
        return m.group(0)
    t=re.sub(r'((?:https://knowledgebase\.autorabit\.com/[^\s)"#<>]*)|(?:[^\s()"#<>]*\.md)|)#([A-Za-z0-9\-._]+)',fix,t)
    if t!=orig: open(src,'w',encoding='utf-8',newline='').write(t)
stats['links_updated']=links
with open(REPORT,'a',newline='') as fh:
    w=csv.writer(fh); [w.writerow((group,)+r) for r in report]
print(group,len(files),'files',stats,'| report rows',len(report))
