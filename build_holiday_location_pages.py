import os
import re
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

# City configuration
CITIES = [
    {
        'slug': 'los-angeles',
        'name': 'Los Angeles',
        'state': 'CA',
        'state_full': 'California',
        'metro': 'Greater Los Angeles & Beverly Hills',
        'phone': '(213) 279-0854',
        'phone_clean': '12132790854',
        'phone_e164': '+12132790854',
    },
    {
        'slug': 'san-diego',
        'name': 'San Diego',
        'state': 'CA',
        'state_full': 'California',
        'metro': 'Greater San Diego & La Jolla',
        'phone': '(619) 225-7576',
        'phone_clean': '16192257576',
        'phone_e164': '+16192257576',
    },
    {
        'slug': 'san-francisco',
        'name': 'San Francisco',
        'state': 'CA',
        'state_full': 'California',
        'metro': 'San Francisco Bay Area & Silicon Valley',
        'phone': '(415) 629-3010',
        'phone_clean': '14156293010',
        'phone_e164': '+14156293010',
    },
    {
        'slug': 'phoenix',
        'name': 'Phoenix',
        'state': 'AZ',
        'state_full': 'Arizona',
        'metro': 'Greater Phoenix & Valley of the Sun',
        'phone': '(602) 610-5012',
        'phone_clean': '16026105012',
        'phone_e164': '+16026105012',
    },
    {
        'slug': 'scottsdale',
        'name': 'Scottsdale',
        'state': 'AZ',
        'state_full': 'Arizona',
        'metro': 'Scottsdale Luxury Resort Corridor & Paradise Valley',
        'phone': '(480) 243-9474',
        'phone_clean': '14802439474',
        'phone_e164': '+14802439474',
    },
    {
        'slug': 'anaheim',
        'name': 'Anaheim',
        'state': 'CA',
        'state_full': 'California',
        'metro': 'Orange County & Anaheim Resort District',
        'phone': '(833) 570-5966',
        'phone_clean': '18335705966',
        'phone_e164': '+18335705966',
    },
    {
        'slug': 'irvine',
        'name': 'Irvine',
        'state': 'CA',
        'state_full': 'California',
        'metro': 'Orange County & Irvine Spectrum Tech Corridor',
        'phone': '(833) 570-5966',
        'phone_clean': '18335705966',
        'phone_e164': '+18335705966',
    },
    {
        'slug': 'santa-ana',
        'name': 'Santa Ana',
        'state': 'CA',
        'state_full': 'California',
        'metro': 'Orange County Civic & Cultural Center',
        'phone': '(833) 570-5966',
        'phone_clean': '18335705966',
        'phone_e164': '+18335705966',
    },
    {
        'slug': 'garden-grove',
        'name': 'Garden Grove',
        'state': 'CA',
        'state_full': 'California',
        'metro': 'Orange County Harbor Boulevard Resort Corridor',
        'phone': '(833) 570-5966',
        'phone_clean': '18335705966',
        'phone_e164': '+18335705966',
    },
    {
        'slug': 'huntington-beach',
        'name': 'Huntington Beach',
        'state': 'CA',
        'state_full': 'California',
        'metro': 'Orange County Coastal Resort Corridor',
        'phone': '(833) 570-5966',
        'phone_clean': '18335705966',
        'phone_e164': '+18335705966',
    }
]

# Read master template
with open('corporate-holiday-party-entertainment.html', 'r', encoding='utf-8') as f:
    master_html = f.read()

CACHE_VERSION = '20261107_v62'
master_html = re.sub(r'css/main\.css\?v=[^\"]+', f'css/main.css?v={CACHE_VERSION}', master_html)
master_html = re.sub(r'css/components\.css\?v=[^\"]+', f'css/components.css?v={CACHE_VERSION}', master_html)
master_html = re.sub(r'js/app\.js\?v=[^\"]+', f'js/app.js?v={CACHE_VERSION}', master_html)

