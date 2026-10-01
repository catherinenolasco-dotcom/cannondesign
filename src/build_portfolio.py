import base64,html,re,sys
from portfolio_content import *
import art_svgs
from plan_art import PLAN_ART
e=html.escape
def b64(p): return base64.b64encode(open(p,'rb').read()).decode()
HEAD="data:image/jpeg;base64,"+b64('/tmp/w/headshot.jpg')
BRAND="#ff2222"
def tool_card(i,title,items,unit,wide=False):
    if wide: bg,shapes,vb=art_svgs.hub()
    else: bg,shapes=art_svgs.ARTS[i](); vb="0 0 400 200"
    cols=['#1ea7e1','#ff2222','#0060a5','#bf0a30','#008b79','#a89f98']
    tag=cols[i%len(cols)]; tcol="#fff" if tag in('#0060a5','#bf0a30','#008b79','#ff2222') else "#1a1817"
    svg='<svg viewBox="%s" preserveAspectRatio="xMidYMid slice" aria-hidden="true"><rect width="1000" height="200" fill="%s"/>%s</svg>'%(vb,bg,shapes)
    lis="".join("<li>%s</li>"%e(t) for t in items)
    return '<article class="tcard%s"><div class="tart">%s<span class="tlabel" style="background:%s;color:%s">%d %s</span></div><div class="tbody"><h3>%s</h3><ul>%s</ul></div></article>'%(" wide" if wide else "",svg,tag,tcol,len(items),unit,e(title),lis)
def sec(id,cls,label,title,body,lede=None):
    return '<section id="%s" class="%s"><div class="wrap"><p class="eyebrow">%s</p><h2>%s</h2>%s%s</div></section>'%(id,cls,e(label),e(title),'<p class="lede">%s</p>'%e(lede) if lede else '',body)
