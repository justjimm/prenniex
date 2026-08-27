#!/usr/bin/env python3
"""Builds a single-file, self-contained preview of the whole Prenniex site for publishing."""
import re, json, base64, pathlib, importlib.util, sys

ROOT = pathlib.Path(__file__).parent
spec = importlib.util.spec_from_file_location("pg", ROOT / "pages.py")
m = importlib.util.module_from_spec(spec); sys.modules["pg"] = m; spec.loader.exec_module(m)

import build

CSS = (ROOT / "assets" / "styles.css").read_text()
EMBLEM = build.EMBLEM

BODIES = [("index", m.home), ("services", m.services), ("sectors", m.sectors),
          ("systems", m.systems), ("products", m.products), ("projects", m.projects), ("about", m.about),
          ("faq", m.faq), ("contact", m.contact)]

# ---- inline images as data URIs
cache = {}
PLACEHOLDER = "data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7"
def datauri(match):
    src = match.group(1)
    key = src.rsplit("/", 1)[-1].rsplit(".", 1)[0]
    if key not in cache:
        cache[key] = "data:image/jpeg;base64," + base64.b64encode((ROOT / src).read_bytes()).decode()
    return 'src="%s" data-k="%s"' % (PLACEHOLDER, key)

def rewrite(html):
    html = re.sub(r'src="(assets/img/[^"]+)"', datauri, html)
    # turn page links into router links
    def link(mo):
        page, frag = mo.group(1), mo.group(2) or ""
        page = "index" if page == "index" else page
        return 'href="#%s" data-nav="%s"%s' % (page, page, ' data-frag="%s"' % frag[1:] if frag else "")
    html = re.sub(r'href="(\w+)\.html(#[\w-]+)?"', link, html)
    return html

pages_html = []
for name, body in BODIES:
    pages_html.append('<section class="page" id="page-%s"%s>\n%s\n</section>'
                      % (name, "" if name == "index" else ' hidden', rewrite(body)))

navlinks = "\n      ".join(
    '<a href="#%s" data-nav="%s"%s>%s</a>' % (h[:-5], h[:-5], ' aria-current="page"' if h == "index.html" else "", l)
    for h, l in build.NAV)

FOOT = rewrite(build.FOOT.replace("{emblem}", EMBLEM).replace("{tel_href}", build.TEL_HREF)
               .replace("{tel}", build.TEL).replace("{email}", build.EMAIL))
# strip the page-level scripts that came from the file build; the router below replaces them
FOOT = re.sub(r"<script>.*?</script>", "", FOOT, flags=re.S)

EXTRA = """
<style>
.page[hidden]{display:none}
.site-header{position:sticky}
</style>
"""

ROUTER = """
<script>
(function(){
  var pages=['index','services','sectors','systems','products','projects','about','faq','contact'];
  function show(name, frag){
    if(pages.indexOf(name)<0) name='index';
    pages.forEach(function(p){
      var el=document.getElementById('page-'+p);
      if(el) el.hidden=(p!==name);
    });
    document.querySelectorAll('[data-nav]').forEach(function(a){
      if(a.closest('.nav')) {
        if(a.getAttribute('data-nav')===name) a.setAttribute('aria-current','page');
        else a.removeAttribute('aria-current');
      }
    });
    if(frag){
      var t=document.getElementById(frag);
      if(t){ t.scrollIntoView({behavior:'auto',block:'start'}); return; }
    }
    window.scrollTo(0,0);
  }
  document.addEventListener('click', function(e){
    var a=e.target.closest('[data-nav]');
    if(!a) return;
    e.preventDefault();
    var name=a.getAttribute('data-nav'), frag=a.getAttribute('data-frag');
    history.replaceState(null,'','#'+name);
    show(name, frag);
    var n=document.getElementById('primary-nav'); if(n) n.classList.remove('open');
  });
  var t=document.querySelector('.menu-toggle'), n=document.getElementById('primary-nav');
  if(t&&n){ t.addEventListener('click', function(){
    var open=n.classList.toggle('open'); t.setAttribute('aria-expanded', open?'true':'false');
  }); }
  var f=document.getElementById('enquiry');
  if(f){ f.addEventListener('submit', function(e){
    e.preventDefault();
    var note=document.getElementById('formnote');
    note.textContent='This is a preview. On the live site this opens your email application with the message ready to send.';
  }); }
  var IMG=window.__PXIMG||{};
  document.querySelectorAll('img[data-k]').forEach(function(i){
    var u=IMG[i.getAttribute('data-k')]; if(u) i.src=u;
  });
  window.addEventListener('hashchange', function(){
    show((location.hash||'#index').slice(1));
  });
  show((location.hash||'#index').slice(1));
})();
</script>
"""

IMGJS = "<script>window.__PXIMG=" + json.dumps(cache) + ";</scr"+"ipt>"

HTML = """<title>Prenniex Global Solutions</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@600;700;800&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<style>
%s
</style>
%s
<header class="site-header">
  <div class="header-inner">
    <a class="brand" href="#index" data-nav="index">
      %s
      <span class="brand-text">
        <span class="brand-name">PRENN<span class="i">I</span>EX</span>
        <span class="brand-sub">GLOBAL SOLUTIONS</span>
      </span>
    </a>
    <button class="menu-toggle" aria-expanded="false" aria-controls="primary-nav">Menu</button>
    <nav class="nav" id="primary-nav">
      %s
      <a class="btn btn--primary" href="#contact" data-nav="contact">Get a free quote</a>
    </nav>
  </div>
</header>
%s
%s
%s
%s
""" % (CSS, EXTRA, EMBLEM, navlinks, "\n".join(pages_html), FOOT, IMGJS, ROUTER)

out = ROOT / "prenniex-preview.html"
out.write_text(HTML)
print("wrote", out, round(len(HTML)/1024/1024, 2), "MB")
