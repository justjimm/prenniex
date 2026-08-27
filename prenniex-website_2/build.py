#!/usr/bin/env python3
"""Builds the Prenniex Global Solutions static site from shared shell + per-page bodies."""
import os, re, pathlib

ROOT = pathlib.Path(__file__).parent
OUT = ROOT

EMBLEM = (ROOT / "assets" / "logo.svg").read_text()
EMBLEM = re.sub(r'<\?xml.*?\?>', '', EMBLEM).strip()
EMBLEM = EMBLEM.replace('<svg ', '<svg aria-hidden="true" focusable="false" ')
EMBLEM = re.sub(r'\srole="img"', '', EMBLEM)
EMBLEM = re.sub(r'\saria-label="[^"]*"', '', EMBLEM, count=1)

NAV = [
    ("index.html", "Home"),
    ("services.html", "Services"),
    ("sectors.html", "Sectors"),
    ("systems.html", "Systems"),
    ("products.html", "Products"),
    ("projects.html", "Projects"),
    ("about.html", "About"),
    ("contact.html", "Contact"),
]

TEL = "0706 079 3977"
TEL_HREF = "+2347060793977"
EMAIL = "prenniexgs@gmail.com"

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Prenniex Global Solutions">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@600;700;800&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/styles.css">
</head>
<body>
<header class="site-header">
  <div class="header-inner">
    <a class="brand" href="index.html">
      {emblem}
      <span class="brand-text">
        <span class="brand-name">PRENN<span class="i">I</span>EX</span>
        <span class="brand-sub">GLOBAL SOLUTIONS</span>
      </span>
    </a>
    <button class="menu-toggle" aria-expanded="false" aria-controls="primary-nav">Menu</button>
    <nav class="nav" id="primary-nav">
      {navlinks}
      <a class="btn btn--primary" href="contact.html">Get a free quote</a>
    </nav>
  </div>
</header>
"""

FOOT = """
<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div class="footer-brand">
        <a class="brand" href="index.html" style="color:#fff">
          {emblem}
          <span class="brand-text">
            <span class="brand-name">PRENN<span class="i">I</span>EX</span>
            <span class="brand-sub">GLOBAL SOLUTIONS</span>
          </span>
        </a>
        <p>Solar hybrid power, battery storage, electrical installation and security systems for homes, businesses and institutions across Nigeria.</p>
      </div>
      <div>
        <h4>Company</h4>
        <ul>
          <li><a href="about.html">About</a></li>
          <li><a href="sectors.html">Who we work with</a></li>
          <li><a href="systems.html">System sizes</a></li>
          <li><a href="products.html">Products</a></li>
          <li><a href="projects.html">Projects</a></li>
          <li><a href="faq.html">Questions</a></li>
          <li><a href="contact.html">Contact</a></li>
        </ul>
      </div>
      <div>
        <h4>Services</h4>
        <ul>
          <li><a href="services.html#hybrid">Solar hybrid systems</a></li>
          <li><a href="services.html#storage">Battery storage</a></li>
          <li><a href="services.html#electrical">Electrical installation</a></li>
          <li><a href="services.html#security">Security &amp; automation</a></li>
          <li><a href="services.html#audit">Energy audit &amp; survey</a></li>
          <li><a href="services.html#lighting">Solar street lighting</a></li>
          <li><a href="services.html#pumping">Solar water pumping</a></li>
          <li><a href="services.html#supply">Equipment supply</a></li>
          <li><a href="services.html#maintenance">Maintenance &amp; support</a></li>
        </ul>
      </div>
      <div>
        <h4>Contact</h4>
        <ul>
          <li>1 Ayo Oluede Street,<br>Ojodu-Berger, Lagos</li>
          <li>No 48B Glory Avenue,<br>Papa Oja, Ibafo, Ogun State</li>
          <li><a href="tel:{tel_href}">{tel}</a></li>
          <li><a href="mailto:{email}">{email}</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; 2026 Prenniex Global Solutions. All rights reserved.</span>
      <span class="parent-note">Solar · Storage · Electrical installation · Security systems &nbsp;|&nbsp; Lagos &amp; Ogun State, Nigeria</span>
    </div>
  </div>
