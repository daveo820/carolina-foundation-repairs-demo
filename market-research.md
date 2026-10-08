# Market research: Carolina Foundation Repairs

Prepared by LuminArch, 8 Oct 2026. Every number here was measured today unless noted.

## 1. Lead check (what Job finder said versus what we found)

| Lead claim | Verdict | What we found |
|---|---|---|
| 2016 WordPress site with no viewport tag | **Partly wrong** | The desktop theme has no viewport tag. But real phones never see it: the server spots iPhone and Android browsers and sends a separate WPtouch mobile theme that does have a viewport tag. Checked with curl twice on an iPhone user agent, once on Android, and in Playwright on iPhone 13 and Pixel 7. The site content dates from Jan 2012 (upload folders and post dates). WordPress core is 4.7.29. |
| "Phones get the shrunken desktop layout" | **Wrong for phones, true for tablets** | iPad Mini gets the desktop layout at 980px wide with no viewport tag. |
| In business since 2000 | **Conflicting** | Their About page says since 1995. A 2012 post says "the past 15 years" (about 1997). BBB says Dec 2000. |
| 4.5 from 34 reviews | Holds | Google listing via Exa: 4.5 from 34. Newest review Feb 2026. |
| Active business | Holds | NC GC license L.54562 Active, first issued 13 Jan 2004, expires 31 Dec 2026, qualifier Sean Corcoran. Reviews from Oct 2025 and Feb 2026. |
| BBB A+, 3 locations | Not rechecked | Not used on the demo. |

## 2. Audit of the current site (rendered, not guessed)

- **Phones skip the homepage.** Any phone that visits carolinafoundationrepairs.com gets a 302 redirect to /about-us/ on the WPtouch theme. The first screen is a "Carolina Foundation Repair" bar, a mustard "About Us" banner and a 2012 photo of the shop. There is no phone button on that screen.
- **Zoom is blocked on phones.** The mobile theme sets `maximum-scale=3.0, user-scalable=no`. That fails accessibility guidance for low vision users.
- **No tap to call anywhere.** Zero `tel:` links in the desktop HTML or the mobile About page. The phone number on desktop is text inside images and the footer.
- **Desktop homepage h1 is "Testimonials".** The page's main heading tells Google the page is about testimonials, not foundation repair. The meta description is "Carolina Foundation Repairs answers Why Should I Fix My Foundation".
- **No schema.** Zero JSON-LD blocks, so no LocalBusiness data for Google.
- **Old software.** WordPress 4.7.29 (the 4.7 branch is from 2016) and PHP 5.6.40 in the response headers. PHP 5.6 stopped getting security fixes in Dec 2018.
- **Stale and contradictory copy.** "Since 1995" next to "the past 15 years". Commercial Foundation Repair page reads "Page under construction". The homepage banner says "Largest Foundation Company in Eastern North Carolina", which they cannot easily prove.
- **Hours conflict.** Site says Mon to Fri 7:30 to 4:00. Google says 7:30 to 4:30.
- **Old photos.** Every photo was uploaded in 2011 or 2012. The good news: they are real job photos at 2048 to 2576px, including a clean leaning chimney before and after. The demo uses them.
- **Lighthouse (mobile, lands on /about-us/ because of the redirect):** Performance 77, Accessibility 74, Best Practices 96, SEO 100. LCP 5.8s, 909 KB. Fails color contrast, heading order and the viewport zoom check.

Renders saved in research/: current-site-iphone13-redirects-to-about.jpg, current-site-ipad-mini-desktop-layout.jpg, current-site-desktop-1440.jpg.

## 3. Top sites in the trade

Lighthouse 12, mobile, measured today from the box.

| Site | Perf | A11y | BP | SEO | LCP | Weight |
|---|---|---|---|---|---|---|
| groundworks.com (national, owns JES) | 87 | 82 | 71 | 92 | 3.6s | 0.8 MB |
| ramjack.com (national pier maker) | 79 | 96 | 79 | 92 | 3.2s | 7.0 MB |
| **carolinafoundationrepairs.com (current)** | 77 | 74 | 96 | 100 | 5.8s | 0.9 MB |
| jeswork.com (Virginia and NC) | 73 | 83 | 79 | 92 | 3.8s | 1.5 MB |
| absolutefoundationrepairservices.com | 55 | 86 | 75 | 77 | 9.1s | 1.2 MB |
| southeastfoundationrepair.com | 50 | 86 | 59 | 100 | 7.9s | 2.4 MB |
| crawlspaceninja.com (franchise) | 28 | 93 | 54 | 100 | 26.0s | 6.5 MB |
| **This concept (local)** | 99 | 100 | 100 | 66* | 2.0s | 0.29 MB |

\* SEO 66 only because the demo is deliberately noindex. Removing the noindex tag puts it at 100.

coastalcrawlspacenc.com refused the connection twice. groundworks.com and jeswork.com show a bot check to screenshot tools, so their screenshots were dropped.

**What the strong ones do:**
- A phone number and an "inspection" button in the first screen on mobile.
- They name the method (helical piers, push piers, encapsulation) and show the hardware.
- Before and after photos and review counts sit high on the page ("1,000+ 5 star reviews" on Crawl Space Ninja's nav).
- National brands lean on warranties and financing. Local firms win on the owner.

## 4. The opening

CFR has something the franchises can't copy: **the owner is a licensed PE who inspects every job himself, and his engineering firm also writes reports for buyers, insurers and lawyers.** Reviews back this up (a buyer used his report in negotiations; another says he talked them out of a full encapsulation another company demanded). The current site buries that on a sub page. The demo leads with it: "An engineer inspects it. His crew levels it."

## 5. Pitch points with numbers

1. Every phone visit lands on About Us, not the homepage, and there is no tap to call link on the whole site (0 `tel:` links).
2. Zoom is disabled on phones (`user-scalable=no`).
3. The homepage h1 is "Testimonials" and the site has 0 schema blocks.
4. WordPress 4.7 and PHP 5.6, which has had no security updates since Dec 2018.
5. Three different founding dates across their site and BBB (1995, about 1997, 2000).
6. Concept: Lighthouse 99/100/100 against 77/74/96, LCP 2.0s against 5.8s, 0.29 MB against 0.91 MB.

## 6. Risks and honest caveats

- Their current site is not broken. It loads in 1.8s FCP and scores SEO 100 on mobile. This pitch is about first impressions, trust and calls, not a dead site.
- All photos are 13 to 14 years old. A real build needs a photo day.
- Pick one founding year before anything goes live.
- One 1 star review (Dec 2025, crew left a tenant's gate open). Low count, but a reply from Sean would help.
- The "largest in Eastern NC" claim is left off the demo. If they want it, they need proof.
