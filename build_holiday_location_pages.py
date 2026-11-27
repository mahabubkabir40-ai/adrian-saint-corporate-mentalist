import json
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

# City configuration (25 total: Original 10 + Batch 2 15)
CITIES = [
    # --- Original 10 Holiday Location Pages ---
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
    },
    # --- Batch 2: 15 New High-ROI Holiday Location Pages ---
    {
        'slug': 'orange-county',
        'name': 'Orange County',
        'state': 'CA',
        'state_full': 'California',
        'metro': 'Orange County, Newport Beach & Laguna Coast',
        'phone': '(833) 570-5966',
        'phone_clean': '18335705966',
        'phone_e164': '+18335705966',
    },
    {
        'slug': 'newport-beach',
        'name': 'Newport Beach',
        'state': 'CA',
        'state_full': 'California',
        'metro': 'Newport Coast, Fashion Island & Orange County',
        'phone': '(833) 570-5966',
        'phone_clean': '18335705966',
        'phone_e164': '+18335705966',
    },
    {
        'slug': 'beverly-hills',
        'name': 'Beverly Hills',
        'state': 'CA',
        'state_full': 'California',
        'metro': 'Beverly Hills, Bel Air & West Los Angeles',
        'phone': '(833) 570-5966',
        'phone_clean': '18335705966',
        'phone_e164': '+18335705966',
    },
    {
        'slug': 'santa-monica',
        'name': 'Santa Monica',
        'state': 'CA',
        'state_full': 'California',
        'metro': 'Santa Monica, Silicon Beach & Westside Los Angeles',
        'phone': '(833) 570-5966',
        'phone_clean': '18335705966',
        'phone_e164': '+18335705966',
    },
    {
        'slug': 'san-jose',
        'name': 'San Jose',
        'state': 'CA',
        'state_full': 'California',
        'metro': 'San Jose, Silicon Valley & South Bay',
        'phone': '(833) 570-5966',
        'phone_clean': '18335705966',
        'phone_e164': '+18335705966',
    },
    {
        'slug': 'palm-springs',
        'name': 'Palm Springs',
        'state': 'CA',
        'state_full': 'California',
        'metro': 'Palm Springs, Palm Desert & Coachella Valley',
        'phone': '(833) 570-5966',
        'phone_clean': '18335705966',
        'phone_e164': '+18335705966',
    },
    {
        'slug': 'pasadena',
        'name': 'Pasadena',
        'state': 'CA',
        'state_full': 'California',
        'metro': 'Pasadena, Old Pasadena & San Gabriel Valley',
        'phone': '(833) 570-5966',
        'phone_clean': '18335705966',
        'phone_e164': '+18335705966',
    },
    {
        'slug': 'las-vegas',
        'name': 'Las Vegas',
        'state': 'NV',
        'state_full': 'Nevada',
        'metro': 'The Las Vegas Strip, Summerlin & Henderson',
        'phone': '(833) 570-5966',
        'phone_clean': '18335705966',
        'phone_e164': '+18335705966',
    },
    {
        'slug': 'new-york-city',
        'name': 'New York City',
        'state': 'NY',
        'state_full': 'New York',
        'metro': 'Manhattan, Midtown, Financial District & Tri-State Area',
        'phone': '(833) 570-5966',
        'phone_clean': '18335705966',
        'phone_e164': '+18335705966',
    },
    {
        'slug': 'chicago',
        'name': 'Chicago',
        'state': 'IL',
        'state_full': 'Illinois',
        'metro': 'Downtown Chicago, River North & Chicagoland',
        'phone': '(833) 570-5966',
        'phone_clean': '18335705966',
        'phone_e164': '+18335705966',
    },
    {
        'slug': 'dallas',
        'name': 'Dallas',
        'state': 'TX',
        'state_full': 'Texas',
        'metro': 'Downtown Dallas, Uptown & DFW Metroplex',
        'phone': '(833) 570-5966',
        'phone_clean': '18335705966',
        'phone_e164': '+18335705966',
    },
    {
        'slug': 'austin',
        'name': 'Austin',
        'state': 'TX',
        'state_full': 'Texas',
        'metro': 'Downtown Austin, Domain & Central Texas',
        'phone': '(833) 570-5966',
        'phone_clean': '18335705966',
        'phone_e164': '+18335705966',
    },
    {
        'slug': 'houston',
        'name': 'Houston',
        'state': 'TX',
        'state_full': 'Texas',
        'metro': 'Downtown Houston, Galleria & Energy Corridor',
        'phone': '(833) 570-5966',
        'phone_clean': '18335705966',
        'phone_e164': '+18335705966',
    },
    {
        'slug': 'miami',
        'name': 'Miami',
        'state': 'FL',
        'state_full': 'Florida',
        'metro': 'Brickell, Miami Beach & South Florida',
        'phone': '(833) 570-5966',
        'phone_clean': '18335705966',
        'phone_e164': '+18335705966',
    },
    {
        'slug': 'denver',
        'name': 'Denver',
        'state': 'CO',
        'state_full': 'Colorado',
        'metro': 'Downtown Denver, Cherry Creek & Front Range',
        'phone': '(833) 570-5966',
        'phone_clean': '18335705966',
        'phone_e164': '+18335705966',
    },
]


