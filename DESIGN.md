# DESIGN.md — Scarlet Rox Salon and Lash Works LLC (concept proposal)

Lead: Scarlet Rox Salon and Lash Works LLC, 63 East Center Street, Moab UT 84532 · phone +1 435-260-8732 · full-service salon (hair, lashes, nails) · stylist "Missy" named in Yelp/bestprosintown reviews · NO own website today (Vagaro booking profile only).
Built: 2026-11-03, lead-hunt-30min run. Suggested repo: `tiyandegital-hue/scarlet-rox-salon-proposal`.

## Tokens

| Token | Value | Role |
|---|---|---|
| `--canvas` | `#F6F0E4` | bone paper page background |
| `--surface` | `#EFE3CB` | tonal bands / cards |
| `--surface-2` | `#E4D0AB` | layered surface step |
| `--ink` | `#221511` | warm near-black (15.6:1 on canvas) |
| `--body` | `#4C3A2C` | body copy (9.5:1 on canvas) |
| `--muted` | `rgba(34,21,17,.62)` | secondary text (~6:1 on canvas) |
| `--line` | `rgba(34,21,17,.16)` | hairlines |
| `--accent` | `#A63F1D` | terracotta — the ONE CTA voltage color (white-on-accent 6.3:1) |
| `--accent-deep` | `#7E2D12` | accent hover / prices (8.2:1 on canvas) |
| `--rose` | `#D9A58C` | dusty rose — media fields only |
| `--dark` | `#1D1310` | closing CTA band / footer |

- **Radius:** 14px (crafted soft). Depth = hairlines + surface steps, zero shadows.
- **Type:** Fraunces (editorial serif, Google Fonts) + Archivo (grotesque) + ui-monospace labels (11px, uppercase, +0.22em tracking, 60% opacity). Max 2 families + mono.
- **Scale:** H1 `clamp(2.625rem, 6.4vw, 5.25rem)`, leading 0.95, tracking −0.035em. H2 30–44px. Body 17px/1.65, measure ≤62ch.
- **Motion:** entrance nav → eyebrow → H1 → sub → CTA, 0.1–0.2s stagger, 0.8s `cubic-bezier(0.16,1,0.3,1)`, done by ~1.5s. JS-gated (`.js .rv`): no-JS = fully visible. `prefers-reduced-motion` branch mandatory. Marquee linear only; scrub animation is decoration-triggered, never blocks reading.
- **First CSS rule sets the page background** (no white flash).

## Psychology brief (5 lines)

- **Visitor:** woman in/around Moab (locals + national-park tourists) choosing where to get hair/lashes/nails; today finds zero website — only a Vagaro profile and directory listings.
- **Pain:** trust before the chair — can't preview the vibe, the work, or how to book.
- **One action:** request an appointment (thumb-reachable "Book a visit" CTA, repeated verb) or call +1 435-260-8732.
- **Trust gap:** online invisibility → answered with editorial craft, honest sample labeling, the one verified fact (Missy named in public reviews), no invented proof.
- **Emotion:** desert-luxe calm — "Moab's own chair of confidence."

## Niche research → design decisions

Winning salon patterns (thesalonbusiness, colorlib, mangomint roundups): editorial + neutral palette + generous whitespace; prominent booking CTAs; deep colour-and-cream pairs (cf. Yello Salon); stylist identity; mobile-first. Translated to Moab: bone/terracotta/ink (desert modern, not generic blush-pink salon), asymmetric split hero, numbered editorial service list, bento gallery, designed closing band — never link-column footers.

## Layout ideas

- **Home:** asymmetric split hero (editorial column + desert-arch art frame) → service marquee → signature lookbook scrubber → numbered editorial service list → philosophy split → illustrative reviews → bento art preview → dark closing CTA.
- **Services:** accordion (progressive disclosure), sample prices in mono, honesty note.
- **Hair/Lashes/Nails:** crumb hero → art + "how it works here" checklist split → grouped sample menu → call strip → closing band.
- **Gallery:** category filter buttons, concept art with honest captions.
- **Team:** philosophy split + 2 cards (Missy = verified; lash artist = sample placeholder).
- **Pricing:** full sample price tables + no-hidden-fees trust cells.
- **Reviews:** verified-fact framing + illustrative quotes badged as placeholders + review policy.
- **Booking:** 3-step explainer → honest request form (per-field errors, consent checkbox, demo-state success) → address + sample hours + Vagaro-today note.
- **Legal:** privacy + terms in plain language; 404 as a designed scene ("That chair is empty.").

## Signature idea (§18)

**"The Lookbook Scrubber"** — a dark full-bleed panel on home with three art slides (Hair / Lash / Nails), draggable + arrow/dot/keyboard navigation, live counter, deep-links to each studio page. One live thing on the home page; real content, not decoration.

## Honesty record

- REAL: business name, street address, city/state/zip, phone (+1 435-260-8732), hair+lashes+nails scope, "Missy" named in Yelp/bestprosintown reviews, no own website today (Vagaro profile exists — positioned as current booking reality on the booking page, never linked as the site).
- SAMPLE (visibly badged): all services, prices, hours, the lash-artist bio, all artwork. Review quotes marked illustrative. No testimonials presented as real, no awards, no invented stats anywhere.
- All imagery is original SVG/CSS art created for this concept — disclosed in footer, gallery captions, team page, terms.
- Booking form validates but submits nowhere — demo states say so explicitly, with the real phone number as the working path.
- Swappable constant: `SRX` in `assets/site.js` (name, street, city, state, zip, phone, phoneHref) — injected into `[data-srx]` slots; mirrored in `build_pages.py` for no-JS readability.

## Known gaps

1. **No real photography** — live site needs the salon's real photos (with permission) replacing all concept art.
2. **No real service/pricing/hours data** — salon must supply; booking form needs a backend or booking-system embed.
3. **No rendered screenshots in this environment** — QA was static (HTML parse, link checker, JS syntax, contrast math, slop-word scan). A visual pass in a real browser is still required before outreach.
4. **Stitch step skipped** per run budget — §18 rules used as design authority instead.
