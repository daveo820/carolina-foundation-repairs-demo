# Static page builder for the Carolina Foundation Repairs concept. Run: python3 build.py
import json
BASE = 'https://carolina-foundation-repairs-demo.vercel.app/'  # Vercel production URL
TEL, TEL_H = '+12526376667', '(252)&nbsp;637&#8209;6667'
EXA = 'https://exa.ai/library/place/hmx2d0t6zt9'
ORG = {"@context":"https://schema.org","@type":"GeneralContractor","name":"Carolina Foundation Repairs, Inc.",
 "url":BASE,"telephone":"+1-252-637-6667","image":BASE+"img/crew-lifting-chimney.webp",
 "founder":{"@type":"Person","name":"Sean Corcoran","jobTitle":"Professional Engineer"},
 "address":{"@type":"PostalAddress","streetAddress":"424 NC Hwy 55 West","addressLocality":"New Bern","addressRegion":"NC","postalCode":"28562","addressCountry":"US"},
 "geo":{"@type":"GeoCoordinates","latitude":35.146314,"longitude":-77.10934},
 "openingHours":"Mo-Fr 07:30-16:00","areaServed":"Eastern North Carolina",
 "aggregateRating":{"@type":"AggregateRating","ratingValue":"4.5","reviewCount":"34"}}
FONTS = 'https://fonts.googleapis.com/css2?family=Schibsted+Grotesk:wght@500;700;800;900&family=Spline+Sans:wght@400;500;600&family=Spline+Sans+Mono:wght@500&display=swap'

def K(t, cls=''): return f'<p class="kicker {cls}"><span class="dot" aria-hidden="true"></span>{t}</p>'
# signature: the laser level line. A red beam with a source dot that sweeps across, plus a reading
def LASER(reading='0.0&deg;', cls=''):
    return f'<div class="laser {cls}" aria-hidden="true"><span class="beam"></span><span class="src"></span><span class="read">{reading}</span></div>'

HEAD = '''<!doctype html><html lang="en" class="no-js"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{t}</title><meta name="description" content="{d}"><link rel="canonical" href="{url}">
<meta property="og:type" content="website"><meta property="og:site_name" content="Carolina Foundation Repairs (concept)"><meta property="og:title" content="{t}"><meta property="og:description" content="{d}"><meta property="og:url" content="{url}"><meta property="og:image" content="{base}og.png">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{t}"><meta name="twitter:description" content="{d}"><meta name="twitter:image" content="{base}og.png">
<meta name="robots" content="noindex, nofollow"><!-- concept demo, not for indexing -->
<meta name="theme-color" content="#1f2226">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preload" as="style" href="{fonts}"><link rel="stylesheet" href="{fonts}" media="print" onload="this.media='all'"><noscript><link rel="stylesheet" href="{fonts}"></noscript>
{pre}<link rel="stylesheet" href="css/design-system.css"><link rel="stylesheet" href="css/components.css"><link rel="stylesheet" href="css/pages.css">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' fill='%231f2226'/%3E%3Crect x='4' y='15' width='24' height='2' fill='%23e3262d'/%3E%3Ccircle cx='6' cy='16' r='3' fill='%23e3262d'/%3E%3C/svg%3E">
<script>document.documentElement.classList.replace('no-js','js-ready')</script><script type="application/ld+json">{ld}</script></head><body>
<a class="skip" href="#main">Skip to content</a>
<div class="demo-bar">Concept by <a href="https://luminarch.pro">LuminArch</a>. Not the official Carolina Foundation Repairs site. Photos and copy come from their current site; reviews are real and sourced; placeholders are labeled.</div>
<header class="top"><div class="wrap nav"><a class="mark" href="index.html"><span class="mk" aria-hidden="true"><i></i></span><span><b>Carolina Foundation Repairs</b><small>New Bern &middot; Eastern North Carolina</small></span></a>
<button class="menu-btn" aria-expanded="false" aria-controls="menu">Menu</button><ul id="menu">{nav}</ul><a class="btn btn--red btn--call" href="tel:{tel}"><span class="cl-full">{telh}</span><span class="cl-short">Call</span></a></div></header><main id="main">'''

