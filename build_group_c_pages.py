import json
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')


def sub_once(pattern, replacement, text, flags=0, label=''):
    new_text, count = re.subn(pattern, lambda _: replacement, text, count=1, flags=flags)
    if count != 1:
        raise ValueError(f"Expected 1 replacement for {label or pattern}, got {count}")
    return new_text


# Read base template from corporate-magician-aurora.html
with open('corporate-magician-aurora.html', 'r', encoding='utf-8') as f:
    base_html = f.read()

# Update cache buster to latest version
base_html = re.sub(r'css/main\.css\?v=[^"]+', 'css/main.css?v=20261107_v62', base_html)
base_html = re.sub(r'css/components\.css\?v=[^"]+', 'css/components.css?v=20261107_v62', base_html)
base_html = re.sub(r'js/app\.js\?v=[^"]+', 'js/app.js?v=20261107_v62', base_html)

GROUP_C_CITIES = [
    {
        "slug": "palm-beach",
        "city": "Palm Beach",
        "state": "FL",
        "state_region": "FL",
        "state_full": "Florida",
        "country": "US",
        "phone": "(833) 570-5966",
        "phone_clean": "18335705966",
        "phone_e164": "+18335705966",
        "badge": "📍 PALM BEACH ISLAND & LUXURY RESORT COVERAGE",
        "h1": "Corporate Magician &amp; Mentalist in <span class=\"hero-headline-highlight\">Palm Beach</span> for The Breakers Galas, Executive Retreats &amp; Incentive Summits",
        "subhead": "Delivering sophisticated psychological entertainment and interactive mind reading for C-suite retreats, President's Club galas, and luxury resort conferences across Palm Beach and South Florida.",
        "lat": 26.7056,
        "lon": -80.0364,
        "areas": ["Palm Beach", "Palm Beach County", "West Palm Beach", "Manalapan", "Palm Beach Gardens", "Worth Avenue", "South Florida"],
        "venue_h2": "Serving Palm Beach's Five-Star Oceanfront Resorts &amp; Private Island Estates",
        "venue_p": "From the historic grandeur of The Breakers Palm Beach to Forbes Five-Star beachfront sanctuaries in Manalapan, Palm Beach sets the gold standard for ultra-luxury executive retreats and black-tie corporate galas.",
        "card1": {
            "sub": "FLAGSHIP OCEANFRONT RESORTS",
            "title": "Five-Star Galas & Incentive Retreats",
            "items": [
                "The Breakers Palm Beach (Iconic oceanfront landmark with Venetian & Ponce de Leon Ballrooms)",
                "Eau Palm Beach Resort & Spa (Forbes Five-Star Manalapan retreat with oceanfront event terraces)",
                "Four Seasons Resort Palm Beach (Five-Star executive boardrooms & private coastal pavilions)",
                "PGA National Resort (Palm Beach Gardens championship golf & executive conference campus)"
            ]
        },
        "card2": {
            "sub": "LUXURY HOTELS & CONVENTION SPACES",
            "title": "Executive Summits & Corporate Dinners",
            "items": [
                "Palm Beach County Convention Center (350,000 sq ft West Palm Beach convention & gala hub)",
                "Hilton West Palm Beach (Connected directly via enclosed walkway to the convention center)",
                "The Colony Hotel Palm Beach (Iconic Worth Avenue boutique hotel for VIP receptions)",
                "The Brazilian Court Hotel (Intimate luxury courtyards & Café Boulud private executive dining)"
            ]
        },
        "card3": {
            "sub": "PRIVATE CLUBS & CULTURAL LANDMARKS",
            "title": "Black-Tie Banquets & Waterfront Events",
            "items": [
                "Henry Morrison Flagler Museum (Whitehall Grand Hall for unforgettable black-tie galas)",
                "The Ben, Autograph Collection (Waterfront rooftop ballrooms overlooking Palm Harbor)",
                "Kravis Center for the Performing Arts (Cohen Pavilion & Dreyfoos Hall keynote productions)",
                "Private Palm Beach Yacht & Country Club Receptions (Exclusive VIP strolling mentalism)"
            ]
        },
        "callout": {
            "sub": "SOUTH FLORIDA LUXURY FLY-IN EXPERTISE",
            "title": "Direct Palm Beach International (PBI) Access • 10 Minutes to The Breakers",
            "p": "Adrian Saint regularly performs for high-net-worth executive boards and Fortune 500 incentive groups across Palm Beach. Arriving directly into Palm Beach International Airport (PBI) just 10 minutes from the island ensures effortless, white-glove delivery."
        },
        "faqs": [
            {
                "q": "CAN ADRIAN HEADLINE EXECUTIVE GALAS AT THE BREAKERS PALM BEACH OR EAU PALM BEACH?",
                "a": "Yes! Adrian regularly headlines President's Club awards banquets, leadership summits, and private black-tie galas at The Breakers, Eau Palm Beach, and Four Seasons Palm Beach for audiences from 30 to over 1,500."
            },
            {
                "q": "HOW DO TRAVEL LOGISTICS WORK FOR PALM BEACH ISLAND RESORT EVENTS?",
                "a": "Adrian flies directly into Palm Beach International Airport (PBI), located just 10 minutes from Palm Beach Island, or Fort Lauderdale (FLL). All travel is turnkey with guaranteed early arrival."
            },
            {
                "q": "IS ADRIAN'S PERFORMANCE APPROPRIATE FOR C-SUITE EXECUTIVES AND PRIVATE WEALTH CLIENTS?",
                "a": "Absolutely. Adrian's modern psychological mentalism is tailored for sophisticated adult audiences—100% clean, sharp, respectful, and completely free of cheesy props or embarrassing humor."
            },
            {
                "q": "WHAT TECHNICAL SETUP DOES ADRIAN REQUIRE AT FIVE-STAR PALM BEACH RESORTS?",
                "a": "Adrian's rider is minimalist: a single wireless handheld or lavalier microphone patched into house sound. He coordinates seamlessly with resort AV teams like Encore at The Breakers."
            },
            {
                "q": "DOES ADRIAN PERFORM INTIMATE AFTER-DINNER SHOWS FOR SMALL BOARD RETREATS IN PALM BEACH?",
                "a": "Yes! In addition to main stage ballroom keynotes, Adrian excels at intimate parlor-style mind reading and strolling close-up mentalism for private executive dinners of 15 to 60 guests."
            }
        ]
    },
    {
        "slug": "naples",
        "city": "Naples",
        "state": "FL",
        "state_region": "FL",
        "state_full": "Florida",
        "country": "US",
        "phone": "(833) 570-5966",
        "phone_clean": "18335705966",
        "phone_e164": "+18335705966",
        "badge": "📍 NAPLES GULF COAST & RITZ-CARLTON RESORT COVERAGE",
        "h1": "Corporate Magician &amp; Mentalist in <span class=\"hero-headline-highlight\">Naples</span> for Ritz-Carlton Retreats, Incentive Trips &amp; Gulf Coast Galas",
        "subhead": "Delivering unforgettable psychological mentalism and interactive mind reading for executive leadership summits, incentive galas, and private dinners across Naples and Southwest Florida.",
        "lat": 26.1420,
        "lon": -81.7948,
        "areas": ["Naples", "Collier County", "Vanderbilt Beach", "Old Naples", "Pelican Bay", "Bonita Springs", "Southwest Florida"],
        "venue_h2": "Serving Naples's Five-Star Gulf Coast Resorts &amp; Exclusive Private Clubs",
        "venue_p": "Renowned for pristine Gulf beaches, championship golf, and world-class luxury resorts like The Ritz-Carlton, Naples is one of America's premier destinations for corporate incentive programs and executive retreats.",
        "card1": {
            "sub": "FIVE-STAR GULF COAST RESORTS",
            "title": "Incentive Trips & Flagship Galas",
            "items": [
                "The Ritz-Carlton, Naples (Iconic beachfront flagship with Vanderbilt Ballroom & 42,000+ sq ft space)",
                "The Ritz-Carlton Naples, Tiburón (Championship golf resort & executive conference pavilion)",
                "Naples Grande Beach Resort (83,000 sq ft of indoor/outdoor resort event venues & Vista Ballroom)",
                "LaPlaya Beach & Golf Resort (Exclusive Vanderbilt Beach Gulf-front executive sanctuary)"
            ]
        },
        "card2": {
            "sub": "LUXURY BOUTIQUE HOTELS & COUNTRY CLUBS",
            "title": "Executive Summits & Board Dinners",
            "items": [
                "Inn on Fifth & Club Level Suites (Old Naples 5th Avenue South VIP executive gatherings)",
                "Edgewater Beach Hotel (All-suite Gulf-front retreat for boutique leadership offsites)",
                "Grey Oaks Country Club & Quail West Golf Club (Private luxury estate clubhouses)",
                "Hyatt Regency Coconut Point Resort & Spa (Nearby Bonita Springs mega-resort retreats)"
            ]
        },
        "card3": {
            "sub": "DISTINCTIVE SOUTHWEST FLORIDA VENUES",
            "title": "Cultural Receptions & Private Banquets",
            "items": [
                "Artis—Naples & The Baker Museum (Sophisticated cultural receptions & keynote events)",
                "Naples Botanical Garden (Kapnick Hall & lush tropical corporate gala terraces)",
                "The Club at Mediterra (Private Mediterranean estate clubhouse banquets)",
                "Naples Princess & Private Gulf Yacht Charters (Sunset cocktail strolling mentalism)"
            ]
        },
        "callout": {
            "sub": "SOUTHWEST FLORIDA RESORT LOGISTICS",
            "title": "Direct RSW International Airport Access • Turnkey Resort Production",
            "p": "Adrian Saint flies directly into Southwest Florida International Airport (RSW) just 35 minutes north of Naples resorts. With a carry-on minimalist rider and seamless resort AV coordination, your incentive gala runs effortlessly."
        },
        "faqs": [
            {
                "q": "CAN ADRIAN HEADLINE INCENTIVE GALAS AT THE RITZ-CARLTON NAPLES OR NAPLES GRANDE?",
                "a": "Yes! Adrian regularly headlines President's Club dinners, opening night receptions, and closing awards galas at The Ritz-Carlton, Naples, Tiburón, and Naples Grande Beach Resort."
            },
            {
                "q": "HOW DO TRAVEL LOGISTICS WORK FOR NAPLES CORPORATE RETREATS?",
                "a": "Adrian flies directly into Southwest Florida International Airport (RSW), located 35 minutes from Vanderbilt Beach and Old Naples. All travel arrangements are turnkey and self-managed."
            },
            {
                "q": "IS ADRIAN'S SHOW GREAT FOR SPOUSE-INCLUSIVE INCENTIVE TRIPS?",
                "a": "Yes! Spouse-inclusive President's Club and incentive galas are Adrian's specialty. His 100% clean, interactive mind reading creates shared astonishment and laughter for executives and guests alike."
            },
            {
                "q": "WHAT AUDIOVISUAL SETUP DOES ADRIAN NEED AT NAPLES LUXURY RESORTS?",
                "a": "Adrian requires only a wireless handheld or lavalier microphone connected to room sound. For beachfront cocktail receptions, strolling mind reading requires zero AV equipment."
            },
            {
                "q": "CAN ADRIAN PERFORM BOTH COCKTAIL HOUR STROLLING AND AN AFTER-DINNER STAGE SHOW?",
                "a": "Yes! Many Naples incentive planners book Adrian's hybrid package: intimate strolling mind reading during sunset cocktails followed by a unified 45-minute after-dinner headline show."
            }
        ]
    },
    {
        "slug": "boca-raton",
        "city": "Boca Raton",
        "state": "FL",
        "state_region": "FL",
        "state_full": "Florida",
        "country": "US",
        "phone": "(833) 570-5966",
        "phone_clean": "18335705966",
        "phone_e164": "+18335705966",
        "badge": "📍 BOCA RATON & THE BOCA RATON RESORT COVERAGE",
        "h1": "Corporate Magician &amp; Mentalist in <span class=\"hero-headline-highlight\">Boca Raton</span> for Resort Summits, Executive Retreats &amp; Gold Coast Galas",
        "subhead": "Delivering world-class psychological mentalism and interactive mind reading for flagship corporate conferences, wealth summits, and luxury resort galas across Boca Raton and South Florida.",
        "lat": 26.3683,
        "lon": -80.1289,
        "areas": ["Boca Raton", "Palm Beach County", "Mizner Park", "East Boca", "Delray Beach", "Deerfield Beach", "South Florida"],
        "venue_h2": "Serving Boca Raton's Legendary Waterfront Resort &amp; Executive Event Venues",
        "venue_p": "Anchored by the iconic 200-acre Boca Raton resort campus and thriving financial and corporate headquarters, Boca Raton hosts some of South Florida's most prestigious executive conferences and incentive galas.",
        "card1": {
            "sub": "ICONIC WATERFRONT RESORT CAMPUSES",
            "title": "Flagship Summits & Black-Tie Galas",
            "items": [
                "The Boca Raton (Legendary 200-acre waterfront sanctuary: Cloister, Tower, Yacht Club & Beach Club)",
                "Mizner Center & Grand Ballroom at The Boca Raton (Over 150,000 sq ft of premier event space)",
                "The Boca Raton Beach Club (Private oceanfront terrace dinners & incentive receptions)",
                "Waldorf Astoria Heritage Suites & Luxury Corporate Hospitality Venues"
            ]
        },
        "card2": {
            "sub": "CORPORATE HOTELS & CHAMPIONSHIP CLUBS",
            "title": "Executive Conferences & Leadership Dinners",
            "items": [
                "Boca Raton Marriott at Boca Center (Premier executive conference center in the business corridor)",
                "Renaissance Boca Raton Hotel (Contemporary meeting halls & poolside gala terraces)",
                "Waterstone Resort & Marina, Curio Collection (Intracoastal waterfront executive suites)",
                "Broken Sound Club & Boca West Country Club (Championship golf clubhouses for corporate galas)"
            ]
        },
        "card3": {
            "sub": "DISTINCTIVE GOLD COAST LANDMARKS",
            "title": "Private Estates & Cultural Receptions",
            "items": [
                "The Addison (Historic 1926 Addison Mizner estate with iconic banyan tree courtyard)",
                "Boca Raton Museum of Art at Mizner Park (Sophisticated gallery receptions & VIP mixers)",
                "Morikami Museum and Japanese Gardens (Serene architectural venue for executive dinners)",
                "The Seagate Hotel & Spa in Delray Beach (Nearby luxury coastal retreats)"
            ]
        },
        "callout": {
            "sub": "SOUTH FLORIDA TRI-AIRPORT MOBILITY",
            "title": "Direct FLL & PBI Airport Access • 25 Minutes to The Boca Raton",
            "p": "Centrally situated between Fort Lauderdale-Hollywood (FLL) and Palm Beach International (PBI) airports, Boca Raton is effortlessly accessible. Adrian Saint delivers turnkey, zero-friction corporate entertainment every time."
        },
        "faqs": [
            {
                "q": "CAN ADRIAN HEADLINE CONFERENCES AND GALAS AT THE BOCA RATON RESORT?",
                "a": "Yes! Adrian regularly headlines corporate summits, financial conferences, and evening awards banquets at The Boca Raton (including the Mizner Center and Grand Ballroom) for groups from 50 to over 2,000."
            },
            {
                "q": "HOW DO TRAVEL LOGISTICS WORK FOR BOCA RATON CORPORATE EVENTS?",
                "a": "Adrian flies directly into Fort Lauderdale-Hollywood International Airport (FLL) or Palm Beach International Airport (PBI), both just 25 minutes from East Boca resorts."
            },
            {
                "q": "IS THE PERFORMANCE 100% CLEAN AND TAILORED FOR FINANCIAL & C-SUITE GROUPS?",
                "a": "Yes, 100%. Adrian's corporate show is clean, intelligent, and HR-approved—built specifically for discerning financial advisors, private equity teams, and Fortune 500 executives."
            },
            {
                "q": "WHAT TECHNICAL EQUIPMENT DOES ADRIAN REQUIRE AT THE BOCA RATON OR THE ADDISON?",
                "a": "Adrian requires only a wireless handheld or lavalier microphone patched into room audio. His minimalist rider makes sound checks fast and effortless."
            },
            {
                "q": "DOES ADRIAN PERFORM STROLLING MIND READING FOR WATERFRONT COCKTAIL HOURS?",
                "a": "Yes! Adrian's strolling close-up mentalism is a massive hit during Intracoastal cocktail hours, Beach Club receptions, and private courtyard dinners at The Addison."
            }
        ]
    },
    {
        "slug": "key-west",
        "city": "Key West",
        "state": "FL",
        "state_region": "FL",
        "state_full": "Florida",
        "country": "US",
        "phone": "(833) 570-5966",
        "phone_clean": "18335705966",
        "phone_e164": "+18335705966",
        "badge": "📍 KEY WEST & CASA MARINA RESORT COVERAGE",
        "h1": "Corporate Magician &amp; Mentalist in <span class=\"hero-headline-highlight\">Key West</span> for Casa Marina Retreats, Incentive Trips &amp; Island Galas",
        "subhead": "Delivering unforgettable psychological entertainment and interactive mind reading for executive incentive trips, oceanfront awards galas, and private island retreats across Key West and the Florida Keys.",
        "lat": 24.5551,
        "lon": -81.7800,
        "areas": ["Key West", "Monroe County", "Old Town Key West", "Duval Street", "Sunset Key", "Stock Island", "Florida Keys"],
        "venue_h2": "Serving Key West's Iconic Oceanfront Resorts &amp; Historic Island Estates",
        "venue_p": "From the historic beachfront elegance of Casa Marina Key West to private island sanctuaries on Sunset Key, Key West transforms corporate incentive trips and executive summits into unforgettable tropical celebrations.",
        "card1": {
            "sub": "FLAGSHIP OCEANFRONT RESORTS",
            "title": "Incentive Galas & Beachfront Summits",
            "items": [
                "Casa Marina Key West, Curio Collection by Hilton (Historic 1920s landmark, private beach & Flagler Ballroom)",
                "The Reach Key West, Curio Collection by Hilton (Only natural sand beach in Key West & oceanfront decks)",
                "Pier House Resort & Spa (Iconic Old Town harborfront sanctuary for VIP executive retreats)",
                "Ocean Key Resort & Spa (Zero Duval Street Sunset Pier receptions & luxury suites)"
            ]
        },
        "card2": {
            "sub": "PRIVATE ISLAND & HARBORFRONT RETREATS",
            "title": "C-Suite Offsites & Executive Dinners",
            "items": [
                "Sunset Key Cottages (Exclusive 27-acre private island retreat accessed by boat for top boards)",
                "Opal Key Resort & Marina (Harborfront ballrooms & panoramic sunset marina event decks)",
                "Hyatt Centric Key West Resort & Spa (Waterfront executive suites & private pier gatherings)",
                "Margaritaville Beach House Key West (Spacious coastal resort venues for incentive groups)"
            ]
        },
        "card3": {
            "sub": "HISTORIC FLORIDA KEYS LANDMARKS",
            "title": "Distinctive Island Receptions & Charters",
            "items": [
                "Harry S. Truman Little White House (Historic presidential estate for prestigious executive dinners)",
                "Audubon House & Tropical Gardens (Lush 19th-century Old Town courtyard gala receptions)",
                "Ernest Hemingway Home & Museum Grounds (Unforgettable private after-hours corporate events)",
                "Private Sunset Catamaran & Yacht Charters (Close-up mind reading on Key West waters)"
            ]
        },
        "callout": {
            "sub": "EFFORTLESS ISLAND FLY-IN PRODUCTION",
            "title": "Direct Key West International (EYW) Access • Zero Heavy Cargo",
            "p": "Because Adrian Saint performs with minds and everyday objects rather than heavy illusion crates, island travel to Key West International Airport (EYW) is effortless—10 minutes from airport tarmac to Casa Marina."
        },
        "faqs": [
            {
                "q": "CAN ADRIAN HEADLINE INCENTIVE DINNERS AT CASA MARINA OR THE REACH KEY WEST?",
                "a": "Yes! Adrian regularly headlines President's Club awards banquets and oceanfront welcome receptions at Casa Marina Key West, The Reach, and Sunset Key for groups from 20 to over 600."
            },
            {
                "q": "HOW DO TRAVEL AND EQUIPMENT LOGISTICS WORK FOR KEY WEST ISLAND EVENTS?",
                "a": "Adrian flies directly into Key West International Airport (EYW) with zero bulky freight or shipping crates. Everything fits in carry-on luggage, eliminating island shipping delays completely."
            },
            {
                "q": "IS THE SHOW APPROPRIATE FOR RELAXED YET UPSCALE INCENTIVE TRIPS?",
                "a": "Yes! Adrian matches the energy of a luxury tropical incentive trip—witty, astonishing, 100% clean, and interactive—so executives and spouses have the highlight night of the entire trip."
            },
            {
                "q": "CAN ADRIAN PERFORM OUTDOORS ON OCEANFRONT DECKS OR PRIVATE YACHTS?",
                "a": "Absolutely! Adrian's strolling close-up mentalism requires zero AV and works seamlessly on Sunset Pier, Casa Marina's beach lawn, or aboard private sunset yacht charters."
            },
            {
                "q": "WHAT TECHNICAL SETUP DOES ADRIAN REQUIRE FOR BALLROOM STAGE SHOWS IN KEY WEST?",
                "a": "For Flagler Ballroom or indoor banquet stage shows, Adrian requires only a wireless handheld or lavalier microphone and standard room sound."
            }
        ]
    },
    {
        "slug": "sarasota",
        "city": "Sarasota",
        "state": "FL",
        "state_region": "FL",
        "state_full": "Florida",
        "country": "US",
        "phone": "(833) 570-5966",
        "phone_clean": "18335705966",
        "phone_e164": "+18335705966",
        "badge": "📍 SARASOTA & LONGBOAT KEY LUXURY RESORT COVERAGE",
        "h1": "Corporate Magician &amp; Mentalist in <span class=\"hero-headline-highlight\">Sarasota</span> for Ritz-Carlton Retreats, Longboat Key Galas &amp; Summits",
        "subhead": "Delivering sophisticated psychological mentalism and interactive mind reading for executive conferences, Gulf Coast incentive retreats, and cultural galas across Sarasota and Longboat Key.",
        "lat": 27.3364,
        "lon": -82.5307,
        "areas": ["Sarasota", "Sarasota County", "Longboat Key", "Lido Key", "Siesta Key", "Downtown Sarasota", "Lakewood Ranch", "Florida Gulf Coast"],
        "venue_h2": "Serving Sarasota's Five-Star Waterfront Resorts &amp; Cultural Estate Landmarks",
        "venue_p": "Combining Gulf Coast island serenity on Longboat Key with world-class cultural landmarks like The Ringling, Sarasota is an extraordinary destination for corporate leadership summits and black-tie incentive banquets.",
        "card1": {
            "sub": "FIVE-STAR WATERFRONT & ISLAND RESORTS",
            "title": "Incentive Retreats & Luxury Galas",
            "items": [
                "The Ritz-Carlton, Sarasota (Premier bayfront luxury hotel, Lido Key Beach Club & Grand Ballroom)",
                "The St. Regis Longboat Key Resort (Ultra-luxury beachfront sanctuary with Astor Ballroom)",
                "The Resort at Longboat Key Club (410-acre Gulf-front resort with golf & conference halls)",
                "Zota Beach Resort (Contemporary Longboat Key oceanfront executive retreats)"
            ]
        },
        "card2": {
            "sub": "DOWNTOWN CONFERENCE & BOUTIQUE HOTELS",
            "title": "Executive Summits & Corporate Banquets",
            "items": [
                "The Westin Sarasota (Bayfront downtown hotel with panoramic rooftop terrace & ballrooms)",
                "Hyatt Regency Sarasota (Waterfront marina resort & expansive corporate convention halls)",
                "Art Ovation Hotel, Autograph Collection (Arts District luxury boutique hotel for VIP retreats)",
                "The Sarasota Modern, a Tribute Portfolio Hotel (Stylish Rosemary District corporate offsites)"
            ]
        },
        "card3": {
            "sub": "ICONIC CULTURAL & ESTATE VENUES",
            "title": "Private Banquets & Architectural Galas",
            "items": [
                "The Ringling Museum of Art & Ca' d'Zan (Venetian Gothic bayfront mansion & Courtyard galas)",
                "Marie Selby Botanical Gardens (Michael's On The Bay & lush waterfront corporate receptions)",
                "Michael's On East (Premier private ballroom for executive banquets in Downtown Sarasota)",
                "The Concession Golf Club & Laurel Oak Country Club (Private executive golf outings)"
            ]
        },
        "callout": {
            "sub": "GULF COAST FLY-IN CONVENIENCE",
            "title": "Direct Sarasota-Bradenton (SRQ) Access • 10 Minutes to Downtown & Lido Key",
            "p": "Flying directly into Sarasota-Bradenton International Airport (SRQ) just 10 minutes from downtown hotels and 15 minutes from Longboat Key, Adrian Saint ensures punctual, turnkey production for every corporate event."
        },
        "faqs": [
            {
                "q": "CAN ADRIAN HEADLINE GALAS AT THE RITZ-CARLTON SARASOTA OR LONGBOAT KEY CLUB?",
                "a": "Yes! Adrian regularly headlines corporate awards banquets, leadership retreats, and executive galas at The Ritz-Carlton, Sarasota, The St. Regis Longboat Key, and Longboat Key Club."
            },
            {
                "q": "HOW DO TRAVEL LOGISTICS WORK FOR SARASOTA AND LONGBOAT KEY EVENTS?",
                "a": "Adrian flies directly into Sarasota-Bradenton International Airport (SRQ), just 10–15 minutes from premier bayfront and barrier island resorts, or Tampa International Airport (TPA) one hour north."
            },
            {
                "q": "IS ADRIAN'S SHOW 100% CLEAN AND APPROPRIATE FOR CORPORATE EXECUTIVES?",
                "a": "Yes, 100%. Adrian's corporate mentalism is clean, intelligent, and HR-approved, captivating sophisticated audiences without ever embarrassing volunteers."
            },
            {
                "q": "WHAT TECHNICAL REQUIREMENTS DOES ADRIAN HAVE AT SARASOTA HOTELS OR THE RINGLING?",
                "a": "Adrian requires only a wireless handheld or lavalier microphone connected to venue sound. His minimalist setup works smoothly in grand ballrooms and historic museum courtyards alike."
            },
            {
                "q": "DOES ADRIAN PERFORM STROLLING MENTALISM FOR BAYFRONT COCKTAIL MIXERS?",
                "a": "Yes! Adrian's strolling close-up mind reading is ideal for sunset cocktail hours at the Lido Key Beach Club, Marie Selby Botanical Gardens, and private yacht charters."
            }
        ]
    },
    {
        "slug": "marco-island",
        "city": "Marco Island",
        "state": "FL",
        "state_region": "FL",
        "state_full": "Florida",
        "country": "US",
        "phone": "(833) 570-5966",
        "phone_clean": "18335705966",
        "phone_e164": "+18335705966",
        "badge": "📍 MARCO ISLAND & JW MARRIOTT BEACH RESORT COVERAGE",
        "h1": "Corporate Magician &amp; Mentalist in <span class=\"hero-headline-highlight\">Marco Island</span> for JW Marriott Summits, Incentive Trips &amp; Beach Galas",
        "subhead": "Delivering unforgettable psychological entertainment and interactive mind reading for national incentive trips, President's Club awards galas, and executive conferences on Marco Island.",
        "lat": 25.9412,
        "lon": -81.7184,
        "areas": ["Marco Island", "Collier County", "Ten Thousand Islands", "Naples", "Goodland", "Southwest Florida"],
        "venue_h2": "Serving Marco Island's Premier Beachfront Resorts &amp; Incentive Destinations",
        "venue_p": "Anchored by the sprawling JW Marriott Marco Island Beach Resort and miles of pristine Gulf coastline, Marco Island is one of America's top luxury destinations for corporate incentive programs and national sales conferences.",
        "card1": {
            "sub": "MEGA-RESORT & INCENTIVE FLAGSHIPS",
            "title": "National Conferences & Incentive Galas",
            "items": [
                "JW Marriott Marco Island Beach Resort (140,000+ sq ft event space, Calusa Ballroom & 3-mile beach)",
                "Sirene at JW Marriott Marco Island (Adults-only luxury beachfront enclave for elite C-suite retreats)",
                "Hilton Marco Island Beach Resort & Spa (Oceanfront conference hub & Gulf-view ballrooms)",
                "Marco Beach Ocean Resort (All-suite luxury Gulf-front sanctuary for leadership boards)"
            ]
        },
        "card2": {
            "sub": "WATERFRONT CLUBS & GOLF VENUES",
            "title": "Executive Outings & Private Dinners",
            "items": [
                "Rookery at Marco & Hammock Bay Golf Clubs (JW Marriott championship golf clubhouses)",
                "Island Country Club (Exclusive private Marco Island dining & executive tournament banquets)",
                "Hideaway Beach Club (Gated beachfront clubhouse for VIP executive dinners)",
                "Rose Marina & Luxury Gulf Yacht Charters (Sunset cocktail strolling mentalism cruises)"
            ]
        },
        "card3": {
            "sub": "DISTINCTIVE ISLAND & COASTAL SPACES",
            "title": "Beachfront Banquets & VIP Receptions",
            "items": [
                "JW Marriott Sunset Beachfront Lawns & Tiki Pavilions (Bespoke dinners under the stars)",
                "Sale e Pepe Private Oceanfront Dining Room (Fine Italian executive board dinners)",
                "Ten Thousand Islands Private Eco-Luxury Excursions (VIP incentive networking add-ons)",
                "Nearby Naples Luxury Resorts & Cultural Venues (Seamless Southwest Florida coverage)"
            ]
        },
        "callout": {
            "sub": "PARADISE COAST TURNKEY DELIVERY",
            "title": "Direct RSW Airport Access • Effortless JW Marriott Production",
            "p": "Adrian Saint performs regularly across Southwest Florida's Paradise Coast. Arriving via Southwest Florida International Airport (RSW) with a zero-freight minimalist rider ensures smooth, reliable production for Marco Island resorts."
        },
        "faqs": [
            {
                "q": "CAN ADRIAN HEADLINE GENERAL SESSIONS AND GALAS AT JW MARRIOTT MARCO ISLAND?",
                "a": "Yes! Adrian regularly headlines national sales summits, President's Club dinners, and Calusa Ballroom awards galas at JW Marriott Marco Island Beach Resort for audiences from 50 to over 2,000."
            },
            {
                "q": "HOW DO TRAVEL LOGISTICS WORK FOR MARCO ISLAND CORPORATE EVENTS?",
                "a": "Adrian flies directly into Southwest Florida International Airport (RSW), just 50 minutes from Marco Island resorts. All travel is turnkey, with guaranteed early arrival prior to sound check."
            },
            {
                "q": "IS ADRIAN'S SHOW 100% CLEAN AND GREAT FOR INCENTIVE TRIPS WITH SPOUSES?",
                "a": "Yes, 100%! Adrian's interactive mind reading is clean, witty, and universally captivating, making it the standout evening highlight for executives, top producers, and their spouses."
            },
            {
                "q": "WHAT TECHNICAL AV SETUP DOES ADRIAN NEED AT JW MARRIOTT OR HILTON MARCO ISLAND?",
                "a": "Adrian requires only a wireless handheld or lavalier microphone connected to room audio. He coordinates directly with in-house Encore AV teams for quick, stress-free sound checks."
            },
            {
                "q": "DOES ADRIAN PERFORM STROLLING MIND READING ON THE BEACHFRONT TERRACES?",
                "a": "Yes! Adrian frequently kicks off Marco Island evenings with strolling close-up mentalism during sunset Gulf-front cocktail receptions before taking the stage after dinner."
            }
        ]
    },
    {
        "slug": "charleston",
        "city": "Charleston",
        "state": "SC",
        "state_region": "SC",
        "state_full": "South Carolina",
        "country": "US",
        "phone": "(833) 570-5966",
        "phone_clean": "18335705966",
        "phone_e164": "+18335705966",
        "badge": "📍 HISTORIC CHARLESTON & KIAWAH ISLAND RESORT COVERAGE",
        "h1": "Corporate Magician &amp; Mentalist in <span class=\"hero-headline-highlight\">Charleston</span> for Charleston Place Galas, Kiawah Retreats &amp; Summits",
        "subhead": "Delivering world-class psychological mentalism and interactive mind reading for executive retreats, corporate galas, and incentive summits across Historic Charleston and the South Carolina Lowcountry.",
        "lat": 32.7765,
        "lon": -79.9311,
        "areas": ["Charleston", "Charleston County", "Historic District", "Mount Pleasant", "Kiawah Island", "Daniel Island", "South Carolina Lowcountry"],
        "venue_h2": "Serving Charleston's Iconic Historic Hotels &amp; Five-Star Lowcountry Resorts",
        "venue_p": "Consistently voted America's #1 destination city, Charleston pairs timeless Historic District elegance at The Charleston Place and The Dewberry with Forbes Five-Star coastal retreats on Kiawah Island.",
        "card1": {
            "sub": "HISTORIC DISTRICT LUXURY HOTELS",
            "title": "Black-Tie Galas & Executive Summits",
            "items": [
                "The Charleston Place (Iconic Historic District landmark with Riviera Theater & Grand Ballroom)",
                "The Dewberry Charleston (Mid-century luxury icon with Citrus Club rooftop & Rivers Ballroom)",
                "Hotel Bennett (Grand luxury hotel on Marion Square with the ornate Crown Ballroom)",
                "The Spectator Hotel & Planters Inn (Intimate Five-Star luxury retreats in the French Quarter)"
            ]
        },
        "card2": {
            "sub": "COASTAL RESORTS & CONVENTION HUBS",
            "title": "Incentive Retreats & Regional Conferences",
            "items": [
                "The Sanctuary at Kiawah Island Golf Resort (Forbes Five-Star oceanfront sanctuary for C-suite summits)",
                "Charleston Area Convention Center (200,000+ sq ft convention & exhibition complex)",
                "Wild Dunes Resort on Isle of Palms (Sweetgrass Inn & coastal oceanfront conference pavilions)",
                "Charleston Harbor Resort & Marina (Waterfront venues with iconic skyline & Fort Sumter views)"
            ]
        },
        "card3": {
            "sub": "LOWCOUNTRY ESTATES & CULTURAL VENUES",
            "title": "Private Banquets & Historic Receptions",
            "items": [
                "The Gibbes Museum of Art (Beaux-Arts Rotunda & European garden corporate galas)",
                "William Aiken House & American Theater (King Street historic mansion & Art Deco showplace)",
                "South Carolina Aquarium Harbor Overlook (Dramatic waterfront corporate receptions)",
                "Lowndes Grove & Boone Hall Plantation (Iconic Lowcountry riverfront & oak-lined banquets)"
            ]
        },
        "callout": {
            "sub": "LOWCOUNTRY FLY-IN EXPERTISE",
            "title": "Direct Charleston International (CHS) Access • 20 Minutes to Downtown",
            "p": "Adrian Saint provides turnkey fly-in entertainment across Charleston and Kiawah Island. Flying directly into Charleston International Airport (CHS) just 20 minutes from King Street ensures effortless arrival and flawless production."
        },
        "faqs": [
            {
                "q": "CAN ADRIAN HEADLINE CORPORATE GALAS AT THE CHARLESTON PLACE OR THE SANCTUARY AT KIAWAH?",
                "a": "Yes! Adrian regularly headlines corporate awards banquets, Riviera Theater keynotes, and executive retreats at The Charleston Place, The Dewberry, Hotel Bennett, and The Sanctuary at Kiawah Island."
            },
            {
                "q": "HOW DO TRAVEL LOGISTICS WORK FOR CHARLESTON AND KIAWAH ISLAND EVENTS?",
                "a": "Adrian flies directly into Charleston International Airport (CHS), just 20 minutes from downtown Charleston and 45 minutes from Kiawah Island. All travel is turnkey and self-managed."
            },
            {
                "q": "IS ADRIAN'S PERFORMANCE 100% CLEAN AND SUITED FOR SOUTHERN HOSPITALITY GALAS?",
                "a": "Yes, 100%. Adrian's performance is polished, witty, and HR-approved, creating genuine astonishment and warm camaraderie without ever embarrassing guests."
            },
            {
                "q": "WHAT TECHNICAL REQUIREMENTS DOES ADRIAN HAVE AT HISTORIC CHARLESTON VENUES?",
                "a": "Adrian requires only a wireless handheld or lavalier microphone connected to house audio. His zero-prop footprint preserves the elegance of historic mansions and grand ballrooms."
            },
            {
                "q": "DOES ADRIAN PERFORM STROLLING MIND READING DURING LOWCOUNTRY COCKTAIL HOURS?",
                "a": "Yes! Adrian's strolling close-up mentalism is a favorite for courtyard cocktail receptions at William Aiken House, rooftop mixers at The Dewberry, and Kiawah oceanfront lawns."
            }
        ]
    },
    {
        "slug": "hilton-head",
        "city": "Hilton Head Island",
        "state": "SC",
        "state_region": "SC",
        "state_full": "South Carolina",
        "country": "US",
        "phone": "(833) 570-5966",
        "phone_clean": "18335705966",
        "phone_e164": "+18335705966",
        "badge": "📍 HILTON HEAD ISLAND & PALMETTO BLUFF RESORT COVERAGE",
        "h1": "Corporate Magician &amp; Mentalist in <span class=\"hero-headline-highlight\">Hilton Head Island</span> for Oceanfront Resorts, Golf Retreats &amp; Galas",
        "subhead": "Delivering interactive psychological mentalism and unforgettable mind reading for corporate conferences, championship golf retreats, and executive banquets across Hilton Head Island and Palmetto Bluff.",
        "lat": 32.2163,
        "lon": -80.7526,
        "areas": ["Hilton Head Island", "Beaufort County", "Sea Pines", "Palmetto Dunes", "Port Royal", "Bluffton", "South Carolina Lowcountry"],
        "venue_h2": "Serving Hilton Head's Premier Oceanfront Conference Resorts &amp; Lowcountry Sanctuaries",
        "venue_p": "With miles of Atlantic shoreline, legendary PGA Tour golf courses, and renowned conference resorts like The Westin, Omni, and Montage Palmetto Bluff, Hilton Head Island is a premier hub for executive retreats.",
        "card1": {
            "sub": "OCEANFRONT CONFERENCE RESORTS",
            "title": "Conventions & Beachfront Galas",
            "items": [
                "The Westin Hilton Head Island Resort & Spa (39,000+ sq ft meeting space & Grand Ocean Terrace)",
                "Omni Hilton Head Oceanfront Resort (20,000 sq ft Palmetto Dunes resort & oceanfront pavilions)",
                "Marriott Hilton Head Resort & Spa (41,000 sq ft oceanfront convention hub in Palmetto Dunes)",
                "Sonesta Resort Hilton Head Island (23,000 sq ft lush coastal resort & Santee Ballroom)"
            ]
        },
        "card2": {
            "sub": "GOLF RESORTS & ULTRA-LUXURY SANCTUARIES",
            "title": "Executive Retreats & Board Summits",
            "items": [
                "The Sea Pines Resort (The Inn & Club at Harbour Town — Forbes Four-Star PGA Tour golf retreat)",
                "Montage Palmetto Bluff in Bluffton (20,000-acre ultra-luxury riverfront sanctuary nearby)",
                "Harbour Town Clubhouse & Liberty Oak Pavilions (Iconic lighthouse views for awards dinners)",
                "Palmetto Dunes Oceanfront Golf & Executive Conference Venues"
            ]
        },
        "card3": {
            "sub": "PRIVATE CLUBS & LOWCOUNTRY VENUES",
            "title": "Private Banquets & Waterfront Receptions",
            "items": [
                "Coastal Discovery Museum at Honey Horn (Historic live-oak Lowcountry event pavilions)",
                "Wexford Plantation & Long Cove Club (Exclusive private clubhouses for VIP dinners)",
                "Hudson's & Skull Creek Waterfront Pavilions (Upscale Lowcountry receptions & mixers)",
                "Calibogue Sound Private Sunset Yacht Charters (Intimate strolling mind reading at sea)"
            ]
        },
        "callout": {
            "sub": "DUAL-AIRPORT ISLAND ACCESS",
            "title": "Direct Savannah/Hilton Head (SAV) & On-Island (HHH) Access",
            "p": "Adrian Saint flies directly into Savannah/Hilton Head International Airport (SAV) just 45 minutes from island resorts, or on-island via Hilton Head Airport (HHH). Turnkey travel ensures effortless timing and zero AV complications."
        },
        "faqs": [
            {
                "q": "CAN ADRIAN HEADLINE CONFERENCES AT THE WESTIN OR OMNI HILTON HEAD OCEANFRONT RESORT?",
                "a": "Yes! Adrian regularly headlines corporate awards banquets, sales conferences, and incentive dinners at The Westin, Omni, Marriott, Sea Pines, and Montage Palmetto Bluff."
            },
            {
                "q": "HOW DO TRAVEL LOGISTICS WORK FOR HILTON HEAD ISLAND AND PALMETTO BLUFF EVENTS?",
                "a": "Adrian flies directly into Savannah/Hilton Head International Airport (SAV) or Hilton Head Island Airport (HHH), providing smooth, punctual arrival with all travel logistics handled turnkey."
            },
            {
                "q": "IS ADRIAN'S SHOW 100% CLEAN AND SUITED FOR EXECUTIVE GOLF RETREATS?",
                "a": "Yes, 100%! Adrian's intelligent, HR-safe mind reading is a huge hit after a day on the golf course, energizing executive teams and spouses with jaw-dropping interactive entertainment."
            },
            {
                "q": "WHAT AUDIOVISUAL SETUP DOES ADRIAN REQUIRE AT HILTON HEAD RESORTS?",
                "a": "Adrian requires only a wireless handheld or lavalier microphone connected to room audio. For oceanfront terrace cocktail hours, strolling close-up mentalism requires zero AV."
            },
            {
                "q": "DOES ADRIAN PERFORM FOR SMALL EXECUTIVE BOARDS AT MONTAGE PALMETTO BLUFF OR SEA PINES?",
                "a": "Yes! In addition to large resort ballrooms, Adrian frequently performs intimate parlor-style mind reading shows for executive boards of 15 to 60 guests at Montage Palmetto Bluff and Harbour Town."
            }
        ]
    },
    {
        "slug": "sedona",
        "city": "Sedona",
        "state": "AZ",
        "state_region": "AZ",
        "state_full": "Arizona",
        "country": "US",
        "phone": "(833) 570-5966",
        "phone_clean": "18335705966",
        "phone_e164": "+18335705966",
        "badge": "📍 SEDONA RED ROCKS & LUXURY SANCTUARY COVERAGE",
        "h1": "Corporate Magician &amp; Mentalist in <span class=\"hero-headline-highlight\">Sedona</span> for Enchantment Retreats, Red Rock Galas &amp; Executive Summits",
        "subhead": "Delivering unforgettable psychological mentalism and interactive mind reading for executive offsites, luxury wellness summits, and intimate canyon banquets across Sedona and Northern Arizona.",
        "lat": 34.8697,
        "lon": -111.7610,
        "areas": ["Sedona", "Yavapai County", "Coconino County", "Boynton Canyon", "Oak Creek Canyon", "Village of Oak Creek", "Northern Arizona"],
        "venue_h2": "Serving Sedona's World-Renowned Red Rock Resorts &amp; Canyon Sanctuaries",
        "venue_p": "Surrounded by towering red rock monoliths, Sedona's ultra-luxury resorts—including Enchantment Resort and L'Auberge de Sedona—offer an inspiring, world-class setting for C-suite retreats and President's Club gatherings.",
        "card1": {
            "sub": "RED ROCK LUXURY RESORTS & SANCTUARIES",
            "title": "C-Suite Retreats & Canyon Galas",
            "items": [
                "Enchantment Resort (Iconic Boynton Canyon resort with Village Ballroom & red rock terraces)",
                "L'Auberge de Sedona (Creekside luxury sanctuary along Oak Creek for elite executive boards)",
                "Ambiente, A Landscape Hotel (Exclusive architectural Atrium sanctuary for VIP offsites)",
                "Hilton Sedona Resort at Bell Rock (21,000 sq ft conference center & championship desert golf)"
            ]
        },
        "card2": {
            "sub": "BOUTIQUE RESORTS & CONFERENCE CENTERS",
            "title": "Executive Summits & Leadership Offsites",
            "items": [
                "Amara Resort and Spa (Uptown Sedona creekside luxury hotel with panoramic red rock views)",
                "Poco Diablo Resort (Secluded 22-acre executive retreat & Canopy Ballroom)",
                "Los Abrigados Resort & Spa (Spacious Oak Creek conference halls & landscaped lawns)",
                "Sedona Golf Resort Event Pavilion (Scenic red rock tournament galas & receptions)"
            ]
        },
        "card3": {
            "sub": "DISTINCTIVE CANYON & CULTURAL VENUES",
            "title": "Private Banquets & Panoramic Galas",
            "items": [
                "Agave of Sedona (360-degree glass-walled panoramic red rock pavilion for private galas)",
                "Seven Canyons Golf Club (Private Boynton Canyon luxury clubhouse dinners)",
                "Sedona Performing Arts Center (750-seat acoustically pristine keynote theater)",
                "Tlaquepaque Arts & Shopping Village (Cobblestone courtyards & candlelit receptions)"
            ]
        },
        "callout": {
            "sub": "SOUTHWEST EXECUTIVE TRAVEL EASE",
            "title": "Direct Phoenix (PHX) & Flagstaff (FLG) Access • Minimalist Mountain Rider",
            "p": "Adrian Saint performs extensively throughout Arizona. With seamless flights into Phoenix Sky Harbor (PHX) or Flagstaff (FLG) and a zero-freight carry-on rider, delivering world-class entertainment to Boynton Canyon is effortless."
        },
        "faqs": [
            {
                "q": "CAN ADRIAN PERFORM AT ENCHANTMENT RESORT OR L'AUBERGE DE SEDONA?",
                "a": "Yes! Adrian regularly headlines executive dinners, leadership retreats, and red rock terrace receptions at Enchantment Resort, L'Auberge de Sedona, and Hilton Sedona at Bell Rock."
            },
            {
                "q": "HOW DO TRAVEL LOGISTICS WORK FOR SEDONA CANYON RETREATS?",
                "a": "Adrian flies into Phoenix Sky Harbor International Airport (PHX) or Flagstaff Pulliam Airport (FLG) and arrives early on-site with all travel logistics handled turnkey."
            },
            {
                "q": "IS ADRIAN'S MIND READING A GOOD FIT FOR INTIMATE EXECUTIVE BOARD RETREATS?",
                "a": "Yes! Sedona is famous for intimate 15- to 80-person C-suite retreats, and Adrian's interactive parlor mentalism creates extraordinary connection, conversation, and awe around the table."
            },
            {
                "q": "WHAT TECHNICAL SETUP DOES ADRIAN REQUIRE FOR OUTDOOR RED ROCK TERRACE EVENTS?",
                "a": "For intimate groups or strolling cocktail hours under the Sedona stars, Adrian requires zero AV. For larger ballroom or patio shows, a single wireless microphone and room audio are all that is needed."
            },
            {
                "q": "IS THE SHOW 100% CLEAN AND APPROPRIATE FOR CORPORATE LEADERSHIP AND SPOUSES?",
                "a": "Yes, 100%. Adrian's performance is completely clean, thoughtful, and HR-approved, resonating deeply with analytical executives and spouses alike."
            }
        ]
    },
    {
        "slug": "lake-tahoe",
        "city": "Lake Tahoe",
        "state": "NV/CA",
        "state_region": "NV",
        "state_full": "Nevada & California",
        "country": "US",
        "phone": "(833) 570-5966",
        "phone_clean": "18335705966",
        "phone_e164": "+18335705966",
        "badge": "📍 LAKE TAHOE NORTH & SOUTH SHORE RESORT COVERAGE",
        "h1": "Corporate Magician &amp; Mentalist in <span class=\"hero-headline-highlight\">Lake Tahoe</span> for Alpine Resort Summits, Incentive Trips &amp; Galas",
        "subhead": "Delivering unforgettable psychological mentalism and interactive mind reading for lakefront executive retreats, ski-season conferences, and awards banquets across North and South Lake Tahoe.",
        "lat": 39.0968,
        "lon": -120.0324,
        "areas": ["Lake Tahoe", "Incline Village", "North Lake Tahoe", "South Lake Tahoe", "Truckee", "Stateline", "Washoe County", "Placer County"],
        "venue_h2": "Serving Lake Tahoe's Five-Star Alpine Resorts &amp; Lakefront Convention Venues",
        "venue_p": "Spanning the crystal-clear waters of Nevada and California, Lake Tahoe blends premier mountain-lake resorts like Hyatt Regency Incline Village and The Ritz-Carlton with state-of-the-art South Shore convention venues.",
        "card1": {
            "sub": "LAKEFRONT & FIVE-STAR ALPINE RESORTS",
            "title": "Executive Retreats & Incentive Galas",
            "items": [
                "Hyatt Regency Lake Tahoe Resort, Spa and Casino (Incline Village private beach & 50,000 sq ft event space)",
                "The Ritz-Carlton, Lake Tahoe (Mid-mountain five-star sanctuary at Northstar with 15,000+ sq ft space)",
                "Edgewood Tahoe Resort (South Lake Tahoe luxury lakefront golf resort & Tahoe Ballroom)",
                "Everline Resort & Spa in Olympic Valley (47,000 sq ft alpine conference & golf resort)"
            ]
        },
        "card2": {
            "sub": "SOUTH SHORE CONVENTION & CASINO RESORTS",
            "title": "Large-Scale Conferences & Trade Summits",
            "items": [
                "Tahoe Blue Event Center in Stateline (Modern 143,000 sq ft convention & corporate rally arena)",
                "Harrah's Lake Tahoe & Harveys Lake Tahoe (South Shore Special Events Center & showrooms)",
                "Caesars Republic Lake Tahoe (Luxury casino resort ballrooms & VIP executive suites)",
                "Palisades Tahoe Alpine Conference Facilities (Scenic mountain village summits)"
            ]
        },
        "card3": {
            "sub": "PRIVATE ALPINE CLUBS & WATERFRONT ESTATES",
            "title": "C-Suite Dinners & Scenic Receptions",
            "items": [
                "Martis Camp & Lahontan Golf Club in Truckee (Ultra-exclusive private clubhouses for C-suite boards)",
                "Thunderbird Lodge Historic Estate (Private Lake Tahoe castle receptions & VIP dinners)",
                "West Shore Cafe & Inn (Iconic lakefront pier receptions overlooking Emerald Bay)",
                "Private Lake Tahoe Luxury Yacht Charters (Close-up mind reading on alpine waters)"
            ]
        },
        "callout": {
            "sub": "SIERRA NEVADA TURNKEY TRAVEL",
            "title": "Direct Reno-Tahoe (RNO) Access • 45 Minutes to Incline Village & Northstar",
            "p": "Based on the West Coast, Adrian Saint travels seamlessly into Reno-Tahoe International Airport (RNO) just 45 minutes from premier North and South Shore resorts. Zero heavy gear guarantees smooth year-round mountain logistics."
        },
        "faqs": [
            {
                "q": "CAN ADRIAN HEADLINE CONFERENCES AT HYATT REGENCY LAKE TAHOE OR THE RITZ-CARLTON?",
                "a": "Yes! Adrian regularly headlines corporate general sessions, winter ski incentive galas, and summer lakefront banquets at Hyatt Regency Incline Village, The Ritz-Carlton Lake Tahoe, and Edgewood Tahoe."
            },
            {
                "q": "HOW DO TRAVEL LOGISTICS WORK FOR NORTH AND SOUTH LAKE TAHOE EVENTS?",
                "a": "Adrian flies directly into Reno-Tahoe International Airport (RNO), 45 minutes from Northstar, Incline Village, and Stateline. All travel is self-contained with early arrival built in for winter weather."
            },
            {
                "q": "IS ADRIAN'S SHOW 100% CLEAN AND SUITED FOR TECH & SILICON VALLEY RETREATS?",
                "a": "Yes, 100%! Lake Tahoe is a top destination for Bay Area tech and finance offsites, and Adrian's sharp, psychological mind reading captivates analytical audiences while staying 100% HR-approved."
            },
            {
                "q": "WHAT TECHNICAL REQUIREMENTS DOES ADRIAN HAVE AT LAKE TAHOE RESORTS?",
                "a": "Adrian requires only a wireless handheld or lavalier microphone connected to house sound. His minimalist footprint integrates seamlessly with resort AV teams."
            },
            {
                "q": "DOES ADRIAN PERFORM STROLLING MENTALISM FOR APRES-SKI OR LAKESIDE COCKTAIL MIXERS?",
                "a": "Yes! Adrian's strolling close-up mind reading is an extraordinary icebreaker for fireside après-ski receptions, private beach barbecues, and VIP yacht charters."
            }
        ]
    },
    {
        "slug": "park-city",
        "city": "Park City",
        "state": "UT",
        "state_region": "UT",
        "state_full": "Utah",
        "country": "US",
        "phone": "(833) 570-5966",
        "phone_clean": "18335705966",
        "phone_e164": "+18335705966",
        "badge": "📍 PARK CITY & DEER VALLEY LUXURY RESORT COVERAGE",
        "h1": "Corporate Magician &amp; Mentalist in <span class=\"hero-headline-highlight\">Park City</span> for Deer Valley Retreats, Ski Summits &amp; Executive Galas",
        "subhead": "Delivering world-class psychological mentalism and interactive mind reading for Five-Star mountain retreats, investor summits, and incentive galas across Park City and Deer Valley.",
        "lat": 40.6461,
        "lon": -111.4980,
        "areas": ["Park City", "Summit County", "Deer Valley", "Canyons Village", "Historic Main Street", "Heber Valley", "Wasatch Back"],
        "venue_h2": "Serving Park City's Five-Star Deer Valley Resorts &amp; Mountain Event Destinations",
        "venue_p": "Just 35 minutes from Salt Lake City International Airport, Park City is North America's most accessible ultra-luxury mountain destination—home to Montage Deer Valley, The St. Regis, and Stein Eriksen Lodge.",
        "card1": {
            "sub": "FIVE-STAR DEER VALLEY & ALPINE RESORTS",
            "title": "Ultra-Luxury Retreats & Investor Summits",
            "items": [
                "Montage Deer Valley (Forbes Five-Star alpine resort with 55,000+ sq ft of indoor/outdoor event space)",
                "The St. Regis Deer Valley (Funicular-access luxury sanctuary with Astor Ballroom & Mountain Terrace)",
                "Stein Eriksen Lodge Deer Valley (Legendary Forbes Five-Star ski-in resort & Olympic Conference Center)",
                "Pendry Park City (Contemporary Canyons Village luxury resort with 7,000 sq ft Pendry Ballroom)"
            ]
        },
        "card2": {
            "sub": "MOUNTAIN VILLAGE CONFERENCE RESORTS",
            "title": "Corporate Conferences & Leadership Offsites",
            "items": [
                "Waldorf Astoria Park City (Luxury slope-side sanctuary for C-suite board retreats)",
                "The Chateaux Deer Valley (20,000 sq ft conference hotel affiliated with Stein Eriksen Lodge)",
                "Grand Summit Hotel at Canyons Village (15,000 sq ft mountain village convention hub)",
                "Hotel Park City, Autograph Collection & Park City Marriott (Executive suites & ballrooms)"
            ]
        },
        "card3": {
            "sub": "SUNDANCE & PRIVATE RANCH VENUES",
            "title": "Private Banquets & Iconic Gatherings",
            "items": [
                "The Lodge at Blue Sky, Auberge Resorts Collection (3,500-acre private mountain ranch sanctuary)",
                "High West Distillery at Blue Sky Ranch (Upscale western luxury corporate dinners & tastings)",
                "Egyptian Theatre on Historic Main Street (Iconic Sundance landmark for VIP keynote shows)",
                "Silver Lake Lodge & Snow Park Lodge at Deer Valley (Panoramic mountain banquet halls)"
            ]
        },
        "callout": {
            "sub": "EFFORTLESS WASATCH MOUNTAIN ACCESS",
            "title": "35 Minutes From Salt Lake City (SLC) • Zero Mountain Pass Hassles",
            "p": "With direct nonstop flights into Salt Lake City International Airport (SLC) and a quick 35-minute interstate transfer straight to Deer Valley, Adrian Saint delivers punctual, turnkey mountain entertainment year-round."
        },
        "faqs": [
            {
                "q": "CAN ADRIAN HEADLINE EXECUTIVE GALAS AT MONTAGE DEER VALLEY OR THE ST. REGIS?",
                "a": "Yes! Adrian frequently headlines investor summits, private equity retreats, and awards banquets at Montage Deer Valley, The St. Regis Deer Valley, Stein Eriksen Lodge, and Pendry Park City."
            },
            {
                "q": "HOW DO TRAVEL LOGISTICS WORK FOR PARK CITY AND DEER VALLEY EVENTS?",
                "a": "Adrian flies directly into Salt Lake City International Airport (SLC), just 35 minutes from Park City via I-80. All travel is turnkey with carry-on production gear and zero freight delays."
            },
            {
                "q": "IS ADRIAN'S SHOW SUITED FOR PRIVATE EQUITY, VENTURE CAPITAL & TECH SUMMITS?",
                "a": "Absolutely. Park City hosts elite finance and tech gatherings, and Adrian's intelligent, 100% clean psychological mind reading engages sharp analytical executives effortlessly."
            },
            {
                "q": "WHAT AUDIOVISUAL SETUP DOES ADRIAN REQUIRE AT DEER VALLEY RESORTS?",
                "a": "Adrian requires only a wireless handheld or lavalier microphone connected to room audio. He coordinates smoothly with in-house resort AV teams for quick, discreet setup."
            },
            {
                "q": "DOES ADRIAN PERFORM FOR PRIVATE DINNERS ON MAIN STREET OR AT BLUE SKY RANCH?",
                "a": "Yes! Adrian excels at intimate strolling mentalism and private after-dinner shows for 15 to 80 guests at The Lodge at Blue Sky, High West Distillery, and Main Street buyouts."
            }
        ]
    },
    {
        "slug": "vail",
        "city": "Vail",
        "state": "CO",
        "state_region": "CO",
        "state_full": "Colorado",
        "country": "US",
        "phone": "(833) 570-5966",
        "phone_clean": "18335705966",
        "phone_e164": "+18335705966",
        "badge": "📍 VAIL VALLEY & BEAVER CREEK LUXURY RESORT COVERAGE",
        "h1": "Corporate Magician &amp; Mentalist in <span class=\"hero-headline-highlight\">Vail</span> for Four Seasons Retreats, Beaver Creek Summits &amp; Galas",
        "subhead": "Delivering unforgettable psychological entertainment and interactive mind reading for executive retreats, winter incentive trips, and mountain galas across Vail Village and Beaver Creek.",
        "lat": 39.6403,
        "lon": -106.3742,
        "areas": ["Vail", "Eagle County", "Vail Village", "Lionshead Village", "Beaver Creek", "Avon", "Colorado Rockies"],
        "venue_h2": "Serving Vail Village's Five-Star Resorts &amp; Beaver Creek Executive Sanctuaries",
        "venue_p": "Styled after classic European alpine villages, Vail and Beaver Creek offer unmatched five-star mountain hospitality at Four Seasons Resort Vail, The Sebastian, and Park Hyatt Beaver Creek.",
        "card1": {
            "sub": "FIVE-STAR VAIL VILLAGE RESORTS",
            "title": "Luxury Retreats & Alpine Galas",
            "items": [
                "Four Seasons Resort and Residences Vail (Iconic Vail Village sanctuary with Bighorn Ballroom)",
                "The Sebastian – Vail (Forbes-rated boutique alpine resort with stylish executive lounges)",
                "Grand Hyatt Vail (Creekside Cascade Village resort with 40,000+ sq ft of conference space)",
                "Sonnenalp Hotel (Bavarian luxury landmark in Vail Village for intimate C-suite retreats)"
            ]
        },
        "card2": {
            "sub": "BEAVER CREEK & LIONSHEAD CONFERENCE HUBS",
            "title": "Corporate Conferences & Incentive Summits",
            "items": [
                "The Hythe, a Luxury Collection Resort, Vail (29,000 sq ft Lionshead Village flagship resort)",
                "Park Hyatt Beaver Creek Resort and Spa (20,000 sq ft ski-in luxury conference resort)",
                "The Ritz-Carlton, Bachelor Gulch (Secluded mountainside timber lodge for elite boards)",
                "The Arrabelle at Vail Square (European-inspired luxury hotel & Grand Ballroom)"
            ]
        },
        "card3": {
            "sub": "MOUNTAINTOP & ICONIC ROCKIES VENUES",
            "title": "Gondola-Access Galas & Private Dinners",
            "items": [
                "Game Creek Club & The 10th on Vail Mountain (Gondola-access fine dining executive galas)",
                "Donovan Pavilion (Architectural timber-and-glass event hall along Gore Creek)",
                "Vail Golf & Nordic Clubhouse (Panoramic Gore Range banquet halls & terrace mixers)",
                "Betty Ford Alpine Gardens & Gerald R. Ford Amphitheater (Summer corporate receptions)"
            ]
        },
        "callout": {
            "sub": "COLORADO ROCKIES TURNKEY MOBILITY",
            "title": "Direct Eagle County (EGE) & Denver (DEN) Access • Zero Freight Rider",
            "p": "Adrian Saint regularly headlines corporate retreats across Colorado's Rocky Mountains. Arriving via Eagle County Regional Airport (EGE, 35 minutes away) or Denver International Airport (DEN) with carry-on production ensures seamless execution."
        },
        "faqs": [
            {
                "q": "CAN ADRIAN HEADLINE RETREATS AT FOUR SEASONS VAIL, THE SEBASTIAN, OR PARK HYATT BEAVER CREEK?",
                "a": "Yes! Adrian regularly headlines corporate leadership retreats, ski incentive galas, and private executive dinners at Four Seasons Resort Vail, The Sebastian, The Hythe, and Park Hyatt Beaver Creek."
            },
            {
                "q": "HOW DO TRAVEL LOGISTICS WORK FOR VAIL AND BEAVER CREEK EVENTS?",
                "a": "Adrian flies directly into Eagle County Regional Airport (EGE), 35 minutes west of Vail, or Denver International Airport (DEN) with early arrival scheduled to eliminate any mountain weather risk."
            },
            {
                "q": "CAN ADRIAN PERFORM AT GONDOLA-ACCESS MOUNTAINTOP VENUES LIKE GAME CREEK CLUB?",
                "a": "Yes! Because Adrian performs pure psychological mentalism with zero bulky props, riding the gondola up to Game Creek Club or The 10th for an intimate VIP evening is completely effortless."
            },
            {
                "q": "IS ADRIAN'S SHOW 100% CLEAN AND SUITED FOR EXECUTIVE INCENTIVE GROUPS?",
                "a": "Yes, 100%. Adrian's performance is polished, witty, and HR-approved—delivering unforgettable amazement for executives and spouses without ever embarrassing anyone."
            },
            {
                "q": "WHAT AUDIOVISUAL SETUP DOES ADRIAN REQUIRE AT VAIL LUXURY HOTELS?",
                "a": "Adrian requires only a wireless handheld or lavalier microphone connected to room audio. For fireside après-ski cocktail hours, strolling mentalism requires zero AV equipment."
            }
        ]
    },
    {
        "slug": "aspen",
        "city": "Aspen",
        "state": "CO",
        "state_region": "CO",
        "state_full": "Colorado",
        "country": "US",
        "phone": "(833) 570-5966",
        "phone_clean": "18335705966",
        "phone_e164": "+18335705966",
        "badge": "📍 ASPEN & SNOWMASS ULTRA-LUXURY RESORT COVERAGE",
        "h1": "Corporate Magician &amp; Mentalist in <span class=\"hero-headline-highlight\">Aspen</span> for St. Regis Galas, C-Suite Retreats &amp; Executive Forums",
        "subhead": "Delivering extraordinary psychological mentalism and interactive mind reading for C-suite board retreats, private wealth summits, and Five-Star alpine galas across Aspen and Snowmass.",
        "lat": 39.1911,
        "lon": -106.8175,
        "areas": ["Aspen", "Pitkin County", "Snowmass Village", "Downtown Aspen", "Red Mountain", "Roaring Fork Valley", "Colorado Rockies"],
        "venue_h2": "Serving Aspen's Five-Star Mountain Landmarks &amp; Snowmass Conference Resorts",
        "venue_p": "Synonymous with global leadership forums and ultra-luxury alpine hospitality, Aspen features legendary properties—from The St. Regis and The Little Nell to the Aspen Institute campus and Snowmass resorts.",
        "card1": {
            "sub": "ULTRA-LUXURY ASPEN FLAGSHIP RESORTS",
            "title": "Five-Star Retreats & Executive Galas",
            "items": [
                "The St. Regis Aspen Resort (Iconic 5-star landmark at Aspen Mountain base with 29,000 sq ft event space)",
                "The Little Nell (Aspen's only Five-Star, Five-Diamond ski-in/ski-out hotel & wine cellar dinners)",
                "Hotel Jerome, Auberge Resorts Collection (Historic 1889 luxury icon with Grand Ballroom)",
                "W Aspen & MOLLIE Aspen (Contemporary boutique luxury hotels for creative executive summits)"
            ]
        },
        "card2": {
            "sub": "SNOWMASS & FORUM CONFERENCE CENTERS",
            "title": "Leadership Forums & Alpine Conferences",
            "items": [
                "Aspen Meadows Resort (Home of the Aspen Institute — Bauhaus campus & Paepcke Auditorium)",
                "Viceroy Snowmass (Luxury slope-side resort with 12,000 sq ft of contemporary event space)",
                "Viewline Resort Snowmass, Autograph Collection (25,000+ sq ft mountain convention hub)",
                "Limelight Hotel Aspen & Snowmass (Vibrant downtown corporate gathering venues)"
            ]
        },
        "card3": {
            "sub": "MOUNTAINTOP & CULTURAL LANDMARKS",
            "title": "Private Estates & Architectural Galas",
            "items": [
                "Sundeck & ASPENX Mountain Club (11,212-ft gondola-access VIP dinners atop Aspen Mountain)",
                "Aspen Art Museum (Shigeru Ban architectural gem & rooftop sculpture garden galas)",
                "Wheeler Opera House (Historic 1889 Victorian theater for flagship keynote performances)",
                "Caribou Club & Private Red Mountain Estates (Ultra-exclusive C-suite board dinners)"
            ]
        },
        "callout": {
            "sub": "ASPEN TURNKEY FLY-IN EXCELLENCE",
            "title": "Direct Aspen/Pitkin County (ASE) Access • 10 Minutes to Downtown",
            "p": "Flying directly into Aspen/Pitkin County Airport (ASE) just 10 minutes from Downtown Aspen—with zero oversized cargo—Adrian Saint provides effortless, white-glove mentalism for Aspen's most discerning corporate hosts."
        },
        "faqs": [
            {
                "q": "CAN ADRIAN HEADLINE EVENTS AT THE ST. REGIS ASPEN, THE LITTLE NELL, OR HOTEL JEROME?",
                "a": "Yes! Adrian regularly performs for ultra-luxury C-suite retreats, private wealth forums, and awards galas at The St. Regis Aspen, The Little Nell, Hotel Jerome, and Viceroy Snowmass."
            },
            {
                "q": "HOW DO TRAVEL LOGISTICS WORK FOR ASPEN AND SNOWMASS EVENTS?",
                "a": "Adrian flies directly into Aspen/Pitkin County Airport (ASE), 10 minutes from downtown, with backup routing through Eagle (EGE) and Denver (DEN) for guaranteed winter reliability."
            },
            {
                "q": "IS ADRIAN'S MENTALISM TAILORED FOR HIGH-NET-WORTH AND INTELLECTUAL AUDIENCES?",
                "a": "Yes! Aspen attracts global leaders, founders, and investors. Adrian's modern, 100% clean psychological mind reading stimulates sharp minds without ever feeling cheesy or intrusive."
            },
            {
                "q": "CAN ADRIAN PERFORM AT PRIVATE RED MOUNTAIN ESTATES OR ATOP ASPEN MOUNTAIN?",
                "a": "Absolutely! Because Adrian requires zero bulky props or heavy staging, he performs seamlessly in private Red Mountain homes, The Caribou Club, or at 11,212 feet at the Sundeck."
            },
            {
                "q": "WHAT TECHNICAL REQUIREMENTS DOES ADRIAN HAVE FOR BALLROOM SHOWS IN ASPEN?",
                "a": "For ballroom keynotes and general sessions, Adrian requires only a wireless handheld or lavalier microphone connected to room audio."
            }
        ]
    },
    {
        "slug": "asheville",
        "city": "Asheville",
        "state": "NC",
        "state_region": "NC",
        "state_full": "North Carolina",
        "country": "US",
        "phone": "(833) 570-5966",
        "phone_clean": "18335705966",
        "phone_e164": "+18335705966",
        "badge": "📍 ASHEVILLE & OMNI GROVE PARK INN COVERAGE",
        "h1": "Corporate Magician &amp; Mentalist in <span class=\"hero-headline-highlight\">Asheville</span> for Omni Grove Park Summits, Biltmore Galas &amp; Retreats",
        "subhead": "Delivering unforgettable psychological entertainment and interactive mind reading for executive retreats, Blue Ridge conferences, and historic estate banquets across Asheville and Western North Carolina.",
        "lat": 35.5951,
        "lon": -82.5515,
        "areas": ["Asheville", "Buncombe County", "Downtown Asheville", "Biltmore Village", "Blue Ridge Mountains", "Hendersonville", "Western North Carolina"],
        "venue_h2": "Serving Asheville's Historic Mountain Resorts &amp; Biltmore Estate Venues",
        "venue_p": "Nestled in the scenic Blue Ridge Mountains, Asheville pairs legendary resort hospitality at The Omni Grove Park Inn with the unmatched grandeur of Biltmore Estate and vibrant downtown boutique hotels.",
        "card1": {
            "sub": "ICONIC MOUNTAIN RESORTS & ESTATES",
            "title": "Flagship Retreats & Estate Galas",
            "items": [
                "The Omni Grove Park Inn (Historic 1913 Blue Ridge landmark with 58,000+ sq ft & Grand Ballroom)",
                "The Inn on Biltmore Estate (Four-Star luxury sanctuary on America's Largest Home estate)",
                "Grand Bohemian Hotel Asheville, Autograph Collection (Tudor luxury hotel in Biltmore Village)",
                "The Foundry Hotel, Curio Collection by Hilton (Historic restored steel foundry boutique retreat)"
            ]
        },
        "card2": {
            "sub": "DOWNTOWN CONFERENCE & LUXURY HOTELS",
            "title": "Executive Summits & Corporate Banquets",
            "items": [
                "Renaissance Asheville Downtown Hotel (25,000+ sq ft conference hub in the heart of downtown)",
                "Embassy Suites by Hilton Asheville Downtown (Modern convention hotel with Blue Ridge views)",
                "Kimpton Hotel Arras (Sleek downtown tower for upscale executive board retreats)",
                "Crowne Plaza Resort Asheville (34,000 sq ft Expo Center & wooded mountain campus)"
            ]
        },
        "card3": {
            "sub": "BLUE RIDGE LANDMARK EVENT VENUES",
            "title": "Private Banquets & Cultural Receptions",
            "items": [
                "Biltmore Estate Lioncrest & Deerpark (Grand historic estate banquet halls & winery dinners)",
                "Harrah's Cherokee Center – Asheville (Large-scale regional convention center & auditorium)",
                "The North Carolina Arboretum (Scenic Blue Ridge botanical gardens & Baker Exhibit Center)",
                "Sierra Nevada Brewing Co. Mills River Estate (Architectural private banquet halls & gardens)"
            ]
        },
        "callout": {
            "sub": "BLUE RIDGE TURNKEY FLY-IN DELIVERY",
            "title": "Direct Asheville Regional (AVL) Access • 20 Minutes to Grove Park Inn",
            "p": "Adrian Saint flies directly into Asheville Regional Airport (AVL) just 20 minutes from downtown and The Omni Grove Park Inn, with Greenville-Spartanburg (GSP) nearby for effortless, punctual delivery."
        },
        "faqs": [
            {
                "q": "CAN ADRIAN HEADLINE CONFERENCES AT THE OMNI GROVE PARK INN OR BILTMORE ESTATE?",
                "a": "Yes! Adrian regularly headlines corporate awards banquets, leadership retreats, and annual conferences at The Omni Grove Park Inn, The Inn on Biltmore Estate, and Lioncrest for groups from 30 to over 1,500."
            },
            {
                "q": "HOW DO TRAVEL LOGISTICS WORK FOR ASHEVILLE CORPORATE RETREATS?",
                "a": "Adrian flies directly into Asheville Regional Airport (AVL), just 20 minutes from downtown and Biltmore Village, or Greenville-Spartanburg (GSP). All travel is turnkey and self-managed."
            },
            {
                "q": "IS ADRIAN'S SHOW 100% CLEAN AND HR-APPROVED FOR CORPORATE GROUPS?",
                "a": "Yes, 100%. Adrian's corporate show is completely clean, engaging, and respectful—making your event committee look brilliant without ever embarrassing a volunteer."
            },
            {
                "q": "WHAT TECHNICAL REQUIREMENTS DOES ADRIAN HAVE AT OMNI GROVE PARK INN?",
                "a": "Adrian requires only a wireless handheld or lavalier microphone connected to house sound. He coordinates smoothly with resort AV teams for quick sound checks."
            },
            {
                "q": "DOES ADRIAN PERFORM STROLLING MIND READING ON SUNSET TERRACES IN ASHEVILLE?",
                "a": "Yes! Adrian's strolling close-up mentalism is an unforgettable icebreaker for Blue Ridge sunset cocktail receptions at the Grove Park Inn terrace and Biltmore Estate gardens."
            }
        ]
    },
    {
        "slug": "williamsburg",
        "city": "Williamsburg",
        "state": "VA",
        "state_region": "VA",
        "state_full": "Virginia",
        "country": "US",
        "phone": "(833) 570-5966",
        "phone_clean": "18335705966",
        "phone_e164": "+18335705966",
        "badge": "📍 WILLIAMSBURG & KINGSMILL RESORT COVERAGE",
        "h1": "Corporate Magician &amp; Mentalist in <span class=\"hero-headline-highlight\">Williamsburg</span> for Kingsmill Retreats, Colonial Galas &amp; Summits",
        "subhead": "Delivering sophisticated psychological mentalism and interactive mind reading for association conventions, championship golf retreats, and executive banquets across Williamsburg and Virginia's Historic Triangle.",
        "lat": 37.2707,
        "lon": -76.7075,
        "areas": ["Williamsburg", "James City County", "Colonial Williamsburg", "Yorktown", "Jamestown", "Newport News", "Historic Triangle Virginia"],
        "venue_h2": "Serving Williamsburg's Premier Resort Campuses &amp; Historic Triangle Venues",
        "venue_p": "Combining riverfront championship golf at Kingsmill Resort with the timeless elegance of Colonial Williamsburg's Five-Star hospitality, Williamsburg is a top Mid-Atlantic destination for association summits and corporate retreats.",
        "card1": {
            "sub": "PREMIER RESORT & CONFERENCE CAMPUSES",
            "title": "Association Summits & Golf Retreats",
            "items": [
                "Kingsmill Resort (AAA Four-Diamond James River resort with 16,000 sq ft conference center & PGA golf)",
                "Williamsburg Lodge, Autograph Collection (45,000 sq ft premier Colonial Williamsburg conference hub)",
                "The Williamsburg Inn (Forbes Five-Star Regency-style landmark for prestigious executive retreats)",
                "Williamsburg Woodlands Hotel & Conference Center (Spacious regional corporate meeting halls)"
            ]
        },
        "card2": {
            "sub": "EXECUTIVE HOTELS & GOLF CLUBHOUSES",
            "title": "Corporate Conferences & Awards Dinners",
            "items": [
                "DoubleTree by Hilton Hotel Williamsburg (48,000 sq ft convention hotel & presidential ballroom)",
                "Fort Magruder Historic Williamsburg (26,000 sq ft conference center near Historic Triangle)",
                "Ford's Colony Country Club (54-hole luxury golf community with grand banquet pavilions)",
                "Golden Horseshoe Golf Club Clubhouse (Iconic Robert Trent Jones Sr. retreat dining)"
            ]
        },
        "card3": {
            "sub": "HISTORIC TRIANGLE CULTURAL VENUES",
            "title": "Private Banquets & Vineyard Galas",
            "items": [
                "Colonial Williamsburg Historic Taverns & Pavilions (Unforgettable private executive receptions)",
                "Williamsburg Winery at Wessex Hundred (300-acre vineyard estate for VIP corporate dinners)",
                "Jamestown Settlement & American Revolution Museum at Yorktown (Dramatic museum gallery galas)",
                "William & Mary Alumni House & Sadler Center (Academic & executive leadership summit halls)"
            ]
        },
        "callout": {
            "sub": "MID-ATLANTIC TRI-AIRPORT ACCESS",
            "title": "Convenient Richmond (RIC), Norfolk (ORF) & PHF Airport Access",
            "p": "Ideally positioned within 25 to 45 minutes of Newport News/Williamsburg (PHF), Richmond (RIC), and Norfolk (ORF) airports, Williamsburg is seamlessly accessible for turnkey fly-in corporate entertainment."
        },
        "faqs": [
            {
                "q": "CAN ADRIAN HEADLINE CONFERENCES AT KINGSMILL RESORT OR WILLIAMSBURG LODGE?",
                "a": "Yes! Adrian regularly headlines association conferences, executive golf retreats, and annual awards banquets at Kingsmill Resort, Williamsburg Lodge, and The Williamsburg Inn for audiences from 30 to over 1,500."
            },
            {
                "q": "HOW DO TRAVEL LOGISTICS WORK FOR WILLIAMSBURG CORPORATE EVENTS?",
                "a": "Adrian flies into Richmond International (RIC), Norfolk International (ORF), or Newport News/Williamsburg (PHF), all within 25 to 45 minutes of Kingsmill and Colonial Williamsburg."
            },
            {
                "q": "IS ADRIAN'S PERFORMANCE 100% CLEAN AND SUITED FOR ASSOCIATION & EXECUTIVE GROUPS?",
                "a": "Yes, 100%. Adrian's corporate show is completely clean, intelligent, and HR-safe, captivating association leaders, government contractors, and corporate executives respectfully."
            },
            {
                "q": "WHAT TECHNICAL SETUP DOES ADRIAN REQUIRE AT KINGSMILL OR WILLIAMSBURG INN?",
                "a": "Adrian requires only a wireless handheld or lavalier microphone connected to room audio. His minimalist rider allows rapid sound checks with hotel AV teams."
            },
            {
                "q": "DOES ADRIAN PERFORM STROLLING MIND READING FOR RIVERFRONT OR WINERY RECEPTIONS?",
                "a": "Yes! Adrian's strolling close-up mentalism is a favorite for James River sunset cocktail hours at Kingsmill and private corporate dinners at The Williamsburg Winery."
            }
        ]
    }
]

