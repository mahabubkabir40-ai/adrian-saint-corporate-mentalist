# MASTER PROJECT RULES & KNOWLEDGE BASE: ADRIAN SAINT CORPORATE MENTALIST

This document provides permanent, comprehensive context for Antigravity AI agents working on `adriansaintmentalist.com`. It ensures 100% continuity, domain knowledge, and execution accuracy across all accounts, sessions, and future updates.

---

## 1. PROJECT OVERVIEW & CLIENT IDENTITY

* **Client**: Adrian Saint — Master Corporate Mentalist & Mind Reader
* **Live Production URL**: `https://adriansaintmentalist.com`
* **Repository**: `https://github.com/mahabubkabir40-ai/adrian-saint-corporate-mentalist.git` (Branch: `main`)
* **Hosting Platform**: Vercel (`cleanUrls: true`, `trailingSlash: false`)
* **Primary Contact Email**: `adrian@saintmentalist.com`
* **Form CC Notification Emails**: `gowrish@rightkey.net,sganeshomg@gmail.com,mahabubkabir36@gmail.com`
* **Phone Numbers**:
  * **San Diego / Chula Vista / Coronado (Local Line)**: `(619) 225-7576` (`tel:16192257576` / `+16192257576`)
  * **Nationwide & Corporate Toll-Free**: `(833) 570-5966` (`tel:18335705966` / `+18335705966`)

---

## 2. TECHNICAL ARCHITECTURE & CODING STANDARDS

* **Tech Stack**: Vanilla HTML5, modern modular CSS (`css/main.css`, `css/components.css`), ES Modules (`js/app.js`). Zero heavy JS frameworks.
* **Cache-Busting Version**: Check the latest cache-buster version (e.g., `?v=20261107_v62`) on stylesheets and scripts across all pages.
* **Form Routing & Resiliency**:
  * Dual-layer form handling: Client-side fetch to `/api/contact` (Resend backend) with fallback to FormSubmit (`https://formsubmit.co/adrian@saintmentalist.com`).
  * Hidden FormSubmit fields must include `_subject`, `_template="table"`, `_captcha="false"`, `_autoresponse`, `_next`, and `_cc`.
  * Thank-you redirect targets:
    * General Corporate Pages: `/corporate-mentalist-thank-you`
    * Holiday Event Pages: `/corporate-holiday-party-entertainment-thank-you`
* **Google Ads Conversion Tracking**:
  * Global Site Tag: `AW-18508397402`
  * Form Fill Conversion: `AW-18508397402/DyxRCOyrwJsdENr2vvlE` (placed on `/corporate-holiday-party-entertainment-thank-you`)
  * Phone Click-to-Call Conversion: `AW-18508397402/ZMQaCOqswJsdENr2vvlE` (triggers on clicks to `a[href^="tel:"]`)
* **Brand Logo Ticker**:
  * 44 verified corporate client logos doubled into an 88-card symmetric infinite loop (`.ticker-move`).
  * Must always include the official **loanDepot** logo (`loandepot.png` / `loandepot.svg`), Google, Sony, Chevron, etc.
* **Video Testimonials Section**:
  * 15 authentic client video testimonial cards in a responsive carousel grid (`.video-testimonials-section`).
  * Connected to `#video-testimonial-modal` lightbox player.
  * Accompanied by the 25-card written reviews slider (`.reviews-carousel-track`).
* **Environment Rule (Windows PowerShell)**:
  * Never run inline Python one-liners containing double quotes or bracket indexing via PowerShell. Always write a `.py` script and run `python <script>.py`.

---

## 3. SEO & SCHEMA.ORG REQUIREMENTS FOR LOCATION PAGES

Every city hub (`corporate-magician-[city].html`) must include:
1. **Canonical Tag**: `<link rel="canonical" href="https://adriansaintmentalist.com/corporate-magician-[city]">`
2. **Open Graph & Twitter Tags**: Complete titles, descriptions, and sharing image.
3. **Structured Data (JSON-LD)** inside `<script id="geo-jsonld-script" type="application/ld+json">`:
   * `@graph` containing `EntertainmentBusiness` / `ProfessionalService`
   * Correct `name`, `url`, `telephone`, `email`, `priceRange`, and `image`
   * `address` with `addressLocality`, `addressRegion`, `addressCountry`
   * `geo` with accurate latitude and longitude
   * `areaServed` with local neighborhoods and counties
   * `Person` entity for Adrian Saint
   * `FAQPage` entity with 5 localized questions + 5 standard questions
