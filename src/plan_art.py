# ---- 30-60-90 plan step cards (PLAN_ART, CSS, builder) ----
PLAN_ART = [
    '<svg viewBox="0 0 120 100" aria-hidden="true"><path d="M8 18 L92 8 L100 70 L18 88Z" fill="#bf0a30"/><rect x="24" y="22" width="56" height="30" rx="6" fill="#1a1817"/><path d="M36 52 l-4 12 l14 -12z" fill="#1a1817"/><rect x="50" y="44" width="52" height="28" rx="6" fill="#f3efeb" stroke="#1a1817" stroke-width="2"/><path d="M84 72 l6 12 l2 -12z" fill="#f3efeb" stroke="#1a1817" stroke-width="2"/><path d="M34 34h36M34 42h22M60 54h32M60 62h20" stroke="#f3efeb" stroke-width="3" opacity=".9"/></svg>',
    '<svg viewBox="0 0 120 100" aria-hidden="true"><path d="M6 30 Q30 4 70 12 L108 26 L96 84 L14 90Z" fill="#0060a5"/><path d="M22 70 Q40 40 62 56 T98 34" stroke="#f3efeb" stroke-width="3" fill="none" stroke-dasharray="5 5"/><circle cx="22" cy="70" r="6" fill="#f3efeb"/><circle cx="62" cy="56" r="6" fill="#ff2222"/><circle cx="98" cy="34" r="6" fill="#f3efeb"/><rect x="50" y="14" width="34" height="22" fill="#1a1817"/><path d="M56 22h22M56 29h14" stroke="#f3efeb" stroke-width="3"/></svg>',
    '<svg viewBox="0 0 120 100" aria-hidden="true"><circle cx="54" cy="44" r="38" fill="#008b79"/><path d="M8 92 L70 78 L112 92Z" fill="#1ea7e1"/><rect x="30" y="50" width="14" height="30" fill="#1a1817"/><rect x="50" y="36" width="14" height="44" fill="#ff2222"/><rect x="70" y="20" width="14" height="60" fill="#1a1817"/><path d="M28 40 L56 26 L90 10" stroke="#f3efeb" stroke-width="3" fill="none"/></svg>',
    '<svg viewBox="0 0 120 100" aria-hidden="true"><circle cx="62" cy="48" r="40" fill="#ff2222"/><circle cx="20" cy="20" r="5" fill="#1a1817"/><circle cx="32" cy="10" r="3" fill="#1a1817"/><path d="M50 84 V22" stroke="#1a1817" stroke-width="4"/><path d="M52 22 L92 34 L52 48Z" fill="#f3efeb" stroke="#1a1817" stroke-width="3" stroke-linejoin="round"/></svg>',
]

PLAN_CSS = r"""
.plansec{background:var(--cream)}
.plansec .wrap>h2,.plansec .wrap>.lede{text-align:center;margin-left:auto;margin-right:auto}
.plansec .lede{max-width:60ch}
.steps{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:16px;margin-top:40px;position:relative}
.steps::before{content:"";position:absolute;left:6%;right:6%;top:19px;border-top:2px dashed #1a181733}
.step{display:flex;flex-direction:column;align-items:center;min-width:0;position:relative}
.stag{background:var(--white);font-family:var(--mono);font-size:13px;letter-spacing:.14em;text-transform:uppercase;padding:11px 18px;margin-bottom:22px;position:relative;white-space:nowrap}
.stag.dark{background:var(--ink);color:var(--cream)}
.pcard{background:var(--white);border-radius:18px;padding:24px 22px 28px;width:100%;flex:1;min-width:0}
.pcard svg{display:block;width:120px;height:auto;margin-bottom:20px}
.pcard h3{font-size:27px;line-height:1.12;margin:0 0 14px}
.pcard ul{margin:0;padding-left:18px;display:grid;gap:9px;font-size:15px;line-height:1.45}
.pcard li::marker{color:var(--orange)}
.pnote{margin:28px auto 0;color:var(--ink2);max-width:70ch;text-align:center;font-size:14px}
.pcta{text-align:center;margin-top:30px}
@media(max-width:980px){.steps{grid-template-columns:repeat(2,minmax(0,1fr))}.steps::before{display:none}}
@media(max-width:600px){.steps{grid-template-columns:minmax(0,1fr)}.step{align-items:flex-start}}
"""

PLAN_BUILDER = r'''
    plan = "".join(f'<div class="step"><span class="stag{" dark" if i == len(PLAN) - 1 else ""}">{e(a)}</span><div class="pcard">{PLAN_ART[i]}<h3>{e(b)}</h3><ul>' + "".join(f"<li>{e(x)}</li>" for x in c) + "</ul></div></div>" for i, (a, b, c) in enumerate(PLAN))
    p.append(sec("plan", "plansec", "30-60-90", "A proposed plan built around the success picture in the role description.", f'<div class="steps">{plan}</div><p class="pnote">This is a starting point. I would adjust it after the first conversations with the CEO, CFO and leadership team.</p><div class="pcta"><a class="btn" href="mailto:{EMAIL}">Let\'s talk</a></div>'))
'''
