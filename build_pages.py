#!/usr/bin/env python3
"""Generator for the Scarlet Rox Salon concept proposal site.
Single source of truth for business facts lives in assets/site.js (SRX) AND here
(SRX_PY) — both must match. Static HTML is shipped, so the generator mirrors the
same constant into the markup for no-JS readability."""
import os, html

OUT = os.path.dirname(os.path.abspath(__file__))

SRX_PY = {
    "name": "Scarlet Rox Salon and Lash Works LLC",
    "short": "Scarlet Rox",
    "street": "63 East Center Street",
    "city": "Moab",
    "state": "UT",
    "zip": "84532",
    "phone": "+1 435-260-8732",
    "phoneHref": "tel:+14352608732",
}
ADDR = f'{SRX_PY["street"]}, {SRX_PY["city"]}, {SRX_PY["state"]} {SRX_PY["zip"]}'

FONTS = ("https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300..600;"
         "1,9..144,300..600&family=Archivo:wght@400;500;600;700&display=swap")

NAV = [
    ("services.html", "Services"),
    ("hair.html", "Hair"),
    ("lashes.html", "Lashes"),
    ("nails.html", "Nails"),
    ("gallery.html", "Gallery"),
    ("reviews.html", "Reviews"),
]

# ---------------- SVG art (all original, created for this concept) ----------------
GRAIN = ('<filter id="gr"><feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" '
         'stitchTiles="stitch"/><feColorMatrix type="saturate" values="0"/>'
         '<feComponentTransfer><feFuncA type="linear" slope="0.05"/></feComponentTransfer>'
         '<feComposite operator="over" in2="SourceGraphic"/></filter>')


def svg_open(vb, label, ratio=1.0):
    w = 800
    h = int(800 / ratio)
    return (f'<svg viewBox="{vb}" role="img" aria-label="{html.escape(label)}" '
            f'preserveAspectRatio="xMidYMid slice" style="aspect-ratio:{w}/{h}">'
            f'<defs>{GRAIN}</defs>')


def art_desert_arch(label="Stylised desert arch at sunrise, terracotta and bone"):
    return (svg_open("0 0 800 640", label, 800/640) +
        '<rect width="800" height="640" fill="#efe3cb"/>'
        '<circle cx="400" cy="300" r="150" fill="#d9a58c"/>'
        '<circle cx="400" cy="300" r="108" fill="#e4d0ab"/>'
        '<path d="M140 640 L140 380 Q140 220 320 220 L480 220 Q660 220 660 380 L660 640 L580 640 L580 400 Q580 300 440 300 L360 300 Q220 300 220 400 L220 640 Z" fill="#a63f1d"/>'
        '<path d="M300 640 L300 460 Q300 380 380 380 Q460 380 460 460 L460 640 Z" fill="#f6f0e4"/>'
        '<rect y="560" width="800" height="80" fill="#7e2d12" opacity="0.85"/>'
        '<rect y="596" width="800" height="44" fill="#221511" opacity="0.9"/>'
        '<rect width="800" height="640" filter="url(#gr)"/></svg>')


def art_hair(label="Abstract flowing hair strands in ink and terracotta"):
    paths = "".join(
        f'<path d="M-20 {120+i*58} C 200 {100+i*58}, 340 {200+i*44}, 560 {140+i*52} S 780 {220+i*40}, 840 {180+i*48}" '
        f'fill="none" stroke="{"#221511" if i%3 else "#a63f1d"}" stroke-width="{5 if i%2 else 9}" stroke-linecap="round" opacity="{0.9 if i%2 else 0.55}"/>'
        for i in range(8))
    return (svg_open("0 0 800 620", label, 800/620) +
        '<rect width="800" height="620" fill="#d9a58c"/>' + paths +
        '<circle cx="640" cy="120" r="54" fill="#f6f0e4" opacity="0.7"/>'
        '<rect width="800" height="620" filter="url(#gr)"/></svg>')


def art_lash(label="Abstract eyelash curl strokes on dusty rose"):
    rows = ""
    for r in range(5):
        y = 120 + r * 92
        curls = "".join(
            f'<path d="M{60+c*118} {y} q 26 34 12 62" fill="none" stroke="#221511" stroke-width="7" stroke-linecap="round" opacity="0.85"/>'
            for c in range(6))
        rows += f'<path d="M40 {y+4} Q 400 {y-46} 760 {y+4}" fill="none" stroke="#a63f1d" stroke-width="5" opacity="0.8"/>' + curls
    return (svg_open("0 0 800 620", label, 800/620) +
        '<rect width="800" height="620" fill="#efe3cb"/>' + rows +
        '<rect width="800" height="620" filter="url(#gr)"/></svg>')