4. **Local Venues Section**: 3 custom cards (Convention Centers, Luxury Hotels/Resorts, Distinctive Venues) + Logistics Callout Box.
5. **Vercel Redirects (`vercel.json`)**:
   * `/{city}` -> `/corporate-magician-{slug}`
   * `/corporate-mentalist-{city}` -> `/corporate-magician-{slug}`
   * `/corporate-macigian-{city}` -> `/corporate-magician-{slug}`
6. **Sitemap (`sitemap.xml`)**: Add new location URLs with priority `0.85` and `weekly` changefreq.

---

## 4. CURRENT STATUS OF ALL 85 LIVE LOCATION PAGES

### A. Original 60 Location Pages
* **California (19)**: Anaheim, Beverly Hills, Garden Grove, Huntington Beach, Irvine, Los Angeles, Napa, Newport Beach, Orange County, Palm Desert, Palm Springs, San Diego, San Francisco, San Jose, Santa Ana, Santa Barbara, Santa Monica, Temecula.
* **Texas (6)**: Arlington (TX - `corporate-magician-arlington.html`), Austin, Dallas, Fort Worth, Grapevine, Houston, San Antonio.
* **Florida (5)**: Fort Lauderdale, Kissimmee, Miami, Orlando, Tampa.
* **Nevada (2)**: Las Vegas, Reno.
* **Arizona (2)**: Phoenix, Scottsdale.
* **Colorado (2)**: Aurora, Denver.
* **Other Major Metros (24)**: Atlanta, Atlantic City, Baltimore, Boise, Boston, Charlotte, Chicago, Cleveland, Columbus, Indianapolis, Kansas City, Louisville, Minneapolis, Nashville, National Harbor (MD), New Orleans, New York City, Philadelphia, Portland, Salt Lake City, Seattle, St. Louis, Virginia Beach, Washington DC.

### B. Group A: 10 Cvent Top 50 Markets (Published in November & Live)
1. **Chula Vista, CA**: `corporate-magician-chula-vista.html` (Gaylord Pacific Resort) — Phone: `(619) 225-7576`
2. **Irving, TX**: `corporate-magician-irving.html` (Las Colinas / Irving Convention Center) — Phone: `(833) 570-5966`
3. **Frisco, TX**: `corporate-magician-frisco.html` (Omni PGA Resort / The Star) — Phone: `(833) 570-5966`
4. **Coronado, CA**: `corporate-magician-coronado.html` (Hotel del Coronado) — Phone: `(619) 225-7576`
5. **Rosemont, IL**: `corporate-magician-rosemont.html` (Donald E. Stephens Convention Center) — Phone: `(833) 570-5966`
6. **Arlington, VA**: `corporate-magician-arlington-va.html` (Crystal City / Amazon HQ2 / National Landing) — Phone: `(833) 570-5966` *(Note slug is `arlington-va` to avoid conflict with Arlington, TX)*
7. **Colorado Springs, CO**: `corporate-magician-colorado-springs.html` (The Broadmoor / Cheyenne Mountain) — Phone: `(833) 570-5966`
8. **Aventura, FL**: `corporate-magician-aventura.html` (JW Marriott Turnberry Resort) — Phone: `(833) 570-5966`
9. **Savannah, GA**: `corporate-magician-savannah.html` (Savannah Convention Center) — Phone: `(833) 570-5966`
10. **Toronto, ON**: `corporate-magician-toronto.html` (Metro Toronto Convention Centre / Financial District) — Phone: `(833) 570-5966`

*Generator Script Reference*: `build_group_a_pages.py`