def sub_once(pattern, replacement, text, flags=0, label=''):
    new_text, count = re.subn(pattern, lambda _: replacement, text, count=1, flags=flags)
    if count != 1:
        raise ValueError(f"Expected 1 replacement for {label or pattern}, got {count}")
    return new_text


# Read master approved template (without modifying it)
with open('corporate-holiday-party-entertainment.html', 'r', encoding='utf-8') as f:
    master_html = f.read()

CACHE_VERSION = '20261107_v62'
master_html = re.sub(r'css/main\.css\?v=[^"]+', f'css/main.css?v={CACHE_VERSION}', master_html)
master_html = re.sub(r'css/components\.css\?v=[^"]+', f'css/components.css?v={CACHE_VERSION}', master_html)
master_html = re.sub(r'js/app\.js\?v=[^"]+', f'js/app.js?v={CACHE_VERSION}', master_html)

created_files = []

for city in CITIES:
    slug = city['slug']
    name = city['name']
    state = city['state']
    metro = city['metro']
    phone = city['phone']
    phone_clean = city['phone_clean']
    phone_e164 = city['phone_e164']

    html = master_html

    # 1. Title & Canonical URL
    page_title = f"Corporate Holiday Party Entertainment {name}, {state} | Mind-Blowing Magician &amp; Mentalist Adrian Saint"
    canonical_url = f"https://adriansaintmentalist.com/corporate-holiday-party-entertainment-{slug}"
    og_desc = (
        f"Looking for engaging, unique, and 100% HR-approved corporate holiday party entertainment in {name}, {state}? "
        f"Adrian Saint delivers interactive mind reading and psychological magic for company parties across {metro}."
    )
    keywords = (
        f"Corporate Holiday Party Entertainment {name}, {name} Company Christmas Party Magician, "
        f"Corporate Holiday Party Mentalist {name}, Holiday Event Entertainment {name}, "
        f"Corporate Party Mind Reader {name}, Holiday Banquet Entertainment {name}, "
        f"Adrian Saint {name} Holiday Party"
    )

    html = sub_once(r'<title>.*?</title>', f'<title>{page_title}</title>', html, label='title')
    html = sub_once(r'<link rel="canonical" href="[^"]*">', f'<link rel="canonical" href="{canonical_url}">', html, label='canonical')

    # 2. Open Graph & Twitter Meta Tags
    html = sub_once(r'<meta property="og:url" content="[^"]*">', f'<meta property="og:url" content="{canonical_url}">', html, label='og:url')
    html = sub_once(r'<meta property="og:title" content="[^"]*">', f'<meta property="og:title" content="{page_title}">', html, label='og:title')
    html = sub_once(r'<meta property="og:description" content="[^"]*">', f'<meta property="og:description" content="{og_desc}">', html, label='og:description')
    html = sub_once(r'<meta name="twitter:title" content="[^"]*">', f'<meta name="twitter:title" content="{page_title}">', html, label='twitter:title')
    html = sub_once(r'<meta name="twitter:description" content="[^"]*">', f'<meta name="twitter:description" content="{og_desc}">', html, label='twitter:description')
    html = sub_once(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{og_desc}">', html, label='description')
    html = sub_once(r'<meta name="keywords" content="[^"]*">', f'<meta name="keywords" content="{keywords}">', html, label='keywords')

    # 3. Localized Schema.org JSON-LD
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
                "description": (
                    f"Adrian Saint is the premier corporate holiday party mentalist and mind reader in {name}, {state}, "
                    f"delivering 100% clean, interactive psychological entertainment for company banquets, Christmas parties, "
                    f"and annual executive galas across {name} and {metro}."
                ),
                "areaServed": {
                    "@type": "AdministrativeArea" if "County" in name else "City",
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
                "telephone": phone_e164,
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
                            "text": (
                                f"Holiday season dates in November, December, and January in {name} and {metro} are the most competitive "
                                f"of the entire year. Many corporate clients book 6 to 12 months in advance, though travel routing occasionally "
                                f"opens up prime dates. We strongly recommend submitting a date hold inquiry as early as possible."
                            )
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
                        "name": "CAN ADRIAN CUSTOMIZE HIS SHOW FOR OUR COMPANY'S ANNUAL MILESTONES?",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "Yes! Adrian can seamlessly incorporate your company's core values, annual achievements, product launches, or special recognitions directly into his mind reading demonstrations."
                        }
                    },
                    {
                        "@type": "Question",
                        "name": "WHAT SOUND AND STAGE EQUIPMENT DOES ADRIAN REQUIRE?",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "Adrian has a minimalist, client-friendly rider. For stage shows, he requires only a wireless handheld or lavalier microphone and appropriate room sound. For strolling cocktail hour mind reading, zero AV or staging is required."
                        }
                    },
                    {
                        "@type": "Question",
                        "name": f"DOES ADRIAN PERFORM ACROSS {name.upper()} AND SURROUNDING REGIONS FOR CORPORATE HOLIDAY PARTIES?",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": f"Yes, Adrian Saint regularly headlines corporate holiday parties, banquets, and executive retreats across {name}, {metro}, and nationwide."
                        }
                    }
                ]
            }
        ]
    }
    json_ld_str = json.dumps(json_ld, indent=2)
    html = sub_once(
        r'<script id="geo-jsonld-script" type="application/ld\+json">.*?</script>',
        f'<script id="geo-jsonld-script" type="application/ld+json">\n{json_ld_str}\n</script>',
        html,
        flags=re.DOTALL,
        label='geo-jsonld-script'
    )

    # 4. Hero Badge (Strictly NO Q4 2026 & Q1 2027 text)
    hero_badge_html = (
        '<div class="section-badge">\n'
        f'              <span>🎄 #1 CORPORATE HOLIDAY PARTY ENTERTAINMENT IN {name.upper()}, {state}</span>\n'
        '            </div>'
    )
    html = sub_once(
        r'<div class="section-badge">\s*<span>🎄 #1 CORPORATE HOLIDAY PARTY ENTERTAINMENT</span>\s*</div>',
        hero_badge_html,
        html,
        label='hero badge'
    )

    # 5. Hero Headline
    hero_h1_html = (
        '<h1 class="hero-headline">\n'
        f'              Are You Looking For <span class="hero-headline-highlight">Engaging &amp; Unique</span> Corporate Holiday Entertainment in {name}?\n'
        '            </h1>'
    )
    html = sub_once(r'<h1 class="hero-headline">.*?</h1>', hero_h1_html, html, flags=re.DOTALL, label='hero headline')

    # 6. Hero Subheadline
    hero_sub_html = (
        '<p class="hero-subheadline">\n'
        f'              Whether you need entertainment for an intimate executive dinner of 10 or an annual company gala of 1,000+, Adrian provides the perfect 100% clean, HR-approved entertainment solution to make your {name} holiday party unforgettable and fun.\n'
        '            </p>'
    )
    html = sub_once(r'<p class="hero-subheadline">.*?</p>', hero_sub_html, html, flags=re.DOTALL, label='hero subheadline')

    # 7. Hero Form Configuration & Pre-filled Location
    html = sub_once(
        r'name="_subject" value="[^"]*"',
        f'name="_subject" value="New Corporate Holiday Party Date Hold Request - {name} - Adrian Saint"',
        html,
        label='form subject'
    )
    html = sub_once(
        r'<input type="text" name="event_city"[^>]*>',
        f'<input type="text" name="event_city" value="{name}, {state}" placeholder="{name}, {state} or Venue Name" required class="hero-field-input">',
        html,
        label='form event_city'
    )

    # 8. Logo Ticker Heading
    html = sub_once(
        r'<div class="ticker-title">Trusted by Top Global Brands &amp; Event Planners Nationwide for Annual Holiday Galas</div>',
        f'<div class="ticker-title">Trusted by Top Global Brands &amp; {name} Event Planners for Annual Holiday Galas</div>',
        html,
        label='ticker title'
    )

    # 9. Phone Replacements Across All Page Positions
    if phone_clean != "18335705966":
        html = html.replace("tel:18335705966", f"tel:{phone_clean}")
        html = html.replace("+18335705966", phone_e164)
        html = html.replace("1 (833) 570-5966", f"1 {phone}")
        html = html.replace("(833) 570-5966", phone)

    out_filename = f"corporate-holiday-party-entertainment-{slug}.html"
    with open(out_filename, 'w', encoding='utf-8') as out_f:
        out_f.write(html)

    created_files.append(out_filename)
    print(f"Generated {out_filename} ({len(html)} bytes)")

print(f"\nSuccessfully generated all {len(created_files)} streamlined holiday location pages!")
