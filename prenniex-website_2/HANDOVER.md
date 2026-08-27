# prenniex.com — handover notes

## What's in the zip

```
index.html          Home
services.html       Services — 11 numbered blocks, each with an #anchor
sectors.html        Who we work with — five building types
systems.html        System sizes, battery comparison, what is / isn't included
products.html       Product catalogue — ten categories, enquiry-based, no prices
projects.html       Projects — 9 anonymised entries
about.html          About, commitments, method, leadership, coverage
faq.html            18 questions in four groups
contact.html        Contact details + quotation request form
assets/styles.css   Single stylesheet, all pages
assets/logo.svg     Emblem, rebuilt as vector
assets/favicon.svg  Same file, used as the browser-tab icon
assets/img/         12 optimised project photographs
build.py, pages.py  The generator that produced the HTML (optional — see below)
artifact.py         Builds the single-file preview
```

## Hosting it

Everything is static. Upload the whole folder to any host and point prenniex.com at it — Netlify or Vercel (drag and drop the folder), Cloudflare Pages, GitHub Pages, or a cPanel `public_html`. No server, no database, no build step required.

To preview locally, open `index.html` in a browser, or run `python3 -m http.server` in the folder and visit `http://localhost:8000`.

## Editing content

Two options.

**Edit the HTML directly.** The nine `.html` files are plain, readable HTML. Change the text and re-upload. Note that the header, footer and calls-to-action are repeated in each file, so a change to those must be made nine times.

**Re-generate.** `pages.py` holds all page content in one place and `build.py` holds the shared header, footer, stat strip and call-to-action band. Edit either, run `python3 pages.py`, and the nine HTML files are rewritten. This is the safer route for anything that touches the nav, footer or contact details.

## The enquiry form

The form on `contact.html` currently opens the visitor's email application with the message pre-filled. That works everywhere and needs no setup, but it depends on the visitor having an email client configured.

To make it deliver on its own, pick one:

- **Formspree / Web3Forms / Basin** — create an endpoint, then set `action="https://…"` and `method="post"` on the `<form id="enquiry">` and delete the small script at the bottom of `contact.html`. Five minutes, free tier is enough.
- **Netlify Forms** — if hosting on Netlify, add `netlify` and `name="enquiry"` to the `<form>` tag and delete the script. Nothing else needed.

## Before it goes live

- **Company email.** The site currently shows `prenniexgs@gmail.com`. Once the domain is set up, `info@prenniex.com` or `projects@prenniex.com` will read considerably better on a corporate proposal. Search and replace in `build.py` (`EMAIL`) and `contact.html`.
- **Telephone.** `0706 079 3977`, taken from the invoices. The proposal to NETCO carries a different number — decide which one is the company line.
- **Legal name.** "Limited" is left off throughout, as instructed. If an RC number is to be shown, the footer is the conventional place.
- **Photography.** This is the single biggest upgrade available. The current images are WhatsApp copies, and several were taken as job records rather than as marketing shots. A half-day with a camera at one commercial installation — plant room, boards, array, a technician in branded PPE — would lift the whole site. Drop new files into `assets/img/` under the same names and nothing else needs to change.
- **Site safety.** Photos showing work at height without harness or hard hat were deliberately left out. Corporate and institutional evaluators do look at this, and a visible PPE standard in the photography is worth having.
- **Street lighting and water pumping.** Both are now full service sections (`services.html#lighting`, `services.html#pumping`) and product categories. Neither was evidenced in the material you gave me — they are written from standard practice in this market. Read them before launch and correct anything that overstates what you actually do.
- **Equipment brands.** The site names Felicity Solar, LVTopsun, Cworth, Bestcom and Solarmac — taken from your invoices and site photographs — and frames them as equipment installed, not as partnerships or distributorships. If any of these is a formal distributor relationship, that is worth saying explicitly.

## Claims on the site — and how the capacity figures are framed

- **Stat strip:** 15 years · 100+ installations completed · 103.5 MWp solar delivered · 83 MWh storage delivered, with a footnote under the strip and a link to the explanation.
- **The explanation** lives at `about.html#utility` and separates the two kinds of work explicitly: installations Prenniex delivers end to end, and contributing engineering on four UN-sponsored solar farms. The wording is careful — *"we did not deliver those projects alone and we do not present them as though we did"* — because that sentence is what makes the number survive a technical evaluation rather than sink one.
- **Worth strengthening.** Naming the UN programme, the countries and the years, and stating the specific engineering scope on each farm, would turn a claim into a credential. Send me those and I will write it in.
- **The NETCO proposal** presents the same 103,500 kWp / 83,000 kWh figures in Section 2 with no such distinction, sitting directly under a table headed "Installations completed". Read cold, it says Prenniex installed 103.5 MWp across 103 jobs. Correct that section before the proposal goes to anyone else — the site now has the language you need.
- **Client names:** none. Project entries are described by sector, scope and equipment only.
- **Feyide House / NETCO:** not referenced anywhere on the site.

## Turning the Products page into a real shop

`products.html` is a catalogue, not a store: ten categories, enquiry-based, no prices and no checkout. That is deliberate — prices move with the exchange rate, and most of this market transacts by WhatsApp anyway.

If you later want actual checkout, the least painful route is a hosted cart (Snipcart, Shopify Buy Button, or Paystack's storefront) dropped into the existing markup: each `<li>` becomes a product row with a price and a buy button, and the payment provider handles the rest. The page structure will take it without a redesign. Tell me when you want it and I will wire it.

## Technical notes

- Responsive from 320 px up; nav collapses to a menu button below 760 px.
- Light and dark themes both defined, following the visitor's system setting.
- Fonts are Archivo and Inter, loaded from Google Fonts. If the site must work with no external requests at all, self-host the two font files and swap the `<link>` for a local `@font-face`.
- Every page has a `<title>`, meta description and Open Graph tags. Worth adding a `og:image` (a single good installation photo, 1200 × 630) before the link gets shared.
- No cookies, no analytics, no third-party scripts. Adding analytics later is one script tag in `build.py`.