### C. Group B: 15 Major US Convention & Economic Hubs (Published in November & Live)
11. **Pittsburgh, PA**: `corporate-magician-pittsburgh.html` (David L. Lawrence Convention Center) — Phone: `(833) 570-5966`
12. **Cincinnati, OH**: `corporate-magician-cincinnati.html` (Duke Energy Convention Center) — Phone: `(833) 570-5966`
13. **Milwaukee, WI**: `corporate-magician-milwaukee.html` (Baird Center $456M Expansion) — Phone: `(833) 570-5966`
14. **Sacramento, CA**: `corporate-magician-sacramento.html` (SAFE Credit Union Convention Center) — Phone: `(833) 570-5966`
15. **Raleigh, NC**: `corporate-magician-raleigh.html` (Raleigh Convention Center / RTP) — Phone: `(833) 570-5966`
16. **Richmond, VA**: `corporate-magician-richmond.html` (Greater Richmond Convention Center) — Phone: `(833) 570-5966`
17. **Memphis, TN**: `corporate-magician-memphis.html` (Renasant Convention Center) — Phone: `(833) 570-5966`
18. **Detroit, MI**: `corporate-magician-detroit.html` (Huntington Place Convention Center) — Phone: `(833) 570-5966`
19. **Tucson, AZ**: `corporate-magician-tucson.html` (Tucson Convention Center / JW Starr Pass) — Phone: `(833) 570-5966`
20. **Oklahoma City, OK**: `corporate-magician-oklahoma-city.html` (Oklahoma City Convention Center / Omni OKC) — Phone: `(833) 570-5966`
21. **Omaha, NE**: `corporate-magician-omaha.html` (CHI Health Center Omaha / Berkshire Summit) — Phone: `(833) 570-5966`
22. **Tulsa, OK**: `corporate-magician-tulsa.html` (Cox Business Convention Center) — Phone: `(833) 570-5966`
23. **Birmingham, AL**: `corporate-magician-birmingham.html` (Birmingham-Jefferson Convention Complex BJCC) — Phone: `(833) 570-5966`
24. **Providence, RI**: `corporate-magician-providence.html` (Rhode Island Convention Center) — Phone: `(833) 570-5966`
25. **Des Moines, IA**: `corporate-magician-des-moines.html` (Iowa Events Center) — Phone: `(833) 570-5966`

*Generator Script Reference*: `build_group_b_pages.py`

---

## 5. NEXT EXPANSION ROADMAP: 25 REMAINING NOVEMBER LOCATIONS

The user's expansion roadmap targets 50 total new locations for November. Group A (10) and Group B (15) are finished (25 published total). The remaining 25 locations are organized into Groups C and D:

### Group C: 15 Luxury Resort & Executive Retreat Enclaves (NEXT TO BUILD)
When instructed to build the next batch (Group C 15 resort destinations), build these corporate magician hubs (`/corporate-magician-[city]`):

| # | Destination | State | Key Anchor Resort / Retreat | Target Slug |
|---|---|---|---|---|
| 26 | **Palm Beach** | FL | The Breakers Palm Beach | `corporate-magician-palm-beach.html` |
| 27 | **Naples** | FL | The Ritz-Carlton Naples | `corporate-magician-naples.html` |
| 28 | **Boca Raton** | FL | The Boca Raton | `corporate-magician-boca-raton.html` |
| 29 | **Key West** | FL | Casa Marina Key West | `corporate-magician-key-west.html` |
| 30 | **Sarasota** | FL | The Ritz-Carlton Sarasota | `corporate-magician-sarasota.html` |
| 31 | **Marco Island** | FL | JW Marriott Marco Island | `corporate-magician-marco-island.html` |
| 32 | **Charleston** | SC | The Charleston Place | `corporate-magician-charleston.html` |
| 33 | **Hilton Head Island** | SC | The Westin Hilton Head Island Resort | `corporate-magician-hilton-head.html` |
| 34 | **Sedona** | AZ | Enchantment Resort | `corporate-magician-sedona.html` |
| 35 | **Lake Tahoe** | NV/CA | Hyatt Regency Lake Tahoe Resort | `corporate-magician-lake-tahoe.html` |
| 36 | **Park City** | UT | Montage Deer Valley / Stein Eriksen Lodge | `corporate-magician-park-city.html` |
| 37 | **Vail** | CO | Four Seasons Resort Vail | `corporate-magician-vail.html` |
| 38 | **Aspen** | CO | The St. Regis Aspen Resort | `corporate-magician-aspen.html` |
| 39 | **Asheville** | NC | The Omni Grove Park Inn | `corporate-magician-asheville.html` |
| 40 | **Williamsburg** | VA | Kingsmill Resort | `corporate-magician-williamsburg.html` |

