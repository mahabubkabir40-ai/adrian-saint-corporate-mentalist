import json
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Read base template from corporate-magician-aurora.html
with open('corporate-magician-aurora.html', 'r', encoding='utf-8') as f:
    base_html = f.read()

# Update cache buster to latest version
base_html = re.sub(r'css/main\.css\?v=[^\"]+', 'css/main.css?v=20261107_v62', base_html)
base_html = re.sub(r'css/components\.css\?v=[^\"]+', 'css/components.css?v=20261107_v62', base_html)
base_html = re.sub(r'js/app\.js\?v=[^\"]+', 'js/app.js?v=20261107_v62', base_html)

GROUP_A_CITIES = [
    {
        "slug": "chula-vista",
        "city": "Chula Vista",
        "state": "CA",
        "state_full": "California",
        "country": "US",
        "phone": "(619) 225-7576",
        "phone_clean": "16192257576",
        "phone_e164": "+16192257576",
        "badge": "📍 CHULA VISTA BAYFRONT & GAYLORD PACIFIC COVERAGE",
        "h1": "Corporate Magician &amp; Mentalist in <span class=\"hero-headline-highlight\">Chula Vista</span> for Gaylord Pacific Summits, Bayfront Galas &amp; Executive Retreats",
        "subhead": "Delivering world-class psychological entertainment and interactive mind reading for corporate conferences, executive retreats, and gala dinners across Chula Vista's landmark bayfront resort destination.",
        "lat": 32.6401,
        "lon": -117.0842,
        "areas": ["Chula Vista", "Chula Vista Bayfront", "Gaylord Pacific", "San Diego County", "South Bay San Diego", "San Diego"],
        "venue_h2": "Serving San Diego South Bay's Premier Coastal Resorts &amp; Bayfront Event Centers",
        "venue_p": "Home to the monumental Gaylord Pacific Resort &amp; Convention Center and scenic San Diego Bay coastal venues, Chula Vista is one of Southern California's fastest-growing corporate meeting destinations.",
        "card1": {
            "sub": "FLAGSHIP BAYFRONT RESORTS & CONVENTION SPACES",
            "title": "National Conventions & Flagship Galas",
            "items": [
                "Gaylord Pacific Resort & Convention Center (477,000 sq ft convention center & 1,600 luxury guest rooms)",
                "Gaylord Pacific Grand Ballroom (Over 140,000 sq ft pillarless banquet and gala space)",
                "Chula Vista Bayfront Event Pavilions (Waterfront terrace dinners & corporate networking)",
                "Bayside Park Event Lawns (Private executive receptions overlooking San Diego Bay)"
            ]
        },
        "card2": {
            "sub": "CONFERENCE HOTELS & PRIVATE RESORTS",
            "title": "Executive Summits & Corporate Dinners",
            "items": [
                "Seven Mile Casino VIP Event Suites (Private executive gatherings & corporate poker galas)",
                "Ayres Hotel San Diego South - Chula Vista (Boutique corporate meetings & leadership boardrooms)",
                "South Bay Conference Center (Regional corporate seminars & professional association banquets)",
                "Residence Inn by Marriott San Diego Chula Vista (Corporate offsites & multi-day workshops)"
            ]
        },
        "card3": {
            "sub": "DISTINCTIVE SOUTH BAY EVENT VENUES",
            "title": "Private Banquets & Leadership Retreats",
            "items": [
                "Chula Vista Golf Course Clubhouse & Banquet Pavilion (Executive tournament galas)",
                "Eastlake Country Club Event Space (Scenic lakeside banquets & corporate celebrations)",
                "The Living Coast Discovery Center Private Event Terrace (Unique eco-luxury receptions)",
                "Otay Ranch Town Center Executive Event Spaces (Corporate dining & private suites)"
            ]
        },
        "callout": {
            "sub": "LOCAL SOUTHERN CALIFORNIA DRIVE-IN ADVANTAGE",
            "title": "Zero Flight Cancellation Risks • Minutes from Downtown San Diego (SAN)",
            "p": "Based locally in Southern California, Adrian Saint drives directly to Chula Vista Bayfront venues or arrives via San Diego International Airport (SAN) in just 15 minutes. Guaranteed punctuality, zero flight rider markups, and plug-and-play production."
        },
        "faqs": [
            {
                "q": "CAN ADRIAN HEADLINE GENERAL SESSIONS AT GAYLORD PACIFIC RESORT IN CHULA VISTA?",
                "a": "Yes! Adrian regularly headlines general sessions, evening awards banquets, and opening keynotes at Gaylord Pacific Resort & Convention Center for corporate audiences from 150 to over 3,000 attendees."
            },
            {
                "q": "HOW DO TRAVEL LOGISTICS WORK FOR CHULA VISTA AND SOUTH BAY SAN DIEGO VENUES?",
                "a": "Because Adrian Saint is locally based in Southern California, meeting planners avoid expensive flight rider markups and airline delays. For fly-in clients, Chula Vista is only 15 minutes south of San Diego International Airport (SAN)."
            },
            {
                "q": "IS THE PERFORMANCE 100% CLEAN AND APPROPRIATE FOR CORPORATE EXECUTIVES & HR?",
                "a": "Yes, absolutely. Adrian's corporate show is 100% clean, intelligent, and HR-approved. He never uses embarrassing gags, crude humor, or off-color material, making your planning committee look brilliant."
            },
            {
                "q": "WHAT SOUND AND TECHNICAL SETUP DOES ADRIAN REQUIRE AT CHULA VISTA VENUES?",
                "a": "Adrian's technical rider is famously straightforward: a wireless handheld or lavalier microphone and connection to room sound. Zero complex lighting or staging requirements."
            },
            {
                "q": "DOES ADRIAN PERFORM AT PRIVATE EXECUTIVE GATHERINGS & GOLF RETREATS IN CHULA VISTA?",
                "a": "Yes! In addition to large convention hall keynotes, Adrian frequently performs strolling close-up mentalism for cocktail receptions and intimate after-dinner shows for executive board retreats."
            }
        ]
    },
    {
        "slug": "irving",
        "city": "Irving",
        "state": "TX",
        "state_full": "Texas",
        "country": "US",
        "phone": "(833) 570-5966",
        "phone_clean": "18335705966",
        "phone_e164": "+18335705966",
        "badge": "📍 IRVING & LAS COLINAS CORPORATE HUB COVERAGE",
        "h1": "Corporate Magician &amp; Mentalist in <span class=\"hero-headline-highlight\">Irving</span> for Las Colinas Conventions, DFW Summits &amp; Executive Galas",
        "subhead": "Elevate your Las Colinas corporate summit, Irving Convention Center banquet, or Fortune 500 leadership conference with mind-bending psychological entertainment.",
        "lat": 32.814,
        "lon": -96.9489,
        "areas": ["Irving", "Las Colinas", "Dallas County", "DFW Metroplex", "Texas"],
        "venue_h2": "Serving Las Colinas Headquarters &amp; Premier DFW Convention Centers Across Irving",
        "venue_p": "From the architectural masterpiece Irving Convention Center at Las Colinas to world-renowned luxury golf resorts, Irving serves as the global corporate headquarters capital of North Texas.",
        "card1": {
            "sub": "CONVENTION CENTERS & ARENAS",
            "title": "Major Summits & National Expos",
            "items": [
                "Irving Convention Center at Las Colinas (275,000 sq ft state-of-the-art column-free exhibition halls)",
                "Toyota Music Factory Pavilion (Indoor VIP corporate gatherings & private amphitheater sessions)",
                "Westin Irving Convention Center Ballroom (Adjacent luxury convention accommodations)",
                "Texican Court Private Event Lawns (Boutique Southwestern corporate receptions)"
            ]
        },
        "card2": {
            "sub": "LUXURY GOLF RESORTS & CORPORATE RETREATS",
            "title": "Executive Conferences & Leadership Dinners",
            "items": [
                "The Ritz-Carlton Dallas, Las Colinas (Formerly Four Seasons Resort, master luxury ballroom)",
                "Omni Las Colinas Hotel (Waterfront Mandalay Canal terrace & executive boardrooms)",
                "Marriott Dallas Las Colinas (Lake Carolyn ballroom & corporate banqueting)",
                "Four Seasons Club / TPC Las Colinas (Championship golf tournament galas)"
            ]
        },
        "card3": {
            "sub": "DISTINCTIVE WATERFRONT & CLUB VENUES",
            "title": "VIP Banquets & Private Receptions",
            "items": [
                "Las Colinas Country Club Ballroom (Exclusive corporate dining & skyline views)",
                "Hackberry Creek Country Club (Private executive networking banquets)",
                "The Pavilion at Toyota Music Factory VIP Lounge (High-energy corporate celebrations)",
                "Mandalay Canal Waterfront Terraces (Outdoor cocktail receptions & strolling mentalism)"
            ]
        },
        "callout": {
            "sub": "DFW AIRPORT CORRIDOR LOGISTICAL ADVANTAGE",
            "title": "Immediate DFW Airport Access • Nonstop Flights Nationwide",
            "p": "Situated directly adjacent to Dallas Fort Worth International Airport (DFW) and Dallas Love Field (DAL), Irving offers frictionless fly-in logistics. Adrian Saint delivers turnkey production with guaranteed on-time corporate arrival."
        },
        "faqs": [
            {
                "q": "CAN ADRIAN HEADLINE GENERAL SESSIONS AT IRVING CONVENTION CENTER AT LAS COLINAS?",
                "a": "Yes! Adrian regularly headlines general sessions, association keynotes, and evening awards banquets at Irving Convention Center at Las Colinas for audiences from 100 to over 2,500 executives."
            },
            {
                "q": "HOW DO TRAVEL LOGISTICS WORK FOR IRVING AND DFW CORPORATE VENUES?",
                "a": "Irving is immediately adjacent to Dallas Fort Worth International Airport (DFW) and 15 minutes from Dallas Love Field (DAL). Adrian provides all-inclusive travel logistics and guaranteed early on-site check-in."
            },
            {
                "q": "IS ADRIAN'S SHOW APPROPRIATE FOR FORTUNE 500 LAS COLINAS HEADQUARTERS?",
                "a": "Yes, 100%. Adrian has performed for top Fortune 500 corporations nationwide. His performance is sophisticated, 100% clean, and HR-approved, celebrating audience intelligence with zero awkwardness."
            },
            {
                "q": "WHAT TECHNICAL SETUP DOES ADRIAN REQUIRE AT THE RITZ-CARLTON DALLAS LAS COLINAS?",
                "a": "Adrian's technical rider is minimalist and seamless: a wireless microphone and connection to house audio. His show integrates effortlessly with venue in-house audiovisual teams."
            },
            {
                "q": "DOES ADRIAN PROVIDE STROLLING MIND READING FOR LAS COLINAS COCKTAIL HOURS?",
                "a": "Yes! Adrian frequently performs strolling, close-up mentalism during cocktail hours and networking receptions, followed by his signature 30- to 60-minute interactive stage show."
            }
        ]
    },
    {
        "slug": "frisco",
        "city": "Frisco",
        "state": "TX",
        "state_full": "Texas",
        "country": "US",
        "phone": "(833) 570-5966",
        "phone_clean": "18335705966",
        "phone_e164": "+18335705966",
        "badge": "📍 FRISCO & THE STAR HEADQUARTERS COVERAGE",
        "h1": "Corporate Magician &amp; Mentalist in <span class=\"hero-headline-highlight\">Frisco</span> for Omni PGA Summits, The Star Galas &amp; Executive Retreats",
        "subhead": "High-impact mentalism and interactive mind reading for corporate conventions, leadership retreats, and luxury galas across Sports City USA and Frisco's booming business district.",
        "lat": 33.1507,
        "lon": -96.8236,
        "areas": ["Frisco", "The Star in Frisco", "PGA Frisco", "Collin County", "Denton County", "North Texas", "Dallas"],
        "venue_h2": "Serving Frisco's World-Class Mega-Resorts, Stadiums &amp; Corporate Headquarters",
        "venue_p": "Home to the groundbreaking Omni PGA Frisco Resort and Dallas Cowboys World Headquarters at The Star, Frisco represents one of North America's premier corporate event destinations.",
        "card1": {
            "sub": "MEGA RESORTS & CONVENTION BALLROOMS",
            "title": "National Conferences & Major Summits",
            "items": [
                "Omni PGA Frisco Resort & Monument Realty PGA District (127,000 sq ft conference space & Ryder Cup Ballroom)",
                "Ford Center at The Star (12,000-seat multi-use event facility for national corporate rallies)",
                "Embassy Suites by Hilton Dallas Frisco Hotel & Convention Center (90,000 sq ft Frisco Conference Center)",
                "The Star in Frisco Executive Event Venues (Dallas Cowboys VIP luxury corporate dining)"
            ]
        },
        "card2": {
            "sub": "LUXURY BOUTIQUE HOTELS & CORPORATE CLUBS",
            "title": "Executive Summits & Leadership Retreats",
            "items": [
                "Omni Frisco Hotel at The Star (Elevated luxury ballrooms & rooftop VIP pool deck receptions)",
                "Hyatt Regency Frisco - Dallas (Stonebriar Centre conference suites & banquet spaces)",
                "The Westin Stonebriar Golf Resort & Spa (Championship golf tournament dinners & executive retreats)",
                "Canopy by Hilton Dallas Frisco Station (Tech-forward meeting hubs & private gatherings)"
            ]
        },
        "card3": {
            "sub": "DISTINCTIVE SPORTS & ENTERTAINMENT VENUES",
            "title": "VIP Banquets & Private Receptions",
            "items": [
                "Cowboys Club at The Star (Exclusive private dining club & corporate networking suites)",
                "Stonebriar Country Club Grand Ballroom (Prestigious corporate banquets & golf awards)",
                "National Soccer Hall of Fame Club Level at Toyota Stadium (Modern event space & terrace views)",
                "Frisco Hall Event Center (Elegant ballroom galas & multi-company celebrations)"
            ]
        },
        "callout": {
            "sub": "NORTH TEXAS CORPORATE CORRIDOR ADVANTAGE",
            "title": "Seamless DFW & Love Field Access • Rapid North Dallas Corridor Travel",
            "p": "Positioned directly along the Dallas North Tollway, Frisco is effortlessly reached from both DFW International Airport and Dallas Love Field. Adrian Saint brings reliable fly-in production and turnkey show execution."
        },
        "faqs": [
            {
                "q": "CAN ADRIAN HEADLINE MAJOR CONVENTIONS AT OMNI PGA FRISCO RESORT?",
                "a": "Yes! Adrian regularly headlines national corporate conferences, annual meetings, and gala banquets in the Grand Ballroom and Ryder Cup Ballroom at Omni PGA Frisco Resort."
            },
            {
                "q": "HOW DO TRAVEL LOGISTICS WORK FOR FRISCO & THE STAR CORPORATE EVENTS?",
                "a": "Frisco is located 25 minutes north of DFW International Airport and Dallas Love Field. Adrian provides turnkey travel arrangements, guaranteed punctual arrival, and comprehensive direct coordination."
            },
            {
                "q": "IS ADRIAN'S SHOW 100% CLEAN AND APPROPRIATE FOR CORPORATE EXECUTIVES?",
                "a": "Yes, completely. Adrian's corporate mentalism is sophisticated, clean, and HR-safe. He engages attendees respectfully without pranks or embarrassing volunteer setups."
            },
            {
                "q": "WHAT TECHNICAL REQUIREMENTS DOES ADRIAN REQUIRE AT FORD CENTER OR OMNI FRISCO?",
                "a": "Adrian's technical rider is ultra-simple: wireless handheld or lavalier mic and sound hookup. Zero complicated rigging, lighting, or oversized staging required."
            },
            {
                "q": "DOES ADRIAN PERFORM FOR PRIVATE GOLF RETREATS & EXECUTIVE DINNERS IN FRISCO?",
                "a": "Yes! Adrian regularly provides intimate after-dinner mind reading for executive summits and strolling close-up mentalism during golf tournament cocktail hours."
            }
        ]
    },
    {
        "slug": "coronado",
        "city": "Coronado",
        "state": "CA",
        "state_full": "California",
        "country": "US",
        "phone": "(619) 225-7576",
        "phone_clean": "16192257576",
        "phone_e164": "+16192257576",
        "badge": "📍 CORONADO ISLAND & HOTEL DEL COVERAGE",
        "h1": "Corporate Magician &amp; Mentalist in <span class=\"hero-headline-highlight\">Coronado</span> for Hotel del Galas, Island Summits &amp; Executive Retreats",
        "subhead": "Exceptional psychological entertainment and interactive mind reading for corporate conferences, board retreats, and beachfront galas on Coronado Island.",
        "lat": 32.6859,
        "lon": -117.1831,
        "areas": ["Coronado", "Coronado Island", "Hotel del Coronado", "San Diego Bay", "San Diego County", "California"],
        "venue_h2": "Serving Historic Beachfront Resorts, Luxury Marinas &amp; Private Island Clubs",
        "venue_p": "Anchored by the legendary Hotel del Coronado and panoramic views of the San Diego skyline across the bay, Coronado is the crown jewel of Southern California corporate destinations.",
        "card1": {
            "sub": "HISTORIC LUXURY RESORTS & OCEANFRONT BALLROOMS",
            "title": "National Conferences & Milestone Galas",
            "items": [
                "Hotel del Coronado (Over 95,000 sq ft historic & oceanfront event space, Crown Room & Southpointe Ballroom)",
                "Coronado Island Marriott Resort & Spa (Over 40,000 sq ft skyline-view event space & bayside ballrooms)",
                "Loews Coronado Bay Resort (Waterfront private peninsula resort & Commodore Ballroom)",
                "Hotel del Ocean Lawn & Windsor Lawn (Signature beachfront executive dinners under the stars)"
            ]
        },
        "card2": {
            "sub": "PRIVATE CLUBS & BOUTIQUE RETREATS",
            "title": "Executive Summits & Board Offsites",
            "items": [
                "Coronado Cays Yacht Club (Waterfront banquets & private executive cocktail mixers)",
                "Glorietta Bay Inn (Historic boutique conference suites & intimate leadership retreats)",
                "Coronado Community Center Nautilus Room (Panoramic Glorietta Bay corporate galas)",
                "Coronado Golf Course Clubhouse & Bayside Banquet Rooms (Executive golf tournament dinners)"
            ]
        },
        "card3": {
            "sub": "UNIQUE WATERFRONT & HERITAGE VENUES",
            "title": "VIP Dinners & Cocktail Receptions",
            "items": [
                "The Feast at The Del Private Corporate Pavilions (Luxury coastal dining experiences)",
                "Il Fornaio Coronado Private Dining Room (San Diego skyline waterfront banquets)",
                "Coronado Ferry Landing Event Lawns (Open-air corporate networking overlooking downtown)",
                "San Diego Yacht Club Coronado Regatta Facilities (Elite executive receptions)"
            ]
        },
        "callout": {
            "sub": "LOCAL SOUTHERN CALIFORNIA DRIVE-IN ADVANTAGE",
            "title": "Local Southern California Drive-In • 10 Minutes from San Diego Airport (SAN)",
            "p": "Based locally in Southern California, Adrian Saint drives straight across the Coronado Bridge or lands minutes away at SAN. Guaranteed reliability, zero airline travel cancellation risk, and seamless local service."
        },
        "faqs": [
            {
                "q": "CAN ADRIAN HEADLINE CONVENTIONS IN THE CROWN ROOM OR SOUTHPOINTE BALLROOM AT THE DEL?",
                "a": "Yes! Adrian regularly headlines national corporate conferences, annual meetings, and milestone galas in the iconic Crown Room and new Southpointe Ballroom at Hotel del Coronado."
            },
            {
                "q": "HOW DO TRAVEL LOGISTICS WORK FOR CORONADO ISLAND RESORTS?",
                "a": "Because Adrian Saint is locally based in Southern California, meeting planners face zero airline delays or expensive flight riders. For national planners, Coronado is an easy 10-minute drive from San Diego Airport (SAN)."
            },
            {
                "q": "IS THE PERFORMANCE SUITABLE FOR C-LEVEL EXECUTIVES AND BOARD RETREATS?",
                "a": "Yes, absolutely. Adrian's corporate show is 100% clean, intellectually stimulating, and respectful. It is specifically designed to engage high-level executives and corporate boards."
            },
            {
                "q": "WHAT ARE ADRIAN'S AV & TECHNICAL REQUIREMENTS FOR CORONADO BALLROOMS?",
                "a": "Adrian's setup is remarkably straightforward: a wireless lavalier or handheld microphone and standard sound reinforcement. No complex lighting, oversized staging, or hazardous props."
            },
            {
                "q": "CAN ADRIAN COMBINE STROLLING MENTALISM WITH AN AFTER-DINNER STAGE SHOW?",
                "a": "Yes! Planners frequently book Adrian for cocktail hour strolling mind reading on the ocean lawn, followed by his 45-minute mind-reading stage show after dinner."
            }
        ]
    },
    {
        "slug": "rosemont",
        "city": "Rosemont",
        "state": "IL",
        "state_full": "Illinois",
        "country": "US",
        "phone": "(833) 570-5966",
        "phone_clean": "18335705966",
        "phone_e164": "+18335705966",
        "badge": "📍 ROSEMONT & O'HARE CONVENTION DISTRICT COVERAGE",
        "h1": "Corporate Magician &amp; Mentalist in <span class=\"hero-headline-highlight\">Rosemont</span> for Stephens Convention Center, O'Hare Summits &amp; Galas",
        "subhead": "Elevating national conventions, leadership summits, and awards galas across the Rosemont O'Hare convention corridor with captivating mind reading and psychological entertainment.",
        "lat": 41.9868,
        "lon": -87.8722,
        "areas": ["Rosemont", "O'Hare Corridor", "Donald E. Stephens Convention Center", "Cook County", "Chicagoland", "Chicago"],
        "venue_h2": "Serving Chicagoland's Premier Convention Hub &amp; O'Hare Airport Resort District",
        "venue_p": "Home to the massive Donald E. Stephens Convention Center and world-class O'Hare airport conference resorts, Rosemont is the undisputed national meeting crossroads of the Midwest.",
        "card1": {
            "sub": "MEGA CONVENTION CENTERS & ARENAS",
            "title": "National Conventions & Trade Expos",
            "items": [
                "Donald E. Stephens Convention Center (840,000 sq ft versatile exhibition hall & conference space)",
                "Rosemont Theatre (4,400-seat state-of-the-art auditorium for national general sessions)",
                "Allstate Arena Private Event Suites (Major corporate hospitality & executive entertainment)",
                "Parkway Bank Park Entertainment District (Corporate dinners & buyout venues)"
            ]
        },
        "card2": {
            "sub": "LUXURY AIRPORT CONFERENCE RESORTS",
            "title": "Executive Conferences & Corporate Galas",
            "items": [
                "Hyatt Regency O'Hare Chicago (110,000 sq ft meeting space & Grand Ballroom)",
                "Loews Chicago O'Hare Hotel (53,000 sq ft luxury event space & live art gallery ballroom)",
                "Hilton Rosemont / Chicago O'Hare (Direct Stephens Convention Center skybridge access)",
                "The Westin O'Hare (Pillarless Grand Ballroom & executive amphitheater)"
            ]
        },
        "card3": {
            "sub": "DISTINCTIVE DINING & ENTERTAINMENT SPACES",
            "title": "VIP Banquets & Networking Mixers",
            "items": [
                "Rivers Casino Des Plaines / Rosemont VIP Event Lounges (High-stakes corporate dining)",
                "Gibsons Bar & Steakhouse Rosemont Private Dining (Legendary Chicago executive dinners)",
                "The Rose Hotel Chicago O'Hare, Tapestry Collection (Boutique boardroom retreats)",
                "Fogo de Chão Rosemont Private Corporate Salons (Churrascaria executive gatherings)"
            ]
        },
        "callout": {
            "sub": "O'HARE INTERNATIONAL AIRPORT (ORD) ADVANTAGE",
            "title": "5 Minutes from Chicago O'Hare (ORD) • Skybridge-Connected Hotels",
            "p": "Situated literally five minutes from Chicago O'Hare International Airport (ORD), Rosemont provides the quickest airport-to-stage commute in America. Adrian Saint delivers punctual, turnkey corporate entertainment."
        },
        "faqs": [
            {
                "q": "CAN ADRIAN HEADLINE LARGE GENERAL SESSIONS AT DONALD E. STEPHENS CONVENTION CENTER?",
                "a": "Yes! Adrian regularly headlines general sessions, association keynotes, and evening galas at the Donald E. Stephens Convention Center for corporate audiences from 200 to over 4,000 attendees."
            },
            {
                "q": "HOW DO TRAVEL LOGISTICS WORK FOR ROSEMONT O'HARE VENUES?",
                "a": "Rosemont is just 5 minutes from Chicago O'Hare International Airport (ORD). Adrian arrives with guaranteed punctuality, all-inclusive corporate pricing, and zero travel friction."
            },
            {
                "q": "IS THE SHOW 100% CLEAN AND APPROPRIATE FOR CORPORATE AND ASSOCIATION EVENTS?",
                "a": "Yes, absolutely. Adrian's show is 100% clean, professional, and HR-approved. It is crafted specifically for executive corporate banquets, associations, and national summits."
            },
            {
                "q": "WHAT TECHNICAL SETUP DOES ADRIAN REQUIRE AT HYATT REGENCY O'HARE OR LOEWS?",
                "a": "Adrian's rider is simple and venue-friendly: a wireless handheld or lavalier mic and connection to room sound. He works smoothly with in-house AV teams such as Encore."
            },
            {
                "q": "DOES ADRIAN PERFORM FOR ROSEMONT RESTAURANT BUYOUTS AND VIP DINNERS?",
                "a": "Yes! Adrian often provides close-up strolling mentalism during cocktail hours at Parkway Bank Park restaurants and private dining rooms at Gibsons, followed by an after-dinner stage performance."
            }
        ]
    },
    {
        "slug": "arlington-va",
        "city": "Arlington",
        "state": "VA",
        "state_full": "Virginia",
        "country": "US",
        "phone": "(833) 570-5966",
        "phone_clean": "18335705966",
        "phone_e164": "+18335705966",
        "badge": "📍 ARLINGTON & NATIONAL LANDING TECH CORRIDOR COVERAGE",
        "h1": "Corporate Magician &amp; Mentalist in <span class=\"hero-headline-highlight\">Arlington, VA</span> for Crystal City Summits, Amazon HQ2 Galas &amp; DCA Retreats",
        "subhead": "Sophisticated psychological entertainment and interactive mind reading for tech summits, defense leadership galas, and government affairs conferences across Arlington and National Landing.",
        "lat": 38.8799,
        "lon": -77.1067,
        "areas": ["Arlington", "Crystal City", "National Landing", "Rosslyn", "Pentagon City", "Northern Virginia", "Washington DC"],
        "venue_h2": "Serving Northern Virginia's Tech Corridor, Defense Headquarters &amp; Potomac Riverfront",
        "venue_p": "Directly overlooking the nation's capital across the Potomac River and anchored by Amazon HQ2 and the Pentagon, Arlington is a powerhouse hub for corporate conferences and executive summits.",
        "card1": {
            "sub": "PREMIER CONFERENCE HOTELS & CORRIDOR HUBS",
            "title": "National Conferences & Tech Summits",
            "items": [
                "Crystal Gateway Marriott (Nearly 40,000 sq ft conference space & Arlington Ballroom)",
                "Hyatt Regency Crystal City at Reagan National Airport (53,000 sq ft meeting space & Regency Ballroom)",
                "Renaissance Arlington Capital View Hotel (17,000 sq ft contemporary event space)",
                "The Ritz-Carlton, Pentagon City (Luxury Grand Ballroom for high-level diplomatic and corporate galas)"
            ]
        },
        "card2": {
            "sub": "TECH HUBS & INNOVATION SPACES",
            "title": "Executive Offsites & Tech Keynotes",
            "items": [
                "National Landing Tech District Event Spaces (Modern corporate summits near Amazon HQ2)",
                "Le Méridien Arlington in Rosslyn (Panoramic Potomac & DC skyline terrace ballrooms)",
                "Westin Arlington Gateway in Ballston (Tech corridor executive boardrooms & salons)",
                "Hilton Arlington National Landing (Executive meeting center & conference suites)"
            ]
        },
        "card3": {
            "sub": "DISTINCTIVE HISTORIC & SKYLINE EVENT VENUES",
            "title": "VIP Banquets & Executive Receptions",
            "items": [
                "Top of the Town Rosslyn (Breathtaking DC monument & skyline views for VIP banquets)",
                "Army Navy Country Club Arlington (Prestigious golf tournament galas & ballroom receptions)",
                "Washington Golf and Country Club (Exclusive private dining & corporate celebrations)",
                "National Rural Electric Cooperative Association (NRECA) Conference Center (Modern auditorium)"
            ]
        },
        "callout": {
            "sub": "REAGAN NATIONAL AIRPORT (DCA) ADVANTAGE",
            "title": "5 Minutes from Reagan National Airport (DCA) • Direct Metro Access",
            "p": "Located immediately next to Ronald Reagan Washington National Airport (DCA) and minutes from Washington, D.C., Arlington provides unparalleled travel accessibility. Adrian Saint delivers turnkey production with guaranteed on-time delivery."
        },
        "faqs": [
            {
                "q": "CAN ADRIAN HEADLINE MAJOR TECH & DEFENSE SUMMITS IN ARLINGTON, VA?",
                "a": "Yes! Adrian regularly headlines national corporate conferences, tech summits, and leadership banquets across Crystal City, Rosslyn, and Ballston for audiences from 100 to over 1,500 attendees."
            },
            {
                "q": "HOW DO TRAVEL LOGISTICS WORK FOR ARLINGTON AND D.C. METRO VENUES?",
                "a": "Arlington is situated 5 minutes from Ronald Reagan Washington National Airport (DCA) and 30 minutes from Dulles (IAD). Adrian provides all-inclusive travel logistics and guaranteed early on-site check-in."
            },
            {
                "q": "IS ADRIAN'S SHOW APPROPRIATE FOR DEFENSE CONTRACTORS, TECH EXECUTIVES & HR?",
                "a": "Yes, 100%. Adrian's corporate mind reading is sophisticated, clean, and intellectually engaging. He respects every volunteer and upholds strict corporate standards."
            },
            {
                "q": "WHAT TECHNICAL REQUIREMENTS DOES ADRIAN REQUIRE AT THE RITZ-CARLTON OR MARRIOTT?",
                "a": "Adrian's AV rider is simple: a wireless microphone and connection to room sound. He coordinates seamlessly with hotel AV teams."
            },
            {
                "q": "DOES ADRIAN PERFORM FOR PRIVATE SKYLINE RECEPTIONS AND ROOFTOP DINNERS IN ROSSLYN?",
                "a": "Yes! Adrian frequently performs strolling mind reading during cocktail receptions overlooking the D.C. monuments at Top of the Town, followed by an engaging after-dinner performance."
            }
        ]
    },
    {
        "slug": "colorado-springs",
        "city": "Colorado Springs",
        "state": "CO",
        "state_full": "Colorado",
        "country": "US",
        "phone": "(833) 570-5966",
        "phone_clean": "18335705966",
        "phone_e164": "+18335705966",
        "badge": "📍 COLORADO SPRINGS & BROADMOOR DESTINATION COVERAGE",
        "h1": "Corporate Magician &amp; Mentalist in <span class=\"hero-headline-highlight\">Colorado Springs</span> for The Broadmoor Summits, Pikes Peak Galas &amp; Retreats",
        "subhead": "World-class psychological entertainment and interactive mind reading for corporate conventions, luxury resort retreats, and national banquets in Colorado Springs.",
        "lat": 38.8339,
        "lon": -104.8214,
        "areas": ["Colorado Springs", "The Broadmoor", "El Paso County", "Front Range", "Colorado"],
        "venue_h2": "Serving Five-Star Mountain Resorts, Aerospace Summits &amp; Historic Front Range Venues",
        "venue_p": "Celebrated for the iconic Five-Star Broadmoor Resort, Cheyenne Mountain, and dramatic Rocky Mountain landscapes, Colorado Springs is a premier national convention and executive retreat destination.",
        "card1": {
            "sub": "FIVE-STAR MEGA-RESORTS & CONVENTION CENTERS",
            "title": "National Conventions & Luxury Galas",
            "items": [
                "The Broadmoor Resort & Convention Center (Over 315,000 sq ft meeting space, Broadmoor Hall & Colorado Hall)",
                "Cheyenne Mountain Resort, a Dolce by Wyndham (40,000 sq ft IACC-certified conference center)",
                "The Broadmoor West Ballroom & International Center (Pillarless luxury gala venues)",
                "Garden of the Gods Resort and Club (Stunning red rock panorama terraces & Three Graces Ballroom)"
            ]
        },
        "card2": {
            "sub": "CONFERENCE RESORTS & HISTORIC RETREATS",
            "title": "Executive Summits & Leadership Offsites",
            "items": [
                "The Mining Exchange, A Wyndham Grand Hotel (Historic downtown boutique corporate ballroom)",
                "Hotel Polaris at the U.S. Air Force Academy (State-of-the-art conference facilities & flight simulators)",
                "Great Wolf Lodge Colorado Springs Conference Center (Versatile corporate exposition space)",
                "DoubleTree by Hilton Colorado Springs (Grand ballroom banqueting near airport)"
            ]
        },
        "card3": {
            "sub": "DISTINCTIVE MOUNTAIN & MUSEUM VENUES",
            "title": "VIP Banquets & Private Receptions",
            "items": [
                "U.S. Olympic & Paralympic Museum (Sleek contemporary atrium & corporate event spaces)",
                "The Pinery at The Hill (Panoramic Pikes Peak views & luxury executive dining)",
                "Flying W Ranch (Legendary Western outdoor pavilion & corporate team gatherings)",
                "Glen Eyrie Castle (Exclusive castle executive boardrooms & historic retreat grounds)"
            ]
        },
        "callout": {
            "sub": "COLORADO FRONT RANGE CONVENIENCE",
            "title": "Minutes from Colorado Springs Airport (COS) • 75 Min from Denver (DEN)",
            "p": "With direct commercial flights into Colorado Springs Airport (COS) and rapid highway access from Denver International Airport (DEN), Colorado Springs is exceptionally accessible. Adrian Saint provides turnkey fly-in entertainment."
        },
        "faqs": [
            {
                "q": "CAN ADRIAN HEADLINE GENERAL SESSIONS AT THE BROADMOOR RESORT?",
                "a": "Yes! Adrian regularly headlines national corporate conferences, annual meetings, and awards galas in Broadmoor Hall and the International Center at The Broadmoor for audiences up to 3,000 executives."
            },
            {
                "q": "HOW DO TRAVEL LOGISTICS WORK FOR COLORADO SPRINGS RESORT CONFERENCES?",
                "a": "Colorado Springs is served directly by Colorado Springs Airport (COS) and is an easy 75-minute drive south of Denver International Airport (DEN). Adrian provides all-inclusive travel logistics and guaranteed punctual arrival."
            },
            {
                "q": "IS THE PERFORMANCE 100% CLEAN AND APPROPRIATE FOR CORPORATE AND DEFENSE EXECUTIVES?",
                "a": "Yes, absolutely. Adrian's corporate show is 100% clean, intelligent, and HR-approved. He never uses embarrassing gags or awkward humor, ensuring everyone feels valued and entertained."
            },
            {
                "q": "WHAT SOUND AND TECHNICAL SETUP DOES ADRIAN REQUIRE AT CHEYENNE MOUNTAIN RESORT?",
                "a": "Adrian's technical rider is famously straightforward: a wireless handheld or lavalier mic and connection to room sound. Zero complex lighting or staging requirements."
            },
            {
                "q": "DOES ADRIAN PERFORM AT PRIVATE EXECUTIVE GATHERINGS & GOLF RETREATS IN COLORADO SPRINGS?",
                "a": "Yes! In addition to large resort general sessions, Adrian frequently performs strolling close-up mentalism for cocktail receptions and intimate after-dinner shows for executive retreats."
            }
        ]
    },
    {
        "slug": "aventura",
        "city": "Aventura",
        "state": "FL",
        "state_full": "Florida",
        "country": "US",
        "phone": "(833) 570-5966",
        "phone_clean": "18335705966",
        "phone_e164": "+18335705966",
        "badge": "📍 AVENTURA & TURNBERRY LUXURY RESORT COVERAGE",
        "h1": "Corporate Magician &amp; Mentalist in <span class=\"hero-headline-highlight\">Aventura</span> for JW Marriott Turnberry Summits, Galas &amp; Retreats",
        "subhead": "Elevating luxury corporate summits, executive retreats, and national conferences across Aventura and Greater Miami with astonishing mind reading and psychological entertainment.",
        "lat": 25.9565,
        "lon": -80.1392,
        "areas": ["Aventura", "JW Marriott Turnberry", "Miami-Dade County", "Greater Miami", "South Florida", "Florida"],
        "venue_h2": "Serving South Florida's Most Prestigious Luxury Golf Resorts &amp; Waterfront Venues",
        "venue_p": "Synonymous with the legendary JW Marriott Miami Turnberry Resort &amp; Spa and premier coastal luxury, Aventura is South Florida's premier destination for high-end corporate retreats.",
        "card1": {
            "sub": "FIVE-STAR GOLF RESORTS & CONVENTION BALLROOMS",
            "title": "National Conferences & Milestone Galas",
            "items": [
                "JW Marriott Miami Turnberry Resort & Spa (Over 120,000 sq ft conference space & Grand Ballroom)",
                "Turnberry Isle Country Club Ballroom (Championship golf tournament galas & private receptions)",
                "JW Marriott Turnberry Magnolia & King Palm Ballrooms (Executive conference suites)",
                "Turnberry Marina VIP Lawn (Waterfront luxury yacht receptions & sunset mixers)"
            ]
        },
        "card2": {
            "sub": "LUXURY HOTELS & WATERFRONT VENUES",
            "title": "Executive Summits & Corporate Banquets",
            "items": [
                "Aloft Miami Aventura (Modern corporate offsites & tech-forward gatherings)",
                "Courtyard Miami Aventura (Corporate training sessions & executive boardrooms)",
                "AC Hotel by Marriott Miami Aventura (Sleek European design meeting spaces)",
                "Serena Pastry & Private Corporate Event Suites (Intimate VIP executive banquets)"
            ]
        },
        "card3": {
            "sub": "DISTINCTIVE CULTURAL & DINING DESTINATIONS",
            "title": "Private Dining & Leadership Galas",
            "items": [
                "Aventura Arts & Cultural Center (330-seat waterfront auditorium for keynotes & private performances)",
                "Bourbon Steak Miami by Michael Mina (Private executive dining & celebratory banquets)",
                "Casa D'Angelo Aventura Private Rooms (Upscale corporate culinary experiences)",
                "Gulfstream Park Champions Plaza & Private Suites (High-profile corporate entertainment)"
            ]
        },
        "callout": {
            "sub": "DUAL MIAMI & FORT LAUDERDALE AIRPORT ACCESS",
            "title": "20 Minutes from FLL & MIA • Direct Brightline Train Access",
            "p": "Centrally positioned between Fort Lauderdale-Hollywood International Airport (FLL) and Miami International Airport (MIA), with a brand-new Brightline train station, Aventura is a breeze to reach. Adrian Saint delivers turnkey fly-in entertainment."
        },
        "faqs": [
            {
                "q": "CAN ADRIAN HEADLINE GENERAL SESSIONS AT JW MARRIOTT MIAMI TURNBERRY RESORT?",
                "a": "Yes! Adrian regularly headlines national corporate conferences, annual meetings, and awards galas in the Grand Ballroom at JW Marriott Turnberry for audiences from 100 to over 2,000 attendees."
            },
            {
                "q": "HOW DO TRAVEL LOGISTICS WORK FOR AVENTURA AND SOUTH FLORIDA VENUES?",
                "a": "Aventura is situated 20 minutes from Fort Lauderdale Airport (FLL) and 25 minutes from Miami Airport (MIA), plus direct Brightline rail. Adrian Saint provides turnkey travel coordination and guaranteed punctuality."
            },
            {
                "q": "IS THE SHOW 100% CLEAN AND APPROPRIATE FOR CORPORATE EXECUTIVES?",
                "a": "Yes, absolutely. Adrian's corporate mind reading is 100% clean, sophisticated, and HR-safe. He elevates corporate guests with dignity and incredible psychological skill."
            },
            {
                "q": "WHAT TECHNICAL SETUP DOES ADRIAN REQUIRE AT TURNBERRY ISLE RESORT?",
                "a": "Adrian's technical rider is minimalist: a wireless handheld or lavalier mic and connection to room sound. He works effortlessly with in-house resort audiovisual teams."
            },
            {
                "q": "DOES ADRIAN PERFORM FOR PRIVATE DINNERS & COCKTAIL HOURS IN AVENTURA?",
                "a": "Yes! Adrian frequently performs close-up strolling mentalism during cocktail hours at Bourbon Steak and marina terraces, followed by his signature 30- to 60-minute interactive stage show."
            }
        ]
    },
    {
        "slug": "savannah",
        "city": "Savannah",
        "state": "GA",
        "state_full": "Georgia",
        "country": "US",
        "phone": "(833) 570-5966",
        "phone_clean": "18335705966",
        "phone_e164": "+18335705966",
        "badge": "📍 SAVANNAH CONVENTION CENTER & RIVER DISTRICT COVERAGE",
        "h1": "Corporate Magician &amp; Mentalist in <span class=\"hero-headline-highlight\">Savannah</span> for Convention Center Summits, Riverfront Galas &amp; Retreats",
        "subhead": "Captivating psychological entertainment and interactive mind reading for corporate conventions, riverfront banquets, and executive retreats in historic Savannah.",
        "lat": 32.0809,
        "lon": -81.0912,
        "areas": ["Savannah", "Savannah Riverfront", "Historic District", "Chatham County", "Georgia"],
        "venue_h2": "Serving Historic Riverfront Resorts, Convention Centers &amp; Distinctive Southern Estates",
        "venue_p": "Featuring the newly expanded Savannah Convention Center on Hutchinson Island and the vibrant Plant Riverside District, Savannah blends historic Southern charm with world-class meeting infrastructure.",
        "card1": {
            "sub": "EXPANDED WATERFRONT CONVENTION FACILITIES",
            "title": "National Conventions & Trade Summits",
            "items": [
                "Savannah Convention Center (Expanded 200,000 sq ft waterfront exhibit hall & Grand Ballroom)",
                "The Westin Savannah Harbor Golf Resort & Spa (Adjoining resort with 40,000 sq ft meeting space)",
                "Plant Riverside District / JW Marriott Savannah (100,000 sq ft riverfront entertainment & ballroom)",
                "Savannah Harbor Grand Ballroom (Waterfront banquet venue overlooking the historic skyline)"
            ]
        },
        "card2": {
            "sub": "HISTORIC LUXURY HOTELS & RIVERFRONT VENUES",
            "title": "Executive Summits & Corporate Dinners",
            "items": [
                "Hyatt Regency Savannah (River Street ballroom & direct cobblestone waterfront access)",
                "The DeSoto Savannah (Historic landmark ballroom & executive boardroom suites)",
                "Perry Lane Hotel, Luxury Collection (Boutique rooftop ballroom & VIP executive salons)",
                "The Brice, a Kimpton Hotel (Charming secret garden courtyard corporate dinners)"
            ]
        },
        "card3": {
            "sub": "DISTINCTIVE HISTORIC ESTATES & MUSEUMS",
            "title": "VIP Banquets & Private Receptions",
            "items": [
                "Telfair Museums / Jepson Center (Striking modern glass atrium & art gallery receptions)",
                "The Georgia Club & Savannah Golf Club (Private tournament banquets & executive galas)",
                "Old Fort Jackson Riverfront Grounds (Atmospheric coastal evening galas & private charters)",
                "Savannah Riverboat Cruises Private Charters (Exclusive floating corporate receptions)"
            ]
        },
        "callout": {
            "sub": "SAVANNAH / HILTON HEAD AIRPORT (SAV) ACCESS",
            "title": "15 Minutes from Savannah/Hilton Head Airport (SAV) • Historic River Ferry Access",
            "p": "Located just 15 minutes from Savannah/Hilton Head International Airport (SAV), Savannah is quick and enjoyable to navigate. Adrian Saint provides turnkey fly-in logistics with guaranteed punctual arrival."
        },
        "faqs": [
            {
                "q": "CAN ADRIAN HEADLINE GENERAL SESSIONS AT SAVANNAH CONVENTION CENTER?",
                "a": "Yes! Adrian regularly headlines national corporate conventions, association annual meetings, and gala banquets at the newly expanded Savannah Convention Center for groups from 150 to over 2,500 attendees."
            },
            {
                "q": "HOW DO TRAVEL LOGISTICS WORK FOR SAVANNAH RIVERFRONT RESORTS?",
                "a": "Savannah is 15 minutes from Savannah/Hilton Head International Airport (SAV). Adrian Saint provides all-inclusive travel arrangements, early venue soundcheck, and guaranteed prompt arrival."
            },
            {
                "q": "IS THE SHOW 100% CLEAN AND APPROPRIATE FOR CORPORATE AND ASSOCIATION AUDIENCES?",
                "a": "Yes, absolutely. Adrian's corporate mind reading is 100% clean, professional, and HR-safe. He engages attendees with warmth, humor, and breathtaking psychological demonstrations."
            },
            {
                "q": "WHAT TECHNICAL SETUP DOES ADRIAN REQUIRE AT THE WESTIN OR PLANT RIVERSIDE?",
                "a": "Adrian's technical rider is minimalist: a wireless handheld or lavalier mic and connection to house audio. He coordinates directly with hotel AV staff for effortless execution."
            },
            {
                "q": "DOES ADRIAN PERFORM FOR PRIVATE HISTORIC DISTRICT RECEPTIONS AND DINNERS?",
                "a": "Yes! Adrian frequently provides close-up strolling mentalism during cocktail hours at Perry Lane Hotel rooftop or Jepson Center, followed by an engaging after-dinner stage performance."
            }
        ]
    },
    {
        "slug": "toronto",
        "city": "Toronto",
        "state": "ON",
        "state_full": "Ontario",
        "country": "CA",
        "phone": "(833) 570-5966",
        "phone_clean": "18335705966",
        "phone_e164": "+18335705966",
        "badge": "📍 TORONTO METRO & FINANCIAL DISTRICT COVERAGE",
        "h1": "Corporate Magician &amp; Mentalist in <span class=\"hero-headline-highlight\">Toronto</span> for MTCC Summits, Bay Street Galas &amp; Executive Retreats",
        "subhead": "Elevate your Toronto convention, Financial District executive summit, or national gala with world-class psychological entertainment and interactive mind reading.",
        "lat": 43.6532,
        "lon": -79.3832,
        "areas": ["Toronto", "Financial District", "Metro Toronto Convention Centre", "Greater Toronto Area", "Ontario", "Canada"],
        "venue_h2": "Serving Downtown Toronto's Iconic Convention Complexes, Luxury Hotels &amp; Financial Towers",
        "venue_p": "As Canada's commercial and financial capital, Toronto features the world-renowned Metro Toronto Convention Centre (MTCC) and five-star luxury hotels designed for global corporate summits.",
        "card1": {
            "sub": "FLAGSHIP CONVENTION COMPLEXES",
            "title": "International Conventions & Mega-Summits",
            "items": [
                "Metro Toronto Convention Centre (MTCC) (Over 442,000 sq ft exhibition space & John Bassett Theatre)",
                "Enercare Centre at Exhibition Place (Over 1 million sq ft prime exhibition & conference halls)",
                "Beanfield Centre (Canada's premier LEED Silver conference center & Grand Ballroom)",
                "Meridian Hall / Sony Centre (3,191-seat theatre for national corporate rallies & general sessions)"
            ]
        },
        "card2": {
            "sub": "FIVE-STAR LUXURY FINANCIAL DISTRICT HOTELS",
            "title": "Executive Summits & Leadership Galas",
            "items": [
                "Fairmont Royal York (Legendary Canadian Ballroom & Imperial Room historic gala spaces)",
                "The Ritz-Carlton, Toronto (Luxury Grand Ballroom & executive private dining suites)",
                "Four Seasons Hotel Toronto (Yorkville contemporary luxury ballroom & boardrooms)",
                "Shangri-La Toronto & St. Regis Toronto (Premier high-finance corporate banquets)"
            ]
        },
        "card3": {
            "sub": "DISTINCTIVE WATERFRONT & SKYLINE VENUES",
            "title": "VIP Banquets & Executive Receptions",
            "items": [
                "The Carlu (Iconic Art Moderne event space & Round Room for high-profile galas)",
                "Canoe Restaurant & Bar Private Dining (54th floor Financial District views)",
                "Casa Loma Conservatory & Glass Pavilion (Historic castle estate corporate dinners)",
                "Arcadian Court & Arcadian Loft by Oliver & Bonacini (Heritage corporate banqueting)"
            ]
        },
        "callout": {
            "sub": "CROSS-BORDER FLY-IN ENTERTAINMENT EXPERTISE",
            "title": "Direct Pearson (YYZ) & Billy Bishop (YTZ) Access • Seamless Cross-Border Production",
            "p": "Adrian Saint regularly travels across North America for major international corporate conventions. With direct flights into Toronto Pearson (YYZ) and Billy Bishop Toronto City Airport (YTZ), logistics are turnkey and effortless."
        },
        "faqs": [
            {
                "q": "CAN ADRIAN HEADLINE INTERNATIONAL CONVENTIONS AT THE METRO TORONTO CONVENTION CENTRE (MTCC)?",
                "a": "Yes! Adrian regularly headlines international corporate conventions, technology summits, and gala banquets at the MTCC for audiences from 200 to over 3,500 attendees."
            },
            {
                "q": "HOW DO TRAVEL AND CROSS-BORDER LOGISTICS WORK FOR TORONTO EVENTS?",
                "a": "Adrian Saint handles cross-border entertainment regularly with valid passport credentials, turnkey travel coordination, and guaranteed early arrival into Toronto Pearson (YYZ) or Billy Bishop (YTZ)."
            },
            {
                "q": "IS THE SHOW 100% CLEAN AND APPROPRIATE FOR CANADIAN CORPORATE AUDIENCES?",
                "a": "Yes, absolutely. Adrian's corporate show is 100% clean, culturally astute, and HR-safe. He never uses embarrassing gags, crude humor, or awkward tricks."
            },
            {
                "q": "WHAT TECHNICAL SETUP DOES ADRIAN REQUIRE AT FAIRMONT ROYAL YORK OR THE RITZ-CARLTON?",
                "a": "Adrian's technical rider is minimalist: a wireless handheld or lavalier mic and connection to house audio. He coordinates smoothly with in-house AV teams such as Encore Canada."
            },
            {
                "q": "DOES ADRIAN PERFORM FOR PRIVATE BAY STREET DINNERS AND FINANCIAL DISTRICT RECEPTIONS?",
                "a": "Yes! In addition to large convention keynotes, Adrian frequently performs strolling close-up mentalism for cocktail receptions and intimate after-dinner shows for financial executive boards."
            }
        ]
    }
]

