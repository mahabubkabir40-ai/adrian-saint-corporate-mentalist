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

GROUP_D_CITIES = [
    {
        "slug": "pasadena",
        "city": "Pasadena",
        "state": "CA",
        "state_region": "CA",
        "state_full": "California",
        "country": "US",
        "phone": "(833) 570-5966",
        "phone_clean": "18335705966",
        "phone_e164": "+18335705966",
        "badge": "📍 PASADENA & THE LANGHAM HUNTINGTON COVERAGE",
        "h1": "Corporate Magician &amp; Mentalist in <span class=\"hero-headline-highlight\">Pasadena</span> for Convention Summits, Langham Galas &amp; Executive Retreats",
        "subhead": "Delivering world-class psychological mentalism and interactive mind reading for Pasadena Convention Center expos, black-tie galas at The Langham Huntington, and tech summits across the San Gabriel Valley.",
        "lat": 34.1478,
        "lon": -118.1445,
        "areas": ["Pasadena", "Old Pasadena", "San Gabriel Valley", "Arcadia", "Glendale", "Burbank", "Los Angeles County"],
        "venue_h2": "Serving Pasadena's Premier Convention Center &amp; Five-Star Historic Estates",
        "venue_p": "Trusted by the Pasadena Tournament of Roses and leading engineering, aerospace, and financial institutions, Adrian Saint headlines Pasadena's most prestigious ballrooms and conference venues.",
        "card1": {
            "sub": "CONVENTION CENTERS & CIVIC AUDITORIUMS",
            "title": "Conventions & Flagship Keynotes",
            "items": [
                "Pasadena Convention Center (130,000+ sq ft exhibition hall & 25,000 sq ft Grand Ballroom)",
                "Pasadena Civic Auditorium (Historic 3,000-seat theater for major corporate keynote productions)",
                "Caltech Beckman Auditorium & Athenaeum (Private executive & scientific leadership symposia)",
                "Rose Bowl Stadium Club Lounges & Terry Donahue Pavilion (VIP corporate hospitality galas)"
            ]
        },
        "card2": {
            "sub": "FIVE-STAR RESORTS & LUXURY HOTELS",
            "title": "Executive Retreats & Black-Tie Galas",
            "items": [
                "The Langham Huntington, Pasadena (23-acre luxury estate with historic Georgian & Viennese Ballrooms)",
                "Hotel Dena, Pasadena Los Angeles, a Tribute Portfolio Hotel (Adjacent to Pasadena Convention Center)",
                "The Westin Pasadena (Panoramic San Gabriel Mountain views & Fountain Ballroom suites)",
                "Courtyard & Hyatt Place Old Pasadena (Boutique executive boardrooms & rooftop receptions)"
            ]
        },
        "card3": {
            "sub": "ICONIC CULTURAL & ESTATE VENUES",
            "title": "Private Banquets & Client Receptions",
            "items": [
                "Tournament House — Pasadena Tournament of Roses HQ (Wrigley Mansion executive receptions)",
                "The Huntington Library, Art Museum, and Botanical Gardens (Private evening estate galas)",
                "Norton Simon Museum & Castle Green (Historic architectural gems for VIP corporate dinners)",
                "Annandale Golf Club & Valley Hunt Club (Exclusive private clubhouses for leadership banquets)"
            ]
        },
        "callout": {
            "sub": "LOCAL SOUTHERN CALIFORNIA DRIVE-IN ADVANTAGE",
            "title": "Zero Flight Cancellation Risks • Direct Drive-In Production from SoCal",
            "p": "Based locally in Southern California—and a verified performer for the Pasadena Tournament of Roses—Adrian Saint drives directly to Pasadena venues with zero airfare markups, zero flight delay risk, and effortless AV setup."
        },
        "faqs": [
            {
                "q": "CAN ADRIAN HEADLINE CONFERENCES AT PASADENA CONVENTION CENTER OR THE LANGHAM HUNTINGTON?",
                "a": "Yes! Adrian regularly headlines corporate awards banquets, leadership retreats, and general sessions at The Langham Huntington and Pasadena Convention Center for groups from 30 to over 2,000."
            },
            {
                "q": "HOW DO TRAVEL LOGISTICS WORK FOR PASADENA CORPORATE EVENTS?",
                "a": "Because Adrian Saint is based locally in Southern California, he drives directly to Pasadena venues—eliminating flight costs, hotel buyouts, and airline weather delays."
            },
            {
                "q": "IS ADRIAN'S MENTALISM SUITED FOR ENGINEERING, AEROSPACE & FINANCIAL AUDIENCES IN PASADENA?",
                "a": "Absolutely. Pasadena is a world leader in aerospace, biotech, and wealth management. Adrian's intelligent, 100% clean psychological mind reading captivates analytical audiences without cheesy tricks."
            },
            {
                "q": "WHAT TECHNICAL EQUIPMENT DOES ADRIAN REQUIRE AT PASADENA VENUES?",
                "a": "Adrian requires only a wireless handheld or lavalier microphone connected to house sound. His minimalist footprint allows rapid sound checks with in-house AV teams."
            },
            {
                "q": "DOES ADRIAN PERFORM STROLLING MIND READING FOR GARDEN & COURTYARD RECEPTIONS?",
                "a": "Yes! Adrian's strolling close-up mentalism requires zero AV and is a huge hit for cocktail hours on The Langham's Horseshoe Garden, Castle Green, and Old Pasadena private dining rooms."
            }
        ]
    },
    {
        "slug": "long-beach",
        "city": "Long Beach",
        "state": "CA",
        "state_region": "CA",
        "state_full": "California",
        "country": "US",
        "phone": "(833) 570-5966",
        "phone_clean": "18335705966",
        "phone_e164": "+18335705966",
        "badge": "📍 LONG BEACH WATERFRONT & CONVENTION CENTER COVERAGE",
        "h1": "Corporate Magician &amp; Mentalist in <span class=\"hero-headline-highlight\">Long Beach</span> for Waterfront Conventions, Trade Shows &amp; Harbor Galas",
        "subhead": "Delivering high-impact psychological mentalism and interactive mind reading for Long Beach Convention Center expos, aerospace and maritime summits, and waterfront awards galas.",
        "lat": 33.7701,
        "lon": -118.1937,
        "areas": ["Long Beach", "Downtown Long Beach", "Rainbow Harbor", "Belmont Shore", "San Pedro", "Signal Hill", "Los Angeles County"],
        "venue_h2": "Serving Long Beach's Award-Winning Waterfront Convention Campus &amp; Harbor Venues",
        "venue_p": "Located between Los Angeles and Orange County, the Long Beach Convention & Entertainment Center and Rainbow Harbor waterfront host major national trade conventions and corporate galas year-round.",
        "card1": {
            "sub": "WATERFRONT CONVENTION & ARENA COMPLEX",
            "title": "National Conventions & Trade Expos",
            "items": [
                "Long Beach Convention & Entertainment Center (400,000+ sq ft of turnkey exhibition & summit space)",
                "Pacific Ballroom & Grand Ballroom at LBCEC (Turnkey theatrical lighting & large gala production)",
                "Terrace Theater & Beverly O'Neill Theater (3,000-seat flagship keynote & general session halls)",
                "The Cove & Seaside Way Pavilions (Indoor/outdoor waterfront corporate networking venues)"
            ]
        },
        "card2": {
            "sub": "HARBORFRONT CONFERENCE HOTELS",
            "title": "Executive Summits & Awards Banquets",
            "items": [
                "Hyatt Regency Long Beach (Directly adjacent to the convention center with 25,000 sq ft event space)",
                "Marriott Long Beach Downtown (Newly transformed harborfront convention hotel & grand ballroom)",
                "The Westin Long Beach (Over 34,000 sq ft of corporate meeting space & Centennial Ballroom)",
                "Fairmont Breakers Long Beach (Iconic restored 1926 luxury landmark with Sky Room & Halo rooftop)"
            ]
        },
        "card3": {
            "sub": "ICONIC MARITIME & CULTURAL VENUES",
            "title": "Distinctive Galas & Yacht Receptions",
            "items": [
                "The Queen Mary (Historic Art Deco Grand Salon, Queen's Salon & Britannia Salon for black-tie galas)",
                "Aquarium of the Pacific (Great Hall & Honda Blue Cavern for unforgettable corporate receptions)",
                "Museum of Latin American Art (MOLAA Sculpture Garden & event galleries)",
                "City Cruises Long Beach & Private Harbor Yacht Charters (Sunset cocktail strolling mentalism)"
            ]
        },
        "callout": {
            "sub": "LOCAL SOCAL DRIVE-IN ADVANTAGE",
            "title": "20 Minutes From Adrian's Orange County Base • Zero Travel Markups",
            "p": "Located just 20 minutes from Adrian Saint's Southern California home base, Long Beach events benefit from zero flight costs, guaranteed on-time arrival, and immediate coordination with convention producers."
        },
        "faqs": [
            {
                "q": "CAN ADRIAN HEADLINE GENERAL SESSIONS AT THE LONG BEACH CONVENTION CENTER?",
                "a": "Yes! Adrian regularly headlines opening general sessions, evening awards banquets, and trade show hospitality events at the Long Beach Convention & Entertainment Center for crowds of 100 to 3,000+."
            },
            {
                "q": "HOW DO TRAVEL LOGISTICS WORK FOR LONG BEACH EVENTS?",
                "a": "Adrian Saint is based locally in adjacent Orange County—just 20 minutes down I-405 from Downtown Long Beach—so meeting planners pay zero airfare or hotel travel riders."
            },
            {
                "q": "CAN ADRIAN PERFORM ABOARD THE QUEEN MARY OR AT THE AQUARIUM OF THE PACIFIC?",
                "a": "Yes! Adrian's self-contained stage and strolling mentalism packages are ideal for the Queen Mary's Art Deco ballrooms, the Aquarium of the Pacific's Great Hall, and harbor yacht charters."
            },
            {
                "q": "IS ADRIAN'S SHOW 100% CLEAN AND HR-APPROVED FOR CORPORATE CONVENTIONS?",
                "a": "Yes, 100%. Adrian's performance is completely clean, respectful, and tailored for diverse national association and corporate audiences."
            },
            {
                "q": "CAN ADRIAN DRIVE BOOTH TRAFFIC ON THE LONG BEACH CONVENTION FLOOR?",
                "a": "Yes! In addition to main stage keynotes, Adrian offers a specialized Trade Show Crowd Magnet package that stops attendees in the aisles and integrates your brand message."
            }
        ]
    },
    {
        "slug": "plano",
        "city": "Plano",
        "state": "TX",
        "state_region": "TX",
        "state_full": "Texas",
        "country": "US",
        "phone": "(833) 570-5966",
        "phone_clean": "18335705966",
        "phone_e164": "+18335705966",
        "badge": "📍 PLANO LEGACY WEST & FORTUNE 500 HQ COVERAGE",
        "h1": "Corporate Magician &amp; Mentalist in <span class=\"hero-headline-highlight\">Plano</span> for Legacy West Summits, Fortune 500 Galas &amp; Executive Meetings",
        "subhead": "Delivering sophisticated psychological mentalism and interactive mind reading for Fortune 500 headquarters summits, national sales kickoffs, and executive banquets across Plano and Legacy West.",
        "lat": 33.0198,
        "lon": -96.6989,
        "areas": ["Plano", "Legacy West", "Shops at Legacy", "Granite Park", "Collin County", "Richardson", "North Dallas Metroplex"],
        "venue_h2": "Serving Plano's Legacy West Corporate Headquarters Corridor &amp; Luxury Conference Hotels",
        "venue_p": "Home to the massive Legacy business corridor—housing global and regional headquarters for Toyota, Frito-Lay, JPMorgan Chase, Liberty Mutual, and Ericsson—Plano is one of Texas's premier corporate event hubs.",
        "card1": {
            "sub": "LEGACY WEST & GRANITE PARK FLAGSHIP HOTELS",
            "title": "Fortune 500 Summits & Sales Kickoffs",
            "items": [
                "Renaissance Dallas at Plano Legacy West Hotel (35,000+ sq ft of modern luxury summit space)",
                "Hilton Dallas/Plano Granite Park (30,000 sq ft lakeside conference center & Prairie Ballroom)",
                "Dallas/Plano Marriott at Legacy Town Center (32,000 sq ft executive conference facility)",
                "Legacy West Corporate HQ Campuses (Toyota North America, PepsiCo/Frito-Lay & JPMorgan auditoriums)"
            ]
        },
        "card2": {
            "sub": "CONVENTION CENTERS & EXECUTIVE VENUES",
            "title": "Regional Conventions & Trade Galas",
            "items": [
                "Plano Event Center (86,400 sq ft exhibition & convention complex with Collinwood Ballroom)",
                "NYLO Dallas Plano Hotel, Tapestry Collection by Hilton (Boutique industrial-chic executive mixers)",
                "Sandman Signature Plano-Frisco Hotel (Corporate offsites & multi-day leadership workshops)",
                "Nearby Frisco & Richardson Telecom Corridor Conference Centers"
            ]
        },
        "card3": {
            "sub": "PRIVATE CLUBS & UPSCALE EVENT VENUES",
            "title": "Executive Dinners & Client Receptions",
            "items": [
                "Gleneagles Country Club (Premier private Plano country club for C-suite golf & awards dinners)",
                "Haywire & Legacy Hall VIP Box Garden Buyouts at Legacy West (Upscale Texas corporate receptions)",
                "The Nature & Retreat Center at Oak Point Park (Scenic executive team-building events)",
                "Fogo de Chão & Del Frisco's Double Eagle Legacy West Private Executive Dining Suites"
            ]
        },
        "callout": {
            "sub": "DFW METROPLEX TURNKEY ACCESS",
            "title": "Direct DFW International & Dallas Love Field (DAL) Access • 25 Minutes to Legacy West",
            "p": "With nonstop flights from every major hub into DFW International Airport and Dallas Love Field (DAL)—just 25 minutes from Legacy West—Adrian Saint delivers seamless, punctual corporate entertainment across North Texas."
        },
        "faqs": [
            {
                "q": "CAN ADRIAN HEADLINE CORPORATE EVENTS AT RENAISSANCE PLANO LEGACY WEST OR GRANITE PARK?",
                "a": "Yes! Adrian regularly headlines national sales kickoffs, leadership summits, and awards banquets at Renaissance Plano Legacy West, Hilton Granite Park, Marriott Legacy Town Center, and Plano Event Center."
            },
            {
                "q": "DOES ADRIAN PERFORM ON-SITE AT PLANO FORTUNE 500 CORPORATE CAMPUSES?",
                "a": "Yes! Adrian's minimalist AV rider makes it easy to perform inside private corporate campus auditoriums and town hall spaces across Legacy West and Granite Park."
            },
            {
                "q": "HOW DO TRAVEL LOGISTICS WORK FOR PLANO AND NORTH DALLAS EVENTS?",
                "a": "Adrian flies directly into DFW International Airport or Dallas Love Field (DAL), just 25 minutes from Plano via Sam Rayburn Tollway or Dallas North Tollway, with turnkey travel coordination."
            },
            {
                "q": "IS ADRIAN'S SHOW 100% CLEAN AND HR-APPROVED FOR ENTERPRISE CORPORATIONS?",
                "a": "Yes, 100%. Adrian's performance is completely clean, respectful, and tailored for strict enterprise HR standards—making your planning committee look brilliant."
            },
            {
                "q": "WHAT AUDIOVISUAL SETUP DOES ADRIAN REQUIRE AT PLANO HOTELS?",
                "a": "Adrian requires only a wireless handheld or lavalier microphone connected to house sound. For cocktail mixers at Legacy West, strolling close-up mentalism requires zero AV."
            }
        ]
    },
    {
        "slug": "the-woodlands",
        "city": "The Woodlands",
        "state": "TX",
        "state_region": "TX",
        "state_full": "Texas",
        "country": "US",
        "phone": "(833) 570-5966",
        "phone_clean": "18335705966",
        "phone_e164": "+18335705966",
        "badge": "📍 THE WOODLANDS WATERWAY & ENERGY CORRIDOR COVERAGE",
        "h1": "Corporate Magician &amp; Mentalist in <span class=\"hero-headline-highlight\">The Woodlands</span> for Waterway Marriott Conventions, Energy Summits &amp; Galas",
        "subhead": "Delivering unforgettable psychological mentalism and interactive mind reading for energy summits, executive retreats, and gala banquets across The Woodlands Waterway and North Houston.",
        "lat": 30.1658,
        "lon": -95.4613,
        "areas": ["The Woodlands", "The Woodlands Waterway", "Hughes Landing", "Spring", "Conroe", "Montgomery County", "North Houston"],
        "venue_h2": "Serving The Woodlands Waterway Convention Hotels &amp; Forested Golf Resorts",
        "venue_p": "Surrounded by 28,000 forested acres and anchored by global energy and chemical headquarters (including Occidental, Chevron Phillips, and nearby ExxonMobil Spring campus), The Woodlands is Houston's premier executive retreat enclave.",
        "card1": {
            "sub": "WATERWAY CONVENTION & RESORT FLAGSHIPS",
            "title": "Energy Conventions & Executive Retreats",
            "items": [
                "The Woodlands Waterway Marriott Hotel & Convention Center (70,000+ sq ft of premier event space)",
                "The Woodlands Resort, Curio Collection by Hilton (75,000 sq ft forested conference & golf resort)",
                "The Westin at The Woodlands (28,000 sq ft of modern event space overlooking The Waterway)",
                "Embassy Suites by Hilton The Woodlands at Hughes Landing (Lakeside executive summit suites)"
            ]
        },
        "card2": {
            "sub": "CHAMPIONSHIP GOLF CLUBS & CORPORATE CAMPUSES",
            "title": "Board Dinners & Leadership Summits",
            "items": [
                "The Club at Carlton Woods (Jack Nicklaus & Tom Fazio private clubhouses for C-suite galas)",
                "The Woodlands Country Club (Palmer, Tournament & Gary Player clubhouses for corporate outings)",
                "ExxonMobil Spring Campus & Hughes Landing Corporate Headquarters Auditoriums",
                "Margaritaville Lake Resort Lake Conroe (Nearby 72,000 sq ft lakefront convention center)"
            ]
        },
        "card3": {
            "sub": "DISTINCTIVE WATERWAY & CULTURAL VENUES",
            "title": "Private Banquets & VIP Receptions",
            "items": [
                "The Cynthia Woods Mitchell Pavilion VIP Club & Hospitality Suites (Private corporate receptions)",
                "The Peach Orchard Venue & Madera Estates (Upscale forested estate banquets)",
                "Truluck's, Steak 48 & Del Frisco's Grille Hughes Landing (Private executive board dining)",
                "Glade Cultural Center (Sophisticated art gallery receptions along The Waterway)"
            ]
        },
        "callout": {
            "sub": "EFFORTLESS NORTH HOUSTON ACCESS",
            "title": "20 Minutes From George Bush Intercontinental (IAH) • Turnkey Delivery",
            "p": "Located just 20 minutes north of Houston's George Bush Intercontinental Airport (IAH), The Woodlands is faster and easier to reach than Downtown Houston—ensuring punctual, stress-free production delivery."
        },
        "faqs": [
            {
                "q": "CAN ADRIAN HEADLINE CONFERENCES AT THE WOODLANDS WATERWAY MARRIOTT OR THE WOODLANDS RESORT?",
                "a": "Yes! Adrian regularly headlines energy summits, corporate awards galas, and leadership retreats at The Woodlands Waterway Marriott, The Woodlands Resort, and The Westin at The Woodlands."
            },
            {
                "q": "HOW DO TRAVEL LOGISTICS WORK FOR EVENTS IN THE WOODLANDS?",
                "a": "Adrian flies directly into George Bush Intercontinental Airport (IAH), located just 20 minutes south of The Woodlands via I-45 and the Hardy Toll Road. All travel is turnkey."
            },
            {
                "q": "IS ADRIAN'S SHOW SUITED FOR ENERGY, PETROCHEMICAL & ENGINEERING EXECUTIVES?",
                "a": "Absolutely. Adrian's sharp, psychological mind reading appeals directly to engineers, scientists, and energy executives while staying 100% clean and HR-approved."
            },
            {
                "q": "WHAT TECHNICAL EQUIPMENT DOES ADRIAN REQUIRE AT THE WOODLANDS VENUES?",
                "a": "Adrian requires only a wireless handheld or lavalier microphone connected to room audio. He coordinates directly with in-house resort AV teams for rapid sound checks."
            },
            {
                "q": "DOES ADRIAN PERFORM FOR PRIVATE DINNERS AT CARLTON WOODS OR HUGHES LANDING?",
                "a": "Yes! Adrian excels at intimate after-dinner parlor mentalism and strolling close-up mind reading for executive groups of 15 to 80 guests at Carlton Woods and Hughes Landing."
            }
        ]
    },
    {
        "slug": "bellevue",
        "city": "Bellevue",
        "state": "WA",
        "state_region": "WA",
        "state_full": "Washington",
        "country": "US",
        "phone": "(833) 570-5966",
        "phone_clean": "18335705966",
        "phone_e164": "+18335705966",
        "badge": "📍 BELLEVUE EASTSIDE TECH CORRIDOR & MEYDENBAUER COVERAGE",
        "h1": "Corporate Magician &amp; Mentalist in <span class=\"hero-headline-highlight\">Bellevue</span> for Meydenbauer Tech Summits, Eastside Galas &amp; Executive Offsites",
        "subhead": "Delivering razor-sharp psychological mentalism and interactive mind reading for technology conferences, enterprise leadership summits, and gala dinners across Bellevue, Redmond, and Kirkland.",
        "lat": 47.6101,
        "lon": -122.2015,
        "areas": ["Bellevue", "Downtown Bellevue", "Redmond", "Kirkland", "Woodinville", "Eastside Seattle", "King County"],
        "venue_h2": "Serving Bellevue's Meydenbauer Convention Center &amp; Eastside Tech Corridor Hotels",
        "venue_p": "As the surging heart of the Pacific Northwest's Eastside tech ecosystem—home to major Amazon, Microsoft, T-Mobile, Salesforce, and Valve operations—Bellevue hosts premier technology summits and executive galas.",
        "card1": {
            "sub": "CONVENTION CENTERS & TECH SUMMIT HUBS",
            "title": "Enterprise Conferences & Product Keynotes",
            "items": [
                "Meydenbauer Center (54,000 sq ft convention center & 410-seat Center Theatre in Downtown Bellevue)",
                "Hyatt Regency Bellevue on Seattle's Eastside (70,000+ sq ft of premier conference & ballroom space)",
                "The Westin Bellevue (27,000 sq ft Lincoln Square conference center & Grand Ballroom)",
                "Microsoft Redmond Campus & Bellevue Enterprise Tower Auditoriums"
            ]
        },
        "card2": {
            "sub": "LUXURY HOTELS & WATERFRONT RETREATS",
            "title": "Executive Offsites & Awards Banquets",
            "items": [
                "W Bellevue (Chic Lincoln Square South luxury hotel with Great Room & Living Room mixers)",
                "Seattle Marriott Bellevue (21,000 sq ft Downtown Bellevue corporate meeting hub)",
                "InterContinental Bellevue at the Avenue (Ultra-luxury Avenue Bellevue hotel for C-suite summits)",
                "The Woodmark Hotel & Still Spa in Kirkland (Only luxury hotel directly on the shores of Lake Washington)"
            ]
        },
        "card3": {
            "sub": "WOODINVILLE WINE COUNTRY & PRIVATE CLUBS",
            "title": "VIP Dinners & Leadership Retreats",
            "items": [
                "Chateau Ste. Michelle & The Somm Hotel in Woodinville (Iconic wine country corporate retreats)",
                "Bellevue Arts Museum & Bellevue Botanical Garden (Architectural receptions & evening mixers)",
                "Ascend Prime Steak & Sushi (31st-floor panoramic rooftop buyouts overlooking Lake Washington)",
                "Overlake Golf & Country Club & Glendale Country Club (Private executive board dinners)"
            ]
        },
        "callout": {
            "sub": "WEST COAST TECH CORRIDOR MOBILITY",
            "title": "Direct Sea-Tac (SEA) Access • 20 Minutes via I-405 to Downtown Bellevue",
            "p": "Based on the West Coast, Adrian Saint flies nonstop into Seattle-Tacoma International Airport (SEA) just 20 minutes from Downtown Bellevue. Zero time-zone lag and a minimalist AV rider guarantee effortless execution."
        },
        "faqs": [
            {
                "q": "CAN ADRIAN HEADLINE TECH CONFERENCES AT MEYDENBAUER CENTER OR HYATT REGENCY BELLEVUE?",
                "a": "Yes! Adrian regularly headlines technology conferences, engineering all-hands, and evening galas at Meydenbauer Center, Hyatt Regency Bellevue, W Bellevue, and The Westin Bellevue."
            },
            {
                "q": "WHY DO SOFTWARE ENGINEERS AND TECH EXECUTIVES IN BELLEVUE LOVE ADRIAN'S SHOW?",
                "a": "Tech audiences appreciate intelligent, analytical entertainment. Adrian blends behavioral psychology, pattern recognition, and impossible mind reading—with zero hokey props and 100% HR-safe sophistication."
            },
            {
                "q": "HOW DO TRAVEL LOGISTICS WORK FOR BELLEVUE, REDMOND, AND KIRKLAND EVENTS?",
                "a": "Adrian flies nonstop from Southern California into Seattle-Tacoma International Airport (SEA), just 20 minutes from Downtown Bellevue, in the exact same Pacific Time Zone."
            },
            {
                "q": "WHAT TECHNICAL SETUP DOES ADRIAN REQUIRE AT BELLEVUE HOTELS?",
                "a": "Adrian requires only a wireless handheld or lavalier microphone connected to room audio. He coordinates directly with in-house Encore AV teams for fast, zero-stress sound checks."
            },
            {
                "q": "DOES ADRIAN PERFORM FOR EXECUTIVE DINNERS AT ASCEND PRIME OR IN WOODINVILLE?",
                "a": "Yes! Adrian frequently performs strolling close-up mentalism and private after-dinner shows for executive offsites at Ascend Prime, InterContinental Bellevue, and Woodinville wineries."
            }
        ]
    },
    {
        "slug": "chandler",
        "city": "Chandler",
        "state": "AZ",
        "state_region": "AZ",
        "state_full": "Arizona",
        "country": "US",
        "phone": "(833) 570-5966",
        "phone_clean": "18335705966",
        "phone_e164": "+18335705966",
        "badge": "📍 CHANDLER SILICON DESERT & RESORT CORRIDOR COVERAGE",
        "h1": "Corporate Magician &amp; Mentalist in <span class=\"hero-headline-highlight\">Chandler</span> for Silicon Desert Tech Summits, Resort Galas &amp; Conferences",
        "subhead": "Delivering high-energy psychological mentalism and interactive mind reading for semiconductor and tech conferences, Wild Horse Pass resort conventions, and executive galas across Chandler and the East Valley.",
        "lat": 33.3062,
        "lon": -111.8413,
        "areas": ["Chandler", "Price Corridor", "Silicon Desert", "Gilbert", "Tempe", "Mesa", "East Valley Phoenix", "Maricopa County"],
        "venue_h2": "Serving Chandler's Silicon Desert Resorts &amp; Price Corridor Corporate Hubs",
        "venue_p": "Anchored by Intel's massive semiconductor campuses, the Price Road tech and finance corridor, and expansive desert resorts, Chandler is the economic powerhouse of Phoenix's East Valley.",
        "card1": {
            "sub": "FLAGSHIP CONVENTION & CASINO RESORTS",
            "title": "Large-Scale Conventions & Desert Galas",
            "items": [
                "Sheraton Grand at Wild Horse Pass (100,000+ sq ft of indoor/outdoor Sonoran Desert convention space)",
                "Gila River Resorts & Casinos — Wild Horse Pass (1,200-seat Showroom & expansive conference ballrooms)",
                "Crowne Plaza Phoenix - Chandler Golf Resort (Historic 1912 San Marcos resort in Downtown Chandler)",
                "Marriott Phoenix Chandler (Premier Price Corridor conference center & 25,000+ sq ft event space)"
            ]
        },
        "card2": {
            "sub": "PRICE CORRIDOR CORPORATE HOTELS & CAMPUSES",
            "title": "Tech Summits & Leadership Workshops",
            "items": [
                "Intel Ocotillo & Chandler Boulevard Campus Auditoriums (Semiconductor & engineering town halls)",
                "Hilton Phoenix Chandler (Spacious East Valley corporate ballrooms & executive meeting suites)",
                "Drury Inn & Suites and Cambria Hotel Phoenix Chandler - Fashion Center (Business corridor offsites)",
                "Chandler Center for the Arts (1,500-seat main auditorium for flagship corporate keynotes)"
            ]
        },
        "card3": {
            "sub": "CHAMPIONSHIP GOLF & DISTINCTIVE VENUES",
            "title": "Executive Dinners & Outdoor Receptions",
            "items": [
                "Whirlwind Golf Club at Wild Horse Pass (Championship PGA golf clubhouse & sunset banquet terraces)",
                "Ocotillo Golf Club (Lush lakeside clubhouse for East Valley corporate tournaments & galas)",
                "SoHo63 in Historic Downtown Chandler (Modern urban event venue for creative corporate mixers)",
                "Rawhide Western Town & Event Center (Large-scale Southwestern corporate buyouts & banquets)"
            ]
        },
        "callout": {
            "sub": "RAPID SKY HARBOR FLY-IN ACCESS",
            "title": "20 Minutes From Phoenix Sky Harbor (PHX) • Turnkey Southwest Delivery",
            "p": "Adrian Saint performs frequently across the Valley of the Sun. With 1-hour flights from Southern California into Phoenix Sky Harbor International Airport (PHX)—just 20 minutes from Chandler—logistics are effortless."
        },
        "faqs": [
            {
                "q": "CAN ADRIAN HEADLINE CONFERENCES AT SHERATON GRAND WILD HORSE PASS OR MARRIOTT CHANDLER?",
                "a": "Yes! Adrian regularly headlines corporate conventions, sales summits, and awards galas at Sheraton Grand at Wild Horse Pass, Gila River Resorts, Marriott Phoenix Chandler, and San Marcos Golf Resort."
            },
            {
                "q": "HOW DO TRAVEL LOGISTICS WORK FOR CHANDLER AND EAST VALLEY EVENTS?",
                "a": "Adrian flies nonstop from Southern California into Phoenix Sky Harbor International Airport (PHX), just 20 minutes from Chandler via I-10 and Loop 202, or Mesa Gateway Airport (AZA)."
            },
            {
                "q": "IS ADRIAN'S SHOW TAILORED FOR SEMICONDUCTOR, ENGINEERING & FINANCE TEAMS?",
                "a": "Yes! Chandler's Price Corridor is filled with engineers and financial professionals who love Adrian's intelligent, psychological approach to mind reading—100% clean and HR-approved."
            },
            {
                "q": "WHAT TECHNICAL REQUIREMENTS DOES ADRIAN HAVE AT CHANDLER RESORTS?",
                "a": "Adrian requires only a wireless handheld or lavalier microphone connected to room audio. His minimalist rider allows rapid sound checks with resort AV staff."
            },
            {
                "q": "DOES ADRIAN PERFORM STROLLING MIND READING FOR DESERT PATIO RECEPTIONS?",
                "a": "Yes! Adrian's strolling close-up mentalism requires zero AV and is ideal for sunset cocktail hours at Whirlwind Golf Club, Sheraton Wild Horse Pass lawns, and Ocotillo Golf Club."
            }
        ]
    },
    {
        "slug": "overland-park",
        "city": "Overland Park",
        "state": "KS",
        "state_region": "KS",
        "state_full": "Kansas",
        "country": "US",
        "phone": "(833) 570-5966",
        "phone_clean": "18335705966",
        "phone_e164": "+18335705966",
        "badge": "📍 OVERLAND PARK CONVENTION CENTER & JOHNSON COUNTY COVERAGE",
        "h1": "Corporate Magician &amp; Mentalist in <span class=\"hero-headline-highlight\">Overland Park</span> for Convention Center Expos, Executive Summits &amp; Galas",
        "subhead": "Delivering unforgettable psychological mentalism and interactive mind reading for Overland Park Convention Center conferences, corporate headquarters summits, and awards banquets across Johnson County.",
        "lat": 38.9822,
        "lon": -94.6708,
        "areas": ["Overland Park", "Johnson County", "Leawood", "Lenexa", "Olathe", "College Boulevard Corridor", "Kansas City Metro"],
        "venue_h2": "Serving the Award-Winning Overland Park Convention Center &amp; College Boulevard Corridor",
        "venue_p": "Consistently ranked among North America's best mid-sized convention centers and surrounded by Johnson County's affluent corporate headquarters corridor (Black & Veatch, T-Mobile campus, Compass Minerals), Overland Park is a premier Midwest meeting hub.",
        "card1": {
            "sub": "AWARD-WINNING CONVENTION CAMPUS",
            "title": "National Conventions & Trade Shows",
            "items": [
                "Overland Park Convention Center (OPCC — 245,000 sq ft facility with 60,000 sq ft exhibition hall)",
                "Courtyard Ballroom at OPCC (25,000 sq ft pillarless ballroom for flagship keynotes & awards galas)",
                "Sheraton Overland Park Hotel at the Convention Center (Connected directly to OPCC with 21,000 sq ft space)",
                "Aspiria Corporate Campus Auditoriums (200-acre former Sprint World Headquarters event facilities)"
            ]
        },
        "card2": {
            "sub": "COLLEGE BOULEVARD & LEAWOOD CONFERENCE HOTELS",
            "title": "Executive Summits & Corporate Banquets",
            "items": [
                "Marriott Kansas City Overland Park (Newly renovated College Boulevard hub with 14,000 sq ft space)",
                "DoubleTree by Hilton Hotel Kansas City - Overland Park (19,000 sq ft of corporate ballroom space)",
                "Aloft Leawood-Overland Park & Park Place Hotel (Upscale boutique executive retreats in Leawood)",
                "Hyatt Place Kansas City/Lenexa City Center (Modern suburban conference center nearby)"
            ]
        },
        "card3": {
            "sub": "PRIVATE COUNTRY CLUBS & DISTINCTIVE VENUES",
            "title": "C-Suite Dinners & Client Receptions",
            "items": [
                "Hallbrook Country Club in Leawood (Exclusive private golf clubhouse for executive board dinners)",
                "Nicklaus Golf Club at LionsGate & Shadow Glen Golf Club (Championship golf banquet pavilions)",
                "Museum at Prairiefire (Striking architectural dichroic glass Great Hall for corporate receptions)",
                "Overland Park Arboretum & Botanical Gardens (LongHouse Visitor Center private evening galas)"
            ]
        },
        "callout": {
            "sub": "HEARTLAND FLY-IN CONVENIENCE",
            "title": "Direct Kansas City International (MCI) Access • Turnkey Midwest Production",
            "p": "Flying directly into Kansas City International Airport (MCI)'s brand-new single terminal—just 30 minutes via I-435 from the Overland Park Convention Center—Adrian Saint provides seamless, punctual entertainment."
        },
        "faqs": [
            {
                "q": "CAN ADRIAN HEADLINE CONFERENCES AT THE OVERLAND PARK CONVENTION CENTER (OPCC)?",
                "a": "Yes! Adrian regularly headlines opening general sessions, evening awards banquets, and association conferences at the Overland Park Convention Center and Sheraton Overland Park for groups of 100 to 2,500+."
            },
            {
                "q": "HOW DO TRAVEL LOGISTICS WORK FOR OVERLAND PARK AND JOHNSON COUNTY EVENTS?",
                "a": "Adrian flies directly into Kansas City International Airport (MCI), 30 minutes from College Boulevard and OPCC. All travel logistics are turnkey with guaranteed early arrival."
            },
            {
                "q": "IS ADRIAN'S SHOW 100% CLEAN AND SUITED FOR MIDWEST CORPORATE AUDIENCES?",
                "a": "Yes, 100%. Adrian's performance is completely clean, intelligent, and HR-approved—celebrating your employees and clients without ever embarrassing volunteers."
            },
            {
                "q": "WHAT AUDIOVISUAL SETUP DOES ADRIAN REQUIRE AT OPCC OR MARRIOTT OVERLAND PARK?",
                "a": "Adrian requires only a wireless handheld or lavalier microphone connected to house sound. His minimalist footprint integrates effortlessly with OPCC and hotel AV teams."
            },
            {
                "q": "DOES ADRIAN PERFORM FOR PRIVATE EXECUTIVE DINNERS IN LEAWOOD AND OVERLAND PARK?",
                "a": "Yes! Adrian frequently performs strolling close-up mentalism and intimate after-dinner shows for executive gatherings at Hallbrook Country Club, Museum at Prairiefire, and Park Place."
            }
        ]
    },
    {
        "slug": "grand-rapids",
        "city": "Grand Rapids",
        "state": "MI",
        "state_region": "MI",
        "state_full": "Michigan",
        "country": "US",
        "phone": "(833) 570-5966",
        "phone_clean": "18335705966",
        "phone_e164": "+18335705966",
        "badge": "📍 GRAND RAPIDS & DEVOS PLACE CONVENTION COVERAGE",
        "h1": "Corporate Magician &amp; Mentalist in <span class=\"hero-headline-highlight\">Grand Rapids</span> for DeVos Place Conventions, Amway Grand Galas &amp; Summits",
        "subhead": "Delivering world-class psychological mentalism and interactive mind reading for DeVos Place conventions, West Michigan manufacturing and healthcare summits, and black-tie galas.",
        "lat": 42.9634,
        "lon": -85.6681,
        "areas": ["Grand Rapids", "Downtown Grand Rapids", "Kent County", "Ada", "East Grand Rapids", "Medical Mile", "West Michigan"],
        "venue_h2": "Serving Grand Rapids's Riverfront DeVos Place &amp; Skywalk-Connected Luxury Hotels",
        "venue_p": "Anchored by the gleaming riverfront DeVos Place Convention Center, historic Amway Grand Plaza, and major corporate leaders (Steelcase, Amway, Meijer, Corewell Health), Grand Rapids is West Michigan's premier convention city.",
        "card1": {
            "sub": "RIVERFRONT CONVENTION & PERFORMING ARTS CAMPUS",
            "title": "Statewide Conventions & National Expos",
            "items": [
                "DeVos Place Convention Center (162,000 sq ft exhibit hall & 40,000 sq ft Steelcase Grand Ballroom)",
                "DeVos Performance Hall (2,400-seat theater for flagship corporate keynotes & general sessions)",
                "Van Andel Arena (12,000-seat downtown arena & skywalk-connected corporate hospitality suites)",
                "GLC Live at 20 Monroe (Modern live entertainment theater for dynamic corporate rallies)"
            ]
        },
        "card2": {
            "sub": "SKYWALK-CONNECTED LUXURY HOTELS",
            "title": "Executive Summits & Awards Banquets",
            "items": [
                "Amway Grand Plaza, Curio Collection by Hilton (47,000+ sq ft of space, Ambassador & Pantlind Ballrooms)",
                "JW Marriott Grand Rapids (Four-Diamond riverfront luxury hotel with 15,000 sq ft International Ballroom)",
                "AC Hotel Grand Rapids Downtown & Courtyard Downtown (Skywalk-connected business meeting hubs)",
                "Canopy by Hilton Grand Rapids Downtown (Studio Park boutique executive meeting spaces)"
            ]
        },
        "card3": {
            "sub": "DISTINCTIVE WEST MICHIGAN VENUES",
            "title": "Cultural Galas & Private Club Dinners",
            "items": [
                "Frederik Meijer Gardens & Sculpture Park (Huizenga Grand Room & tropical conservatory galas)",
                "Grand Rapids Art Museum (GRAM — LEED Gold architectural galleries on Rosa Parks Circle)",
                "Grand Rapids Public Museum & Gerald R. Ford Presidential Museum (Riverfront corporate receptions)",
                "Kent Country Club & Egypt Valley Country Club (Exclusive private clubhouses for executive dinners)"
            ]
        },
        "callout": {
            "sub": "WEST MICHIGAN FLY-IN EASE",
            "title": "Direct Gerald R. Ford International (GRR) Access • 15 Minutes to DeVos Place",
            "p": "Flying directly into Gerald R. Ford International Airport (GRR) just 15 minutes from Downtown Grand Rapids—where DeVos Place, Amway Grand Plaza, and JW Marriott connect via enclosed skywalk—Adrian Saint guarantees seamless delivery."
        },
        "faqs": [
            {
                "q": "CAN ADRIAN HEADLINE CONFERENCES AT DEVOS PLACE OR THE AMWAY GRAND PLAZA?",
                "a": "Yes! Adrian regularly headlines corporate general sessions, Steelcase Ballroom awards galas, and association conventions at DeVos Place, Amway Grand Plaza, and JW Marriott Grand Rapids."
            },
            {
                "q": "HOW DO TRAVEL LOGISTICS WORK FOR GRAND RAPIDS CORPORATE EVENTS?",
                "a": "Adrian flies directly into Gerald R. Ford International Airport (GRR), located just 15 minutes from Downtown Grand Rapids. All travel logistics are turnkey and self-contained."
            },
            {
                "q": "IS ADRIAN'S SHOW 100% CLEAN AND SUITED FOR WEST MICHIGAN CORPORATE VALUES?",
                "a": "Yes, 100%! West Michigan planners value clean, family- and HR-friendly corporate entertainment. Adrian never uses profanity, crude humor, or embarrassing gags—delivering pure astonishment and laughter."
            },
            {
                "q": "WHAT TECHNICAL SETUP DOES ADRIAN REQUIRE AT DEVOS PLACE OR MEIJER GARDENS?",
                "a": "Adrian requires only a wireless handheld or lavalier microphone connected to house sound. His minimalist rider works seamlessly with Encore and in-house AV teams."
            },
            {
                "q": "DOES ADRIAN PERFORM STROLLING MIND READING FOR RECEPTIONS AT MEIJER GARDENS OR GRAM?",
                "a": "Yes! Adrian's strolling close-up mentalism requires zero AV and is a favorite for cocktail receptions at Frederik Meijer Gardens, Grand Rapids Art Museum, and the JW Marriott riverfront terrace."
            }
        ]
    },
    {
        "slug": "knoxville",
        "city": "Knoxville",
        "state": "TN",
        "state_region": "TN",
        "state_full": "Tennessee",
        "country": "US",
        "phone": "(833) 570-5966",
        "phone_clean": "18335705966",
        "phone_e164": "+18335705966",
        "badge": "📍 KNOXVILLE CONVENTION CENTER & EAST TENNESSEE COVERAGE",
        "h1": "Corporate Magician &amp; Mentalist in <span class=\"hero-headline-highlight\">Knoxville</span> for Convention Center Summits, Energy Galas &amp; Executive Banquets",
        "subhead": "Delivering unforgettable psychological mentalism and interactive mind reading for Knoxville Convention Center conferences, Oak Ridge scientific and energy summits, and executive galas across East Tennessee.",
        "lat": 35.9606,
        "lon": -83.9207,
        "areas": ["Knoxville", "Downtown Knoxville", "World's Fair Park", "Oak Ridge", "Farragut", "Knox County", "East Tennessee"],
        "venue_h2": "Serving Knoxville's World's Fair Park Convention Campus &amp; Historic Downtown Venues",
        "venue_p": "Anchored by the 500,000-square-foot Knoxville Convention Center, the Oak Ridge National Laboratory innovation corridor, and Tennessee Valley corporate leaders, Knoxville is a vibrant hub for Southeast conferences.",
        "card1": {
            "sub": "WORLD'S FAIR PARK CONVENTION COMPLEX",
            "title": "Regional Conventions & National Summits",
            "items": [
                "Knoxville Convention Center (500,000 sq ft facility with 120,000 sq ft exhibit hall & 27,000 sq ft ballroom)",
                "Lecture Hall at Knoxville Convention Center (461-seat tiered theater for executive keynotes)",
                "Knoxville Civic Auditorium and Coliseum (2,500-seat auditorium for large corporate assemblies)",
                "University of Tennessee Conference Center (Downtown executive education & symposium center)"
            ]
        },
        "card2": {
            "sub": "DOWNTOWN LUXURY & CONFERENCE HOTELS",
            "title": "Executive Summits & Awards Banquets",
            "items": [
                "Marriott Knoxville Downtown (Connected to World's Fair Park with 16,000+ sq ft of ballroom space)",
                "The Tennessean Personal Luxury Hotel (Five-star hospitality adjacent to Knoxville Convention Center)",
                "Crowne Plaza Knoxville Downtown University (15,000 sq ft of central corporate meeting space)",
                "The Oliver Hotel & Embassy Suites Knoxville Downtown (Gay Street boutique & rooftop executive mixers)"
            ]
        },
        "card3": {
            "sub": "HISTORIC THEATERS & DISTINCTIVE VENUES",
            "title": "Private Banquets & Cultural Receptions",
            "items": [
                "Tennessee Theatre & Bijou Theatre (Historic Gay Street palaces for flagship corporate keynotes)",
                "Knoxville Museum of Art (Great Hall overlooking World's Fair Park for upscale corporate galas)",
                "Cherokee Country Club & Fox Den Country Club (Scenic Tennessee River & golf clubhouse dinners)",
                "Blackberry Farm & Blackberry Mountain in Walland (Ultra-luxury Smoky Mountain C-suite retreats nearby)"
            ]
        },
        "callout": {
            "sub": "EAST TENNESSEE TURNKEY ACCESS",
            "title": "Direct McGhee Tyson Airport (TYS) Access • 20 Minutes to World's Fair Park",
            "p": "Flying directly into Knoxville's McGhee Tyson Airport (TYS) just 20 minutes from Downtown Knoxville—or serving nearby Blackberry Farm retreats—Adrian Saint delivers reliable, turnkey corporate entertainment."
        },
        "faqs": [
            {
                "q": "CAN ADRIAN HEADLINE CONFERENCES AT THE KNOXVILLE CONVENTION CENTER?",
                "a": "Yes! Adrian regularly headlines corporate general sessions, evening awards banquets, and trade conventions at the Knoxville Convention Center and Marriott Knoxville Downtown for audiences of 100 to 2,500+."
            },
            {
                "q": "HOW DO TRAVEL LOGISTICS WORK FOR KNOXVILLE AND EAST TENNESSEE EVENTS?",
                "a": "Adrian flies directly into McGhee Tyson Airport (TYS), located 20 minutes south of Downtown Knoxville via Alcoa Highway. All travel is turnkey and self-managed."
            },
            {
                "q": "IS ADRIAN'S SHOW A GREAT FIT FOR OAK RIDGE SCIENTIFIC, ENERGY & ENGINEERING GROUPS?",
                "a": "Absolutely. East Tennessee's deep concentration of engineers, researchers, and energy executives love Adrian's intelligent psychological demonstrations—100% clean and HR-approved."
            },
            {
                "q": "CAN ADRIAN PERFORM AT ULTRA-LUXURY RETREATS LIKE THE TENNESSEAN OR BLACKBERRY FARM?",
                "a": "Yes! Because Adrian requires zero bulky props, he performs intimate C-suite parlor mind reading shows seamlessly at The Tennessean Hotel, Cherokee Country Club, and Blackberry Farm."
            },
            {
                "q": "WHAT TECHNICAL SETUP DOES ADRIAN REQUIRE AT KNOXVILLE VENUES?",
                "a": "Adrian requires only a wireless handheld or lavalier microphone connected to room audio. For cocktail receptions at the Knoxville Museum of Art, strolling mentalism requires zero AV."
            }
        ]
    },
    {
        "slug": "vancouver",
        "city": "Vancouver",
        "state": "BC",
        "state_region": "BC",
        "state_full": "British Columbia",
        "country": "CA",
        "phone": "(833) 570-5966",
        "phone_clean": "18335705966",
        "phone_e164": "+18335705966",
        "badge": "📍 VANCOUVER CONVENTION CENTRE & COAL HARBOUR COVERAGE",
        "h1": "Corporate Magician &amp; Mentalist in <span class=\"hero-headline-highlight\">Vancouver</span> for Waterfront Conventions, Tech Summits &amp; Executive Galas",
        "subhead": "Delivering world-class psychological mentalism and interactive mind reading for international conventions at Vancouver Convention Centre, Coal Harbour galas, and cross-border executive summits.",
        "lat": 49.2827,
        "lon": -123.1207,
        "areas": ["Vancouver", "Coal Harbour", "Downtown Vancouver", "Yaletown", "Gastown", "Richmond", "Burnaby", "Metro Vancouver"],
        "venue_h2": "Serving the Award-Winning Vancouver Convention Centre &amp; Five-Star Waterfront Hotels",
        "venue_p": "Two-time winner of the World's Best Convention Centre and surrounded by Five-Star Coal Harbour hotels, Vancouver is one of North America's premier international destinations for corporate conventions and incentive summits.",
        "card1": {
            "sub": "WORLD-RENOWNED WATERFRONT CONVENTION CAMPUS",
            "title": "International Conventions & Flagship Keynotes",
            "items": [
                "Vancouver Convention Centre East & West (466,500 sq ft double LEED Platinum waterfront complex)",
                "VCC West Ballroom (52,000+ sq ft harbour-view ballroom for 3,000+ attendee keynotes & awards galas)",
                "Canada Place Sails of Light & Pan Pacific Convention Level (Iconic Burrard Inlet summit spaces)",
                "Queen Elizabeth Theatre & Orpheum Theatre (Premier downtown theatres for large corporate keynotes)"
            ]
        },
        "card2": {
            "sub": "COAL HARBOUR & DOWNTOWN FIVE-STAR HOTELS",
            "title": "Executive Summits & Black-Tie Banquets",
            "items": [
                "Fairmont Pacific Rim (Coal Harbour five-star flagship with Star Sapphire Ballroom & Chairman's Suite)",
                "Fairmont Hotel Vancouver (Historic 'Castle in the City' with the grand Pacific & Britishumbia Ballrooms)",
                "JW Marriott Parq Vancouver (Over 60,000 sq ft of luxury event space including the Parq Grand Ballroom)",
                "Rosewood Hotel Georgia & Paradox Hotel Vancouver (Boutique luxury hotels for C-suite board retreats)"
            ]
        },
        "card3": {
            "sub": "DISTINCTIVE VANCOUVER & WHISTLER VENUES",
            "title": "Cultural Galas & Harbour Receptions",
            "items": [
                "Vancouver Art Gallery & Museum of Anthropology at UBC (Architectural corporate gala receptions)",
                "Vancouver Aquarium in Stanley Park (Ocean gallery evening buyouts & VIP corporate dinners)",
                "Terminal City Club & Vancouver Club (Prestigious private business clubs in the Financial District)",
                "Fairmont Chateau Whistler & Four Seasons Resort Whistler (Sea-to-Sky alpine executive retreats)"
            ]
        },
        "callout": {
            "sub": "WEST COAST CROSS-BORDER EASE",
            "title": "Direct Nonstop Flights to Vancouver (YVR) • Same Pacific Time Zone",
            "p": "Flying nonstop from Southern California into Vancouver International Airport (YVR) in the exact same Pacific Time Zone—with zero freight customs carnet required because Adrian uses zero heavy props—cross-border booking is 100% effortless."
        },
        "faqs": [
            {
                "q": "CAN ADRIAN HEADLINE INTERNATIONAL CONVENTIONS AT THE VANCOUVER CONVENTION CENTRE (VCC)?",
                "a": "Yes! Adrian regularly headlines international association conventions, tech summits, and gala banquets at Vancouver Convention Centre East and West for audiences from 150 to over 3,500 attendees."
            },
            {
                "q": "HOW DO CROSS-BORDER TRAVEL AND CUSTOMS WORK FOR VANCOUVER EVENTS?",
                "a": "Because Adrian Saint performs psychological mentalism with zero bulky stage props or merchandise for sale, there are zero customs freight headaches. He flies nonstop from Southern California into YVR in the same Pacific Time Zone."
            },
            {
                "q": "IS ADRIAN'S SHOW 100% CLEAN AND SUITED FOR INTERNATIONAL & CANADIAN AUDIENCES?",
                "a": "Yes, 100%. Adrian's corporate show is clean, culturally astute, and HR-approved—celebrating attendees from across Canada, the US, and around the globe without ever embarrassing volunteers."
            },
            {
                "q": "WHAT TECHNICAL SETUP DOES ADRIAN REQUIRE AT FAIRMONT PACIFIC RIM OR JW MARRIOTT PARQ?",
                "a": "Adrian requires only a wireless handheld or lavalier microphone connected to house sound. He coordinates smoothly with Encore Canada and in-house hotel AV engineers."
            },
            {
                "q": "DOES ADRIAN ALSO PERFORM FOR EXECUTIVE RETREATS IN COAL HARBOUR OR WHISTLER?",
                "a": "Yes! In addition to downtown Vancouver convention keynotes, Adrian frequently performs strolling close-up mentalism and intimate after-dinner shows for executive retreats at Terminal City Club and Whistler resorts."
            }
        ]
    }
]

created_files = []

for c in GROUP_D_CITIES:
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
    desc_str = f"Book the top Corporate Magician & Mentalist in {city}, {state}. Adrian Saint delivers interactive mind reading for corporate conventions, headquarters summits, and executive galas."
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
        is_admin = any(k in a_name for k in ("County", "Metro", "Metroplex", "Area", "District", "Valley", "Corridor", "Eastside", "Michigan", "Tennessee"))
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
                "description": f"Adrian Saint is the premier corporate mentalist and mind reader in {city}, {state_full}, delivering interactive psychological entertainment for convention expos, corporate headquarters summits, and national galas.",
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

print(f"\nSuccessfully generated all {len(created_files)} Group D location pages!")