def art_nails(label="Abstract nail polish colour swatches in terracotta tones"):
    cells = ""
    tones = ["#a63f1d", "#7e2d12", "#d9a58c", "#c08a6e", "#221511", "#e4d0ab"]
    for i in range(12):
        x = 60 + (i % 4) * 180
        y = 70 + (i // 4) * 180
        t = tones[i % len(tones)]
        cells += (f'<rect x="{x}" y="{y}" width="120" height="140" rx="60" fill="{t}"/>'
                  f'<rect x="{x+18}" y="{y+22}" width="26" height="60" rx="13" fill="#ffffff" opacity="0.25"/>')
    return (svg_open("0 0 800 620", label, 800/620) +
        '<rect width="800" height="620" fill="#f6f0e4"/>' + cells +
        '<rect width="800" height="620" filter="url(#gr)"/></svg>')


def art_salon_interior(label="Abstract salon interior with arched mirrors"):
    return (svg_open("0 0 800 620", label, 800/620) +
        '<rect width="800" height="620" fill="#e4d0ab"/>'
        '<rect x="90" y="80" width="200" height="420" rx="100" fill="#f6f0e4" stroke="#221511" stroke-width="6"/>'
        '<rect x="510" y="80" width="200" height="420" rx="100" fill="#f6f0e4" stroke="#221511" stroke-width="6"/>'
        '<circle cx="190" cy="230" r="46" fill="#d9a58c"/><circle cx="610" cy="230" r="46" fill="#d9a58c"/>'
        '<rect x="330" y="200" width="140" height="300" rx="12" fill="#a63f1d"/>'
        '<rect x="352" y="500" width="96" height="16" rx="8" fill="#221511"/>'
        '<rect x="0" y="560" width="800" height="60" fill="#221511" opacity="0.88"/>'
        '<rect width="800" height="620" filter="url(#gr)"/></svg>')


def art_canyon(label="Layered canyon strata in warm tones"):
    bands = ["#7e2d12", "#a63f1d", "#c08a6e", "#d9a58c", "#e4d0ab"]
    rects = "".join(f'<rect y="{i*124}" width="800" height="124" fill="{bands[i]}"/>' for i in range(5))
    return (svg_open("0 0 800 620", label, 800/620) + rects +
        '<circle cx="400" cy="180" r="70" fill="#f6f0e4" opacity="0.85"/>'
        '<rect width="800" height="620" filter="url(#gr)"/></svg>')


def art_tools(label="Abstract salon tools, scissors and brush strokes"):
    return (svg_open("0 0 800 620", label, 800/620) +
        '<rect width="800" height="620" fill="#efe3cb"/>'
        '<circle cx="400" cy="310" r="200" fill="none" stroke="#221511" stroke-width="8"/>'
        '<circle cx="400" cy="310" r="160" fill="none" stroke="#a63f1d" stroke-width="4"/>'
        '<path d="M250 470 L550 150 M250 150 L550 470" stroke="#221511" stroke-width="10" stroke-linecap="round"/>'
        '<circle cx="250" cy="470" r="26" fill="none" stroke="#221511" stroke-width="10"/>'
        '<circle cx="250" cy="150" r="26" fill="none" stroke="#221511" stroke-width="10"/>'
        '<circle cx="550" cy="150" r="14" fill="#a63f1d"/><circle cx="550" cy="470" r="14" fill="#a63f1d"/>'
        '<rect width="800" height="620" filter="url(#gr)"/></svg>')


def art_chair(label="Abstract styling chair silhouette"):
    return (svg_open("0 0 800 620", label, 800/620) +
        '<rect width="800" height="620" fill="#d9a58c"/>'
        '<rect x="300" y="140" width="200" height="280" rx="90" fill="#221511"/>'
        '<rect x="270" y="380" width="260" height="60" rx="30" fill="#221511"/>'
        '<rect x="385" y="440" width="30" height="120" fill="#221511"/>'
        '<ellipse cx="400" cy="580" rx="120" ry="14" fill="#7e2d12"/>'
        '<circle cx="620" cy="120" r="50" fill="#f6f0e4" opacity="0.7"/>'
        '<rect width="800" height="620" filter="url(#gr)"/></svg>')


def brand_mark():
    return ('<svg viewBox="0 0 48 48" aria-hidden="true">'
            '<circle cx="24" cy="24" r="22" fill="none" stroke="#a63f1d" stroke-width="3"/>'
            '<path d="M12 36 L12 26 Q12 14 24 14 Q36 14 36 26 L36 36" fill="none" stroke="#221511" stroke-width="3.5" stroke-linecap="round"/>'
            '<circle cx="24" cy="30" r="4.5" fill="#a63f1d"/></svg>')


# ---------------- page framework ----------------
def head(title, desc, page):
    navlinks = "".join(
        f'<a href="{href}"{" aria-current=\"page\"" if page == href else ""}>{label}</a>'
        for href, label in NAV)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:type" content="website">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="{FONTS}" rel="stylesheet">
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-head">
<div class="wrap head-in">
<a class="brand" href="index.html" aria-label="{html.escape(SRX_PY['name'])} home">{brand_mark()}
<span class="brand-name">{html.escape(SRX_PY['short'])}<small>Salon &amp; Lash Works</small></span></a>
<button class="burger" aria-expanded="false" aria-label="Open menu"><span></span><span></span><span></span></button>
<nav class="nav" aria-label="Primary">{navlinks}<a class="btn" href="booking.html">Book a visit</a></nav>
<a class="btn head-cta" href="booking.html">Book a visit</a>
</div>
</header>
<main id="main">
"""


def footer():
    cols = "".join(
        f'<a href="{href}">{label}</a>' for href, label in
        [("services.html", "All services"), ("hair.html", "Hair studio"), ("lashes.html", "Lash studio"),
         ("nails.html", "Nails"), ("pricing.html", "Pricing"), ("team.html", "About & team")])
    return f"""</main>
<footer>
<div class="wrap">
<div class="foot-grid">
<div>
<div class="foot-brand">{html.escape(SRX_PY['short'])}</div>
<address><span data-srx="fullAddress">{html.escape(ADDR)}</span><br>
<a href="{SRX_PY['phoneHref']}" data-srx="phoneHref" style="color:var(--on-dark)"><span data-srx="phone">{html.escape(SRX_PY['phone'])}</span></a></address>
</div>
<div><h4>Visit</h4>{cols}</div>
<div><h4>More</h4><a href="gallery.html">Gallery</a><a href="reviews.html">Reviews</a><a href="booking.html">Book a visit</a></div>
<div><h4>Legal</h4><a href="privacy.html">Privacy policy</a><a href="terms.html">Terms</a></div>
</div>
<div class="foot-base">
<span>Concept proposal built by <a href="https://tiyandegital.com">Tiyan Digital</a> for {html.escape(SRX_PY['name'])}. All services, prices and hours shown are samples.</span>
<span>Imagery is original art made for this concept — no client photos yet.</span>
</div>
</div>
</footer>
<div class="cookie-bar" id="cookiebar" role="dialog" aria-label="Cookie notice">
<p>This concept demo sets no cookies of its own. A live site would explain any analytics here. <a href="privacy.html">Privacy policy</a></p>
<button class="btn light" id="cookie-accept">Got it</button>
<button class="btn ghost" id="cookie-decline">Decline</button>
</div>
<script src="assets/site.js" defer></script>
</body>
</html>
"""


def sample_note(extra=""):
    return (f'<div class="sample-note" role="note"><strong>Honest note:</strong> the salon has no website today, '
            f'so every service, price and hour below is a <strong>sample</strong> written to show how the real menu '
            f'would read. Real details come from the salon directly. {extra}</div>')


def closing_band(title, text):
    return f"""<div class="wrap"><div class="closing rv">
<span class="label">Ready when you are</span>
<h2>{title}</h2>
<p>{text}</p>
<div class="btn-row">
<a class="btn" href="booking.html">Book a visit</a>
<a class="btn light" href="{SRX_PY['phoneHref']}">Call {html.escape(SRX_PY['phone'])}</a>
</div></div></div>"""


def call_strip():
    return f"""<div class="call-strip rv">
<div><span class="label">Prefer to talk it through?</span><br>
<a class="big" href="{SRX_PY['phoneHref']}">{html.escape(SRX_PY['phone'])}</a></div>
<a class="btn ghost" href="booking.html" style="margin-left:auto">Request online instead</a>
</div>"""


def write(name, body):
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(body)
    print("wrote", name)

# ================= HOME =================
def page_index():
    return head(
        f"{SRX_PY['short']} — Hair, Lashes & Nails in {SRX_PY['city']}, {SRX_PY['state']}",
        f"Full-service salon in {SRX_PY['city']}, {SRX_PY['state']}: precision hair, lash artistry and nails. Book a visit at {SRX_PY['short']}.",
        "index.html") + f"""
<section class="hero"><div class="wrap hero-grid">
<div class="rv">
<span class="eyebrow">{html.escape(SRX_PY['street'])} &middot; {html.escape(SRX_PY['city'])}, {html.escape(SRX_PY['state'])}</span>
<h1>Hair, lashes &amp; nails, <em>done right</em> in Moab.</h1>
<p class="lede">A full-service salon on East Center Street for cuts, lived-in colour, lash sets and nails —
one chair, one stylist, your full attention. Walk out feeling like the best version of yourself.</p>
<div class="hero-cta">
<a class="btn" href="booking.html">Book a visit</a>
<a class="btn ghost" href="services.html">See services</a>
</div>
<p class="hero-note">Prefer to talk? <a href="{SRX_PY['phoneHref']}">{html.escape(SRX_PY['phone'])}</a> — a real person answers.</p>
</div>
<div class="hero-art rv">
<div class="art-frame">{art_desert_arch()}<span class="stamp sample">Concept art</span></div>
</div>
</div></section>

<div class="marquee" aria-hidden="true"><div class="marquee-track">
<span>Precision cuts</span><i>&#9670;</i><span>Lived-in colour</span><i>&#9670;</i><span>Lash sets</span><i>&#9670;</i><span>Manicures</span><i>&#9670;</i><span>Pedicures</span><i>&#9670;</i><span>Bridal parties</span><i>&#9670;</i>
<span>Precision cuts</span><i>&#9670;</i><span>Lived-in colour</span><i>&#9670;</i><span>Lash sets</span><i>&#9670;</i><span>Manicures</span><i>&#9670;</i><span>Pedicures</span><i>&#9670;</i><span>Bridal parties</span><i>&#9670;</i>
</div></div>

<section class="section"><div class="wrap">
<div class="sec-head rv">
<span class="eyebrow">The lookbook</span>
<h2>Three chairs. <em>One standard:</em> yours.</h2>
<p>Drag through the studios. Every look below is a starting point — your stylist builds the plan with you, in the chair, before a single snip or lash goes on.</p>
</div>
<div class="lookbook rv">
<div class="lookbook-top">
<h2>Pick your ritual</h2>
<span class="label">Drag or use the arrows</span>
</div>
<div class="lb-stage" tabindex="0" role="region" aria-label="Lookbook scrubber">
<div class="lb-track">
<div class="lb-slide" aria-hidden="false">
<div class="lb-art">{art_hair("Abstract flowing hair strands")}</div>
<div class="lb-copy"><span class="label">Studio 01 — Hair</span>
<h3>The cut that grows out beautifully.</h3>
<p>Precision cuts and lived-in colour planned around how your hair actually behaves between visits — desert air, hard water and all.</p>
<p><a class="btn light" href="hair.html">Explore hair</a></p></div>
</div>
<div class="lb-slide" aria-hidden="true">
<div class="lb-art">{art_lash("Abstract eyelash curl strokes")}</div>
<div class="lb-copy"><span class="label">Studio 02 — Lashes</span>
<h3>Lashes with intention.</h3>
<p>Classic, hybrid and volume sets mapped to your eye shape — never a one-size strip, never rushed. Fills keep them flawless.</p>
<p><a class="btn light" href="lashes.html">Explore lashes</a></p></div>
</div>
<div class="lb-slide" aria-hidden="true">
<div class="lb-art">{art_nails("Abstract nail colour swatches")}</div>
<div class="lb-copy"><span class="label">Studio 03 — Nails</span>
<h3>Nails that survive real life.</h3>
<p>Structured manicures and pedicures with careful prep — the part you feel for weeks, not the part you see in photos.</p>
<p><a class="btn light" href="nails.html">Explore nails</a></p></div>
</div>
</div>
</div>
<div class="lb-ctrl">
<button class="lb-prev" aria-label="Previous look">&#8592;</button>
<button class="lb-next" aria-label="Next look">&#8594;</button>
<div class="lb-dots" role="tablist" aria-label="Choose look">
<button role="tab" aria-label="Hair look"></button>
<button role="tab" aria-label="Lash look"></button>
<button role="tab" aria-label="Nail look"></button>
</div>
<span class="lb-count" aria-live="polite">01 / 03</span>
</div>
</div>
</div></section>

<section class="section tint"><div class="wrap">
<div class="sec-head rv">
<span class="eyebrow">Services</span>
<h2>Everything under <em>one roof.</em></h2>
<p>One visit can cover the cut, the lashes and the nails. Start with what you need most.</p>
</div>
<ul class="svc-list rv">
<li><a class="svc-row" href="hair.html"><span class="svc-num">01</span><div><h3>Hair studio</h3><p>Cuts, lived-in colour, blonding, smoothing and styling — planned around your hair, not a trend board.</p></div><span class="svc-arrow" aria-hidden="true">&#8594;</span></a></li>
<li><a class="svc-row" href="lashes.html"><span class="svc-num">02</span><div><h3>Lash studio</h3><p>Classic, hybrid and volume sets plus lifts — mapped to your eyes, with fills that keep them fresh.</p></div><span class="svc-arrow" aria-hidden="true">&#8594;</span></a></li>
<li><a class="svc-row" href="nails.html"><span class="svc-num">03</span><div><h3>Nails</h3><p>Structured manicures, pedicures and art — prep-first work that lasts past the photo.</p></div><span class="svc-arrow" aria-hidden="true">&#8594;</span></a></li>
</ul>
</div></section>

<section class="section"><div class="wrap">
<div class="split rv">
<div>
<span class="eyebrow">Why it works</span>
<h2 style="margin:16px 0">A small salon does <em>one thing</em> better: listen.</h2>
<p>No conveyor belt, no upsell script. Your appointment starts with a real consultation — what you like, what you don't, what your mornings look like — and the plan is built from that.</p>
<ul class="check-list" style="margin-top:22px">
<li>Consultation before every first service</li>
<li>One stylist from hello to goodbye</li>
<li>Honest timelines — no double-booked rushing</li>
<li>Aftercare you can actually follow at home</li>
</ul>
<div style="margin-top:28px"><a class="btn" href="team.html">Meet the salon</a></div>
</div>
<div><div class="art-frame">{art_salon_interior()}<span class="stamp sample">Concept art</span></div></div>
</div>
</div></section>

<section class="section tint"><div class="wrap">
<div class="sec-head rv">
<span class="eyebrow">From the chair</span>
<h2>What reviewers <em>mention by name.</em></h2>
<p>Public reviews on Yelp and BestProsInTown name stylist <strong>Missy</strong> — the quotes below are illustrative placeholders showing how real client words would appear here.</p>
</div>
<div class="rev-card rv">
<blockquote>"The kind of cut that still looks intentional six weeks later."</blockquote>
<p class="who">Illustrative sample &mdash; replace with a real client quote</p>
</div>
<div class="rev-card rv">
<blockquote>"My lashes looked like mine, only better. That's exactly what I asked for."</blockquote>
<p class="who">Illustrative sample &mdash; replace with a real client quote</p>
</div>
<div style="margin-top:24px"><a class="btn ghost" href="reviews.html">Read the reviews page</a></div>
</div></section>

<section class="section"><div class="wrap">
<div class="bento rv">
<figure class="w7">{art_hair("Abstract flowing hair")}<figcaption>Concept &mdash; hair</figcaption></figure>
<figure class="w5">{art_lash("Abstract lash curls")}<figcaption>Concept &mdash; lashes</figcaption></figure>
<figure class="w5">{art_nails("Abstract nail swatches")}<figcaption>Concept &mdash; nails</figcaption></figure>
<figure class="w7">{art_canyon("Layered canyon strata")}<figcaption>Moab, always</figcaption></figure>
</div>
<div style="margin-top:26px"><a class="btn ghost" href="gallery.html">Open the gallery</a></div>
</div></section>

<section class="section" style="padding-top:0">""" + closing_band(
    "Your chair is waiting.",
    f"{SRX_PY['short']} sits at {ADDR}. Request a visit online in under a minute — or call and talk it through with a real person.") + """</section>
""" + footer()

# ================= SERVICES =================
SERVICES = [
    ("hair.html", "Hair studio",
     "Cuts and colour that work with real life — desert air, hard water, busy mornings.",
     [("Signature cut", "Consultation, cleanse, precision cut and finish styling.", "from $65"),
      ("Lived-in colour", "Dimensional colour that grows out softly — fewer appointments, no harsh lines.", "from $140"),
      ("Full blonding", "Foils or balayage with bond care and a gloss to finish.", "from $180"),
      ("Smoothing treatment", "Frizz control that lasts for months, not days.", "from $120"),
      ("Styling & updos", "Event styling, bridal parties and special occasions.", "from $55")]),
    ("lashes.html", "Lash studio",
     "Sets mapped to your eye shape — natural to dramatic, never rushed.",
     [("Classic set", "One extension per natural lash. The 'are they real?' look.", "from $110"),
      ("Hybrid set", "A mix of classic and volume for texture with softness.", "from $135"),
      ("Volume set", "Full, fluffy density built lash by lash.", "from $160"),
      ("Lash lift & tint", "Your natural lashes, curled and darkened for 6–8 weeks.", "from $75"),
      ("Lash fill", "Keeps any set fresh — recommended every 2–3 weeks.", "from $55")]),
    ("nails.html", "Nails",
     "Prep-first manicures and pedicures — the part you feel for weeks.",
     [("Structured manicure", "Careful cuticle work, shaping and long-wear polish.", "from $45"),
      ("Luxury pedicure", "Soak, exfoliation, massage and polish. The full reset.", "from $60"),
      ("Gel manicure", "Chip-resistant colour that holds through real life.", "from $55"),
      ("Nail art", "Hand-painted details, from minimal lines to full sets.", "from $15"),
      ("Polish change", "Quick refresh between full services.", "from $20")]),
]


def page_services():
    acc = ""
    for i, (href, title, blurb, items) in enumerate(SERVICES):
        rows = "".join(
            f'<div class="menu-item"><h4>{n}</h4><span class="price">{p} <span class="badge-sample">Sample</span></span><p>{d}</p></div>'
            for n, d, p in items)
        acc += (f'<div class="acc-item"><button class="acc-btn" aria-expanded="{"true" if i == 0 else "false"}" '
                f'aria-controls="acc{i}">{title}<span class="plus" aria-hidden="true">+</span></button>'
                f'<div class="acc-panel" id="acc{i}"{" style=\"max-height:none\"" if i == 0 else ""}><div>'
                f'<p style="margin-bottom:14px">{blurb}</p>{rows}'
                f'<p style="margin-top:16px"><a href="{href}">Open the {title.lower()} page &#8594;</a></p>'
                f'</div></div></div>')
    return head("Services — " + SRX_PY["short"],
                f"Full service menu: hair, lashes and nails at {SRX_PY['short']} in {SRX_PY['city']}, {SRX_PY['state']}.",
                "services.html") + f"""
<div class="wrap"><div class="page-hero rv">
<span class="crumb"><a href="index.html">Home</a> / Services</span>
<h1>One salon, <em>three studios.</em></h1>
<p class="lede">Hair, lashes and nails under one roof — book them together or one at a time.</p>
</div>
{sample_note()}
<div class="acc rv">{acc}</div>
{call_strip()}
</div>
<section class="section" style="padding-top:0">""" + closing_band(
    "Not sure where to start?",
    "Call and describe what you're after — you'll get an honest recommendation, not a sales pitch.") + """</section>
""" + footer()


def studio_page(page, title, crumb, h1, lede, art_fn, sections, why_list):
    blocks = ""
    for gtitle, items in sections:
        rows = "".join(
            f'<div class="menu-item"><h4>{n}</h4><span class="price">{p} <span class="badge-sample">Sample</span></span><p>{d}</p></div>'
            for n, d, p in items)
        blocks += f'<div class="menu-group"><h3>{gtitle}</h3>{rows}</div>'
    whys = "".join(f"<li>{w}</li>" for w in why_list)
    return head(f"{title} — {SRX_PY['short']}",
                f"{title} at {SRX_PY['short']}, {SRX_PY['city']} {SRX_PY['state']}: {lede[:120]}",
                page) + f"""
<div class="wrap"><div class="page-hero rv">
<span class="crumb"><a href="index.html">Home</a> / <a href="services.html">Services</a> / {crumb}</span>
<h1>{h1}</h1>
<p class="lede">{lede}</p>
</div>
<div class="hero-grid rv" style="margin-bottom:56px">
<div class="art-frame">{art_fn()}<span class="stamp sample">Concept art</span></div>
<div>
<span class="eyebrow">How it works here</span>
<ul class="check-list" style="margin-top:16px">{whys}</ul>
</div>
</div>
{sample_note()}
{blocks}
{call_strip()}
</div>
<section class="section" style="padding-top:0">""" + closing_band(
    "Book your " + crumb.lower() + " visit.",
    "Request online in under a minute, or call and talk it through first.") + """</section>
""" + footer()


def page_hair():
    return studio_page(
        "hair.html", "Hair studio", "Hair",
        "Hair that behaves <em>between</em> visits.",
        "Cuts and colour planned around your real routine — how often you wash, how you style, how Moab's dry air treats your ends.",
        art_hair,
        [("Cuts", [("Signature cut", "Consultation, cleanse, precision cut, finish.", "from $65"),
                   ("Restyle", "A full change — length, shape or both, planned together.", "from $80"),
                   ("Kids cut", "Patient, no-rush cuts for under-12s.", "from $35")]),
         ("Colour", [("Lived-in colour", "Dimensional, soft grow-out.", "from $140"),
                     ("Full blonding", "Foils or balayage with bond care + gloss.", "from $180"),
                     ("Grey blending", "Soft, low-maintenance coverage.", "from $110"),
                     ("Gloss & tone", "Refresh and shine between colour visits.", "from $55")]),
         ("Texture & events", [("Smoothing treatment", "Months of frizz control.", "from $120"),
                               ("Styling & updos", "Events, bridal parties, photos.", "from $55"),
                               ("Deep conditioning ritual", "Restorative mask + scalp massage.", "from $40")])],
        ["Consultation first — the plan is agreed before we start",
         "Colour formulas recorded, so results repeat",
         "Honest grow-out timelines — no surprise roots in week three",
         "Aftercare explained in plain language, not product-speak"])


def page_lashes():
    return studio_page(
        "lashes.html", "Lash studio", "Lashes",
        "Lashes mapped to <em>your</em> eyes.",
        "Classic, hybrid and volume sets designed around your eye shape and lash health — with fills that keep them flawless.",
        art_lash,
        [("Full sets", [("Classic set", "One extension per natural lash — the natural look.", "from $110"),
                        ("Hybrid set", "Classic + volume texture.", "from $135"),
                        ("Volume set", "Full, fluffy density.", "from $160"),
                        ("Mega volume", "Maximum drama, still healthy application.", "from $190")]),
         ("Natural options", [("Lash lift & tint", "Your lashes, curled and darkened — 6–8 weeks.", "from $75"),
                              ("Lash tint", "Darker natural lashes, no extensions.", "from $30")]),
         ("Maintenance", [("Lash fill (2–3 weeks)", "Keeps any set looking new.", "from $55"),
                          ("Lash removal", "Safe, gentle removal of old extensions.", "from $25")])],
        ["Eye-shape mapping before every first set",
         "Lash health checked at every fill — weak lashes get a rest, not more weight",
         "No-rush appointments — a full set takes the time it takes",
         "Aftercare card to take home, so retention actually holds"])


def page_nails():
    return studio_page(
        "nails.html", "Nails", "Nails",
        "Nails that survive <em>real life.</em>",
        "Structured manicures and pedicures with careful prep — because longevity lives in the prep, not the polish.",
        art_nails,
        [("Hands", [("Structured manicure", "Cuticle care, shaping, long-wear polish.", "from $45"),
                    ("Gel manicure", "Chip-resistant colour for weeks.", "from $55"),
                    ("Nail art", "Hand-painted, minimal to full sets.", "from $15"),
                    ("Polish change", "Quick refresh.", "from $20")]),
         ("Feet", [("Classic pedicure", "Soak, shaping, cuticle care, polish.", "from $50"),
                   ("Luxury pedicure", "Exfoliation, mask, massage — the full reset.", "from $60"),
                   ("Gel pedicure", "Long-wear colour for toes.", "from $65")]),
         ("Care", [("IBX repair treatment", "Strengthening for damaged nails.", "from $25"),
                   ("Paraffin add-on", "Deep moisture for hands.", "from $15")])],
        ["Prep-first: shaping and cuticle work before any colour",
         "Sanitised tools, fresh files — every client, every time",
         "Honest advice when a break would serve your nails better",
         "Art priced by detail, quoted before we start"])

# ================= GALLERY =================
GALLERY = [
    ("hair", "Hair", "Flowing lengths, lived-in tone", art_hair),
    ("lashes", "Lashes", "Curl, mapped and lifted", art_lash),
    ("nails", "Nails", "Colour stories in terracotta", art_nails),
    ("salon", "The space", "Arches, light and calm", art_salon_interior),
    ("hair", "Hair", "Shape that grows out well", art_hair),
    ("salon", "The space", "Your chair, ready", art_chair),
    ("nails", "Nails", "Prep-first finishes", art_nails),
    ("lashes", "Lashes", "Natural to dramatic", art_lash),
    ("salon", "The space", "Craft in the details", art_tools),
]


def page_gallery():
    figs = "".join(
        f'<figure data-cat="{cat}" class="rv"><div>{fn(f"Concept art — {cap.lower()}")}</div>'
        f'<figcaption><span class="label">{label} &middot; Concept</span>{cap}. Original art made for this proposal — the live site would show real salon photography.</figcaption></figure>'
        for cat, label, cap, fn in GALLERY)
    return head("Gallery — " + SRX_PY["short"],
                f"Concept gallery for {SRX_PY['short']} salon in {SRX_PY['city']}, {SRX_PY['state']}.",
                "gallery.html") + f"""
<div class="wrap"><div class="page-hero rv">
<span class="crumb"><a href="index.html">Home</a> / Gallery</span>
<h1>The work, <em>in pictures.</em></h1>
<p class="lede">Every image here is original concept art made for this proposal — clearly labelled. The live site would carry real photography of the salon's actual work, with client permission.</p>
</div>
<div class="gal-filters rv" role="group" aria-label="Filter gallery">
<button data-cat="all" aria-pressed="true">Everything</button>
<button data-cat="hair" aria-pressed="false">Hair</button>
<button data-cat="lashes" aria-pressed="false">Lashes</button>
<button data-cat="nails" aria-pressed="false">Nails</button>
<button data-cat="salon" aria-pressed="false">The space</button>
</div>
<div class="gal-grid">{figs}</div>
<div class="sample-note rv"><strong>Photography plan:</strong> a half-day shoot in the real salon — the chair, the tools, the light on East Center Street — replaces every concept image before launch. No stock faces, no borrowed work.</div>
</div>
<section class="section" style="padding-top:0">""" + closing_band(
    "Like what you see?",
    "Imagine this gallery filled with the salon's real work — then come make your own before-photo.") + """</section>
""" + footer()


# ================= TEAM =================
def page_team():
    return head("About & team — " + SRX_PY["short"],
                f"Meet the team at {SRX_PY['short']} salon, {SRX_PY['city']} {SRX_PY['state']}.",
                "team.html") + f"""
<div class="wrap"><div class="page-hero rv">
<span class="crumb"><a href="index.html">Home</a> / About</span>
<h1>A small salon with <em>high standards.</em></h1>
<p class="lede">{SRX_PY['short']} is a full-service salon on East Center Street in {SRX_PY['city']} — hair, lashes and nails, with the kind of attention only a small team can give.</p>
</div>
<div class="hero-grid rv" style="margin-bottom:56px">
<div class="art-frame">{art_canyon("Layered canyon strata, Moab")}<span class="stamp sample">Concept art</span></div>
<div>
<span class="eyebrow">The philosophy</span>
<h2 style="margin:14px 0 16px">Moab deserves a <em>great</em> salon.</h2>
<p>Between the river trips and the red rock, people here live outdoors — and still want to look sharp doing it. This salon was built for that life: colour that survives the sun, lashes that survive the river, nails that survive the trailhead.</p>
<p>Everything runs on appointments, every first visit starts with a consultation, and nobody is ever rushed out of the chair.</p>
</div>
</div>
<div class="sec-head rv"><span class="eyebrow">The team</span><h2>Faces <em>behind</em> the chair.</h2></div>
<div class="team-grid">
<div class="team-card rv">
<div class="art">{art_tools("Abstract salon tools")}</div>
<div class="bio"><h3>Missy</h3><span class="label">Stylist &middot; named in public reviews</span>
<p>Reviewers on Yelp and BestProsInTown mention Missy by name — the one verified team fact on this page. Everything else about the team below is illustrative until the salon confirms it.</p></div>
</div>
<div class="team-card rv">
<div class="art">{art_chair("Abstract styling chair")}</div>
<div class="bio"><h3>Your lash artist <span class="badge-sample">Sample</span></h3><span class="label">Lash studio</span>
<p>Placeholder profile showing where the lash artist's real bio, specialties and photo would appear. Real name, real credentials, real photo — supplied by the salon.</p></div>
</div>
</div>
{call_strip()}
</div>
<section class="section" style="padding-top:0">""" + closing_band(
    "Come say hello.",
    "The kettle's on and the consultation is free — book a visit or just call.") + """</section>
""" + footer()


# ================= PRICING =================
def page_pricing():
    groups = ""
    for href, title, blurb, items in SERVICES:
        rows = "".join(
            f'<tr><td><strong>{n}</strong><br><span style="color:var(--muted);font-size:14px">{d}</span></td>'
            f'<td style="text-align:right;font-family:var(--mono);font-size:14px;white-space:nowrap">{p} <span class="badge-sample">Sample</span></td></tr>'
            for n, d, p in items)
        groups += (f'<div class="menu-group"><h3>{title} <a href="{href}" style="font-size:14px;font-family:var(--sans)">Details &#8594;</a></h3>'
                   f'<table class="hours-table" style="max-width:100%"><tbody>{rows}</tbody></table></div>')
    return head("Pricing — " + SRX_PY["short"],
                f"Sample service pricing for {SRX_PY['short']} in {SRX_PY['city']}, {SRX_PY['state']}.",
                "pricing.html") + f"""
<div class="wrap"><div class="page-hero rv">
<span class="crumb"><a href="index.html">Home</a> / Pricing</span>
<h1>Honest prices, <em>quoted upfront.</em></h1>
<p class="lede">No surprises at the till. Final quotes are confirmed in your consultation — before any work begins.</p>
</div>
{sample_note("The salon sets every real price; nothing here is a quote.")}
{groups}
<div class="rev-proof rv">
<div class="cell"><h3>No hidden fees</h3><p>What's quoted is what's charged. Product and toner costs are included in colour quotes.</p></div>
<div class="cell"><h3>Deposits</h3><p>Longer appointments may ask for a small deposit — confirmed by phone, never a surprise.</p></div>
<div class="cell"><h3>Cancellations</h3><p>Life happens. 24 hours' notice lets us offer your chair to someone else.</p></div>
</div>
{call_strip()}
</div>
<section class="section" style="padding-top:0">""" + closing_band(
    "Get your exact quote.",
    "Tell us what you're dreaming of — we'll confirm the price before you commit to anything.") + """</section>
""" + footer()


# ================= REVIEWS =================
def page_reviews():
    return head("Reviews — " + SRX_PY["short"],
                f"What clients say about {SRX_PY['short']} salon in {SRX_PY['city']}, {SRX_PY['state']}.",
                "reviews.html") + f"""
<div class="wrap"><div class="page-hero rv">
<span class="crumb"><a href="index.html">Home</a> / Reviews</span>
<h1>Word of <em>mouth.</em></h1>
<p class="lede">The salon's public reviews on Yelp and BestProsInTown mention stylist <strong>Missy</strong> by name.
This concept page shows how verified reviews would be presented — every quote below is an <strong>illustrative placeholder</strong>, not a real client review.</p>
</div>
<div class="sample-note"><strong>Review policy for the live site:</strong> only genuine, attributed client reviews appear here —
never invented, never bought, never edited beyond typos. The salon approves every word.</div>
<div class="rev-card rv">
<blockquote>"Missy listened to what I actually wanted instead of doing the haircut she felt like doing. First time that's happened in years."</blockquote>
<p class="who">Illustrative sample &mdash; style of a real Yelp-style review, not a real quote</p>
</div>
<div class="rev-card rv">
<blockquote>"Booked lashes before a desert wedding. They photographed beautifully and lasted the whole trip."</blockquote>
<p class="who">Illustrative sample &mdash; style of a real Yelp-style review, not a real quote</p>
</div>
<div class="rev-card rv">
<blockquote>"Finally, a pedicure that didn't chip by day three. The prep work here is on another level."</blockquote>
<p class="who">Illustrative sample &mdash; style of a real Yelp-style review, not a real quote</p>
</div>
<div class="rev-proof rv">
<div class="cell"><h3>Where to read them</h3><p>Public reviews live on Yelp and BestProsInTown today — the live site would link directly to both profiles.</p></div>
<div class="cell"><h3>Just visited?</h3><p>The live site would include a private feedback form and a nudge to share public reviews — only if you loved it.</p></div>
<div class="cell"><h3>Our promise</h3><p>Every review shown here will be real, attributed and unedited. No exceptions, ever.</p></div>
</div>
{call_strip()}
</div>
<section class="section" style="padding-top:0">""" + closing_band(
    "Your turn to review.",
    "Book a visit, then tell Moab what you thought — honestly.") + """</section>
""" + footer()

# ================= BOOKING / CONTACT =================
def page_booking():
    return head("Book a visit — " + SRX_PY["short"],
                f"Request an appointment at {SRX_PY['short']}, {SRX_PY['street']}, {SRX_PY['city']} {SRX_PY['state']}.",
                "booking.html") + f"""
<div class="wrap"><div class="page-hero rv">
<span class="crumb"><a href="index.html">Home</a> / Booking</span>
<h1>Book <em>your</em> visit.</h1>
<p class="lede">Three steps, under a minute. This concept form shows the flow — the live site would confirm your slot by text or call.</p>
</div>
<div class="book-steps rv">
<div class="step"><span class="label">Step 1</span><p>Pick your service and a preferred day below.</p></div>
<div class="step"><span class="label">Step 2</span><p>We confirm your slot by phone or text — a real person, not a robot.</p></div>
<div class="step"><span class="label">Step 3</span><p>Arrive, consult, relax. Your stylist handles the rest.</p></div>
</div>
<div class="two-col">
<div class="rv">
<form class="book" id="bookform" novalidate>
<div class="field"><label for="b-name">Your name</label>
<input id="b-name" name="name" type="text" autocomplete="name" data-need required>
<span class="err">Please tell us your name.</span></div>
<div class="field"><label for="b-phone">Phone number</label>
<input id="b-phone" name="phone" type="tel" autocomplete="tel" data-need required>
<span class="hint">So we can confirm your slot. Nothing else, ever.</span>
<span class="err">Please add a phone number we can reach you on.</span></div>
<div class="field"><label for="b-service">Service</label>
<select id="b-service" name="service" data-need required>
<option value="">Choose a service&hellip;</option>
<option>Hair — cut</option><option>Hair — colour</option><option>Hair — styling / event</option>
<option>Lashes — full set</option><option>Lashes — fill</option><option>Lashes — lift &amp; tint</option>
<option>Nails — manicure</option><option>Nails — pedicure</option><option>Nails — nail art</option>
<option>Not sure yet — advise me</option>
</select><span class="err">Please choose a service (or "advise me").</span></div>
<div class="field"><label for="b-day">Preferred day</label>
<input id="b-day" name="day" type="text" placeholder="e.g. Thursday afternoon" data-need required>
<span class="err">Please suggest a day that suits you.</span></div>
<div class="field"><label for="b-notes">Anything we should know? <span style="font-weight:400;color:var(--faint)">(optional)</span></label>
<textarea id="b-notes" name="notes" rows="3" placeholder="Allergies, inspiration, timing&hellip;"></textarea></div>
<div class="field">
<div class="consent">
<input type="checkbox" id="b-consent" data-need required>
<label for="b-consent">I agree the salon may contact me about this booking request. My details are used only to arrange the visit — never shared, never marketed. <a href="privacy.html">Privacy policy</a></label>
</div>
<span class="err">Please tick the consent box so we can contact you.</span>
</div>
<button class="btn" type="submit">Request my appointment</button>
</form>
<div class="form-ok" id="bookok" role="status">
<h3>Request received — thank you.</h3>
<p><strong>Demo note:</strong> this concept form doesn't send anywhere yet. On the live site, your request would go straight to the salon, and a real person would confirm your slot by phone or text — usually the same day.</p>
<p>In the meantime, the fastest way to book is to call <a href="{SRX_PY['phoneHref']}">{html.escape(SRX_PY['phone'])}</a>.</p>
</div>
</div>
<div class="rv">
<span class="eyebrow">Visit us</span>
<h2 style="margin:14px 0">Find the salon.</h2>
<address style="font-style:normal;font-size:17px;line-height:1.8;margin-bottom:20px">
<strong>{html.escape(SRX_PY['name'])}</strong><br>
{html.escape(ADDR)}<br>
<a href="{SRX_PY['phoneHref']}">{html.escape(SRX_PY['phone'])}</a>
</address>
<table class="hours-table">
<caption class="label" style="text-align:left;margin-bottom:8px">Hours <span class="badge-sample">Sample</span></caption>
<tr><th scope="row">Tue – Fri</th><td>9:00a – 6:00p</td></tr>
<tr><th scope="row">Saturday</th><td>9:00a – 4:00p</td></tr>
<tr><th scope="row">Sun – Mon</th><td>Closed</td></tr>
</table>
<p style="font-size:14.5px;color:var(--faint)">Sample hours — the salon confirms real opening times by phone.</p>
<div class="sample-note" style="margin-top:24px"><strong>About booking today:</strong> the salon currently takes bookings through its Vagaro profile. This concept site demonstrates what an in-house booking flow would feel like — the live site would connect to the salon's real calendar.</div>
</div>
</div>
</div>
<section class="section" style="padding-top:0">""" + closing_band(
    "Rather just call?",
    f"{html.escape(SRX_PY['phone'])} — a real person answers during salon hours.") + """</section>
""" + footer()


# ================= LEGAL =================
def page_privacy():
    return head("Privacy policy — " + SRX_PY["short"],
                f"Privacy policy for the {SRX_PY['short']} concept website.",
                "privacy.html") + f"""
<div class="wrap"><div class="page-hero"><span class="crumb"><a href="index.html">Home</a> / Privacy</span>
<h1>Privacy, <em>in plain language.</em></h1></div>
<div class="legal rv">
<p><strong>Last updated:</strong> 3 November 2026. This is a concept proposal site for {html.escape(SRX_PY['name'])} ({html.escape(ADDR)}).</p>
<h2>What we collect</h2>
<ul><li><strong>Booking requests:</strong> your name, phone number, chosen service, preferred day and any notes you add — only what we need to arrange your visit.</li>
<li><strong>Nothing else.</strong> No accounts, no tracking profiles, no analytics on this concept demo.</li></ul>
<h2>Why we collect it</h2>
<p>To confirm your appointment. That's the entire list.</p>
<h2>What we never do</h2>
<ul><li>Never sell or share your details with anyone.</li><li>Never send marketing messages you didn't ask for.</li><li>Never keep your details longer than needed to run the booking.</li></ul>
<h2>Cookies</h2>
<p>This concept demo sets no cookies of its own. If the live site adds analytics, this page will name them and the cookie banner will ask first.</p>
<h2>Your rights</h2>
<p>Ask us to see, correct or delete your details any time — call <a href="{SRX_PY['phoneHref']}">{html.escape(SRX_PY['phone'])}</a>.</p>
<h2>Third parties</h2>
<p>Fonts load from Google Fonts (Google's privacy policy applies to that request). The live site will list every third-party service here.</p>
</div></div>
""" + footer()


def page_terms():
    return head("Terms — " + SRX_PY["short"],
                f"Terms of use for the {SRX_PY['short']} concept website.",
                "terms.html") + f"""
<div class="wrap"><div class="page-hero"><span class="crumb"><a href="index.html">Home</a> / Terms</span>
<h1>Terms, <em>kept simple.</em></h1></div>
<div class="legal rv">
<p><strong>Last updated:</strong> 3 November 2026. This is a concept proposal site for {html.escape(SRX_PY['name'])}.</p>
<h2>The concept</h2>
<p>All services, prices, hours, team details and imagery on this site are illustrative samples made to demonstrate the design — except the business name, address ({html.escape(ADDR)}), phone ({html.escape(SRX_PY['phone'])}) and the fact that reviewers name stylist Missy. Real details are confirmed by the salon.</p>
<h2>Bookings</h2>
<p>A booking request is a request, not a confirmed appointment — your slot is confirmed when the salon replies by phone or text.</p>
<h2>Cancellations</h2>
<p>Please give 24 hours' notice if you can't make it, so your chair can go to someone else.</p>
<h2>Content</h2>
<p>All artwork on this site was created for this concept. Don't reuse it without permission.</p>
<h2>Contact</h2>
<p>Questions about these terms: call <a href="{SRX_PY['phoneHref']}">{html.escape(SRX_PY['phone'])}</a>.</p>
</div></div>
""" + footer()


def page_404():
    return head("Page not found — " + SRX_PY["short"],
                "The page you're looking for isn't here.",
                "404.html") + f"""
<div class="wrap"><div class="notfound rv">
<div class="giant" aria-hidden="true">404</div>
<h1 style="margin:20px 0">That chair is <em>empty.</em></h1>
<p class="lede" style="margin:0 auto 30px">The page you're after doesn't exist — but a real appointment does.</p>
<div class="hero-cta" style="justify-content:center">
<a class="btn" href="index.html">Back home</a>
<a class="btn ghost" href="booking.html">Book a visit</a>
</div></div></div>
""" + footer()


PAGES = {
    "index.html": page_index,
    "services.html": page_services,
    "hair.html": page_hair,
    "lashes.html": page_lashes,
    "nails.html": page_nails,
    "gallery.html": page_gallery,
    "team.html": page_team,
    "pricing.html": page_pricing,
    "reviews.html": page_reviews,
    "booking.html": page_booking,
    "privacy.html": page_privacy,
    "terms.html": page_terms,
    "404.html": page_404,
}

if __name__ == "__main__":
    for name, fn in PAGES.items():
        write(name, fn())
    with open(os.path.join(OUT, "robots.txt"), "w") as f:
        f.write("User-agent: *\nAllow: /\n")
    with open(os.path.join(OUT, "sitemap.xml"), "w") as f:
        urls = "".join(f"  <url><loc>/{n}</loc></url>\n" for n in PAGES if n != "404.html")
        f.write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n')
    print("wrote robots.txt, sitemap.xml")