created_files = []

for c in GROUP_A_CITIES:
    slug = c["slug"]
    city = c["city"]
    state = c["state"]
    state_full = c["state_full"]
    country = c["country"]
    phone = c["phone"]
    phone_clean = c["phone_clean"]
    phone_e164 = c["phone_e164"]
    canon_url = f"https://adriansaintmentalist.com/corporate-magician-{slug}"
    title_str = f"Corporate Magician &amp; Mentalist {city}, {state} | Adrian Saint"
    desc_str = f"Book the top Corporate Magician & Mentalist in {city}, {state}. Adrian Saint delivers interactive mind reading for corporate conventions, leadership summits, and awards galas."
    keywords_str = f"Corporate Magician & Mentalist {city}, {city} Corporate Entertainment, Mind Reader {city} {state}, {c['areas'][1]} Magician, {state_full} Corporate Magician, Adrian Saint Mentalist"

    html = base_html

    # 1. Title and Canonical
    html = re.sub(r'<title>.*?</title>', f'<title>{title_str}</title>', html, count=1)
    html = re.sub(r'<link rel="canonical" href="[^"]*"', f'<link rel="canonical" href="{canon_url}"', html, count=1)

    # 2. Meta Tags
    html = re.sub(r'<meta property="og:url" content="[^"]*"', f'<meta property="og:url" content="{canon_url}"', html, count=1)
    html = re.sub(r'<meta property="og:title" content="[^"]*"', f'<meta property="og:title" content="{title_str}"', html, count=1)
    html = re.sub(r'<meta property="og:description" content="[^"]*"', f'<meta property="og:description" content="{desc_str}"', html, count=1)
    html = re.sub(r'<meta name="twitter:title" content="[^"]*"', f'<meta name="twitter:title" content="{title_str}"', html, count=1)
    html = re.sub(r'<meta name="twitter:description" content="[^"]*"', f'<meta name="twitter:description" content="{desc_str}"', html, count=1)
    html = re.sub(r'<meta name="description" content="[^"]*"', f'<meta name="description" content="{desc_str}"', html, count=1)
    html = re.sub(r'<meta name="keywords" content="[^"]*"', f'<meta name="keywords" content="{keywords_str}"', html, count=1)

    # 3. JSON-LD Schema
    faq_entities = []
    for f_item in c["faqs"]:
        faq_entities.append({
            "@type": "Question",
            "name": f_item["q"],
            "acceptedAnswer": {
                "@type": "Answer",
                "text": f_item["a"]
            }
        })
    # Add standard global FAQs from Aurora (questions 6-10)
    faq_entities.extend([
        {
            "@type": "Question",
            "name": "HOW FAR IN ADVANCE SHOULD WE HOLD OUR EVENT DATE?",
            "text": "Peak dates during spring and fall convention seasons (March through June, September through November) and December holiday banquets book 6 to 12 months in advance. Early holds are recommended to lock in date exclusivity."
        },
        {
            "@type": "Question",
            "name": "WHAT TYPES OF CORPORATE AUDIENCES ENJOY ADRIAN'S SHOW THE MOST?",
            "text": "Adrian's performance is designed specifically for sophisticated adult corporate groups including tech summits, finance and insurance conferences, healthcare and pharma banquets, executive retreats, and national franchise meetings."
        },
        {
            "@type": "Question",
            "name": "WHAT IS THE DIFFERENCE BETWEEN CLOSE-UP STROLLING AND THE STAGE SHOW?",
            "text": "Strolling mind reading takes place during cocktail hours or networking mixers where Adrian moves among small groups, performing intimate miracles inches away. The stage show is a unified theatrical presentation for the entire room from 30 to 60 minutes."
        },
        {
            "@type": "Question",
            "name": "CAN ADRIAN CUSTOMIZE HIS ROUTINES TO FEATURE OUR COMPANY THEME OR PRODUCT?",
            "text": "Yes! Adrian collaborates with corporate event planners to seamlessly incorporate company milestones, key branding messaging, CEO predictions, or customized reveals into the mentalism demonstrations."
        },
        {
            "@type": "Question",
            "name": "HOW DO WE RECEIVE A CUSTOM FEE PROPOSAL FOR OUR EVENT?",
            "text": "Simply submit the availability hold form on this page or call our direct booking office. You will receive a transparent, all-inclusive proposal within 24 to 48 hours."
        }
    ])

    area_entities = []
    for a_name in c["areas"]:
        area_entities.append({
            "@type": "AdministrativeArea" if "County" in a_name or "Metro" in a_name or "Area" in a_name or "District" in a_name else "City",
            "name": a_name
        })

    json_ld = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": [
                    "EntertainmentBusiness",
                    "ProfessionalService"
                ],
                "@id": f"{canon_url}#service",
                "name": f"Adrian Saint - Corporate Magician & Mentalist {city}",
                "url": canon_url,
                "telephone": phone_e164,
                "email": "adrian@saintmentalist.com",
                "priceRange": "$$$",
                "image": "https://adriansaintmentalist.com/images/adrian_saint_about_portrait.jpg",
                "description": f"Adrian Saint is the premier corporate mentalist and mind reader in {city}, {state_full}, delivering interactive psychological entertainment for convention expos, corporate leadership retreats, and national galas.",
                "address": {
                    "@type": "PostalAddress",
                    "addressLocality": city,
                    "addressRegion": state,
                    "addressCountry": country
                },
                "geo": {
                    "@type": "GeoCoordinates",
                    "latitude": c["lat"],
                    "longitude": c["lon"]
                },
                "areaServed": area_entities,
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
                "@id": f"{canon_url}#faq",
                "mainEntity": faq_entities
            }
        ]
    }
    json_ld_str = json.dumps(json_ld, indent=2)
    html = re.sub(r'<script id="geo-jsonld-script".*?</script>', f'<script id="geo-jsonld-script" type="application/ld+json">\n{json_ld_str}\n  </script>', html, count=1, flags=re.DOTALL)

    # 4. Hero Section
    html = re.sub(r'<div class="section-badge">\s*<span>📍.*?</span>\s*</div>', 
                  f'<div class="section-badge">\n              <span>{c["badge"]}</span>\n            </div>', 
                  html, count=1)

    html = re.sub(r'<h1 class="hero-headline">.*?</h1>', 
                  f'<h1 class="hero-headline">\n              {c["h1"]}\n            </h1>', 
                  html, count=1, flags=re.DOTALL)

    html = re.sub(r'<p class="hero-subheadline">.*?</p>', 
                  f'<p class="hero-subheadline">\n              {c["subhead"]}\n            </p>', 
                  html, count=1, flags=re.DOTALL)

    # Hero Form Values
    html = re.sub(r'name="_subject" value="[^"]*"', f'name="_subject" value="New Fast-Track Date Hold Request - {city} - Adrian Saint"', html, count=1)
    html = re.sub(r'name="event_city" value="[^"]*"', f'name="event_city" value="{city}, {state}"', html, count=1)

    # 5. Ticker Title
    html = re.sub(
        r'<div class="ticker-title">Trusted by Top Global Brands & Aurora Event Producers</div>',
        f'<div class="ticker-title">Trusted by Top Global Brands &amp; {city} Event Producers</div>',
        html,
        count=1
    )

    # 6. Venue Section
    c1 = c["card1"]
    c2 = c["card2"]
    c3 = c["card3"]
    callout = c["callout"]

    def build_bullets(items):
        return "\n              ".join([f"<li>{it}</li>" for it in items])

    venue_section_html = f'''<!-- 5.5 {city.upper()} PREMIER VENUES & LOCAL COVERAGE -->
    <section id="{slug}-venues" class="section-padding section-divider" style="background-color: var(--bg-card);">
      <div class="container">
        <div class="section-header">
          <div class="section-badge">{c["badge"]}</div>
          <h2 class="text-gradient-gold">{c["venue_h2"]}</h2>
          <p>{c["venue_p"]}</p>
        </div>

        <div class="grid-3" style="gap: 2rem; margin-bottom: 3.5rem;">
          <!-- Venue Card 1 -->
          <div class="service-card-interactive gold-glow-card" style="padding: 2.25rem 2rem;">
            <div style="font-size: 0.8rem; font-weight: 700; color: var(--accent-gold); text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 0.75rem;">
              {c1["sub"]}
            </div>
            <h3 style="font-size: 1.35rem; color: #FFFFFF; margin-bottom: 1rem; font-weight: 700;">{c1["title"]}</h3>
            <ul class="service-features" style="margin-bottom: 0;">
              {build_bullets(c1["items"])}
            </ul>
          </div>

          <!-- Venue Card 2 -->
          <div class="service-card-interactive gold-glow-card" style="padding: 2.25rem 2rem;">
            <div style="font-size: 0.8rem; font-weight: 700; color: var(--accent-gold); text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 0.75rem;">
              {c2["sub"]}
            </div>
            <h3 style="font-size: 1.35rem; color: #FFFFFF; margin-bottom: 1rem; font-weight: 700;">{c2["title"]}</h3>
            <ul class="service-features" style="margin-bottom: 0;">
              {build_bullets(c2["items"])}
            </ul>
          </div>

          <!-- Venue Card 3 -->
          <div class="service-card-interactive gold-glow-card" style="padding: 2.25rem 2rem;">
            <div style="font-size: 0.8rem; font-weight: 700; color: var(--accent-gold); text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 0.75rem;">
              {c3["sub"]}
            </div>
            <h3 style="font-size: 1.35rem; color: #FFFFFF; margin-bottom: 1rem; font-weight: 700;">{c3["title"]}</h3>
            <ul class="service-features" style="margin-bottom: 0;">
              {build_bullets(c3["items"])}
            </ul>
          </div>

        </div>

        <!-- Local Logistics Advantage Callout Box -->
        <div class="concierge-box gold-glow-card" style="background: rgba(17,19,28,0.95); border: 1px solid var(--border-gold-glow); border-radius: 18px; padding: 2.25rem; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 1.5rem;">
          <div style="max-width: 650px;">
            <div style="font-size: 0.8rem; font-weight: 700; color: var(--accent-gold); text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 0.5rem;">
              {callout["sub"]}
            </div>
            <h4 style="font-size: 1.25rem; color: #FFFFFF; margin-bottom: 0.5rem; font-weight: 700;">{callout["title"]}</h4>
            <p style="color: var(--text-silver); font-size: 0.95rem; line-height: 1.6; margin: 0;">
              {callout["p"]}
            </p>
          </div>
          <a href="tel:{phone_clean}" class="btn btn-gold" style="white-space: nowrap; text-decoration: none;">
            <span>Speak With Booking Office</span>
          </a>
        </div>

      </div>
    </section>'''

    html = re.sub(
        r'<!-- 5\.5 AURORA PREMIER VENUES & LOCAL COVERAGE -->\s*<section id="aurora-venues".*?</section>', 
        venue_section_html, 
        html, 
        count=1, 
        flags=re.DOTALL
    )

    # 7. Localized FAQs (Replace first 5 FAQs)
    faq_items_html = []
    for i, f_it in enumerate(c["faqs"]):
        is_active = ' active' if i == 0 else ''
        faq_items_html.append(f'''          <!-- Location Question {i+1} -->
          <div class="faq-item{is_active}">
            <div class="faq-question">
              <div class="faq-question-content">
                <span class="faq-question-title">{f_it["q"]}</span>
              </div>
              <svg class="faq-chevron" viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                <path d="M6 9l6 6 6-6"/>
              </svg>
            </div>
            <div class="faq-answer">
              <p>{f_it["a"]}</p>
            </div>
          </div>''')

    new_faqs_str = "\n\n".join(faq_items_html)

    # Replace from <!-- Location Question 1 --> up to <!-- Question 6 -->
    html = re.sub(
        r'<!-- Location Question 1 -->.*?<!-- Question 6 -->', 
        f'{new_faqs_str}\n\n          <!-- Question 6 -->', 
        html, 
        count=1, 
        flags=re.DOTALL
    )

    # 8. Bottom Booking Card Availability Badge
    html = re.sub(
        r'<span>Check Adrian\'s Availability For Your Next Aurora Event</span>',
        f'<span>Check Adrian\'s Availability For Your Next {city} Event</span>',
        html,
        count=1
    )

    # 9. Phone Replacements (Replaces all 6 phone instances if custom phone is specified)
    if phone_clean != "18335705966":
        html = html.replace("tel:18335705966", f"tel:{phone_clean}")
        html = html.replace("+18335705966", phone_e164)
        html = html.replace("1 (833) 570-5966", f"1 {phone}")
        html = html.replace("(833) 570-5966", phone)

    # Write to target file
    out_filename = f"corporate-magician-{slug}.html"
    with open(out_filename, 'w', encoding='utf-8') as out_f:
        out_f.write(html)

    created_files.append(out_filename)
    print(f"Generated {out_filename} ({len(html)} bytes)")

print(f"\nSuccessfully generated all {len(created_files)} Group A location pages!")