def get_adapted_venue_section(city):
    src_file = f"corporate-magician-{city['slug']}.html"
    if not os.path.exists(src_file):
        raise FileNotFoundError(f"Missing source file: {src_file}")
    
    with open(src_file, 'r', encoding='utf-8') as f:
        src_html = f.read()
    
    venue_m = re.search(r'(<section[^>]*id=["\'][^"\']*venues?["\'].*?</section>)', src_html, re.DOTALL)
    if not venue_m:
        raise ValueError(f"Could not extract venue section from {src_file}")
    
    v_sec = venue_m.group(1)
    
    # Adapt badge
    v_sec = re.sub(r'<div class="section-badge">.*?</div>', 
                   f'<div class="section-badge">📍 {city["name"].upper()} HOLIDAY VENUE COVERAGE</div>', 
                   v_sec, count=1)
    
    # Adapt H2
    v_sec = re.sub(r'<h2 class="text-gradient-gold">.*?</h2>', 
                   f'<h2 class="text-gradient-gold">Serving Premier Holiday Party Venues Across {city["name"]}</h2>', 
                   v_sec, count=1)
    
    # Adapt subtitle paragraph
    orig_sub_m = re.search(r'<div class="section-header">.*?<p>(.*?)</p>', v_sec, re.DOTALL)
    if orig_sub_m:
        new_sub = f"Whether hosting an executive Christmas gala, annual client celebration, or end-of-year banquet, Adrian Saint regularly headlines {city['name']}'s premier hotels, luxury ballrooms, and private clubs."
        v_sec = v_sec.replace(orig_sub_m.group(1), new_sub, 1)
    
    # Ensure phone number in venue callout matches city
    v_sec = re.sub(r'href="tel:1\d{10}"', f'href="tel:{city["phone_clean"]}"', v_sec)
    
    return v_sec

# Destination Navigation Grid for internal linking
def build_destinations_section(current_slug=None):
    cards_html = []
    for c in CITIES:
        is_active = (c['slug'] == current_slug)
        active_style = 'border: 2px solid var(--accent-gold); box-shadow: 0 0 25px rgba(239,68,68,0.25);' if is_active else ''
        badge_html = '<span style="display: inline-block; font-size: 0.7rem; font-weight: 800; background: #EF4444; color: #FFFFFF; padding: 2px 8px; border-radius: 9999px; margin-bottom: 0.5rem;">CURRENT PAGE</span>' if is_active else ''
        
        card = f'''
          <a href="/corporate-holiday-party-entertainment-{c['slug']}" class="service-card-interactive gold-glow-card" style="text-decoration: none; padding: 1.5rem 1.25rem; text-align: center; border-radius: 14px; {active_style}">
            {badge_html}
            <div style="font-size: 1.15rem; font-weight: 800; color: #FFFFFF; margin-bottom: 0.35rem;">
              {c['name']}
            </div>
            <div style="font-size: 0.8rem; color: var(--accent-gold); font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 0.5rem;">
              {c['state_full']}
            </div>
            <div style="font-size: 0.82rem; color: var(--text-muted); line-height: 1.4;">
              {c['metro']}
            </div>
            <div style="margin-top: 0.75rem; font-size: 0.82rem; font-weight: 700; color: #EF4444; display: flex; align-items: center; justify-content: center; gap: 4px;">
              <span>Explore {c['name']} Holiday Parties</span> &rarr;
            </div>
          </a>'''
        cards_html.append(card)
    
    dest_section = f'''
    <!-- Top Corporate Holiday Party Destinations Grid -->
    <section id="holiday-destinations" class="section-padding section-divider" style="background-color: var(--bg-card);">
      <div class="container">
        <div class="section-header">
          <div class="section-badge">🎄 SELECT CORPORATE HOLIDAY PARTY DESTINATIONS</div>
          <h2 class="text-gradient-gold">Premier Holiday Party Entertainment by City</h2>
          <p>Adrian Saint regularly headlines high-end corporate Christmas parties, annual executive banquets, and year-end celebrations across these leading metropolitan business hubs.</p>
        </div>
        <div class="grid-3" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 1.25rem;">
          {''.join(cards_html)}
        </div>
      </div>
    </section>'''
    return dest_section

# Build each city page
created_files = []