</footer>
<script>
(function(){
  var t=document.querySelector('.menu-toggle'), n=document.getElementById('primary-nav');
  if(!t||!n) return;
  t.addEventListener('click', function(){
    var open=n.classList.toggle('open');
    t.setAttribute('aria-expanded', open?'true':'false');
  });
  n.addEventListener('click', function(e){ if(e.target.tagName==='A') n.classList.remove('open'); });
})();
</script>
</body>
</html>
"""


def nav_links(current):
    out = []
    for href, label in NAV:
        cur = ' aria-current="page"' if href == current else ''
        out.append(f'<a href="{href}"{cur}>{label}</a>')
    return "\n      ".join(out)


def page(filename, title, desc, body):
    html = HEAD.format(title=title, desc=desc, emblem=EMBLEM, navlinks=nav_links(filename))
    html += body
    foot = (FOOT.replace("{emblem}", EMBLEM).replace("{tel_href}", TEL_HREF)
                .replace("{tel}", TEL).replace("{email}", EMAIL))
    html += foot
    (OUT / filename).write_text(html)
    print("wrote", filename, len(html), "bytes")


# ---------------------------------------------------------------- shared blocks
CTA = """
<section class="cta">
  <div class="wrap cta-inner">
    <div>
      <h2>Tell us what you need powered.</h2>
      <p>A site visit and a written quotation cost you nothing. You will get a real load assessment, a system sized to it, and a price with every item listed — not a lump sum.</p>
    </div>
    <div class="btn-row" style="margin:0">
      <a class="btn btn--light" href="contact.html">Get a free quote</a>
      <a class="btn btn--outline-light" href="tel:+2347060793977">Call 0706 079 3977</a>
    </div>
  </div>
</section>
"""

STATS = """
<section class="stats">
  <div class="stats-grid">
    <div class="stat"><b>15 yrs</b><span>In solar and power engineering</span></div>
    <div class="stat"><b>100+</b><span>Installations completed</span></div>
    <div class="stat"><b>103.5 MWp</b><span>Solar capacity delivered</span></div>
    <div class="stat"><b>83 MWh</b><span>Storage capacity delivered</span></div>
  </div>
  <p class="stats-note">Capacity delivered includes four UN-sponsored solar farm projects on which our engineers worked as contributing engineers. <a href="about.html#utility">How to read these figures</a>.</p>
</section>
"""

ICON = {
 "sun": '<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M2 12h2M20 12h2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M19.1 4.9l-1.4 1.4M6.3 17.7l-1.4 1.4"/>',
 "battery": '<rect x="2" y="7" width="16" height="10" rx="2"/><path d="M22 10v4M9 10l-2 4h4l-2 4"/>',
 "board": '<rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18M9 9v12M13 13h4M13 17h4"/>',
 "shield": '<path d="M12 3l7 3v5c0 4.5-3 8.3-7 10-4-1.7-7-5.5-7-10V6z"/><path d="M9.5 12l1.8 1.8 3.4-3.6"/>',
 "clipboard": '<rect x="5" y="4" width="14" height="17" rx="2"/><path d="M9 4h6v3H9zM9 12h6M9 16h4"/>',
 "wrench": '<path d="M14.7 6.3a4 4 0 105.3 5.3L14 17.6 6.4 10 12.7 4a4 4 0 002 2.3z"/><path d="M6.4 10L3 13.4l7.6 7.6L14 17.6"/>',
 "bolt": '<path d="M13 2L4 14h7l-1 8 9-12h-7z"/>',
 "lamp": '<path d="M12 3a6 6 0 016 6c0 2.6-1.6 4-2.4 5.3-.4.7-.6 1.2-.6 1.7H9c0-.5-.2-1-.6-1.7C7.6 13 6 11.6 6 9a6 6 0 016-6z"/><path d="M10 19h4M10.5 22h3"/>',
 "drop": '<path d="M12 3s6 6.4 6 10.2A6 6 0 016 13.2C6 9.4 12 3 12 3z"/><path d="M9.2 14.2a2.8 2.8 0 002.8 2.6"/>',
 "leaf": '<path d="M20 4C10 4 4 9 4 16c0 2 .7 3.4.7 3.4S9 12 19 9c0 0-6 3-9.5 7.5C7.7 18.8 7 20 7 20c9 2 13-4 13-9z"/>',
}


def icon(name):
    return f'<span class="card-icon"><svg viewBox="0 0 24 24">{ICON[name]}</svg></span>'
