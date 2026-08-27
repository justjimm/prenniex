#!/usr/bin/env python3
from build import page, CTA, STATS, icon

BRANDS = """
    <div class="brands">
      <span>Felicity Solar</span><span>LVTopsun</span><span>Cworth</span><span>Bestcom</span>
      <span>Solarmac</span><span>Tubular &amp; LiFePO&#8324; storage</span><span>Mono-crystalline PV</span>
    </div>
"""

# =============================================================== HOME
home = """
<section class="hero">
  <img class="hero-bg" src="assets/img/roof-array-longspan.jpg" alt="Solar array installed along a long-span roof by Prenniex">
  <div class="hero-inner">
    <p class="eyebrow">Power systems · Solar and storage · Electrical installation</p>
    <h1>Power that holds when the grid doesn't.</h1>
    <p class="lede">Prenniex designs, supplies, installs and maintains solar and inverter systems for homes, businesses and institutions across Nigeria — sized to a load we have actually measured, and installed by our own crews.</p>
    <div class="btn-row">
      <a class="btn btn--light" href="contact.html">Get a free quote</a>
      <a class="btn btn--outline-light" href="systems.html">See system sizes</a>
    </div>
    <div class="hero-sub">
      <span>Free site visit and written quotation</span>
      <span>100+ installations completed</span>
      <span>Lagos · Ibadan · Akure · Ado-Ekiti</span>
    </div>
  </div>
</section>
""" + STATS + """
<section class="section">
  <div class="wrap">
    <p class="eyebrow">What we do</p>
    <h2>Solar, storage, and the electrical work that carries it.</h2>
    <p class="lede">Most installers stop at the inverter. We do the distribution, the protection and the switching as well, because that is where a system either lasts or starts giving trouble in the second year.</p>
    <div class="grid grid-4" style="margin-top:44px">
      <div class="card">""" + icon("sun") + """<h3>Solar hybrid systems</h3><p>PV array, hybrid inverter and automatic switching between solar, battery, grid and generator. From a single home up to a multi-floor building.</p></div>
      <div class="card">""" + icon("battery") + """<h3>Battery storage</h3><p>Lithium and tubular banks, new installations and retrofits onto inverters that are still sound. Sized against your evening load, not the brochure.</p></div>
      <div class="card">""" + icon("board") + """<h3>Electrical installation</h3><p>Distribution boards, DC and AC protection, surge devices, changeover, load separation, cabling and earthing — done by us, not subcontracted.</p></div>
      <div class="card">""" + icon("shield") + """<h3>Security and automation</h3><p>CCTV, access control, intercom and automated gates, on supply that is backed up and protected so the system does not go down with the light.</p></div>
      <div class="card">""" + icon("clipboard") + """<h3>Energy audit and survey</h3><p>We measure what your building actually draws, hour by hour, before anyone quotes a system size. It is the step most often skipped.</p></div>
      <div class="card">""" + icon("wrench") + """<h3>Maintenance and support</h3><p>Servicing, array cleaning, battery health checks, settings review and fault attendance — for our installations and for systems we inherit.</p></div>
      <div class="card">""" + icon("lamp") + """<h3>Solar street lighting</h3><p>All-in-one and pole-mounted street lights for estate roads, compounds, car parks and perimeters. No cabling back to a board, nothing added to your load.</p></div>
      <div class="card">""" + icon("drop") + """<h3>Solar water pumping</h3><p>Borehole and surface pumps running off their own array, filling the tank by day. Most installations need no battery at all.</p></div>
    </div>
    <div class="btn-row"><a class="btn btn--ghost" href="services.html">All services in detail</a></div>
  </div>
</section>

<section class="section section--surface">
  <div class="wrap">
    <p class="eyebrow">Who we work with</p>
    <h2>The same method, at every scale.</h2>
    <p class="lede">A three-bedroom flat and a nine-storey office building are the same problem at different sizes: find out what the load really is, size for it honestly, and install it so it can be maintained.</p>
    <div class="grid grid-5" style="margin-top:40px">
      <div class="sector"><img src="assets/img/residential-roof-array.jpg" alt="Residential rooftop solar installation"><div class="sector-body"><h3>Homes and estates</h3><p>Whole-house and essential-load systems, and estate-wide standards.</p></div></div>
      <div class="sector"><img src="assets/img/plant-room-wide.jpg" alt="Commercial inverter plant room"><div class="sector-body"><h3>Offices and commercial</h3><p>Shops, branches, offices and multi-tenant buildings.</p></div></div>
      <div class="sector"><img src="assets/img/industrial-roof-array.jpg" alt="Industrial roof solar array"><div class="sector-body"><h3>Industrial</h3><p>Factories, workshops and warehouses with heavy motive load.</p></div></div>
      <div class="sector"><img src="assets/img/roof-array-longspan.jpg" alt="Rooftop array on an institutional building"><div class="sector-body"><h3>Institutions</h3><p>Schools, clinics, places of worship and public buildings.</p></div></div>
      <div class="sector"><img src="assets/img/plant-room-inverter-bank.jpg" alt="Multi-inverter installation in a corporate building"><div class="sector-body"><h3>Corporate buildings</h3><p>Multi-storey installations, floor by floor, in occupied premises.</p></div></div>
    </div>
    <div class="btn-row"><a class="btn btn--ghost" href="sectors.html">What we install for each</a></div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <p class="eyebrow">System sizes</p>
    <h2>Where most people start.</h2>
    <p class="lede">These are the configurations we install most often. Every one is confirmed against your own load before it is quoted — the sizes below are a starting point for the conversation, not a menu.</p>
    <div class="grid grid-4" style="margin-top:40px">
      <div class="plan">
        <span class="cap">2.5 kVA</span>
        <span class="for">Flat or small home</span>
        <dl>
          <dt>Inverter</dt><dd>2.5 kVA pure sine wave</dd>
          <dt>Storage</dt><dd>2 × 200 Ah tubular</dd>
          <dt>Array</dt><dd>6 × 300 W</dd>
        </dl>
        <div class="runs"><b>Typically runs</b>Lights, fans, TV, decoder, laptops, phone charging and a small fridge.</div>
      </div>
      <div class="plan">
        <span class="cap">3.5 kVA</span>
        <span class="for">Family home</span>
        <dl>
          <dt>Inverter</dt><dd>3.5 kVA hybrid</dd>
          <dt>Storage</dt><dd>5 kWh lithium</dd>
          <dt>Array</dt><dd>8 × 320 W</dd>
        </dl>
        <div class="runs"><b>Typically runs</b>Everything above plus a full-size fridge-freezer, pumping set, and a bedroom air conditioner for part of the night.</div>
      </div>
      <div class="plan">
        <span class="cap">5–10 kW</span>
        <span class="for">Large home, shop or office</span>
        <dl>
          <dt>Inverter</dt><dd>5–10 kW hybrid</dd>
          <dt>Storage</dt><dd>10–20 kWh lithium</dd>
          <dt>Array</dt><dd>10–20 modules</dd>
        </dl>
        <div class="runs"><b>Typically runs</b>Multiple air conditioners, a small server or POS setup, office equipment, freezers and borehole pumps.</div>
      </div>
      <div class="plan">
        <span class="cap">15 kW +</span>
        <span class="for">Building or multi-floor</span>
        <dl>
          <dt>Inverter</dt><dd>15 kW units, paralleled</dd>
          <dt>Storage</dt><dd>20 kWh and upward per unit</dd>
          <dt>Array</dt><dd>Roof, ground or canopy</dd>
        </dl>
        <div class="runs"><b>Typically runs</b>Whole floors or wings, with each floor able to operate independently of the others.</div>
      </div>
    </div>
    <div class="btn-row"><a class="btn btn--ghost" href="systems.html">Full sizing guide</a></div>
  </div>
</section>

<section class="section section--surface">
  <div class="wrap">
    <p class="eyebrow">How we work</p>
    <h2>Five steps, and you can stop after any of them.</h2>
    <div class="steps grid-5" style="margin-top:36px; display:grid; gap:16px">
      <div class="step"><h3>Enquiry and site visit</h3><p>You tell us the building and what troubles you. We come and look. No charge, no obligation.</p></div>
      <div class="step"><h3>Load assessment</h3><p>We list what has to run, for how long, and measure or log where it matters. This decides everything downstream.</p></div>
      <div class="step"><h3>Design and quotation</h3><p>A configuration sized to that load, and a quotation with every item, quantity and rate shown separately.</p></div>
      <div class="step"><h3>Installation</h3><p>Our own crews. Mounting, cabling, boards, protection and commissioning, with the premises kept usable throughout.</p></div>
      <div class="step"><h3>Handover and support</h3><p>Walk-through, settings explained, warranties passed to you, and someone to call when you need us.</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap split">
    <div>
      <p class="eyebrow">Why Prenniex</p>
      <h2>Four things that decide whether a system is still good in year five.</h2>
      <ul class="ticks">
        <li><strong>We do the electrical work ourselves.</strong> Boards, protection, changeover and load separation are not handed to a third party. Most system failures we are called to fix are distribution problems, not inverter problems.</li>
        <li><strong>Equipment is chosen for the site.</strong> We are not tied to selling one brand. What goes in is what suits the load, the space and the budget in front of us.</li>
        <li><strong>Warranties reach you intact.</strong> Manufacturer warranties are passed through in your name. We do not sit between you and the manufacturer.</li>
        <li><strong>Everything is labelled.</strong> Every board and every way is marked, so any competent electrician — not only us — can work on your system afterwards.</li>
      </ul>
      <div class="btn-row"><a class="btn btn--ghost" href="about.html">More about how we work</a></div>
    </div>
    <div class="split-media"><img src="assets/img/dc-ac-distribution-boards.jpg" alt="Labelled DC and AC distribution boards with surge protection and changeover"></div>
  </div>
</section>

<section class="section section--surface">
  <div class="wrap">
    <div class="grid grid-2">
      <div>
        <p class="eyebrow">Equipment</p>
        <h2>What we install.</h2>
        <p>We work with equipment that can be serviced and replaced in Nigeria, and we will tell you plainly when a cheaper component is a false economy and when it is not. Where you have a preference, we will quote it.</p>
        """ + BRANDS + """
      </div>
      <div>
        <p class="eyebrow">Supply</p>
        <h2>Buying equipment only.</h2>
        <p>If you already have an installer, or your own electrician, we will supply the equipment on its own — inverters, batteries, panels, mounting, protection and cabling — with the sizing advice included at no charge.</p>
        <p>We would rather you buy the right thing from us than the wrong thing from anyone.</p>
        <div class="btn-row" style="margin-top:14px"><a class="btn btn--ghost" href="products.html">See what we stock</a></div>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap split">
    <div>
      <p class="eyebrow">Utility scale</p>
      <h2>Four UN-sponsored solar farms.</h2>
      <p>Alongside our own installations, our engineers have served as contributing engineers on four solar farm projects sponsored under United Nations programmes. That is where the bulk of the capacity figures on this site comes from, and it is a different order of work from a building installation — larger arrays, formal design review, and delivery standards set by an international programme.</p>
      <p>We state it separately because it should be read separately. The buildings, homes and premises described on this site are jobs we deliver end to end. The farm work is engineering contribution at utility scale, and we are glad to set out our specific role on any of them on request.</p>
      <div class="btn-row"><a class="btn btn--ghost" href="about.html#utility">How to read our figures</a></div>
    </div>
    <div class="split-media"><img src="assets/img/industrial-roof-array.jpg" alt="Large-scale solar array"></div>
  </div>
</section>

<section class="section section--surface">
  <div class="wrap">
    <p class="eyebrow">Selected work</p>
    <h2>Installations, not renderings.</h2>
    <p class="lede">Client names are withheld as a matter of course. References and site visits can be arranged, with the client's consent.</p>
    <div class="grid grid-3" style="margin-top:40px">
      <article class="proj">
        <img src="assets/img/plant-room-wide.jpg" alt="Plant room with six parallel inverters and a hybrid storage unit">
        <div class="proj-body">
          <span class="tag">Commercial</span>
          <h3>Multi-inverter plant room</h3>
          <p>Parallel inverter bank with hybrid storage, dedicated DC and AC boards, and dressed cable routing in a purpose-cleared plant space.</p>
          <div class="meta">Lagos</div>
        </div>
      </article>
      <article class="proj">
        <img src="assets/img/industrial-roof-array.jpg" alt="Solar modules rail-mounted on an industrial roof">
        <div class="proj-body">
          <span class="tag">Industrial</span>
          <h3>Long-span roof array</h3>
          <p>Rail-mounted array across a profile-sheet roof, strung and routed to a ground-level inverter room without disturbing the sheet line.</p>
          <div class="meta">Nigeria</div>
        </div>
      </article>
      <article class="proj">
        <img src="assets/img/lithium-storage-unit.jpg" alt="Wall-mounted lithium storage unit installed beside an inverter">
        <div class="proj-body">
          <span class="tag">Residential</span>
          <h3>Lithium storage retrofit</h3>
          <p>Tubular bank replaced with lithium storage on an existing hybrid inverter, with load separation and new surge protection.</p>
          <div class="meta">Lagos</div>
        </div>
      </article>
    </div>
    <div class="btn-row"><a class="btn btn--ghost" href="projects.html">See more work</a></div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <p class="eyebrow">Common questions</p>
    <h2>Before you call.</h2>
    <div class="faq" style="max-width:820px">
      <details><summary>How much will my system cost?</summary><div class="answer"><p>It depends entirely on what has to run and for how long, and equipment prices move with the exchange rate. Anyone who quotes you a figure before asking what you want powered is guessing. Tell us the appliances and the hours, and we will give you a written price with every item shown.</p></div></details>
      <details><summary>Do I have to power the whole house?</summary><div class="answer"><p>No, and usually you should not. Separating essential circuits — lights, fans, fridge, sockets, pumps — from heavy loads like air conditioning and water heaters gives you far more hours of backup for the same money. We do that separation as part of the installation.</p></div></details>
      <details><summary>Lithium or tubular batteries?</summary><div class="answer"><p>Lithium costs more at the start, lasts several times longer, gives you more usable energy per naira over its life and needs no maintenance. Tubular is cheaper today and still sensible on a tight budget or a small system. We will show you both on the quotation.</p></div></details>
      <details><summary>What happens on cloudy days and in the rainy season?</summary><div class="answer"><p>Panels still generate in diffuse light, at reduced output. A properly sized hybrid system covers this by charging from the grid or a generator when there is not enough sun, so the batteries stay ready. Rain also washes the array, which helps.</p></div></details>
    </div>
    <div class="btn-row"><a class="btn btn--ghost" href="faq.html">All questions answered</a></div>
  </div>
</section>
""" + CTA