def build(standalone):
    P=[]
    P.append('<div class="annc">A portfolio prepared for the Sr. Manager, HRIS &amp; Operations role at CannonDesign</div>')
    P.append('<header class="nav"><div class="wrap navin"><a class="brand" href="#top"><span class="mark" aria-hidden="true"></span>Catherine Nolasco</a><nav aria-label="Sections"><a href="#summary">Summary</a><a href="#fit">Role fit</a><a href="#results">Results</a><a href="#cases">Case studies</a><a href="#values">Values</a><a href="#tools">Tools</a><a href="#experience">Experience</a><a href="#plan">30-60-90</a><a href="#credentials">Credentials</a><a href="#kind">Kind words</a></nav></div></header>')
    P.append('<section id="top" class="hero"><div class="wrap herogrid"><div><p class="eyebrow lt">Sr. Manager, HRIS &amp; Operations | CannonDesign</p><h1>Catherine Nolasco</h1><p class="tag">people ops. <span>powered by AI.</span></p><p class="hlede">13+ years owning HR systems, data and operations, so the people side of work can stay human. SHRM-CP.</p><p class="kw">HRIS ownership | Implementations and migrations | Integrations | Data governance | Dashboards and reporting | Change management | Responsible AI</p><p><a class="btn" href="#fit">&rarr; See how I fit the role</a></p></div><div class="photo"><img src="%s" alt="Catherine Nolasco" width="340" height="427"></div></div></section>'%HEAD)
    P.append('<section class="stats"><div class="wrap statgrid">%s</div></section>'%''.join('<div class="stat"><b>%s</b><span>%s</span></div>'%(e(a),e(b)) for a,b in STATS))
    P.append(sec("summary","light","Summary","Systems that stay accurate, and people who trust them",'<ul class="sumlist">%s</ul>'%''.join('<li>%s</li>'%e(s) for s in SUMMARY_P)))
    P.append(sec("fit","cream","Role fit","What you will own, and what I have already done",'<div class="fitgrid">%s</div>'%''.join('<div class="fcard" style="background:%s;color:%s"><p class="flab">%s</p><h3>%s</h3><p>%s</p></div>'%(c,tc,e(l),e(h),e(b)) for l,h,c,tc,b in FIT)))
    P.append(sec("results","light","Results","Numbers behind the work",'<div class="resgrid">%s</div>'%''.join('<div class="rcard"><b>%s</b><h3>%s</h3><p>%s</p></div>'%(e(a),e(b),e(c)) for a,b,c in RESULTS)))
    cs=''
    for c in CASES:
        cs+='<article class="case" style="border-top:6px solid %s"><h3>%s</h3><p class="org">%s</p><p><b>Challenge</b><br>%s</p><p><b>What I did</b><br>%s</p><p class="resbox"><b>Result</b><br>%s</p><p><b>What I would do differently</b><br>%s</p><ul class="chips">%s</ul></article>'%(c['c'],e(c['t']),e(c['org']),e(c['ch']),e(c['did']),e(c['res']),e(c['diff']),''.join('<li>%s</li>'%e(x) for x in c['chips']))
    P.append(sec("cases","cream","Case studies","Five projects, told straight",'<div class="casegrid">%s</div>'%cs))
    vs=''.join('<div class="val"><h3 style="color:%s">%s</h3><p class="vq">%s %s</p><p>%s</p></div>'%(c,e(n),e(n),e(q),e(d)) for n,c,q,d in VALUES)
    P.append(sec("values","light","Values","Living-Centered Design, and where I have seen it in HR",'<div class="valgrid">%s</div><p class="small">Value lines are paraphrased from CannonDesign\'s public site; each pairing is something I actually did.</p>'%vs))
    tc=''.join(tool_card(i,t,it,u) for i,(t,it,u) in enumerate(TOOL_CARDS))
    tc+=tool_card(6,"Core competencies",COMPETENCIES,"areas",wide=True)
    P.append(sec("tools","cream","Tools and systems","What I work in",'<div class="tools">%s</div><p class="small">Card illustrations are simplified examples with sample shapes, not screenshots of real systems or data.</p>'%tc))
    ex=''
    for r in ROLES:
        ex+='<div class="exrole"><div class="exh"><h3>%s</h3><span>%s</span></div><p class="org">%s | %s</p><ul>%s</ul></div>'%(e(r['title']),e(r['dates']),e(r['org']),e(r['sub']),''.join('<li>%s</li>'%e(b) for b in r['bullets']))
    ex+='<div class="exrole"><div class="exh"><h3>Earlier experience</h3></div><ul class="early">%s</ul></div>'%''.join('<li><span>%s</span><em>%s</em></li>'%(e(a),e(b)) for a,b in EARLIER)
    P.append(sec("experience","light","Experience","Where I have done it",ex))
    s0=2013.0; s1=2026.6
    rows=''
    for n,a,b,top in ARC:
        x=(a[0]+(a[1]-1)/12-s0)/(s1-s0)*100; w=max((b[0]+(b[1]-1)/12)-(a[0]+(a[1]-1)/12),0.25)/(s1-s0)*100
        rows+='<div class="arow"><span class="an">%s</span><div class="atrack"><i style="left:%.2f%%;width:%.2f%%;background:%s"></i></div></div>'%(e(n),x,w,BRAND if top else '#1a1817')
    yrs=''.join('<span style="left:%.2f%%">%d</span>'%((y-s0)/(s1-s0)*100,y) for y in range(2013,2027,2))
    P.append(sec("arc","cream","Career arc","Drawn to scale",'<div class="arc">%s<div class="ayrs"><span class="an"></span><div class="atrack yr">%s</div></div></div>'%(rows,yrs)))
    plan=''.join('<div class="step"><span class="stag%s">%s</span><div class="pcard">%s<h3>%s</h3><ul>%s</ul></div></div>'%(" dark" if i==3 else "",e(a),PLAN_ART[i],e(b),''.join('<li>%s</li>'%e(x) for x in c)) for i,(a,b,c) in enumerate(PLAN))
    P.append(sec("plan","plansec","30-60-90","What I would do first","<div class=\"steps\">%s</div><p class=\"pnote\">This is a starting point. I would adjust it after the first conversations with HR, Finance, Payroll and Technology leaders.</p><div class=\"pcta\"><a class=\"btn dark\" href=\"mailto:%s\">Let&#39;s talk</a></div>"%(plan,EMAIL),"A proposed plan built around the priorities in the role description."))
    cred='<div class="credgrid"><div class="ccard"><h3>SHRM-CP</h3><p>Society for Human Resource Management<br>Issued Jan 2023, Expires Dec 2029</p></div><div class="ccard"><h3>Bachelor of Arts, Criminal Justice</h3><p>San Francisco State University</p></div><div class="ccard"><h3>Certificate in Human Resource Management</h3><p>California State University, Long Beach</p></div></div>'
    P.append(sec("credentials","light","Credentials","Certification and education",cred))
    tm=''.join('<blockquote class="tq"><p>%s</p><footer><b>%s</b>, %s | %s</footer></blockquote>'%(e(q),e(n),e(r),e(s)) for n,r,s,q in TESTIMONIALS)
    rc=''.join('<article class="rec"><h3>%s</h3><p class="org">%s</p><p class="org">%s</p>%s</article>'%(e(n),e(t),e(d),''.join('<p>%s</p>'%e(x) for x in body.split('\n\n'))) for n,t,d,body in RECS)
    P.append(sec("kind","cream","Kind words","What colleagues have said",'<div class="tqgrid">%s</div><h3 class="subh">LinkedIn recommendations</h3><div class="recs">%s</div>'%(tm,rc)))
    P.append('<footer class="foot"><div class="wrap"><h2>Let\'s design to flourish.</h2><p><a href="mailto:%s">%s</a> | %s | %s</p><p class="small">This page is an independent portfolio styled after the CannonDesign brand and is not affiliated with CannonDesign.</p></div></footer>'%(EMAIL,EMAIL,LINKEDIN,"SF Bay Area"))
    body='\n'.join(P)
    return body