for city in CITIES:
    slug = city['slug']
    name = city['name']
    state = city['state']
    state_full = city['state_full']
    metro = city['metro']
    phone = city['phone']
    phone_clean = city['phone_clean']
    phone_e164 = city['phone_e164']
    
    html = master_html
    
    # 1. Title tag
    page_title = f"Corporate Holiday Party Entertainment {name} | Mind-Blowing Magician &amp; Mentalist Adrian Saint"
    html = re.sub(r'<title>.*?</title>', f'<title>{page_title}</title>', html, count=1)
    
    # 2. Canonical URL
    canonical_url = f"https://adriansaintmentalist.com/corporate-holiday-party-entertainment-{slug}"
    html = re.sub(r'<link rel="canonical" href=".*?">', f'<link rel="canonical" href="{canonical_url}">', html, count=1)
    
    # 3. Open Graph
    html = re.sub(r'<meta property="og:url" content=".*?">', f'<meta property="og:url" content="{canonical_url}">', html, count=1)
    html = re.sub(r'<meta property="og:title" content=".*?">', f'<meta property="og:title" content="{page_title}">', html, count=1)
    og_desc = f"Looking for engaging, unique, and 100% HR-approved corporate holiday party entertainment in {name}, {state}? Adrian Saint delivers interactive mind reading and psychological magic for company parties across {metro}."
    html = re.sub(r'<meta property="og:description" content=".*?">', f'<meta property="og:description" content="{og_desc}">', html, count=1)
    
    # 4. Twitter Cards
    html = re.sub(r'<meta name="twitter:title" content=".*?">', f'<meta name="twitter:title" content="{page_title}">', html, count=1)
    html = re.sub(r'<meta name="twitter:description" content=".*?">', f'<meta name="twitter:description" content="{og_desc}">', html, count=1)
    
    # 5. Meta Description & Keywords
    html = re.sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="{og_desc}">', html, count=1)
    keywords = f"Corporate Holiday Party Entertainment {name}, {name} Company Christmas Party Magician, Corporate Holiday Party Mentalist {name}, Holiday Event Entertainment {name}, Corporate Party Mind Reader {name}, Holiday Banquet Entertainment {name}, Adrian Saint {name} Holiday Party"
    html = re.sub(r'<meta name="keywords" content=".*?">', f'<meta name="keywords" content="{keywords}">', html, count=1)
    
    # 6. Schema.org JSON-LD Graph
    # Build localized JSON-LD
    json_ld = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": ["EntertainmentBusiness", "ProfessionalService"],
                "@id": f"{canonical_url}#service",
                "name": f"Adrian Saint - Corporate Holiday Party Entertainment {name}",
                "url": canonical_url,
                "telephone": phone_e164,
                "email": "adrian@saintmentalist.com",
                "priceRange": "$$$",
                "image": "https://adriansaintmentalist.com/images/adrian_saint_about_portrait.jpg",
                "description": f"Adrian Saint is the premier corporate holiday party mentalist and mind reader in {name}, {state}, delivering 100% clean, interactive psychological entertainment for company banquets, Christmas parties, and annual executive galas across {name} and {metro}.",
                "areaServed": {
                    "@type": "City",
                    "name": f"{name}, {state}"
                },
                "aggregateRating": {
                    "@type": "AggregateRating",
                    "ratingValue": "5.0",
                    "reviewCount": "127",
                    "bestRating": "5",
                    "worstRating": "1"
                }
            },
            {
                "@type": "Person",
                "@id": "https://adriansaintmentalist.com/#adrian",
                "name": "Adrian Saint",
                "jobTitle": "Corporate Mentalist & Mind Reader",
                "url": "https://adriansaintmentalist.com",
                "email": "adrian@saintmentalist.com",
                "telephone": "+18335705966",
                "sameAs": [
                    "https://www.linkedin.com/in/adriansaintmentalist/",
                    "https://www.instagram.com/ocmentalist/",
                    "https://www.youtube.com/@ocmentalist",
                    "https://www.facebook.com/ocmentalist/",
                    "https://x.com/sainttwins",
                    "https://www.yelp.com/biz/adrian-and-john-the-saint-twins-irvine",
                    "https://www.ocmentalist.com"
                ]
            },
            {
                "@type": "FAQPage",
                "@id": f"{canonical_url}#faq",
                "mainEntity": [
                    {
                        "@type": "Question",
                        "name": f"HOW FAR IN ADVANCE SHOULD WE BOOK ADRIAN FOR OUR CORPORATE HOLIDAY PARTY IN {name.upper()}?",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": f"Holiday season dates across November, December, and January in {name} and {metro} are the most in-demand of the entire year. Many corporate planners book 6 to 12 months ahead. We strongly recommend submitting a date hold inquiry as early as possible."
                        }
                    },
                    {
                        "@type": "Question",
                        "name": "IS ADRIAN'S SHOW 100% CLEAN AND HR-SAFE FOR COMPANY HOLIDAY PARTIES?",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "Yes, 100% clean and corporate-safe! Adrian never uses vulgarity, suggestive humor, or embarrassing antics. His goal is to celebrate your team and make you look like a hero for hiring him."
                        }
                    },
                    {
                        "@type": "Question",
                        "name": f"DOES ADRIAN PERFORM ACROSS {name.upper()} AND SURROUNDING VENUES?",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": f"Yes, Adrian Saint regularly headlines corporate holiday parties, annual company galas, and VIP executive dinners across {name}, {metro}, and surrounding regions."
                        }
                    },
                    {
                        "@type": "Question",
                        "name": "WHAT SOUND AND STAGE EQUIPMENT DOES ADRIAN REQUIRE?",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "Adrian has a minimalist, client-friendly rider. For stage shows, he requires only a wireless handheld or lavalier microphone and appropriate room sound. For strolling cocktail hour mind reading, zero AV or staging is required."
                        }
                    }
                ]
            }
        ]
    }
    
    json_ld_str = json.dumps(json_ld, indent=2)
    html = re.sub(r'<script id="geo-jsonld-script".*?</script>', 
                  f'<script id="geo-jsonld-script" type="application/ld+json">\n{json_ld_str}\n</script>', 
                  html, count=1, flags=re.DOTALL)
    
    # 7. Hero Badge
    hero_badge_html = f'<span>🎄 #1 CORPORATE HOLIDAY PARTY ENTERTAINMENT IN {name.upper()}, {state} • Q4 2026 &amp; Q1 2027 BOOKINGS</span>'
    html = re.sub(r'<div class="section-badge">\s*<span>🎄.*?</span>\s*</div>', 
                  f'<div class="section-badge">\n              {hero_badge_html}\n            </div>', 
                  html, count=1)
    
    # 8. Hero Headline
    hero_h1_html = f'<h1 class="hero-headline">\n              Mind-Blowing Corporate Holiday Party Entertainment in <span class="hero-headline-highlight">{name}</span> Audiences Will Thank You For\n            </h1>'
    html = re.sub(r'<h1 class="hero-headline">.*?</h1>', hero_h1_html, html, count=1, flags=re.DOTALL)
    
    # 9. Hero Subheadline
    hero_sub_html = f'<p class="hero-subheadline">\n              Are you looking for engaging and unique holiday entertainment in {name}? Whether your gathering is an intimate VIP dinner of 10 or a grand annual gala of 1,000+, Adrian Saint provides the perfect 100% clean, HR-approved entertainment solution to make your {name} company holiday event unforgettable and fun.\n            </p>'
    html = re.sub(r'<p class="hero-subheadline">.*?</p>', hero_sub_html, html, count=1, flags=re.DOTALL)
    
    # 10. Hero CTA Call Button
    hero_call_btn = f'<a href="tel:{phone_clean}" class="btn btn-gold" style="display: inline-flex; align-items: center; gap: 0.55rem; text-decoration: none; font-weight: 800; letter-spacing: 0.03em;">\n                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink: 0;">\n                  <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/>\n                </svg>\n                <span>Call {phone}</span>\n              </a>'
    html = re.sub(r'<a href="tel:[^"]+" class="btn btn-gold".*?</a>', hero_call_btn, html, count=1, flags=re.DOTALL)
    
    # 11. Form Configuration & Pre-filled Location
    html = re.sub(r'name="_subject" value="[^"]*"', 
                  f'name="_subject" value="New Corporate Holiday Party Date Hold Request - {name} - Adrian Saint"', 
                  html, count=1)
    
    html = re.sub(r'<input type="text" name="event_city"[^>]*>', 
                  f'<input type="text" name="event_city" value="{name}, {state}" placeholder="{name}, {state} or Venue Name" required class="hero-field-input">', 
                  html, count=1)
    
    # 12. Insert Venue Section after #why-adrian
    venue_sec_html = get_adapted_venue_section(city)
    why_adrian_end = html.find('</section>', html.find('id="why-adrian"'))
    if why_adrian_end != -1:
        insert_pos = why_adrian_end + len('</section>')
        html = html[:insert_pos] + '\n\n' + venue_sec_html + html[insert_pos:]
    else:
        print(f"Warning: Could not find why-adrian end tag in {slug}")
    
    # 13. Localized FAQ items
    # Replace FAQ 1
    html = re.sub(r'<span class="faq-question-title">HOW FAR IN ADVANCE SHOULD WE BOOK ADRIAN FOR OUR CORPORATE HOLIDAY PARTY\?</span>',
                  f'<span class="faq-question-title">HOW FAR IN ADVANCE SHOULD WE BOOK ADRIAN FOR OUR CORPORATE HOLIDAY PARTY IN {name.upper()}?</span>',
                  html, count=1)
    
    html = re.sub(r'<p>Holiday season dates across November, December, and January are the most in-demand of the entire year\..*?</p>',
                  f'<p>Holiday season dates across November, December, and January in {name} and {metro} are the most in-demand of the entire year. Many corporate planners book 6 to 12 months ahead, although travel routing occasionally opens up prime dates. We strongly suggest submitting your date hold inquiry as early as possible to secure your preferred date.</p>',
                  html, count=1, flags=re.DOTALL)
    
    # Replace FAQ 5 (Travel)
    html = re.sub(r'<span class="faq-question-title">DOES ADRIAN TRAVEL NATIONWIDE FOR CORPORATE HOLIDAY EVENTS\?</span>',
                  f'<span class="faq-question-title">DOES ADRIAN PERFORM ACROSS {name.upper()} AND {metro.upper()}?</span>',
                  html, count=1)
    
    html = re.sub(r'<p>Yes, Adrian Saint regularly flies nationwide to headline corporate holiday parties, banquets, and executive retreats across all 50 states\..*?</p>',
                  f'<p>Yes! Adrian Saint frequently headlines annual holiday galas, company banquets, and VIP executive celebrations across {name}, {metro}, and surrounding regions. With streamlined technical requirements and direct management coordination, booking is effortless for event committees.</p>',
                  html, count=1, flags=re.DOTALL)
    
    # 14. Insert Destinations Grid right above #contact
    dest_grid_html = build_destinations_section(current_slug=slug)
    contact_start = html.find('<section id="contact"')
    if contact_start != -1:
        html = html[:contact_start] + dest_grid_html + '\n\n' + html[contact_start:]
    else:
        print(f"Warning: Could not find contact start in {slug}")
        
    # Write to target file
    out_filename = f"corporate-holiday-party-entertainment-{slug}.html"
    with open(out_filename, 'w', encoding='utf-8') as out_f:
        out_f.write(html)
    
    created_files.append(out_filename)
    print(f"Generated {out_filename} ({len(html)} bytes)")

# Also update the master corporate-holiday-party-entertainment.html with the destinations grid
if '<section id="holiday-destinations"' not in master_html:
    master_dest_grid = build_destinations_section(current_slug=None)
    contact_start = master_html.find('<section id="contact"')
    if contact_start != -1:
        master_updated = master_html[:contact_start] + master_dest_grid + '\n\n' + master_html[contact_start:]
        with open('corporate-holiday-party-entertainment.html', 'w', encoding='utf-8') as f:
            f.write(master_updated)
        print("Updated corporate-holiday-party-entertainment.html with holiday destinations grid!")

print(f"\nSuccessfully generated all {len(created_files)} location pages!")