page("index.html",
     "Prenniex Global Solutions — Solar, Storage and Electrical Engineering in Nigeria",
     "Prenniex Global Solutions designs, supplies, installs and maintains solar hybrid power systems, battery storage, electrical installations and security systems for homes, businesses and institutions across Nigeria.",
     home)


# =============================================================== SERVICES
services = """
<section class="pagehead">
  <div class="wrap">
    <p class="eyebrow">Services</p>
    <h1>What we install, and what we stand behind.</h1>
    <p class="lede">Power, the electrical infrastructure it runs on, and the systems that depend on both. Any of these can be taken on its own or as part of a single scope.</p>
  </div>
</section>

<section class="section" id="hybrid">
  <div class="wrap split">
    <div>
      <span class="kicker-num">01</span>
      <p class="eyebrow">Solar hybrid power systems</p>
      <h2>Solar, battery, grid and generator — switching between them automatically.</h2>
      <p>A hybrid system combines PV generation, battery storage and an inverter that can draw from the array, the battery, public supply or a generator and move between them without interrupting what is running. The array carries the daytime load; the battery carries the evening and rides through outages.</p>
      <p>We install off-grid, hybrid and grid-interactive configurations. Which one suits you depends on how reliable your supply is, what you are trying to eliminate, and whether the priority is cost per month or independence from the grid.</p>
      <ul class="ticks">
        <li>Single-inverter systems from 2.5 kVA, and paralleled units for larger buildings</li>
        <li>Roof, ground-mount, car park canopy and façade array deployment</li>
        <li>Automatic changeover between solar, battery, public supply and generator</li>
        <li>Generator integration, so the set starts only when it is genuinely needed</li>
        <li>Remote monitoring where the equipment supports it</li>
      </ul>
    </div>
    <div class="split-media"><img src="assets/img/twin-hybrid-inverters.jpg" alt="Two hybrid inverters mounted on a board with PV isolators and metering"></div>
  </div>
</section>

<section class="section section--surface" id="storage">
  <div class="wrap split split--rev">
    <div class="split-media"><img src="assets/img/lithium-storage-unit.jpg" alt="Floor-standing lithium storage unit installed by Prenniex"></div>
    <div>
      <span class="kicker-num">02</span>
      <p class="eyebrow">Battery energy storage</p>
      <h2>Sized against the evening, not the midday peak.</h2>
      <p>Storage is where most systems are under-specified. An installation that is correct at noon and short at seven in the evening is one you stop trusting, and then the generator comes back on. We size storage against the hours you actually need covered.</p>
      <p>We install lithium (LiFePO&#8324;) and tubular banks, wall-mounted and floor-standing, and we retrofit lithium onto existing inverters where the inverter is sound and only the bank has reached end of life. That is often the cheapest useful upgrade available to a household.</p>
      <ul class="ticks">
        <li>Lithium and tubular banks, with racking, enclosures and ventilation</li>
        <li>Retrofits onto existing inverters — you keep the equipment that still works</li>
        <li>Battery protection, isolation and correct DC cable sizing</li>
        <li>Charge strategy set against your own outage pattern, not a default</li>
      </ul>
    </div>
  </div>
</section>

<section class="section" id="electrical">
  <div class="wrap split">
    <div>
      <span class="kicker-num">03</span>
      <p class="eyebrow">Electrical installation and distribution</p>
      <h2>The part that decides whether the rest of it lasts.</h2>
      <p>Bringing new equipment into an existing building electrically is where quality shows. We do the distribution work ourselves rather than subcontract it: DC and AC boards, isolation, surge protection, changeover, load separation, cable sizing and routing, earthing and labelling.</p>
      <p>Every board we install is labelled so that someone who has never met us can work on it. That is not a courtesy — it is what keeps the system serviceable when we are not the ones on site.</p>
      <ul class="ticks">
        <li>DC and AC distribution boards, breakers, fuses and surge protective devices</li>
        <li>Load separation — essential, off-peak and non-essential circuits kept apart</li>
        <li>Changeover and transfer switching between public supply, generator and inverter</li>
        <li>Rewiring and enabling works, quoted openly as their own line rather than buried</li>
        <li>Earthing, bonding and lightning protection where the site calls for it</li>
      </ul>
    </div>
    <div class="split-media"><img src="assets/img/hybrid-inverter-wall.jpg" alt="Hybrid inverter and solar panel board mounted above a doorway"></div>
  </div>
</section>

<section class="section section--surface" id="security">
  <div class="wrap split split--rev">
    <div class="split-media"><img src="assets/img/inverter-room-standby.jpg" alt="Inverter and battery installation in an equipment room with fire extinguishers mounted"></div>
    <div>
      <span class="kicker-num">04</span>
      <p class="eyebrow">Security systems and automation</p>
      <h2>Cameras and gates that stay up when the light goes.</h2>
      <p>Security systems fail most often for power reasons — a camera on a circuit that drops with the generator, a gate motor with no backed-up supply, a controller behind an unprotected outlet. Because we do the power and the distribution, we can put these systems on supply that actually holds.</p>
      <ul class="ticks">
        <li>CCTV — camera specification, siting, cabling, recording and remote viewing</li>
        <li>Access control and intercom for gates, doors and lobbies</li>
        <li>Automated gate installation, including matched units across several entrances</li>
        <li>Backed-up supply and surge protection for every element of the system</li>
      </ul>
    </div>
  </div>
</section>

<section class="section" id="audit">
  <div class="wrap">
    <span class="kicker-num">05</span>
    <p class="eyebrow">Energy audit and site survey</p>
    <h2>Finding out what the building actually uses.</h2>
    <p class="lede">Almost every oversized system and every disappointing one traces back to a size chosen without measurement. This is the step we will not skip.</p>
    <div class="grid grid-2" style="margin-top:34px">
      <div class="card">
        <h3>For homes and small premises</h3>
        <p>A visit, an appliance-by-appliance schedule, a look at the existing board and wiring, and a check of roof space and orientation. Usually an hour or two, and it is free.</p>
        <ul class="dash">
          <li>What you want running, and for how many hours</li>
          <li>Existing board condition and whether load separation is possible</li>
          <li>Roof area, shading and mounting options</li>
          <li>A recommended size, with a smaller and a larger option beside it</li>
        </ul>
      </div>
      <div class="card">
        <h3>For buildings and businesses</h3>
        <p>A logged load profile over a working week, so the design is built on measurement rather than on nameplate ratings, which almost always overstate what a building draws.</p>
        <ul class="dash">
          <li>Load logged and separated into working hours, evening, night and weekend</li>
          <li>Distribution survey — how supply is arranged, spare capacity, rewiring needed</li>
          <li>Plant space, ventilation, access and fire provision for equipment</li>
          <li>Roof area, orientation and structural load-bearing assessment</li>
          <li>Output: a measured load schedule, a confirmed bill of quantities and a firm price</li>
        </ul>
      </div>
    </div>
    <div class="callout">
      <p><strong>On larger jobs we go on to install, the cost of a full audit is credited against the contract.</strong> If you decide not to proceed, the report is yours to keep and to use with any contractor you choose.</p>
    </div>
  </div>
</section>

<section class="section section--surface" id="supply">
  <div class="wrap split">
    <div>
      <span class="kicker-num">06</span>
      <p class="eyebrow">Supply of equipment</p>
      <h2>Buying the parts without the installation.</h2>
      <p>If you have your own electrician, or you are managing the job yourself, we will supply the equipment on its own: inverters, lithium and tubular batteries, panels, mounting rails and accessories, charge controllers, breakers, surge devices, MC4 connectors, DC and AC cable.</p>
      <p>Sizing advice comes with it at no charge. We would rather talk you out of the wrong configuration before you buy it than be called to fix it afterwards.</p>
      <ul class="ticks">
        <li>Itemised quotation — you see every unit rate, not a lump sum</li>
        <li>Delivery arranged within Lagos, Ogun and to other states</li>
        <li>Manufacturer warranties registered in your name</li>
        <li>Commissioning support available separately if your electrician wants it</li>
      </ul>
      """ + BRANDS + """
      <div class="btn-row"><a class="btn btn--ghost" href="products.html">Full product list</a></div>
    </div>
    <div class="split-media"><img src="assets/img/storage-and-boards.jpg" alt="Inverter, boards and storage installed together"></div>
  </div>
</section>

<section class="section" id="lighting">
  <div class="wrap split split--rev">
    <div class="split-media"><img src="assets/img/industrial-roof-exterior.jpg" alt="Solar installation on a secured compound"></div>
    <div>
      <span class="kicker-num">07</span>
      <p class="eyebrow">Solar street lighting and outdoor power</p>
      <h2>Light on the road, the compound and the perimeter — with nothing to switch on.</h2>
      <p>All-in-one and split-array solar street lights for estate roads, compounds, car parks, filling stations, school grounds and perimeter security. Each unit carries its own panel, battery and controller, so there is no cabling back to a board and nothing added to the building's load.</p>
      <p>Sizing is done against dusk-to-dawn hours in the rainy season rather than the dry, which is the difference between lights that hold through the night in August and lights that fade by two in the morning. Poles, foundations and spacing are set out to the run, not guessed.</p>
      <ul class="ticks">
        <li>All-in-one integrated units and separate panel-and-pole configurations</li>
        <li>Estate roads, compounds, car parks, perimeter and security lighting</li>
        <li>Pole supply, foundations, spacing and lux planning for the run</li>
        <li>Motion-sensing and dimming profiles where they extend the night</li>
        <li>Replacement of failed units from other suppliers, and maintenance schedules</li>
      </ul>
    </div>
  </div>
</section>

<section class="section" id="pumping">
  <div class="wrap split">
    <div>
      <span class="kicker-num">08</span>
      <p class="eyebrow">Solar water pumping</p>
      <h2>The tank is the battery.</h2>
      <p>A solar pumping system fills your overhead tank during the day and the tank holds the water for the night — which means most installations need no battery at all, and cost far less than people assume. It also takes the pump off the generator, which on many compounds is the single most annoying reason the set gets started.</p>
      <p>We install submersible borehole pumps and surface pumps, with dedicated arrays, controllers, dry-run and level protection, and manual changeover to public supply where you want a fallback.</p>
      <ul class="ticks">
        <li>Submersible borehole and surface pump installations</li>
        <li>Direct-drive systems with the tank as storage — no battery required</li>
        <li>Hybrid configurations where night pumping or pressure is needed</li>
        <li>Dry-run, level and surge protection, and float or probe control</li>
        <li>Estate, farm, irrigation and institutional water supply</li>
      </ul>
    </div>
    <div class="split-media"><img src="assets/img/residential-roof-array.jpg" alt="Rooftop solar array serving a residential property"></div>
  </div>
</section>

<section class="section" id="maintenance">
  <div class="wrap">
    <div class="grid grid-3">
      <div class="card">
        """ + icon("wrench") + """
        <span class="kicker-num">09</span>
        <h3>Maintenance and monitoring</h3>
        <p>Scheduled servicing, array cleaning, torque and connection checks, battery health testing, firmware and settings review, and fault attendance. We maintain systems we did not install — including ones that were left in a poor state by whoever did.</p>
      </div>
      <div class="card">
        """ + icon("clipboard") + """
        <span class="kicker-num">10</span>
        <h3>Design and second opinions</h3>
        <p>Load flow and sizing calculations, bills of quantities, and independent review of a quotation you already hold. We will tell you what a stated capacity will and will not actually carry, and what has been left out of the price.</p>
      </div>
      <div class="card">
        """ + icon("bolt") + """
        <span class="kicker-num">11</span>
        <h3>Payment structuring on large jobs</h3>
        <p>Where the capital is the obstacle rather than the case, we can arrange a facility against the installation and structure repayment monthly. Terms are set by the lender's own credit process, and the facility can be placed with a lender of your choosing.</p>
      </div>
    </div>
  </div>
</section>
""" + CTA