created_files = []

for c in GROUP_C_CITIES:
    slug = c["slug"]
    city = c["city"]
    state = c["state"]
    state_region = c["state_region"]
    state_full = c["state_full"]
    country = c["country"]
    phone = c["phone"]
    phone_clean = c["phone_clean"]
    phone_e164 = c["phone_e164"]
    canon_url = f"https://adriansaintmentalist.com/corporate-magician-{slug}"
    title_str = f"Corporate Magician &amp; Mentalist {city}, {state} | Adrian Saint"
    desc_str = f"Book the top Corporate Magician & Mentalist in {city}, {state}. Adrian Saint delivers interactive mind reading for luxury resort retreats, leadership summits, and executive galas."
    keywords_str = f"Corporate Magician & Mentalist {city}, {city} Corporate Entertainment, Mind Reader {city} {state}, {c['areas'][1]} Magician, {state_full} Corporate Magician, Adrian Saint Mentalist"

    html = base_html

    # 1. Title and Canonical
    html = sub_once(r'<title>.*?</title>', f'<title>{title_str}</title>', html, label=f'{slug} title')
    html = sub_once(r'<link rel="canonical" href="[^"]*"', f'<link rel="canonical" href="{canon_url}"', html, label=f'{slug} canonical')

    # 2. Meta Tags
    html = sub_once(r'<meta property="og:url" content="[^"]*"', f'<meta property="og:url" content="{canon_url}"', html, label=f'{slug} og:url')
    html = sub_once(r'<meta property="og:title" content="[^"]*"', f'<meta property="og:title" content="{title_str}"', html, label=f'{slug} og:title')
    html = sub_once(r'<meta property="og:description" content="[^"]*"', f'<meta property="og:description" content="{desc_str}"', html, label=f'{slug} og:description')
    html = sub_once(r'<meta name="twitter:title" content="[^"]*"', f'<meta name="twitter:title" content="{title_str}"', html, label=f'{slug} twitter:title')
    html = sub_once(r'<meta name="twitter:description" content="[^"]*"', f'<meta name="twitter:description" content="{desc_str}"', html, label=f'{slug} twitter:description')
    html = sub_once(r'<meta name="description" content="[^"]*"', f'<meta name="description" content="{desc_str}"', html, label=f'{slug} description')
    html = sub_once(r'<meta name="keywords" content="[^"]*"', f'<meta name="keywords" content="{keywords_str}"', html, label=f'{slug} keywords')

    # 3. JSON-LD Schema (All 10 FAQ items use valid acceptedAnswer format)
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
    standard_faqs = [
        (
            "HOW FAR IN ADVANCE SHOULD WE HOLD OUR EVENT DATE?",
            "Peak dates during spring and fall convention seasons (March through June, September through November) and December holiday banquets book 6 to 12 months in advance. Early holds are recommended to lock in date exclusivity."
        ),
        (
            "WHAT TYPES OF CORPORATE AUDIENCES ENJOY ADRIAN'S SHOW THE MOST?",
            "Adrian's performance is designed specifically for sophisticated adult corporate groups including tech summits, finance and insurance conferences, healthcare and pharma banquets, executive retreats, and national franchise meetings."
        ),
        (
            "WHAT IS THE DIFFERENCE BETWEEN CLOSE-UP STROLLING AND THE STAGE SHOW?",
            "Strolling mind reading takes place during cocktail hours or networking mixers where Adrian moves among small groups, performing intimate miracles inches away. The stage show is a unified theatrical presentation for the entire room from 30 to 60 minutes."
        ),
        (
            "CAN ADRIAN CUSTOMIZE HIS ROUTINES TO FEATURE OUR COMPANY THEME OR PRODUCT?",
            "Yes! Adrian collaborates with corporate event planners to seamlessly incorporate company milestones, key branding messaging, CEO predictions, or customized reveals into the mentalism demonstrations."
        ),
        (
            "HOW DO WE RECEIVE A CUSTOM FEE PROPOSAL FOR OUR EVENT?",
            "Simply submit the availability hold form on this page or call our direct booking office. You will receive a transparent, all-inclusive proposal within 24 to 48 hours."
        )
    ]
    for q_text, a_text in standard_faqs:
        faq_entities.append({
            "@type": "Question",
            "name": q_text,
            "acceptedAnswer": {
                "@type": "Answer",
                "text": a_text
            }
        })

    area_entities = []
    for a_name in c["areas"]:
        is_admin = any(k in a_name for k in ("County", "Metro", "Area", "District", "Valley", "Florida", "Lowcountry", "Rockies", "Arizona", "Carolina", "Virginia", "Wasatch"))
        area_entities.append({
            "@type": "AdministrativeArea" if is_admin else "City",
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
                "description": f"Adrian Saint is the premier corporate mentalist and mind reader in {city}, {state_full}, delivering interactive psychological entertainment for luxury resort retreats, corporate leadership summits, and national galas.",
                "address": {
                    "@type": "PostalAddress",
                    "addressLocality": city,
                    "addressRegion": state_region,
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
    html = sub_once(
        r'<script id="geo-jsonld-script".*?</script>',
        f'<script id="geo-jsonld-script" type="application/ld+json">\n{json_ld_str}\n  </script>',
        html,
        flags=re.DOTALL,
        label=f'{slug} json-ld'
    )

    # 4. Hero Section
    html = sub_once(
        r'<div class="section-badge">\s*<span>📍.*?</span>\s*</div>',
        f'<div class="section-badge">\n              <span>{c["badge"]}</span>\n            </div>',
        html,
        label=f'{slug} hero badge'
    )

    html = sub_once(
        r'<h1 class="hero-headline">.*?</h1>',
        f'<h1 class="hero-headline">\n              {c["h1"]}\n            </h1>',
        html,
        flags=re.DOTALL,
        label=f'{slug} hero h1'
    )

    html = sub_once(
        r'<p class="hero-subheadline">.*?</p>',
        f'<p class="hero-subheadline">\n              {c["subhead"]}\n            </p>',
        html,
        flags=re.DOTALL,
        label=f'{slug} hero subhead'
    )

    # Hero Form Values
    html = sub_once(
        r'name="_subject" value="[^"]*"',
        f'name="_subject" value="New Fast-Track Date Hold Request - {city} - Adrian Saint"',
        html,
        label=f'{slug} form subject'
    )
    html = sub_once(
        r'name="event_city" value="[^"]*"',
        f'name="event_city" value="{city}, {state}"',
        html,
        label=f'{slug} form city'
    )

    # 5. Ticker Title
    html = sub_once(
        r'<div class="ticker-title">Trusted by Top Global Brands & Aurora Event Producers</div>',
        f'<div class="ticker-title">Trusted by Top Global Brands &amp; {city} Event Producers</div>',
        html,
        label=f'{slug} ticker title'
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

    html = sub_once(
        r'<!-- 5\.5 AURORA PREMIER VENUES & LOCAL COVERAGE -->\s*<section id="aurora-venues".*?</section>',
        venue_section_html,
        html,
        flags=re.DOTALL,
        label=f'{slug} venue section'
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

    html = sub_once(
        r'<!-- Location Question 1 -->.*?<!-- Question 6 -->',
        f'{new_faqs_str}\n\n          <!-- Question 6 -->',
        html,
        flags=re.DOTALL,
        label=f'{slug} faqs'
    )

    # 8. Bottom Booking Card Availability Badge
    html = sub_once(
        r"<span>Check Adrian's Availability For Your Next Aurora Event</span>",
        f"<span>Check Adrian's Availability For Your Next {city} Event</span>",
        html,
        label=f'{slug} bottom badge'
    )

    # 9. Phone Replacements
    if phone_clean != "18335705966":
        html = html.replace("tel:18335705966", f"tel:{phone_clean}")
        html = html.replace("+18335705966", phone_e164)
        html = html.replace("1 (833) 570-5966", f"1 {phone}")
        html = html.replace("(833) 570-5966", phone)

    out_filename = f"corporate-magician-{slug}.html"
    with open(out_filename, 'w', encoding='utf-8') as out_f:
        out_f.write(html)

    created_files.append(out_filename)
    print(f"Generated {out_filename} ({len(html)} bytes)")

print(f"\nSuccessfully generated all {len(created_files)} Group C location pages!")