### Group D: 10 High-Net-Worth Corporate HQs & Tech Satellites
41. **Pasadena, CA** (`corporate-magician-pasadena.html`) — Pasadena Convention Center / Langham Huntington
42. **Long Beach, CA** (`corporate-magician-long-beach.html`) — Long Beach Convention Center
43. **Plano, TX** (`corporate-magician-plano.html`) — Legacy West (Toyota & Frito-Lay HQs)
44. **The Woodlands, TX** (`corporate-magician-the-woodlands.html`) — The Woodlands Waterway Marriott
45. **Bellevue, WA** (`corporate-magician-bellevue.html`) — Meydenbauer Center (Amazon & Microsoft Eastside)
46. **Chandler, AZ** (`corporate-magician-chandler.html`) — Gila River Resorts / Intel Silicon Desert
47. **Overland Park, KS** (`corporate-magician-overland-park.html`) — Overland Park Convention Center
48. **Grand Rapids, MI** (`corporate-magician-grand-rapids.html`) — DeVos Place Convention Center
49. **Knoxville, TN** (`corporate-magician-knoxville.html`) — Knoxville Convention Center
50. **Vancouver, BC** (`corporate-magician-vancouver.html`) — Vancouver Convention Centre

### Group D: 10 High-Net-Worth Corporate HQs & Tech Satellites
41. **Pasadena, CA** (`corporate-magician-pasadena.html`) — Pasadena Convention Center / Langham Huntington
42. **Long Beach, CA** (`corporate-magician-long-beach.html`) — Long Beach Convention Center
43. **Plano, TX** (`corporate-magician-plano.html`) — Legacy West (Toyota & Frito-Lay HQs)
44. **The Woodlands, TX** (`corporate-magician-the-woodlands.html`) — The Woodlands Waterway Marriott
45. **Bellevue, WA** (`corporate-magician-bellevue.html`) — Meydenbauer Center (Amazon & Microsoft Eastside)
46. **Chandler, AZ** (`corporate-magician-chandler.html`) — Gila River Resorts / Intel Silicon Desert
47. **Overland Park, KS** (`corporate-magician-overland-park.html`) — Overland Park Convention Center
48. **Grand Rapids, MI** (`corporate-magician-grand-rapids.html`) — DeVos Place Convention Center
49. **Knoxville, TN** (`corporate-magician-knoxville.html`) — Knoxville Convention Center
50. **Vancouver, BC** (`corporate-magician-vancouver.html`) — Vancouver Convention Centre

---

## 6. HOLIDAY PAGES SPECIFICATIONS & RULES

* **National Holiday Landing Page**: `corporate-holiday-party-entertainment.html`
  * Purpose: Highly streamlined Google Ads landing page optimized for corporate holiday leads.
  * Hero Badge: `🎄 #1 CORPORATE HOLIDAY PARTY ENTERTAINMENT` (strictly NO "Q4 2026 & Q1 2027" text).
  * Direct Copy: Uses concise headline and text from `ocmentalist.com/holidayevents.php`.
  * Performance Showcase Images:
    * Strolling Close-Up: `images/strolling_mind_reading.jpg` (official high-res main site photo).
    * Main Stage Keynote: `images/holiday-events9.jpg` (Asahi Intecc 20th anniversary keynote).
  * Social Proof Kept 100%: 88-card client logo ticker + 15-video testimonial carousel + 25 written reviews.
  * CTA Button Routing: All call-to-action buttons ("Contact" in About card, "Check Date & Request Fee Options" in bottom card, and mobile drawer button) link directly to `#hero-fast-track-form`.
  * Form Redirect: Lands on `/corporate-holiday-party-entertainment-thank-you`.
* **Existing 10 Holiday Location Pages**:
  * Anaheim, Garden Grove, Huntington Beach, Irvine, Los Angeles, Phoenix, San Diego, San Francisco, Santa Ana, Scottsdale.
* **CRITICAL RULE**: Do **NOT** create new holiday location pages unless the user explicitly asks. The default task is to build general corporate entertainment hubs (`/corporate-magician-[city]`).

---

## 7. PROTOCOL FOR ANY FUTURE AGENT IN THIS WORKSPACE

Whenever the user gives a prompt:
1. Check this `GEMINI.md` file to immediately know the full history, active pages, and planned roadmap.
2. If the user asks to build the next batch of location pages (e.g. Group B 15 cities):
   - Reference `build_group_a_pages.py` as the generation template.
   - Generate the corresponding `corporate-magician-[slug].html` files with localized coordinates, venues, and FAQs.
   - Update `sitemap.xml` and `vercel.json`.
   - Test locally with Python verification scripts.
   - Commit and push to `origin/main`.
3. If the user asks questions or provides screenshots, review their explicit instructions carefully before modifying files.