page("services.html",
     "Services — Prenniex Global Solutions",
     "Solar hybrid systems, battery storage, electrical installation and distribution, security and automation, energy audits, equipment supply, maintenance and design services from Prenniex Global Solutions.",
     services)


# =============================================================== SECTORS
sectors = """
<section class="pagehead">
  <div class="wrap">
    <p class="eyebrow">Who we work with</p>
    <h1>Different buildings, different failure points.</h1>
    <p class="lede">What a system has to survive changes completely between a family home and a factory. These are the patterns we see, and what we install for each.</p>
  </div>
</section>

<section class="section">
  <div class="wrap split">
    <div>
      <p class="eyebrow">Homes and estates</p>
      <h2>Quiet nights, and a fridge that never warms up.</h2>
      <p>Most households do not need the whole house on backup — they need the right half of it, for long enough. We separate essential circuits from heavy loads, which usually doubles the hours you get for the same spend, and size the battery around the evening rather than around the array.</p>
      <p>For estates, we install to a single specification across units so that spares, servicing and fault-finding stay simple, and so residents are not each negotiating separately with a different installer.</p>
      <ul class="ticks">
        <li>2.5–10 kVA whole-house and essential-load systems</li>
        <li>Lithium retrofits onto existing inverters</li>
        <li>Borehole and pumping-set integration</li>
        <li>Estate-wide standards, with matched equipment across units</li>
      </ul>
    </div>
    <div class="split-media"><img src="assets/img/residential-roof-array.jpg" alt="Solar array on a residential roof"></div>
  </div>
</section>

<section class="section section--surface">
  <div class="wrap split split--rev">
    <div class="split-media"><img src="assets/img/plant-room-wide.jpg" alt="Commercial inverter plant room"></div>
    <div>
      <p class="eyebrow">Offices, shops and commercial buildings</p>
      <h2>The cost is the generator, and everybody knows it.</h2>
      <p>A commercial building's diesel bill is usually treated as a fixed cost of trading. It is not fixed — it moves with the pump price, and it carries servicing, overhaul and downtime behind it. A hybrid system moves the generator from daily service to genuine standby.</p>
      <p>Work in a trading premises has to happen without closing it. We phase the installation so that the parts of the building in use stay in use, and we do the noisy and disruptive work outside business hours where that is what it takes.</p>
      <ul class="ticks">
        <li>5–45 kW systems for single premises, branches and multi-tenant buildings</li>
        <li>POS, server, CCTV and cold-storage circuits identified and protected</li>
        <li>Generator integration and run-hour reduction</li>
        <li>Installation phased around trading hours</li>
      </ul>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap split">
    <div>
      <p class="eyebrow">Industrial and manufacturing</p>
      <h2>Motive load is a different problem.</h2>
      <p>Factories and workshops are dominated by motors, compressors and pumps — loads with high starting currents that punish an undersized inverter and a badly designed board. Sizing here is about surge behaviour and duty cycle, not just kilowatt-hours.</p>
      <p>Industrial roofs are usually the best asset on the site: large, unobstructed long-span or profile-sheet surfaces that take an array cleanly, with mounting designed around the existing sheet line so the roof covering is not compromised.</p>
      <ul class="ticks">
        <li>Long-span and profile-sheet roof mounting, and ground-mount alternatives</li>
        <li>Sizing for motor starting current and duty cycle, not average draw</li>
        <li>Three-phase configurations and phase-balancing</li>
        <li>Daytime process load carried by the array, with storage for critical circuits</li>
      </ul>
    </div>
    <div class="split-media"><img src="assets/img/industrial-roof-array.jpg" alt="Solar array across an industrial roof"></div>
  </div>
</section>

<section class="section section--surface">
  <div class="wrap split split--rev">
    <div class="split-media"><img src="assets/img/roof-array-longspan.jpg" alt="Array installed on a pitched roof"></div>
    <div>
      <p class="eyebrow">Schools, clinics and places of worship</p>
      <h2>Budgets that are raised, not borrowed.</h2>
      <p>Institutions are usually spending money that was contributed rather than earned, and the system has to be defensible to whoever gave it. We quote in a form that a committee can read: every item, every quantity, every rate, and a clear statement of what is not included.</p>
      <p>These buildings also tend to have concentrated, predictable demand — a clinic's cold chain and theatre, a school's daytime classrooms, a church's weekend peak — which is exactly the kind of profile solar suits well.</p>
      <ul class="ticks">
        <li>Phased deployment where the budget arrives in stages</li>
        <li>Cold-chain and critical-care circuits given dedicated backup</li>
        <li>Daytime-dominant profiles sized to run largely off the array</li>
        <li>Training for in-house maintenance staff at handover</li>
      </ul>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap split">
    <div>
      <p class="eyebrow">Multi-storey and corporate buildings</p>
      <h2>Installed floor by floor, in an occupied building.</h2>
      <p>In multi-floor buildings we install per floor rather than centrally. Each floor gets its own inverter capacity, storage and share of the array, tied through a transfer switch into that floor's distribution. Floors operate independently, so a fault or a maintenance shutdown on one does not take the building down.</p>
      <p>It also means the work can proceed a floor at a time, with two crews on separate floors, while the building stays occupied and trading. Roof area is usually the binding constraint rather than budget, which is why siting is settled before anything is ordered.</p>
      <ul class="ticks">
        <li>Per-floor inverter, storage and array allocation with independent operation</li>
        <li>Two-crew phased installation in occupied premises</li>
        <li>Roof, ground, canopy and façade options where roof area is short</li>
        <li>As-built drawings, O&amp;M manuals and operator training at handover</li>
      </ul>
    </div>
    <div class="split-media"><img src="assets/img/plant-room-inverter-bank.jpg" alt="Bank of parallel inverters with hybrid storage"></div>
  </div>
</section>
""" + CTA