CSS=r'''
:root{--ink:#1a1817;--cream:#e1dcd7;--light:#f3efeb;--white:#fff;--orange:#ff2222;--red:#ff2222;--ink2:#4a4642;--display:'Hanken Grotesk',Arial,sans-serif;--mono:'Hanken Grotesk',Arial,sans-serif}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;background:#f3efeb;color:#1a1817;font-family:'Hanken Grotesk',Arial,sans-serif;font-size:17px;line-height:1.55}
a{color:inherit}.wrap{max-width:1180px;margin:0 auto;padding:0 20px}
.annc{background:#ff2222;color:#fff;text-align:center;font-size:13px;padding:8px 16px}
.nav{position:sticky;top:env(safe-area-inset-top,0px);z-index:20;background:#1a1817;color:#fff}
.navin{display:flex;align-items:center;gap:20px;padding-top:12px;padding-bottom:12px}
.brand{display:flex;align-items:center;gap:10px;text-decoration:none;font-weight:600;white-space:nowrap}
.mark{width:26px;height:16px;border:4px solid #ff2222;border-radius:10px 4px 4px 10px;display:inline-block}
.nav nav{display:flex;gap:18px;overflow-x:auto;min-width:0;flex:1;justify-content:safe flex-end;font-size:14px;scrollbar-width:none}
.nav nav a{text-decoration:none;white-space:nowrap;color:#e1dcd7}.nav nav a:hover{color:#ff2222}
.hero{background:#1a1817;color:#fff;padding:60px 0 70px;border-bottom:1px solid #2c2926}
.herogrid{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,340px);gap:48px;align-items:center}
.eyebrow{font-size:12.5px;letter-spacing:.14em;text-transform:uppercase;font-weight:600;color:#ff2222;margin:0 0 14px}.eyebrow.lt{color:#e1dcd7}
.hero h1{font-weight:200;font-size:clamp(40px,6vw,80px);line-height:1.02;margin:0 0 14px}
.tag{font-weight:200;font-size:clamp(26px,3.6vw,44px);margin:0 0 18px;line-height:1.1}.tag span{color:#ff2222}
.hlede{font-size:19px;color:#e1dcd7;max-width:52ch;margin:0 0 14px}.kw{font-size:13px;color:#a89f98;max-width:60ch}
.btn{display:inline-block;background:#ff2222;color:#fff;padding:13px 22px;text-decoration:none;font-weight:600;border-radius:0;margin-top:10px}.btn.dark{background:#1a1817}
.photo{position:relative;justify-self:center;width:100%;max-width:320px}.photo::before{content:"";position:absolute;inset:16px -16px -16px 16px;background:#ff2222;z-index:0}
.photo img{position:relative;z-index:1;width:100%;height:auto;display:block;border-radius:4px}
.stats{background:#e1dcd7}.statgrid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:20px;padding-top:30px;padding-bottom:30px}
.stat b{display:block;font-weight:200;font-size:clamp(36px,5vw,58px);line-height:1;color:#1a1817}.stat span{font-size:14px;color:#4a4642}
section{padding:72px 0}.light{background:#f3efeb}.cream{background:#e1dcd7}
h2{font-weight:200;font-size:clamp(30px,4.4vw,52px);line-height:1.08;margin:0 0 22px;max-width:22ch}
h3{font-weight:600;line-height:1.15;margin:0 0 10px}
.lede{max-width:60ch;color:#4a4642;margin:0 0 26px}
.sumlist{margin:10px 0 0;padding-left:20px;max-width:75ch;display:grid;gap:12px;font-size:19px}.sumlist li::marker{color:#ff2222}
.fitgrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,320px),1fr));gap:16px;margin-top:16px}
.fcard{padding:26px 24px 30px;min-width:0}.flab{font-size:12px;letter-spacing:.14em;text-transform:uppercase;font-weight:600;margin:0 0 10px;opacity:.9}.fcard h3{font-weight:300;font-size:26px}.fcard p:last-child{margin:0;font-size:15.5px}
.resgrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,300px),1fr));gap:16px;margin-top:16px}
.rcard{background:#fff;padding:24px;min-width:0}.rcard b{display:block;font-weight:200;font-size:60px;line-height:1;color:#ff2222;margin-bottom:8px}.rcard h3{font-size:18px}.rcard p{margin:0;font-size:14.5px;color:#4a4642}
.casegrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,460px),1fr));gap:20px;margin-top:16px}
.case{background:#fff;padding:26px 26px 30px;min-width:0}.case h3{font-weight:300;font-size:27px}.org{font-size:13.5px;color:#4a4642;margin:0 0 14px}.case p{margin:0 0 12px;font-size:15.5px}
.resbox{background:#f3efeb;padding:12px 14px;border-left:4px solid #ff2222}
.chips{display:flex;flex-wrap:wrap;gap:8px;list-style:none;margin:6px 0 0;padding:0}.chips li{background:#1a1817;color:#fff;padding:6px 10px;font-size:11.5px;letter-spacing:.1em;text-transform:uppercase;font-weight:600}
.valgrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,300px),1fr));gap:24px;margin-top:16px}
.val{border-top:2px solid #1a1817;padding-top:16px;min-width:0}.val h3{font-weight:700;font-size:26px;letter-spacing:.02em;text-transform:uppercase}.vq{font-size:15px;color:#4a4642}.val p{margin:0 0 10px}
.small{font-size:13px;color:#4a4642;margin-top:18px}
.tools{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,360px),1fr));gap:28px;margin-top:32px}
.tcard{background:#fff;min-width:0;display:flex;flex-direction:column}.tcard.wide{grid-column:1/-1}
.tart{position:relative;aspect-ratio:2/1;overflow:hidden;background:#e1dcd7}.tart svg{position:absolute;inset:0;width:100%;height:100%;display:block}
.tcard.wide .tart{aspect-ratio:auto;height:150px}
.tlabel{position:absolute;top:16px;left:16px;font-size:12px;letter-spacing:.14em;text-transform:uppercase;font-weight:600;padding:10px 14px}
.tbody{padding:22px 20px 26px;min-width:0}.tbody h3{font-weight:300;font-size:28px;margin:0 0 18px}
.tcard ul{display:flex;flex-wrap:wrap;gap:8px;margin:0;padding:0;list-style:none}
.tcard li{font-size:12px;letter-spacing:.1em;text-transform:uppercase;font-weight:600;line-height:1.3;padding:10px 13px;background:#1ea7e1;color:#1a1817}
.tcard li:nth-child(8n+2){background:#ff2222;color:#fff}.tcard li:nth-child(8n+3){background:#1a1817;color:#fff}.tcard li:nth-child(8n+4){background:#bf0a30;color:#fff}.tcard li:nth-child(8n+5){background:#008b79;color:#fff}.tcard li:nth-child(8n+6){background:#0060a5;color:#fff}.tcard li:nth-child(8n+7){background:#a89f98}.tcard li:nth-child(8n+8){background:#e1dcd7}
.exrole{padding:22px 0;border-top:1px solid #cfc8c1}.exh{display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap}.exh h3{font-weight:300;font-size:26px}.exh span{color:#4a4642;font-size:15px}
.exrole ul{margin:6px 0 0;padding-left:20px;display:grid;gap:8px;font-size:15.5px}.exrole li::marker{color:#ff2222}
.early{padding-left:0!important;list-style:none}.early li{display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap}.early em{font-style:normal;color:#4a4642}
.arc{margin-top:20px;display:grid;gap:8px}.arow,.ayrs{display:grid;grid-template-columns:minmax(110px,190px) minmax(0,1fr);gap:12px;align-items:center}
.an{font-size:13.5px}.atrack{position:relative;height:14px;background:#d4cdc6}.atrack i{position:absolute;top:0;bottom:0;display:block}.atrack.yr{background:none;height:20px}.atrack.yr span{position:absolute;font-size:12px;color:#4a4642;transform:translateX(-50%)}
.plansec{background:#e1dcd7}.plansec .wrap>h2,.plansec .wrap>.lede,.plansec .wrap>.eyebrow{text-align:center;margin-left:auto;margin-right:auto}.plansec .lede{max-width:60ch}
.steps{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:16px;margin-top:40px;position:relative}.steps::before{content:"";position:absolute;left:6%;right:6%;top:19px;border-top:2px dashed #1a181733}
.step{display:flex;flex-direction:column;align-items:center;min-width:0;position:relative}
.stag{background:#fff;font-size:13px;letter-spacing:.14em;text-transform:uppercase;font-weight:600;padding:11px 18px;margin-bottom:22px;position:relative;white-space:nowrap}.stag.dark{background:#1a1817;color:#e1dcd7}
.pcard{background:#fff;border-radius:18px;padding:24px 22px 28px;width:100%;flex:1;min-width:0}.pcard svg{display:block;width:120px;height:auto;margin-bottom:20px}.pcard h3{font-weight:300;font-size:27px;margin:0 0 14px}
.pcard ul{margin:0;padding-left:18px;display:grid;gap:9px;font-size:15px;line-height:1.45}.pcard li::marker{color:#ff2222}
.pnote{margin:28px auto 0;color:#4a4642;max-width:70ch;text-align:center;font-size:14px}.pcta{text-align:center;margin-top:20px}
.credgrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,300px),1fr));gap:16px;margin-top:16px}.ccard{background:#fff;padding:24px;border-top:6px solid #ff2222}.ccard h3{font-weight:300;font-size:24px}.ccard p{margin:0;color:#4a4642}
.tqgrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,340px),1fr));gap:16px;margin-top:16px}
.tq{margin:0;background:#fff;padding:24px;border-left:6px solid #ff2222;min-width:0}.tq p{margin:0 0 12px;font-size:16px}.tq footer{font-size:13.5px;color:#4a4642}
.subh{font-weight:200;font-size:34px;margin:48px 0 16px}
.recs{display:grid;gap:16px}.rec{background:#fff;padding:26px;min-width:0}.rec h3{font-weight:600;font-size:22px;margin:0 0 4px}.rec .org{margin:0 0 4px}.rec p{margin:12px 0 0;font-size:15.5px}.rec .org+.org{margin-bottom:12px}
.foot{background:#1a1817;color:#e1dcd7;padding:64px 0}.foot h2{font-weight:200;color:#fff}.foot a{color:#ff2222}.foot .small{color:#a89f98}
@media(max-width:820px){.herogrid{grid-template-columns:minmax(0,1fr)}.photo{max-width:300px;margin:10px auto 0}.statgrid{grid-template-columns:repeat(2,minmax(0,1fr))}.steps{grid-template-columns:repeat(2,minmax(0,1fr))}.steps::before{display:none}.arow,.ayrs{grid-template-columns:100px minmax(0,1fr)}}
@media(max-width:600px){.steps{grid-template-columns:minmax(0,1fr)}.step{align-items:flex-start}section{padding:52px 0}.navin{gap:12px}.brand{font-size:14px}}
'''
FONTCSS=''.join("@font-face{font-family:'Hanken Grotesk';font-weight:%s;font-style:normal;src:url(data:font/woff2;base64,%s) format('woff2')}"%(w,b64('/tmp/w/node_modules/@fontsource/hanken-grotesk/files/hanken-grotesk-latin-%s-normal.woff2'%w)) for w in (200,300,400,600,700))
body=build(True)
title="Catherine Nolasco"
standalone='<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>%s</title><style>%s%s</style></head><body>%s</body></html>'%(title,FONTCSS,CSS,body)
open('/tmp/w/portfolio_standalone.html','w').write(standalone)
art='<title>%s</title><link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Hanken+Grotesk:wght@200;300;400;600;700&display=swap" rel="stylesheet"><style>%s</style>%s'%(title,CSS,body)
open('/tmp/w/portfolio_artifact.html','w').write(art)
print(len(standalone),len(art))