FOOT = f'''</main><footer class="site-foot">{LASER('0.0&deg; LEVEL','laser--foot')}<div class="wrap">
<div class="ft-top">
 <div><p class="ft-k">Estimates and inspections</p><a class="ft-num" href="tel:{TEL}">{TEL_H}</a><p class="ft-sub">Monday to Friday, 7:30 to 4:00</p></div>
 <address>424 NC Hwy 55 West<br>New Bern, NC 28562<br><a href="https://maps.google.com/?q=424+NC+Hwy+55+West+New+Bern+NC+28562" rel="noopener">Directions</a></address>
 <nav aria-label="Footer"><a href="services.html">Repairs</a><a href="engineering.html">Engineering</a><a href="reviews.html">Reviews</a><a href="about.html">About</a><a href="contact.html">Request an inspection</a></nav>
</div>
<div class="ft-row"><span>Carolina Foundation Repairs, Inc. &middot; NC General Contractor L.54562 &middot; Engineering by Sean Corcoran, PE, PLLC (P&#8209;1776)</span><span>Concept by <a href="https://luminarch.pro">LuminArch</a></span></div></div></footer>
<script src="js/main.js"></script></body></html>'''

NAV = [('services.html','Repairs'),('engineering.html','Engineering'),('reviews.html','Reviews'),('about.html','About'),('contact.html','Contact')]
def bc(*n): return {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":i+1,"name":a,"item":BASE+b} for i,(a,b) in enumerate(n)]}
def page(fn, t, d, body, ld=None, pre=''):
    assert 50 <= len(t) <= 60, (fn, len(t), t)
    assert 140 <= len(d) <= 160, (fn, len(d), d)
    nav = ''.join(f'<li><a href="{h}"' + (' aria-current="page"' if h == fn else '') + f'>{n}</a></li>' for h, n in NAV)
    url = BASE + ('' if fn == 'index.html' else fn)
    open(fn,'w').write(HEAD.format(t=t,d=d,url=url,base=BASE,nav=nav,ld=json.dumps(ld or [ORG]),fonts=FONTS,tel=TEL,telh=TEL_H,pre=pre) + body + FOOT)

# Google reviews, word for word, from the Exa place page (Google listing data, checked 8 Oct 2026). "..." = cut short at the source.
# Not quoted: the 1 star review from 31 Dec 2025 (a tenant says the crew left a gate open with a dog inside). It counts in the 4.5 average.
REV = {
 'enc':('2026-02-27','Feb 2026',5,'I have nothing but positive things to say about Carolina Foundation Repairs. From my first interaction with the office personnel, to Sean&rsquo;s inspection, to the crew performing the job, I was pleased with their work and communication. I thank Sean for not demanding that my entire encapsulation be redone at great expense as another company did at their inspection. Instead, Sean made a plan to improve the existing encapsulation, provide a better entry into the crawlspace, install flood vents to comply with insurance regulations, and do what was necessary to support the existing framework in the...','Crawl space'),
 'settle':('2025-10-22','Oct 2025',5,'Foundation settling can be so scary, that&rsquo;s why it&rsquo;s so important to be in good hands. I highly recommend this company! Sean and his team are professional, friendly, and approachable, with great communication from start to finish. They were very thorough and knowledgeable during the inspection and took the time to answer all of my questions (and trust me, I had a million!). They did excellent work on our property, and we&rsquo;re very satisfied with the results...','Foundation settling'),
 'old':('2024-10-01','Oct 2024',5,'Did great work for me on my 100 yr old house. Their work exceeded expectations and the cost was way less than expected. Delt mostly with Sean who was amazing, personable and professional, the woman I spoke to whenever I called the office was a sweetheart and walked me through what I was confused about. Repeat customer, saved me from wasting several thousand on a &ldquo;crawlspace specialist&rdquo;&rsquo;s recommendations that were definitely predatory. Highly recommend.','100 year old house'),
 'floor':('2021-07-21','Jul 2021',5,'Carolina Foundation Repairs did a great job for us. The evaluation of our floor was thorough and included pictures that helped us understand the scope of the project. The guys who worked on our floor showed up on time and did a great job especially with the finishing touches. Patty was also a pleasure to work with. It was a great experience would and I would recommend them to anyone.','Floor repair'),
 'years':('2021-03-24','Mar 2021',5,'I highly recommend Carolina Foundation for all your foundation and/or crawlspace needs. They are extremely professional and their quality of work is excellent! I would trust them 100% and their pricing is very reasonable. I have used Carolina Foundation for many years and will continue to use them...','Repeat customer'),
 'laser':('2020-01-29','Jan 2020',5,'Some issues about settling became apparent as part of a home inspection before purchase. We contracted with Sean Corcoran&rsquo;s company and received a thorough report with recommendations. The report was very helpful in final negotiations. We recently followed up with Sean to get the recommended work done. The process of putting in pilings, jacking up the sloping parts of the house, and monitoring with lasers was amazing to me. It is of course an expensive process too but we now have level floors!','Pilings and jacking'),
 'broker':('2017-05-05','May 2017',5,'Sean and his crew were outstanding! I&rsquo;m a real estate broker and his estimate was only a 1/3 of all the others! Sean took a tough situation and gave us hope! Patty at the office is also wonderful! They are my new &ldquo;go to&rdquo; people for foundation problems! I can&rsquo;t express my appreciation enough.','Real estate broker'),
}
# House style edits: one em dash replaced with a comma (Oct 2025), one emoji removed (Oct 2025). "Delt" and "would and I would" kept as written.
def rcard(k, cls=''):
    iso,d,s,txt,job = REV[k]
    return (f'<figure class="rcard rv {cls}"><div class="rc-top"><span class="rc-job">{job}</span><span class="rc-stars" aria-label="{s} out of 5">{"&#9733;"*s}</span></div>'
            f'<blockquote><p>{txt}</p></blockquote><figcaption>Google review &middot; <time datetime="{iso}">{d}</time></figcaption></figure>')

SRCSET = {'crew-lifting-chimney':(800,'(max-width:700px) 100vw, 1240px'),'chimney-before':(600,'(max-width:640px) 100vw, 50vw'),'chimney-after':(600,'(max-width:640px) 100vw, 50vw'),'brick-crack':(600,'(max-width:980px) 100vw, 33vw'),'pier-bracket':(600,'(max-width:980px) 100vw, 50vw')}
def IMG(src, alt, w, h, cls='', lazy=True, fp=False):
    ss = f' srcset="img/{src}-{SRCSET[src][0]}.webp {SRCSET[src][0]}w, img/{src}.webp {w}w" sizes="{SRCSET[src][1]}"' if src in SRCSET else ''
    return f'<img class="{cls}" src="img/{src}.webp"{ss} alt="{alt}" width="{w}" height="{h}"' + (' loading="lazy" decoding="async"' if lazy else '') + (' fetchpriority="high"' if fp else '') + '>'

METHODS = [
 ('S&#8209;101','helical','Helical piers','Steel shafts with helix plates screwed down to load bearing soil, then bracketed to the footing. Used for repairs and for new construction.'),
 ('S&#8209;102','push','Push piers','Hydraulically driven steel piers pressed down under the weight of the house until they reach firm soil, then used to lift.'),
 ('S&#8209;103','chimney','Leaning chimney repair','Chimneys are the heaviest part of a house per square foot, so they settle first. The fix is support under the footing, not straps to the wall.'),
 ('S&#8209;104','crawl','Crawl space repair','Rotted joists, caps, studs and subfloor replaced, plus grading, drainage and ventilation changes so it does not come back.'),
 ('S&#8209;105','walls','Wall reinforcement','Bowed foundation and retaining walls pushed back toward plumb and reinforced.'),
 ('S&#8209;106','slab','Mud jacking and slab leveling','Sunken slabs raised and supported from below.'),
 ('S&#8209;107','new','New construction foundations','Helical pier foundations for new buildings: no concrete curing, no vibration, loaded the same day.'),
]

# ---------- HOME ----------
page('index.html','Foundation Repair, New Bern NC | Carolina Foundation Repairs',
 'Foundation repair, piers, leaning chimneys and crawl space repair in Eastern NC. Owner Sean Corcoran, PE inspects every job. Call (252) 637-6667 in New Bern.', f'''
<section class="hero"><div class="hero-grid">
 <div class="hero-copy">{K('Foundation repair &middot; New Bern and Eastern NC')}
  <h1>An engineer inspects it. <span class="lvl">His crew levels it.</span></h1>
  <div class="hero-side"><p class="lede">Carolina Foundation Repairs is owned by Sean Corcoran, a licensed professional engineer who personally inspects every property. Then his crew installs the piers, lifts the house and fixes the crawl space.</p>
  <div class="cta"><a class="btn btn--red" href="tel:{TEL}">Call {TEL_H}</a><a class="btn btn--ghost" href="contact.html">Request an inspection</a></div></div>
 </div>
 <figure class="hero-photo">{IMG('crew-lifting-chimney','Two Carolina Foundation Repairs crew members installing hydraulic lifting jacks at the base of a brick chimney',1600,1193,'',False,True)}
  {LASER('LEVEL 0.0&deg;','laser--hero')}
  <figcaption>Crew lifting a leaning chimney. Photo from their current site.</figcaption></figure>
</div>
<dl class="readout wrap">
 <div><dt>Structural repair projects</dt><dd><span data-count="2000">2,000</span>+</dd><dd class="ro-s">their figure</dd></div>
 <div><dt>Google rating</dt><dd>4.5</dd><dd class="ro-s">34 reviews</dd></div>
 <div><dt>NC general contractor license</dt><dd>2004</dd><dd class="ro-s">L.54562, active</dd></div>
 <div><dt>Engineering firm</dt><dd>P&#8209;1776</dd><dd class="ro-s">Sean Corcoran, PE, PLLC</dd></div>
</dl></section>

<section class="symptoms" aria-labelledby="sy-h"><div class="wrap sy-grid">
 <div class="sy-head rv">{K('Field check')}<h2 id="sy-h">Signs your foundation is moving.</h2><p>Eastern North Carolina has soft sandy soil and a high water table. These are the symptoms Carolina Foundation Repairs lists on its own site. If you see two or more, call for an inspection.</p></div>
 <div class="sy-cols rv">
  <div><h3>Inside</h3><ul class="checks"><li>Cracks in floor surfaces</li><li>Sloping floors</li><li>Doors and windows that don&rsquo;t line up</li><li>Cracked plaster or sheetrock</li><li>Soft or uneven floors</li></ul></div>
  <div><h3>Outside</h3><ul class="checks"><li>Cracks in foundation walls or brick</li><li>Windows and doors pulling away from siding and trim</li><li>A chimney leaning away from the house</li><li>Bowed foundation or retaining walls</li></ul></div>
 </div>
</div></section>

<section class="ba wrap" aria-labelledby="ba-h">
 <div class="ba-head rv">{K('Before and after')}<h2 id="ba-h">A leaning chimney, plumb again.</h2><p>Same chimney, same corner of the house. Look at the gap between the brick and the siding.</p></div>
 <div class="ba-pair rv">
  <figure class="ba-fig ba-before">{IMG('chimney-before','Brick chimney leaning away from a house, with a gap opening between the brick and the green siding',1000,745)}<figcaption><b>Before</b> Gap open at the top</figcaption></figure>
  <figure class="ba-fig ba-after">{IMG('chimney-after','The same chimney after repair, sitting tight against the siding',1000,745)}<figcaption><b>After</b> Back against the house</figcaption></figure>
 </div>
 <p class="fine rv">Photos from the Leaning Chimney Repair page on carolinafoundationrepairs.com, posted in 2011 and 2012. <span class="ph">Placeholder</span> newer before and after sets.</p>
</section>

<section class="sheets" aria-labelledby="sh-h"><div class="wrap">
 <div class="sh-head rv">{K('Repairs','kicker--lt')}<h2 id="sh-h">Sheet index.</h2><p>Every repair Carolina Foundation Repairs offers, laid out like the drawing set an engineer would hand you.</p></div>
 <ol class="sheet-list">{''.join(f'<li class="rv"><a href="services.html#{k}"><span class="sh-no">{n}</span><b>{t}</b><span class="sh-d">{d}</span></a></li>' for n,k,t,d in METHODS)}</ol>
</div></section>

<section class="quote-band wrap rv" aria-labelledby="qb-h">
 <h2 id="qb-h" class="sr">What a customer saw</h2>
 <blockquote><p>&ldquo;The process of putting in pilings, jacking up the sloping parts of the house, and monitoring with lasers was amazing to me. It is of course an expensive process too but we now have level floors!&rdquo;</p></blockquote>
 <p class="qb-src">Google review, January 2020</p>
</section>

<section class="voices wrap" aria-labelledby="vo-h">
 <div class="vo-head rv">{K('Reviews')}<h2 id="vo-h">4.5 stars from 34 Google reviews.</h2></div>
 <div class="vo-grid">{rcard('enc','rcard--wide')}{rcard('old')}{rcard('broker')}</div>
 <a class="btn btn--ghost rv" href="reviews.html">Read more reviews</a>
</section>

<section class="pe wrap rv" aria-labelledby="pe-h">
 <div class="pe-card">{K('Engineering')}<h2 id="pe-h">Need a report, not a repair?</h2><p>Sean Corcoran, PE also does structural investigations, insurance cause of loss inspections, pre purchase evaluations and expert witness work through his engineering firm.</p><a class="btn btn--red" href="engineering.html">Engineering services</a></div>
 <figure>{IMG('pier-bracket','A steel foundation pier bracket installed against a brick footing in an excavated hole',1000,750)}<figcaption>Pier bracket installed at the footing.</figcaption></figure>
</section>
''', ld=[ORG, bc(('Home',''))], pre='<link rel="preload" as="image" href="img/crew-lifting-chimney.webp" imagesrcset="img/crew-lifting-chimney-800.webp 800w, img/crew-lifting-chimney.webp 1600w" imagesizes="(max-width:700px) 100vw, 1240px" fetchpriority="high">')

# ---------- SERVICES ----------
def method(i,m):
    n,k,t,d = m
    extra = {
     'helical':f'<figure>{IMG("pier-stock","Racks of galvanized helical pier shafts and extensions in the Carolina Foundation Repairs shop",400,300)}<figcaption>Helical piers and extensions in stock.</figcaption></figure>',
     'push':f'<figure>{IMG("crew-lifting-chimney","Crew installing hydraulic jacks at a chimney footing",1600,1193)}<figcaption>Hydraulic lift in progress.</figcaption></figure>',
     'chimney':f'<figure>{IMG("chimney-gap-closeup","Close up of the gap between a leaning chimney and the siding",900,671)}<figcaption>Leaning chimney close up, before repair.</figcaption></figure>',
     'walls':f'<figure>{IMG("brick-crack","A stair step crack running through a brick wall",1000,750)}<figcaption>Cracked brick before repair.</figcaption></figure>',
     'new':f'<figure>{IMG("pier-brackets","Helical pier brackets stacked on pallets",400,300)}<figcaption>Brackets ready for the next job.</figcaption></figure>',
    }.get(k, '<p class="note"><span class="ph">Placeholder</span> job photo</p>')
    return f'<article id="{k}" class="mth rv"><div class="mth-no">{n}</div><div class="mth-body"><h2>{t}</h2><p>{d}</p></div>{extra}</article>'
page('services.html','Piers and Crawl Space Repair | Carolina Foundation Repairs',
 'Helical and push piers, leaning chimney repair, crawl space repair, wall reinforcement, slab leveling and new construction foundations across Eastern NC.', f'''
<section class="page-head"><div class="wrap">{K('Repairs')}<h1>Repairs, sheet by sheet.</h1><p class="lede">Hydraulically driven and helical pier systems for everything from a sinking chimney to a whole house, plus the crawl space work that keeps it from happening again.</p></div>{LASER('S&#8209;100 SERIES','laser--head')}</section>
<div class="wrap mth-list">{''.join(method(i,m) for i,m in enumerate(METHODS))}</div>
<section class="wrap causes rv"><h2>What causes settlement</h2><ul class="checks checks--2"><li>Building on poorly compacted soil, fill, organic material or debris</li><li>Too much moisture, poor drainage or flooding</li><li>Soil moving or eroding on a slope</li><li>Poor original construction</li></ul><p class="fine">From the Residential Foundation Repair page on their current site.</p></section>
<section class="wrap warranty rv"><div><h2>Life of structure warranty</h2><p>Their current site says to ask about a transferable life of structure warranty on foundation repairs.</p><p class="note"><span class="ph">Placeholder</span> warranty terms, confirmed by Carolina Foundation Repairs.</p></div></section>
''', ld=[ORG, bc(('Home',''),('Repairs','services.html'))]+[{"@context":"https://schema.org","@type":"Service","name":m[2],"provider":{"@type":"GeneralContractor","name":"Carolina Foundation Repairs, Inc."},"areaServed":"Eastern North Carolina"} for m in METHODS])

# ---------- ENGINEERING ----------
ENG = ['Commercial building inspections','Structural investigations','Property insurance inspections and cause of loss','Expert witness testimony','Sizing of structural members','Wall system design','Metal building anchor bolt inspections','Monolithic slabs','Leak and moisture investigations','Documentation of deficiencies','Structural evaluations following pest inspections','Thermal evaluations','Draw inspections','Uplift connections','Truss repairs','Retaining structures','Sign foundations and supports']
page('engineering.html','Structural Engineering | Sean Corcoran PE, New Bern NC',
 'Structural investigations, insurance cause of loss inspections, pre purchase reports and expert witness work from Sean Corcoran, PE, PLLC in New Bern, NC.', f'''
<section class="page-head page-head--dark"><div class="wrap eng-head"><div>{K('Engineering','kicker--lt')}<h1>The report behind the repair.</h1><p class="lede">Sean Corcoran, PE personally inspects and evaluates each property. Engineering services are offered through his associated firm, Sean Corcoran, PE, PLLC (P&#8209;1776).</p></div>
<div class="plate" aria-hidden="true"><span>NC engineering firm</span><b>P&#8209;1776</b><span>Sean Corcoran, PE, PLLC</span></div></div></section>
<div class="wrap eng">
 <section class="rv"><h2>Services</h2><ol class="eng-list">{''.join(f'<li><span>{i+1:02d}</span>{e}</li>' for i,e in enumerate(ENG))}</ol></section>
 <aside class="rv">{rcard('laser','rcard--note')}<p class="note"><span class="ph">Placeholder</span> a sample report page (redacted) to show what buyers and insurers get.</p></aside>
</div>
''', ld=[ORG, bc(('Home',''),('Engineering','engineering.html')), {"@context":"https://schema.org","@type":"ProfessionalService","name":"Sean Corcoran, PE, PLLC","founder":{"@type":"Person","name":"Sean Corcoran"},"address":ORG["address"],"telephone":"+1-252-637-6667"}])

# ---------- REVIEWS ----------
page('reviews.html','Carolina Foundation Repairs Reviews | 4.5 Stars on Google',
 'Read Google reviews of Carolina Foundation Repairs in New Bern: piers and jacking, crawl space work, a 100 year old house and an estimate a third of the others.', f'''
<section class="page-head"><div class="wrap">{K('Reviews')}<h1>4.5 stars from 34 Google reviews.</h1><p class="lede">Seven of them, word for word. Customers name Sean, the crew, and Patty in the office.</p></div>{LASER('34 READINGS','laser--head')}</section>
<div class="wrap rv-wall">{''.join(rcard(k) for k in ['enc','settle','old','floor','years','laser','broker'])}</div>
<section class="wrap sources rv"><h2>Where these come from</h2><p>Copied from Carolina Foundation Repairs&rsquo; Google listing data on the <a href="{EXA}" rel="noopener">Exa place page</a>, checked 8 October 2026. Reviewer names were not included. Three dots mark where the source cuts a review short. We removed one emoji and changed one dash to a comma. The 4.5 average includes a 1 star review from December 2025 that is not shown here.</p>
<p class="note"><span class="ph">Placeholder</span> live Google reviews feed, plus a reply to every review.</p></section>
''', ld=[ORG, bc(('Home',''),('Reviews','reviews.html'))])

# ---------- ABOUT ----------
page('about.html','About Carolina Foundation Repairs | Sean Corcoran, PE',
 'Carolina Foundation Repairs is owned by Sean Corcoran, PE. More than 2,000 structural repair projects across Eastern North Carolina from a shop on NC Hwy 55.', f'''
<section class="page-head"><div class="wrap">{K('About')}<h1>Owned by an engineer. Run from a real shop.</h1><p class="lede">&ldquo;Don&rsquo;t trust your most valuable asset to some fly by night contractor working out of his home or truck.&rdquo; That line is on their site, and the shop on NC Hwy 55 backs it up.</p></div>{LASER('','laser--head')}</section>
<div class="wrap ab">
 <section class="ab-copy rv"><h2>The company</h2>
  <p>Carolina Foundation Repairs is owned by Sean Corcoran, a professionally licensed engineer who treats every job as its own problem and checks for the cause, not just the cracks you can see. The company says it has completed more than 2,000 structural repair projects across Eastern North Carolina, from Greenville to Jacksonville.</p>
  <p>Customers name Sean on inspections and Patty in the office. The crew carries its own stock of helical piers and brackets, a mini excavator, an excavator and a Bobcat loader.</p>
  <p class="note"><span class="ph">Placeholder</span> founding year. Their site says both &ldquo;since 1995&rdquo; and &ldquo;the past 15 years&rdquo; (written in 2012), and BBB lists 2000. One date needs confirming before launch.</p></section>
 <section class="ab-facts rv"><h2>On record</h2><dl>
  <div><dt>NC general contractor</dt><dd>License L.54562, Building, Limited. Active, first issued January 2004. Qualifier Sean Corcoran.</dd></div>
  <div><dt>Engineering</dt><dd>Sean Corcoran, PE, PLLC, P&#8209;1776</dd></div>
  <div><dt>Shop</dt><dd>424 NC Hwy 55 West, New Bern, NC 28562</dd></div>
  <div><dt>Hours</dt><dd>Monday to Friday, 7:30 to 4:00</dd></div>
  <div><dt>Service area</dt><dd>Greenville to Jacksonville and across Eastern North Carolina</dd></div>
 </dl><p class="fine">License from the NC Licensing Board for General Contractors. Firm number from their site.</p></section>
</div>
<section class="wrap yard rv" aria-labelledby="yd-h"><h2 id="yd-h">The yard</h2><div class="yard-grid">
 <figure>{IMG('trucks-banner','Three white Carolina Foundation Repairs pickup trucks outside the shop',470,275)}<figcaption>Trucks at the shop</figcaption></figure>
 <figure>{IMG('pier-stock','Stock of helical piers and extensions',400,300)}<figcaption>Helical piers and extensions</figcaption></figure>
 <figure>{IMG('pier-brackets','Helical piers and lifting brackets',400,300)}<figcaption>Piers and lifting brackets</figcaption></figure>
 <figure>{IMG('mini-excavator','Mini excavator parked in the shop next to a company trailer',400,300)}<figcaption>Mini excavator</figcaption></figure>
 <figure>{IMG('excavator-loader','Excavator and Bobcat loader on a trailer in the yard',400,300)}<figcaption>Excavator and Bobcat loader</figcaption></figure>
</div><p class="fine">Photos from the About Us page of their current site, 2012. <span class="ph">Placeholder</span> current crew photo.</p></section>
''', ld=[ORG, bc(('Home',''),('About','about.html'))])

# ---------- CONTACT ----------
page('contact.html','Request an Inspection | Carolina Foundation Repairs, NC',
 'Request a foundation or crawl space inspection from Carolina Foundation Repairs in New Bern NC. Call (252) 637-6667, Monday to Friday, 7:30am to 4:00pm.', f'''
<section class="page-head"><div class="wrap">{K('Contact')}<h1>Request an inspection.</h1><p class="lede">Tell us what you are seeing. Photos of cracks, gaps and sloping floors help Sean plan the visit.</p></div>{LASER('','laser--head')}</section>
<div class="wrap q-grid">
<form id="qform" class="rv" novalidate>
 <fieldset><legend>What are you seeing?</legend><div class="chips-in">{''.join(f'<label><input type="checkbox" name="sym" value="{v}"> {v}</label>' for v in ['Cracks in brick or block','Sloping or soft floors','Doors or windows sticking','Leaning chimney','Wet crawl space','Bowed wall','Need an engineering report'])}</div></fieldset>
 <div class="two"><div class="field"><label for="q-name">Name</label><input id="q-name" name="name" autocomplete="name" required></div><div class="field"><label for="q-tel">Phone</label><input id="q-tel" name="tel" type="tel" autocomplete="tel" required></div></div>
 <div class="two"><div class="field"><label for="q-email">Email</label><input id="q-email" name="email" type="email" autocomplete="email"></div><div class="field"><label for="q-loc">Job location (city)</label><input id="q-loc" name="loc" autocomplete="address-level2"></div></div>
 <div class="field"><label for="q-msg">Anything else</label><textarea id="q-msg" name="msg" rows="4"></textarea></div>
 <div class="field"><label for="q-ph">Photos (optional)</label><input id="q-ph" name="photos" type="file" accept="image/*" multiple></div>
 <button class="btn btn--red" type="submit">Request inspection</button><p id="qmsg" class="note" role="status" aria-live="polite">Demo form. Nothing is sent.</p>
</form>
<aside class="rv"><div class="card"><p class="kicker kicker--lt"><span class="dot" aria-hidden="true"></span>Call</p><a class="phone" href="tel:{TEL}">{TEL_H}</a><p>Monday to Friday<br>7:30 to 4:00</p><address>424 NC Hwy 55 West<br>New Bern, NC 28562</address></div></aside>
</div>
''', ld=[ORG, bc(('Home',''),('Contact','contact.html'))])

page('404.html','Page Not Found | Carolina Foundation Repairs, New Bern NC',
 'That page is not here. Head back to the Carolina Foundation Repairs home page, or call (252) 637-6667 for foundation and crawl space repair in Eastern NC.',
 f'<section class="wrap nf">{K("404")}<h1>Out of level.</h1><p class="lede">That page does not exist.</p><p><a class="btn btn--red" href="index.html">Back to the home page</a></p></section>')
print('built')