page("sectors.html",
     "Who we work with — Prenniex Global Solutions",
     "Solar and power systems for homes and estates, offices and commercial buildings, industrial premises, schools and clinics, and multi-storey corporate buildings across Nigeria.",
     sectors)


# =============================================================== SYSTEMS
systems = """
<section class="pagehead">
  <div class="wrap">
    <p class="eyebrow">System sizes</p>
    <h1>What size you actually need.</h1>
    <p class="lede">These are the configurations we install most often, with what each one typically carries. Treat them as a starting point — the size that ends up on your quotation is the one your own load calls for.</p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="grid grid-3">

      <div class="plan">
        <span class="cap">2.5 kVA</span>
        <span class="for">Flat, small home, small shop</span>
        <dl>
          <dt>Inverter</dt><dd>2.5 kVA pure sine wave</dd>
          <dt>Storage</dt><dd>2 × 200 Ah tubular, or 5 kWh lithium</dd>
          <dt>Array</dt><dd>6 × 300 W (1.8 kWp)</dd>
          <dt>Also included</dt><dd>Charge controller, surge protection, DC and AC boards, mounting</dd>
        </dl>
        <div class="runs"><b>Typically runs</b>Lights, ceiling and standing fans, TV and decoder, laptops and phones, Wi-Fi, and a small fridge overnight.</div>
      </div>

      <div class="plan">
        <span class="cap">3.5 kVA</span>
        <span class="for">Family home, small office</span>
        <dl>
          <dt>Inverter</dt><dd>3.5 kVA hybrid, built-in MPPT</dd>
          <dt>Storage</dt><dd>5 kWh lithium</dd>
          <dt>Array</dt><dd>8 × 320 W (2.6 kWp)</dd>
          <dt>Also included</dt><dd>Load separation, surge protection, boards, mounting and accessories</dd>
        </dl>
        <div class="runs"><b>Typically runs</b>Everything above plus a full fridge-freezer, water pump, printer, and one bedroom air conditioner for part of the night.</div>
      </div>

      <div class="plan">
        <span class="cap">5 kVA</span>
        <span class="for">Larger home, duplex</span>
        <dl>
          <dt>Inverter</dt><dd>5 kVA hybrid</dd>
          <dt>Storage</dt><dd>10 kWh lithium</dd>
          <dt>Array</dt><dd>10–12 × 550–600 W (5.5–7 kWp)</dd>
          <dt>Also included</dt><dd>Full essential-load separation, protection, boards, rails</dd>
        </dl>
        <div class="runs"><b>Typically runs</b>A duplex on essential load with two air conditioners running through the evening, plus pumps, freezers and a home office.</div>
      </div>

      <div class="plan">
        <span class="cap">10 kW</span>
        <span class="for">Business premises, guesthouse, clinic</span>
        <dl>
          <dt>Inverter</dt><dd>10 kW hybrid, or paralleled units</dd>
          <dt>Storage</dt><dd>20 kWh lithium</dd>
          <dt>Array</dt><dd>18–22 × 600 W (11–13 kWp)</dd>
          <dt>Also included</dt><dd>Generator integration, changeover, protection, sub-distribution</dd>
        </dl>
        <div class="runs"><b>Typically runs</b>Several air conditioners, cold storage, POS and server equipment, CCTV, lighting and general power through a working day.</div>
      </div>

      <div class="plan">
        <span class="cap">15 kW</span>
        <span class="for">Floor of a building, workshop</span>
        <dl>
          <dt>Inverter</dt><dd>15 kW hybrid, single or three-phase</dd>
          <dt>Storage</dt><dd>20 kWh and upward</dd>
          <dt>Array</dt><dd>Sized to available roof, ground or canopy area</dd>
          <dt>Also included</dt><dd>Transfer switching into existing distribution, phase balancing</dd>
        </dl>
        <div class="runs"><b>Typically runs</b>A full office floor, or a workshop with motor loads, with the generator reduced to genuine standby.</div>
      </div>

      <div class="plan">
        <span class="cap">45 kW +</span>
        <span class="for">Multi-storey, per floor</span>
        <dl>
          <dt>Inverter</dt><dd>3 × 15 kW per floor (45 kW)</dd>
          <dt>Storage</dt><dd>3 × 20 kWh per floor (60 kWh)</dd>
          <dt>Array</dt><dd>Approx. 27 kWp per floor, roughly 99 m² of surface</dd>
          <dt>Also included</dt><dd>Per-floor transfer switching, independent operation, as-built drawings</dd>
        </dl>
        <div class="runs"><b>Typically runs</b>An entire floor of an occupied office building, scaled across as many floors as the roof and siting allow.</div>
      </div>

    </div>
    <p class="note">Capacities above are typical configurations, not a price list. Equipment costs move with the exchange rate, so we quote against current rates at the time of the enquiry and hold that price for a stated validity period.</p>
  </div>
</section>

<section class="section section--surface">
  <div class="wrap">
    <p class="eyebrow">Choosing a battery</p>
    <h2>Lithium or tubular.</h2>
    <p class="lede">This is the single biggest decision on most quotations, and the one where the cheapest option is most often the wrong one — but not always.</p>
    <div class="table-scroll">
      <table class="spec cmp" style="margin-top:26px">
        <thead><tr><th></th><th scope="col">Tubular (lead-acid)</th><th scope="col">Lithium (LiFePO&#8324;)</th></tr></thead>
        <tbody>
        <tr><th scope="row">Cost at purchase</th><td>Lower</td><td>Higher, typically two to three times</td></tr>
        <tr><th scope="row">Usable capacity</th><td>About half the rated capacity</td><td>Most of the rated capacity</td></tr>
        <tr><th scope="row">Expected life</th><td>Around 3–5 years with good care</td><td>Around 10 years or more</td></tr>
        <tr><th scope="row">Maintenance</th><td>Topping up and ventilation needed</td><td>None</td></tr>
        <tr><th scope="row">Space and weight</th><td>Bulky, needs a ventilated rack</td><td>Compact, wall or floor mounted</td></tr>
        <tr><th scope="row">Cost over ten years</th><td>Usually higher, once replacements are counted</td><td>Usually lower</td></tr>
        <tr><th scope="row">Best when</th><td>Budget is tight today and the system is small</td><td>The system matters and you intend to keep it</td></tr>
        </tbody>
      </table>
    </div>
    <p class="note">We will quote both on the same document where it is a real choice, so you can see the difference rather than take our word for it.</p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="grid grid-2">
      <div>
        <p class="eyebrow">Included in every installation</p>
        <h2>What the price covers.</h2>
        <ul class="ticks">
          <li>Site visit, load assessment and system design</li>
          <li>Supply of inverter, batteries, panels and mounting</li>
          <li>DC and AC protection — breakers, fuses and surge devices</li>
          <li>DC and AC distribution boards, fully labelled</li>
          <li>Load separation between backed-up and non-essential circuits</li>
          <li>Cabling, connectors, earthing and mounting accessories</li>
          <li>Installation, testing and commissioning</li>
          <li>Handover walk-through and settings explained</li>
          <li>Manufacturer warranties registered in your name</li>
        </ul>
      </div>
      <div>
        <p class="eyebrow">Quoted separately</p>
        <h2>What is not assumed.</h2>
        <p>These are the items that move a budget after work starts, so we price them openly rather than bury an allowance that will not hold.</p>
        <ul class="dash">
          <li>Rewiring of existing circuits found to be unsafe or inadequate</li>
          <li>Civil work — plinths, trenching, roof strengthening, plant room preparation</li>
          <li>Structural assessment where roof capacity is in doubt</li>
          <li>Generator repair or replacement</li>
          <li>Long cable runs and any work at height requiring scaffolding</li>
          <li>Statutory or landlord approvals, where these are required</li>
        </ul>
        <div class="btn-row"><a class="btn btn--ghost" href="contact.html">Get a quotation</a></div>
      </div>
    </div>
  </div>
</section>
""" + CTA

page("systems.html",
     "System sizes — Prenniex Global Solutions",
     "Typical solar and inverter system configurations from 2.5 kVA to 45 kW and above, what each one runs, a lithium versus tubular battery comparison, and what is and is not included in an installation.",
     systems)


# =============================================================== PROJECTS
projects = """
<section class="pagehead">
  <div class="wrap">
    <p class="eyebrow">Projects</p>
    <h1>Selected work.</h1>
    <p class="lede">Client names and addresses are withheld as a matter of course. References and site visits can be arranged for serious enquiries, with the client's consent.</p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="grid grid-3">

      <article class="proj">
        <img src="assets/img/plant-room-inverter-bank.jpg" alt="Six parallel inverters and a hybrid storage unit in a plant room">
        <div class="proj-body">
          <span class="tag">Commercial</span>
          <h3>Parallel inverter plant room</h3>
          <p>Bank of parallel inverters alongside a hybrid unit and enclosed storage, with dedicated distribution and isolation between strings. Laid out for access and future capacity rather than to fit the wall.</p>
          <div class="meta">Lagos · Solar hybrid · Plant room build</div>
        </div>
      </article>

      <article class="proj">
        <img src="assets/img/industrial-roof-array.jpg" alt="Modules mounted across an industrial roof">
        <div class="proj-body">
          <span class="tag">Industrial</span>
          <h3>Industrial roof array</h3>
          <p>Array set out across a long-span roof, rail-mounted and strung to keep cable runs short and shading losses down. Mounting designed around the existing sheet line and access routes.</p>
          <div class="meta">Solar PV · Roof mounting</div>
        </div>
      </article>

      <article class="proj">
        <img src="assets/img/roof-array-longspan.jpg" alt="Close view of rail-mounted modules and connectors on a metal roof">
        <div class="proj-body">
          <span class="tag">Institutional</span>
          <h3>Pitched profile-sheet installation</h3>
          <p>Modules mounted either side of a ridge to use both faces of a pitched roof, with connectors dressed and secured off the sheet to keep water out of the cable path.</p>
          <div class="meta">Solar PV · Dual-pitch array</div>
        </div>
      </article>

      <article class="proj">
        <img src="assets/img/twin-hybrid-inverters.jpg" alt="Two hybrid inverters with PV isolators and metering on a mounting board">
        <div class="proj-body">
          <span class="tag">Commercial</span>
          <h3>Twin hybrid inverter installation</h3>
          <p>Paired hybrid inverters on a fabricated mounting board with separate PV isolation per inverter, live metering, and positive and negative junctions kept apart and labelled.</p>
          <div class="meta">Solar hybrid · Distribution</div>
        </div>
      </article>

      <article class="proj">
        <img src="assets/img/dc-ac-distribution-boards.jpg" alt="Labelled DC and AC boards with surge devices and changeover">
        <div class="proj-body">
          <span class="tag">Electrical</span>
          <h3>DC and AC board installation</h3>
          <p>Solar DC board with per-string breakers and surge devices, AC board with input and output metering and an inverter-to-utility changeover. Every way labelled by hand and by function.</p>
          <div class="meta">Electrical installation · Protection</div>
        </div>
      </article>

      <article class="proj">
        <img src="assets/img/storage-and-boards.jpg" alt="Hybrid inverter, DC and AC boards and a lithium storage unit installed together">
        <div class="proj-body">
          <span class="tag">Residential</span>
          <h3>Hybrid inverter and lithium storage</h3>
          <p>Complete single-property installation: hybrid inverter, floor-standing lithium storage, solar and AC boards, DC isolator and full load separation between backed-up and non-essential circuits.</p>
          <div class="meta">Solar hybrid · Storage · Distribution</div>
        </div>
      </article>

      <article class="proj">
        <img src="assets/img/residential-roof-array.jpg" alt="Array installed across a residential pitched roof">
        <div class="proj-body">
          <span class="tag">Residential</span>
          <h3>Residential roof array</h3>
          <p>Array laid across two roof faces on a private residence, sized to the measured evening load rather than to the roof area available, and routed down to a ground-floor inverter position.</p>
          <div class="meta">Ogun State · Solar PV</div>
        </div>
      </article>

      <article class="proj">
        <img src="assets/img/industrial-roof-exterior.jpg" alt="Solar array visible along the ridge of an industrial building roof">
        <div class="proj-body">
          <span class="tag">Industrial</span>
          <h3>Ridge-line array, secured site</h3>
          <p>Array set along the full ridge of a secured industrial building, positioned for orientation and for access during cleaning and maintenance without disturbing the roof covering.</p>
          <div class="meta">Solar PV · Industrial roof</div>
        </div>
      </article>

      <article class="proj">
        <img src="assets/img/inverter-room-standby.jpg" alt="Inverter and battery bank in an equipment room with fire extinguishers">
        <div class="proj-body">
          <span class="tag">Commercial</span>
          <h3>Backup room with fire provision</h3>
          <p>Inverter and battery bank on a fabricated rack in a small equipment room, with a separate hybrid unit, changeover to public supply, and fire extinguishers mounted and signed at the point of use.</p>
          <div class="meta">Storage · Electrical · Fire provision</div>
        </div>
      </article>

    </div>

    <div class="callout">
      <p><strong>Considering something similar?</strong> Send us a photograph of your existing board or inverter position and a list of what you want running. That is usually enough for us to tell you the range you are looking at before anyone visits.</p>
    </div>
  </div>
</section>
""" + CTA

page("projects.html",
     "Projects — Prenniex Global Solutions",
     "Selected solar hybrid, battery storage and electrical installation work by Prenniex Global Solutions across commercial, industrial, institutional and residential buildings in Nigeria.",
     projects)


# =============================================================== ABOUT
about = """
<section class="pagehead">
  <div class="wrap">
    <p class="eyebrow">About</p>
    <h1>Fifteen years of keeping the lights on.</h1>
    <p class="lede">Prenniex Global Solutions is a Nigerian power engineering company. We design, supply, install and maintain solar and inverter systems, and we do the electrical work that carries them.</p>
  </div>
</section>
""" + STATS + """

<section class="section">
  <div class="wrap split">
    <div>
      <p class="eyebrow">Who we are</p>
      <h2>An engineering contractor, not a distributor with a van.</h2>
      <p>We started in electrical installation and moved into solar as the economics changed, which is the reverse of how most solar companies in this market began. It shows in the work: the boards, the protection and the switching get the same attention as the panels, because we were doing that part first.</p>
      <p>The company works across the range — a 2.5 kVA system in a flat, a plant room full of paralleled inverters, an array across a factory roof, a multi-storey building installed floor by floor. What does not change between them is the method: measure first, size honestly, install so it can be maintained, and stay reachable afterwards.</p>
      <p>We are not tied to one manufacturer. What goes into a job is what suits the load, the space and the budget in front of us, and we will say so when a cheaper component is a false economy — and when it is not.</p>
    </div>
    <div class="split-media"><img src="assets/img/plant-room-wide.jpg" alt="Prenniex plant room installation with parallel inverters and storage"></div>
  </div>
</section>

<section class="section" id="utility">
  <div class="wrap">
    <p class="eyebrow">Utility scale, and how to read our figures</p>
    <h2>Four UN-sponsored solar farms, and a hundred buildings.</h2>
    <p class="lede">Two different kinds of work sit behind the numbers at the top of this page, and it matters which is which.</p>
    <div class="grid grid-2" style="margin-top:34px">
      <div class="card">
        <h3>Installations we deliver end to end</h3>
        <p>Homes, offices, industrial premises, institutions and multi-storey buildings — over a hundred of them. On these we do everything: survey, design, supply, installation, commissioning and support. Individually they run from 2.5 kVA in a flat to 45 kW and upward per floor in a corporate building. This is the work described everywhere else on this site.</p>
      </div>
      <div class="card">
        <h3>Contributing engineering at utility scale</h3>
        <p>Our engineers have worked as contributing engineers on four solar farm projects sponsored under United Nations programmes. Utility-scale arrays and storage of that size are what carry the 103.5 MWp and 83 MWh figures. We did not deliver those projects alone and we do not present them as though we did — we contributed engineering to them, and we will describe exactly what we did on request.</p>
      </div>
    </div>
    <div class="callout">
      <p><strong>Why we spell this out.</strong> A capacity figure with no explanation invites the obvious question, and a technical evaluator is right to ask it. The honest answer is more interesting than the number: a company that has worked to utility-scale delivery standards and also wires a three-bedroom flat properly is a rarer thing than either on its own.</p>
    </div>
  </div>
</section>

<section class="section section--surface">
  <div class="wrap">
    <p class="eyebrow">What we hold to</p>
    <h2>Four commitments, and you can hold us to all of them.</h2>
    <div class="grid grid-4" style="margin-top:40px">
      <div class="value">
        <h3>Measure before you quote</h3>
        <p>No system size is offered before someone has looked at the building and listed what has to run. A number given before that is a guess dressed as a quotation.</p>
      </div>
      <div class="value">
        <h3>Price every item</h3>
        <p>Quotations show quantities and unit rates, and state plainly what is excluded. A lump sum hides both the margin and the omissions.</p>
      </div>
      <div class="value">
        <h3>Build it serviceable</h3>
        <p>Labelled boards, accessible equipment, as-built information handed over. Any competent electrician should be able to work on your system, not only us.</p>
      </div>
      <div class="value">
        <h3>Be there afterwards</h3>
        <p>Warranties pass to you in your own name, and we answer the phone when a system we installed gives trouble. Most of our work now comes from people we installed for before.</p>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap split split--rev">
    <div class="split-media"><img src="assets/img/roof-array-longspan.jpg" alt="Array installation across a pitched long-span roof"></div>
    <div>
      <p class="eyebrow">How we deliver</p>
      <h2>What keeps a job to weeks rather than months.</h2>
      <ul class="ticks">
        <li><strong>Our own crews.</strong> Installation is not subcontracted out to whoever is free that week. The people who quote the job are the people who deliver it.</li>
        <li><strong>Phased working.</strong> On larger buildings, crews work in parallel on separate floors or zones, which compresses the programme without working the premises around the clock.</li>
        <li><strong>Established supply lines.</strong> Equipment is drawn down against standing supplier relationships, which keeps procurement off the critical path when rates and availability move.</li>
        <li><strong>Handover that transfers capability.</strong> Settings explained, drawings and manuals provided, and your own maintenance staff trained where you have them.</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section--surface">
  <div class="wrap">
    <div class="grid grid-2">
      <div>
        <p class="eyebrow">Leadership</p>
        <h2>Who you will be dealing with.</h2>
        <p>Jobs are run by the people who priced them. The director is on site during survey and commissioning, and the same engineer carries a job from measurement through to handover.</p>
        <div class="card" style="margin-top:26px">
          <h3>Engr. P. Omoniyi</h3>
          <p style="color:var(--link); font-weight:600; margin:.2em 0 .8em">Director</p>
          <p>Project engineer and graduate of Ladoke Akintola University of Technology, and the technical lead on the company's commercial and institutional installations.</p>
        </div>
      </div>
      <div>
        <p class="eyebrow">Coverage</p>
        <h2>Where we work.</h2>
        <p>Lagos is the base and the majority of the work. Beyond it we install in Ibadan, Akure and Ado-Ekiti, and we travel for clients extending a single standard across several sites.</p>
        <ul class="dash">
          <li>Head office — 1 Ayo Oluede Street, Ojodu-Berger, Lagos</li>
          <li>Ogun office — No 48B Glory Avenue, Papa Oja, Ibafo, Ogun State</li>
          <li>Project coverage — Lagos, Ibadan, Akure, Ado-Ekiti</li>
          <li>Elsewhere in Nigeria by arrangement, for multi-site clients</li>
        </ul>
        <div class="btn-row"><a class="btn btn--ghost" href="contact.html">Talk to us</a></div>
      </div>
    </div>
  </div>
</section>
""" + CTA

page("about.html",
     "About — Prenniex Global Solutions",
     "Prenniex Global Solutions is a Nigerian solar and electrical engineering contractor working across Lagos, Ibadan, Akure and Ado-Ekiti.",
     about)


# =============================================================== FAQ
faq = """
<section class="pagehead">
  <div class="wrap">
    <p class="eyebrow">Questions</p>
    <h1>The things people ask before they commit.</h1>
    <p class="lede">Answered as we would answer them on the phone. If yours is not here, call and ask.</p>
  </div>
</section>

<section class="section">
  <div class="wrap" style="max-width:860px">

    <h2>Cost and quotations</h2>
    <div class="faq">
      <details><summary>How much will my system cost?</summary><div class="answer"><p>It depends on what has to run and for how long. A flat needing lights, fans, a TV and a fridge is a different order of expense from a duplex running two air conditioners overnight. Equipment prices also move with the exchange rate, which is why we do not publish a price list that would be wrong within weeks.</p><p>Tell us the appliances and the hours you need covered and we will give you a written quotation with every item, quantity and rate shown, held for a stated validity period.</p></div></details>
      <details><summary>Is the site visit really free?</summary><div class="answer"><p>Yes, for homes and small premises — a visit, an appliance schedule, a look at your existing board and roof, and a recommended size. On larger buildings a full logged energy audit takes a working week and is charged, but that cost is credited in full against the contract if you go on to install with us.</p></div></details>
      <details><summary>Do you offer payment in instalments?</summary><div class="answer"><p>On larger installations we can arrange a facility against the system and structure repayment monthly. Terms are set by the lender's own credit process and the facility can be placed with a lender of your choosing. We are not a finance company and we will not pretend the arithmetic is better than it is — we will show you the total cost of the money alongside the cost of the system.</p></div></details>
      <details><summary>Why is your quotation higher than the one I have from someone else?</summary><div class="answer"><p>Usually because of what is in it. The commonest differences are protection devices and boards, cable sizing, load separation, and whether the battery capacity quoted is the rated figure or the usable figure. Send us the other quotation and we will tell you specifically what is different — including when the other one is genuinely the better buy.</p></div></details>
    </div>

    <h2 style="margin-top:60px">Sizing and equipment</h2>
    <div class="faq">
      <details><summary>How do I know what size I need?</summary><div class="answer"><p>By listing what must run, its wattage, and how many hours a day you need it. That gives the energy in kilowatt-hours, which sizes the battery; the largest things running at once size the inverter; and the battery plus the sunshine you get sizes the array. We do this properly during the site visit rather than guessing from the size of the house.</p></div></details>
      <details><summary>Do I have to power the whole building?</summary><div class="answer"><p>No, and usually you should not. Separating essential circuits from heavy loads such as air conditioning, water heaters and cookers gives you far more backup hours for the same money. That separation is part of our installation, not an extra.</p></div></details>
      <details><summary>Lithium or tubular batteries?</summary><div class="answer"><p>Lithium costs more to buy, gives you most of its rated capacity rather than about half, needs no maintenance and lasts roughly three times as long. Over ten years it is usually the cheaper option. Tubular still makes sense on a small system or a tight budget. We quote both where it is a real choice.</p></div></details>
      <details><summary>Which brands do you install?</summary><div class="answer"><p>We are not tied to a single manufacturer. We work with equipment that can be serviced and replaced in Nigeria — including Felicity Solar, LVTopsun, Cworth, Bestcom and Solarmac — and we will quote a brand you prefer if you have one. What matters more than the badge is that the specification is honest and the protection around it is right.</p></div></details>
      <details><summary>Can I add to the system later?</summary><div class="answer"><p>Yes, if it is designed for it from the start. Tell us at the survey what you expect to add — more air conditioning, a borehole, a new wing — and we will leave the inverter capacity, board space and cable routes to take it. Retrofitting expansion into a system that was sized exactly is always more expensive.</p></div></details>
      <details><summary>Can I keep my existing inverter?</summary><div class="answer"><p>Often, yes. If the inverter is sound and only the batteries have failed, a lithium retrofit onto the existing unit is usually the best value upgrade available. We will tell you honestly if the inverter is not worth keeping.</p></div></details>
    </div>

    <h2 style="margin-top:60px">Installation and the building</h2>
    <div class="faq">
      <details><summary>How long does an installation take?</summary><div class="answer"><p>A domestic system is typically two to four days from delivery to commissioning. A commercial installation depends on the distribution work involved. On multi-floor buildings we work floor by floor with more than one crew, and the building stays occupied throughout.</p></div></details>
      <details><summary>Will you have to close my business or leave the house without power?</summary><div class="answer"><p>There are short interruptions when the boards are cut over — usually an hour or two, scheduled with you. Everything else is done live alongside the existing supply. On trading premises we do the disruptive work outside business hours where that is what it takes.</p></div></details>
      <details><summary>My roof will not take an array. What are the options?</summary><div class="answer"><p>Ground-mount on available land, a car park canopy, or a façade installation. Roof area — not budget — is the commonest constraint we meet, and structural capacity has to be verified before anything is committed to a roof. We settle this before ordering, not after.</p></div></details>
      <details><summary>Do the panels work in the rainy season?</summary><div class="answer"><p>They generate at reduced output in diffuse light rather than stopping. A hybrid system covers the shortfall by charging from public supply or a generator, so the battery stays ready. Rain also washes dust off the array, which helps output when the sun returns.</p></div></details>
      <details><summary>Can I disconnect from the grid entirely?</summary><div class="answer"><p>Technically yes, and occasionally it is the right answer where there is no supply at all. For most buildings it is not: sizing for the worst week of the year without any other source means buying far more array and battery than the other fifty-one weeks need. A hybrid system that uses whatever supply exists is almost always the better economics.</p></div></details>
    </div>

    <h2 style="margin-top:60px">After handover</h2>
    <div class="faq">
      <details><summary>What warranty do I get?</summary><div class="answer"><p>Manufacturer warranties on the equipment, registered in your name and passed to you at handover, plus our own warranty on the installation workmanship. We do not stand between you and the manufacturer on a claim.</p></div></details>
      <details><summary>What maintenance does the system need?</summary><div class="answer"><p>Array cleaning, connection and torque checks, battery health testing and a settings review. How often depends on the site — a dusty industrial roof needs attention several times a year, a domestic array much less. We will tell you what yours needs and you can do it yourself, use your own people, or put it on a schedule with us.</p></div></details>
      <details><summary>Will you maintain a system somebody else installed?</summary><div class="answer"><p>Yes. We will inspect it first and tell you what we find, including anything unsafe. We will not take on a maintenance schedule for an installation we consider dangerous until the dangerous part is corrected.</p></div></details>
      <details><summary>What happens if something fails?</summary><div class="answer"><p>Call us. For our own installations we attend, diagnose, and handle the warranty claim with the manufacturer on your behalf where the part is covered. Where it is not, you get a price before we do the work.</p></div></details>
    </div>

  </div>
</section>
""" + CTA

page("faq.html",
     "Questions — Prenniex Global Solutions",
     "Answers on cost, sizing, batteries, installation, roofs, warranties and maintenance for solar and inverter systems in Nigeria, from Prenniex Global Solutions.",
     faq)


# =============================================================== CONTACT
contact = """
<section class="pagehead">
  <div class="wrap">
    <p class="eyebrow">Contact</p>
    <h1>Tell us what you need powered.</h1>
    <p class="lede">The more you can say about the appliances and the hours, the more useful our first reply will be. A photograph of your existing board or inverter position helps too.</p>
  </div>
</section>

<section class="section">
  <div class="wrap contact-grid">
    <div>
      <div class="contact-block">
        <h3>Telephone and WhatsApp</h3>
        <p><a href="tel:+2347060793977">0706 079 3977</a></p>
      </div>
      <div class="contact-block">
        <h3>Email</h3>
        <p><a href="mailto:prenniexgs@gmail.com">prenniexgs@gmail.com</a></p>
      </div>
      <div class="contact-block">
        <h3>Head office</h3>
        <p>1 Ayo Oluede Street<br>Ojodu-Berger, Lagos<br>Nigeria</p>
      </div>
      <div class="contact-block">
        <h3>Ogun State office</h3>
        <p>No 48B Glory Avenue<br>Papa Oja, Ibafo<br>Ogun State, Nigeria</p>
      </div>
      <div class="contact-block">
        <h3>Office hours</h3>
        <p>Monday to Friday, 8am – 5pm<br>Saturday, 9am – 2pm<br>Site work is scheduled outside these hours where a premises needs it.</p>
      </div>
      <div class="contact-block">
        <h3>Coverage</h3>
        <p>Lagos · Ibadan · Akure · Ado-Ekiti, and elsewhere in Nigeria by arrangement.</p>
      </div>
      <div class="callout">
        <p><strong>Already holding a quotation from someone else?</strong> Send it over. We will tell you what the stated capacity will actually carry and what has been left out of the price. There is no charge for that, and no obligation.</p>
      </div>
    </div>

    <div>
      <h2>Request a quotation</h2>
      <p>No charge for the visit or the quotation. We will come and look, list what has to run, and price a system against it.</p>

      <form id="enquiry" novalidate>
        <div class="field">
          <label for="name">Your name</label>
          <input id="name" name="name" type="text" autocomplete="name" required>
        </div>
        <div class="field">
          <label for="org">Organisation <span style="color:var(--muted);font-weight:400">(if any)</span></label>
          <input id="org" name="org" type="text" autocomplete="organization">
        </div>
        <div class="field">
          <label for="email">Email</label>
          <input id="email" name="email" type="email" autocomplete="email" required>
        </div>
        <div class="field">
          <label for="phone">Telephone or WhatsApp</label>
          <input id="phone" name="phone" type="tel" autocomplete="tel">
        </div>
        <div class="field">
          <label for="place">Where is the property?</label>
          <input id="place" name="place" type="text" placeholder="Area and state">
        </div>
        <div class="field">
          <label for="type">What do you need?</label>
          <select id="type" name="type">
            <option>Solar or inverter system for a home</option>
            <option>Solar or inverter system for a business premises</option>
            <option>System for a school, clinic or place of worship</option>
            <option>System for an industrial or multi-storey building</option>
            <option>Battery replacement or lithium retrofit</option>
            <option>Electrical installation or distribution work</option>
            <option>CCTV, access control or gate automation</option>
            <option>Energy audit or site survey only</option>
            <option>Equipment supply only, no installation</option>
            <option>Maintenance or repair of an existing system</option>
            <option>Review of a quotation I already have</option>
            <option>Something else</option>
          </select>
        </div>
        <div class="field">
          <label for="message">What needs to run, and for how long?</label>
          <textarea id="message" name="message" placeholder="For example: lights and fans throughout, fridge and freezer, TV, three laptops, water pump, and one bedroom air conditioner from 9pm to 6am. Also useful: how many hours of public supply you get on a normal day."></textarea>
        </div>
        <div class="btn-row" style="margin-top:6px">
          <button class="btn btn--primary" type="submit">Send enquiry</button>
          <a class="btn btn--ghost" href="https://wa.me/2347060793977">Message on WhatsApp</a>
        </div>
        <p class="form-note" id="formnote">Sending opens your email application with the message ready to go. To have the form deliver on its own, connect it to a mail handler — see the handover notes.</p>
      </form>
    </div>
  </div>
</section>

<script>
(function(){
  var f=document.getElementById('enquiry'); if(!f) return;
  var note=document.getElementById('formnote');
  f.addEventListener('submit', function(e){
    e.preventDefault();
    var v=function(id){ var el=document.getElementById(id); return el?el.value.trim():''; };
    if(!v('name')||!v('email')){ note.textContent='Please add your name and email address before sending.'; return; }
    var body=['Name: '+v('name'),'Organisation: '+v('org'),'Email: '+v('email'),
              'Telephone: '+v('phone'),'Location: '+v('place'),'Enquiry type: '+v('type'),
              '','What needs to run:',v('message')].join('\\n');
    window.location.href='mailto:prenniexgs@gmail.com?subject='+
      encodeURIComponent('Website enquiry - '+v('type'))+'&body='+encodeURIComponent(body);
    note.textContent='Your email application should now be open with the message ready to send.';
  });
})();
</script>
"""

page("contact.html",
     "Contact — Prenniex Global Solutions",
     "Contact Prenniex Global Solutions in Lagos and Ogun State for a free site visit and quotation on solar, inverter, battery storage, electrical and security installations.",
     contact)


# =============================================================== PRODUCTS
products = """
<section class="pagehead">
  <div class="wrap">
    <p class="eyebrow">Products</p>
    <h1>What we stock, and what we will supply on its own.</h1>
    <p class="lede">Everything below can be bought from us without an installation, with sizing advice included at no charge. Tell us what you are building and we will send an itemised quotation the same day where we can.</p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="callout" style="margin-top:0">
      <p><strong>Why there are no prices on this page.</strong> Solar equipment is imported and priced against the exchange rate, so a published price list would be wrong within weeks and we are not going to quote you a figure we cannot hold. Send us a list and you will get current rates, held for a stated validity period. Nothing about that is a negotiating tactic — it is just how this market prices.</p>
    </div>

    <div class="grid grid-2" style="margin-top:44px">

      <div class="prodgroup">
        <h3>Solar panels</h3>
        <ul>
          <li>Mono-crystalline module <span>300 W</span></li>
          <li>Mono-crystalline module <span>320 W</span></li>
          <li>Mono-crystalline module <span>450 W</span></li>
          <li>Mono-crystalline module <span>550 W</span></li>
          <li>Mono-crystalline module <span>600 W</span></li>
        </ul>
      </div>

      <div class="prodgroup">
        <h3>Inverters</h3>
        <ul>
          <li>Pure sine wave inverter <span>1.5 – 2.5 kVA</span></li>
          <li>Hybrid inverter, built-in MPPT <span>3.5 kVA</span></li>
          <li>Hybrid inverter <span>5 kVA</span></li>
          <li>Hybrid inverter <span>10 kW</span></li>
          <li>Hybrid inverter, single or three-phase <span>15 kW</span></li>
          <li>Parallel-capable units for larger banks <span>on request</span></li>
        </ul>
      </div>

      <div class="prodgroup">
        <h3>Lithium storage (LiFePO&#8324;)</h3>
        <ul>
          <li>Wall-mounted lithium battery <span>5 kWh</span></li>
          <li>Floor-standing lithium battery <span>10 kWh</span></li>
          <li>Floor-standing lithium battery <span>15 kWh</span></li>
          <li>Rack and cabinet systems <span>20 kWh +</span></li>
          <li>Battery racking, enclosures and cabling <span>to suit</span></li>
        </ul>
      </div>

      <div class="prodgroup">
        <h3>Tubular and lead-acid storage</h3>
        <ul>
          <li>Deep-cycle tubular battery <span>200 Ah / 12 V</span></li>
          <li>Deep-cycle tubular battery <span>220 Ah / 12 V</span></li>
          <li>Battery racks and trays <span>2 – 8 units</span></li>
          <li>Terminal hardware, links and covers <span>to suit</span></li>
        </ul>
      </div>

      <div class="prodgroup">
        <h3>Charge controllers</h3>
        <ul>
          <li>MPPT charge controller <span>60 A</span></li>
          <li>MPPT charge controller <span>80 A</span></li>
          <li>MPPT charge controller <span>100 A</span></li>
          <li>PWM controllers for small systems <span>on request</span></li>
        </ul>
      </div>

      <div class="prodgroup">
        <h3>Protection and switching</h3>
        <ul>
          <li>DC isolators and PV MCCBs <span>various</span></li>
          <li>Surge protective devices, DC and AC <span>Type 2</span></li>
          <li>MCBs, RCDs and string fuses <span>various</span></li>
          <li>Manual and automatic changeover switches <span>to load</span></li>
          <li>Populated DC and AC distribution boards <span>built to order</span></li>
        </ul>
      </div>

      <div class="prodgroup">
        <h3>Mounting and installation accessories</h3>
        <ul>
          <li>Aluminium mounting rail <span>per metre</span></li>
          <li>End clamps, mid clamps and roof hooks <span>various</span></li>
          <li>Tin, tile and long-span roof mounts <span>to roof type</span></li>
          <li>Ground-mount and canopy frames <span>fabricated</span></li>
          <li>MC4 connectors, cable lugs and glands <span>various</span></li>
          <li>Solar DC cable <span>4 / 6 / 10 mm&#178;</span></li>
        </ul>
      </div>

      <div class="prodgroup">
        <h3>Solar street lighting</h3>
        <ul>
          <li>All-in-one integrated street light <span>60 W</span></li>
          <li>All-in-one integrated street light <span>100 W</span></li>
          <li>All-in-one integrated street light <span>150 – 200 W</span></li>
          <li>Split-array pole light with separate panel <span>to spec</span></li>
          <li>Poles, brackets and foundation cages <span>4 – 8 m</span></li>
          <li>Flood and perimeter security lights <span>various</span></li>
        </ul>
      </div>

      <div class="prodgroup">
        <h3>Solar water pumping</h3>
        <ul>
          <li>Submersible borehole pump and controller <span>to head and yield</span></li>
          <li>Surface and booster pumps <span>various</span></li>
          <li>Dry-run and level protection <span>float or probe</span></li>
          <li>Dedicated pump arrays and frames <span>to duty</span></li>
        </ul>
      </div>

      <div class="prodgroup">
        <h3>Security and automation</h3>
        <ul>
          <li>CCTV cameras, recorders and storage <span>to site</span></li>
          <li>Access control readers and controllers <span>various</span></li>
          <li>Gate motors and automation kits <span>sliding / swing</span></li>
          <li>Intercom and door entry <span>various</span></li>
        </ul>
      </div>

    </div>

    """ + BRANDS + """
    <p class="note">Brands vary with what is available and what suits the job. Where you have a preference, tell us and we will quote it; where you do not, we will recommend and explain why.</p>
  </div>
</section>

<section class="section section--surface">
  <div class="wrap">
    <div class="grid grid-3">
      <div class="card">
        <h3>How to order</h3>
        <p>Send a list, or a photograph of what you are replacing, by WhatsApp or email. We reply with an itemised quotation showing quantity and unit rate for every line, plus delivery. Payment terms and delivery time are confirmed on the quotation.</p>
        <div class="btn-row" style="margin-top:16px"><a class="btn btn--ghost" href="contact.html">Request a quotation</a></div>
      </div>
      <div class="card">
        <h3>Delivery</h3>
        <p>Delivered across Lagos and Ogun State, and to other states by arrangement. Batteries and panels are handled and packed for transit — we would rather add a day than send you a cracked module or a dented cabinet.</p>
      </div>
      <div class="card">
        <h3>Warranty and support</h3>
        <p>Manufacturer warranties are registered in your name, not ours. If you are installing it yourself or using your own electrician, commissioning support is available separately and the sizing advice is free either way.</p>
      </div>
    </div>
  </div>
</section>
""" + CTA

page("products.html",
     "Products — Prenniex Global Solutions",
     "Solar panels, hybrid inverters, lithium and tubular batteries, charge controllers, protection, mounting, street lighting, water pumping and security equipment supplied by Prenniex Global Solutions across Nigeria.",
     products)
