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

GROUP_B_CITIES = [
    {
        "slug": "pittsburgh",
        "city": "Pittsburgh",
        "state": "PA",
        "state_full": "Pennsylvania",
        "country": "US",
        "phone": "(833) 570-5966",
        "phone_clean": "18335705966",
        "phone_e164": "+18335705966",
        "badge": "📍 PITTSBURGH METRO & LAWRENCE CONVENTION COVERAGE",
        "h1": "Corporate Magician &amp; Mentalist in <span class=\"hero-headline-highlight\">Pittsburgh</span> for Conventions, Steel City Galas &amp; Executive Summits",
        "subhead": "Delivering world-class psychological entertainment and interactive mind reading for corporate conventions, leadership summits, and gala banquets across Pittsburgh and Western Pennsylvania.",
        "lat": 40.4406,
        "lon": -79.9959,
        "areas": ["Pittsburgh", "Allegheny County", "Downtown Pittsburgh", "North Shore", "Strip District", "Oakland", "Western Pennsylvania"],
        "venue_h2": "Serving Pittsburgh's Premier Convention Centers &amp; Iconic Riverfront Venues",
        "venue_p": "From the LEED Platinum David L. Lawrence Convention Center to historic grand ballrooms, Pittsburgh combines industrial innovation with world-class corporate event infrastructure.",
        "card1": {
            "sub": "CONVENTION HUBS & EXHIBITION CENTERS",
            "title": "National Conventions & Steel City Galas",
            "items": [
                "David L. Lawrence Convention Center (1.5M sq ft LEED Platinum certified green convention complex)",
                "Spirit of Pittsburgh Grand Ballroom (Over 31,000 sq ft column-free gala and keynote hall)",
                "Stage AE & North Shore Waterfront Amphitheater (Corporate festivals & large receptions)",
                "Wyndham Grand Pittsburgh Downtown Ballroom (Over 17,000 sq ft prime meeting space)"
            ]
        },
        "card2": {
            "sub": "LUXURY CONFERENCE HOTELS & CLUBS",
            "title": "Executive Summits & Corporate Banquets",
            "items": [
                "Omni William Penn Hotel (Historic Grand Ballroom & Urban Room for black-tie galas)",
                "The Westin Pittsburgh (Connected directly via skywalk to Lawrence Convention Center)",
                "Fairmont Pittsburgh (Contemporary luxury boardrooms in Market Square)",
                "Duquesne Club (Prestigious private business club hosting executive leadership dinners)"
            ]
        },
        "card3": {
            "sub": "DISTINCTIVE PITTSBURGH EVENT SPACES",
            "title": "Private Banquets & Cultural Receptions",
            "items": [
                "Acrisure Stadium Champions Club & UPMC Club (Riverfront suites & VIP corporate dinners)",
                "Phipps Conservatory and Botanical Gardens (Stunning glasshouse corporate galas)",
                "Carnegie Museum of Art & Natural History (Majestic Music Hall Foyer & Grand Hall banquets)",
                "Heinz History Center (Unique multi-story museum and Great Hall corporate celebrations)"
            ]
        },
        "callout": {
            "sub": "TURNKEY FLY-IN CONVENTION EXPERTISE",
            "title": "Direct Pittsburgh International (PIT) Access • Effortless Production Delivery",
            "p": "Adrian Saint regularly travels nationwide for flagship corporate conferences. With direct flights into Pittsburgh International Airport (PIT) and convenient downtown hotel access, logistics are turnkey and seamless."
        },
        "faqs": [
            {
                "q": "CAN ADRIAN HEADLINE GENERAL SESSIONS AT DAVID L. LAWRENCE CONVENTION CENTER?",
                "a": "Yes! Adrian frequently headlines general sessions, opening keynotes, and evening awards banquets at David L. Lawrence Convention Center for audiences ranging from 150 to over 3,000 attendees."
            },
            {
                "q": "HOW DO TRAVEL LOGISTICS WORK FOR PITTSBURGH CORPORATE EVENTS?",
                "a": "Adrian Saint flies directly into Pittsburgh International Airport (PIT), located just 25 minutes from Downtown Pittsburgh. Turnkey travel coordination ensures early arrival and zero logistical friction for event organizers."
            },
            {
                "q": "IS THE PERFORMANCE 100% CLEAN AND APPROPRIATE FOR CORPORATE LEADERSHIP?",
                "a": "Yes, absolutely. Adrian's corporate show is 100% clean, intelligent, and HR-approved. He never uses embarrassing jokes or offensive humor, keeping your event prestigious and sophisticated."
            },
            {
                "q": "WHAT ARE ADRIAN'S TECHNICAL AND AV REQUIREMENTS AT PITTSBURGH HOTELS?",
                "a": "Adrian's rider is minimalist: a wireless handheld or lavalier microphone and standard house audio. He coordinates directly with in-house AV providers such as Encore at the Westin or Omni."
            },
            {
                "q": "DOES ADRIAN PERFORM AT PRIVATE EXECUTIVE DINNERS AND CLUBS IN PITTSBURGH?",
                "a": "Yes! In addition to large convention keynotes, Adrian frequently performs intimate after-dinner mind reading shows and strolling close-up mentalism for executive dinners at venues like the Duquesne Club and Fairmont."
            }
        ]
    },
    {
        "slug": "cincinnati",
        "city": "Cincinnati",
        "state": "OH",
        "state_full": "Ohio",
        "country": "US",
        "phone": "(833) 570-5966",
        "phone_clean": "18335705966",
        "phone_e164": "+18335705966",
        "badge": "📍 GREATER CINCINNATI & DUKE ENERGY CONVENTION COVERAGE",
        "h1": "Corporate Magician &amp; Mentalist in <span class=\"hero-headline-highlight\">Cincinnati</span> for Duke Energy Summits, Queen City Galas &amp; Banquets",
        "subhead": "Delivering interactive psychological entertainment and high-impact mind reading for corporate conferences, trade conventions, and executive galas across Cincinnati and Northern Kentucky.",
        "lat": 39.1031,
        "lon": -84.5120,
        "areas": ["Cincinnati", "Hamilton County", "Downtown Cincinnati", "Over-the-Rhine", "The Banks", "Northern Kentucky", "Greater Cincinnati"],
        "venue_h2": "Serving Cincinnati's Landmark Convention Facilities &amp; Historic Grand Ballrooms",
        "venue_p": "Home to numerous Fortune 500 headquarters and premier meeting venues, the Queen City offers an exceptional backdrop for corporate conferences and high-profile leadership events.",
        "card1": {
            "sub": "CONVENTION HUBS & CIVIC VENUES",
            "title": "Conventions & Flagship Galas",
            "items": [
                "Duke Energy Convention Center (750,000 sq ft exhibition complex in the heart of Downtown)",
                "Grand Ballroom at Duke Energy Center (40,000 sq ft pillar-free space for national keynote events)",
                "Northern Kentucky Convention Center (Waterfront meeting facility directly across the river)",
                "Sharonville Convention Center (Suburban Cincinnati's premier meeting & conference hub)"
            ]
        },
        "card2": {
            "sub": "HISTORIC LUXURY HOTELS & RESORTS",
            "title": "Executive Summits & Awards Dinners",
            "items": [
                "Hilton Cincinnati Netherland Plaza (Legendary French Art Deco Hall of Mirrors)",
                "The Westin Cincinnati (Overlooking historic Fountain Square with premier ballroom suites)",
                "21c Museum Hotel Cincinnati (Boutique contemporary art museum hotel for VIP retreats)",
                "The Lytle Park Hotel (Autograph Collection luxury hotel with rooftop terrace lounges)"
            ]
        },
        "card3": {
            "sub": "DISTINCTIVE QUEEN CITY EVENT SPACES",
            "title": "Private Banquets & Networking Receptions",
            "items": [
                "Cincinnati Music Hall Ballroom (Historic Victorian Gothic masterpiece for gala banquets)",
                "Great American Ball Park Champions Club (Exclusive riverfront corporate suites)",
                "The Phoenix (Historic neo-Renaissance private event venue in Downtown Cincinnati)",
                "Manor House Event Center (Mason luxury banquet campus for large corporate gatherings)"
            ]
        },
        "callout": {
            "sub": "EFFORTLESS FLY-IN CONVENTION DELIVERY",
            "title": "Direct CVG International Airport Access • Seamless Midwest Production",
            "p": "Adrian Saint provides turnkey entertainment delivery for Cincinnati corporate events. Arriving via Cincinnati/Northern Kentucky International Airport (CVG) just 15 minutes from downtown, Adrian ensures flawless punctuality and zero AV headaches."
        },
        "faqs": [
            {
                "q": "CAN ADRIAN HEADLINE EVENTS AT DUKE ENERGY CONVENTION CENTER IN CINCINNATI?",
                "a": "Yes! Adrian regularly headlines national corporate conventions, annual leadership meetings, and evening banquets at Duke Energy Convention Center for audiences from 150 to over 2,500 attendees."
            },
            {
                "q": "HOW DO TRAVEL LOGISTICS WORK FOR CINCINNATI CORPORATE GATHERINGS?",
                "a": "Adrian flies directly into Cincinnati/Northern Kentucky International Airport (CVG), providing rapid 15-minute access to downtown hotels and convention facilities with all-inclusive, turnkey travel logistics."
            },
            {
                "q": "IS THE PERFORMANCE HR-FRIENDLY AND RESPECTFUL TO EXECUTIVES?",
                "a": "Yes, 100%. Adrian's corporate show is completely clean, engaging, and dignified. He specializes in elevating corporate audiences without ever embarrassing volunteers or using off-color material."
            },
            {
                "q": "WHAT ARE ADRIAN'S AV REQUIREMENTS AT HILTON NETHERLAND PLAZA OR THE WESTIN?",
                "a": "Adrian requires only a wireless handheld or lavalier mic and standard connection to house sound. His minimalist footprint allows for rapid sound checks and zero staging complications."
            },
            {
                "q": "CAN ADRIAN PERFORM STROLLING MIND READING DURING CINCINNATI NETWORKING MIXERS?",
                "a": "Yes! Adrian's close-up strolling mentalism is ideal for cocktail hours, VIP receptions, and trade show booths, delivering personal mind-reading demonstrations right in guests' hands."
            }
        ]
    },
    {
        "slug": "milwaukee",
        "city": "Milwaukee",
        "state": "WI",
        "state_full": "Wisconsin",
        "country": "US",
        "phone": "(833) 570-5966",
        "phone_clean": "18335705966",
        "phone_e164": "+18335705966",
        "badge": "📍 MILWAUKEE METRO & BAIRD CENTER EXPANSION COVERAGE",
        "h1": "Corporate Magician &amp; Mentalist in <span class=\"hero-headline-highlight\">Milwaukee</span> for Baird Center Summits, Lakefront Galas &amp; Banquets",
        "subhead": "Delivering jaw-dropping psychological mentalism and interactive mind reading for corporate conventions, leadership retreats, and annual banquets across Milwaukee and Southeast Wisconsin.",
        "lat": 43.0389,
        "lon": -87.9065,
        "areas": ["Milwaukee", "Milwaukee County", "Downtown Milwaukee", "Historic Third Ward", "Lakefront", "Waukesha", "Southeast Wisconsin"],
        "venue_h2": "Serving Milwaukee's Expanded Baird Center &amp; Historic Lakefront Event Destinations",
        "venue_p": "With the transformative $456M expansion of the Baird Center and a vibrant cultural lakefront, Milwaukee has emerged as one of the Midwest's premier hubs for national corporate conventions.",
        "card1": {
            "sub": "EXPANDED CONVENTION CENTERS & CIVIC HUBS",
            "title": "National Conventions & Expo Galas",
            "items": [
                "Baird Center (Monumental $456M expanded convention campus with 1.3M sq ft of state-of-the-art space)",
                "Baird Center Rooftop Ballroom & Terrace (Panoramic city views for premier corporate galas)",
                "UW-Milwaukee Panther Arena (Multi-thousand attendee keynote and corporate rally arena)",
                "Miller High Life Theatre (Historic 4,000-seat theater for major corporate keynote productions)"
            ]
        },
        "card2": {
            "sub": "ICONIC LUXURY HOTELS & CLUBS",
            "title": "Executive Summits & Awards Dinners",
            "items": [
                "The Pfister Hotel (Historic Victorian luxury landmark with the ornate Grand Ballroom)",
                "Saint Kate - The Arts Hotel (Creative boutique hotel for high-end corporate retreats)",
                "Hilton Milwaukee City Center (Skywalk-connected to Baird Center with elegant Art Deco ballrooms)",
                "The University Club of Milwaukee (Exclusive lakefront business club for executive board dinners)"
            ]
        },
        "card3": {
            "sub": "DISTINCTIVE LAKEFRONT EVENT VENUES",
            "title": "Private Banquets & Architectural Galas",
            "items": [
                "Milwaukee Art Museum (Santiago Calatrava-designed Windhover Hall for unforgettable galas)",
                "Discovery World on Lake Michigan (Pilot Pavilion & Lake Michigan corporate terrace receptions)",
                "The Grain Exchange (Historic architectural gem with soaring 3-story cathedral ceilings)",
                "Harley-Davidson Museum Event Grounds (Industrial-chic corporate gatherings & private halls)"
            ]
        },
        "callout": {
            "sub": "RAPID MIDWEST CONVENTION MOBILITY",
            "title": "Direct Mitchell International (MKE) Access • Seamless Turnkey Delivery",
            "p": "Adrian Saint offers turnkey travel execution for Milwaukee corporate events. Flying directly into Milwaukee Mitchell International Airport (MKE) just 10 minutes from downtown, Adrian ensures effortless arrival, flawless timing, and zero AV stress."
        },
        "faqs": [
            {
                "q": "CAN ADRIAN HEADLINE MAJOR SESSIONS AT THE EXPANDED BAIRD CENTER IN MILWAUKEE?",
                "a": "Yes! Adrian is built for large convention crowds, delivering engaging general sessions and evening galas at the Baird Center for audiences ranging from 150 to over 3,000 attendees."
            },
            {
                "q": "HOW DO TRAVEL LOGISTICS WORK FOR MILWAUKEE CORPORATE RETREATS?",
                "a": "Adrian flies directly into Milwaukee Mitchell International Airport (MKE), located only 10 minutes from downtown hotels. His turnkey travel coordination ensures punctual arrival without hassle."
            },
            {
                "q": "IS ADRIAN'S MENTALISM SHOW 100% CLEAN AND HR-SAFE?",
                "a": "Yes, absolutely. Adrian's show is 100% clean, respectful, and sophisticated. He showcases incredible human potential and psychological feats without embarrassing guests or using blue humor."
            },
            {
                "q": "WHAT ARE ADRIAN'S AUDIOVISUAL SPECIFICATIONS AT THE PFISTER OR SAINT KATE?",
                "a": "Adrian requires only a wireless handheld or lavalier microphone patched into the venue sound system. His setup is completely self-contained, allowing for rapid sound checks."
            },
            {
                "q": "CAN ADRIAN CUSTOMIZE MENTALISM DEMONSTRATIONS FOR OUR MILWAUKEE EVENT?",
                "a": "Yes! Adrian can weave company milestones, product launches, or CEO messaging into his mind-reading routines, creating an unforgettable customized moment for your attendees."
            }
        ]
    },
    {
        "slug": "sacramento",
        "city": "Sacramento",
        "state": "CA",
        "state_full": "California",
        "country": "US",
        "phone": "(833) 570-5966",
        "phone_clean": "18335705966",
        "phone_e164": "+18335705966",
        "badge": "📍 SACRAMENTO METRO & SAFE CREDIT UNION CONVENTION COVERAGE",
        "h1": "Corporate Magician &amp; Mentalist in <span class=\"hero-headline-highlight\">Sacramento</span> for SAFE Credit Union Summits, Galas &amp; Association Banquets",
        "subhead": "Providing world-class psychological entertainment and interactive mind reading for corporate conferences, trade associations, and executive retreats across California's state capital.",
        "lat": 38.5816,
        "lon": -121.4944,
        "areas": ["Sacramento", "Sacramento County", "Downtown Commons", "DOCO", "Midtown Sacramento", "Capitol Mall", "Roseville", "Folsom", "Northern California"],
        "venue_h2": "Serving Sacramento's Modernized Convention Facilities &amp; Premier Downtown Venues",
        "venue_p": "As California's capital and a burgeoning tech and agriculture hub, Sacramento offers state-of-the-art event spaces centered around Downtown Commons (DOCO) and the Capitol Mall.",
        "card1": {
            "sub": "CONVENTION HUBS & CIVIC AUDITORIUMS",
            "title": "State Conventions & Association Galas",
            "items": [
                "SAFE Credit Union Convention Center (240,000 sq ft modernized downtown convention complex)",
                "SAFE Credit Union Performing Arts Center (2,400-seat theater for flagship corporate keynotes)",
                "Golden 1 Center Premium Lounges (Lexus Lounge & Assembly by Hartley for VIP receptions)",
                "Memorial Auditorium (Historic landmark venue with 3,800-seat main hall for major galas)"
            ]
        },
        "card2": {
            "sub": "CAPITOL DISTRICT LUXURY HOTELS",
            "title": "Executive Summits & Corporate Banquets",
            "items": [
                "Hyatt Regency Sacramento (Directly opposite the State Capitol with elegant ballroom space)",
                "Sheraton Grand Sacramento Hotel (Historic Public Market Building with spacious ballrooms)",
                "The Citizen Hotel, Autograph Collection (Boutique luxury hotel with Metropolitan Terrace)",
                "The Kimpton Sawyer Hotel (Chic DOCO rooftop pool deck and ballroom suites)"
            ]
        },
        "card3": {
            "sub": "HISTORIC & WATERFRONT EVENT RETREATS",
            "title": "Private Dinners & Leadership Offsites",
            "items": [
                "The Sutter Club (Prestigious private business club hosting executive board banquets)",
                "Vizcaya Sacramento (Historic Victorian estate and pavilion for intimate corporate celebrations)",
                "Old Sacramento Waterfront Event Centers (Unique Gold Rush ambiance for corporate mixers)",
                "Timber Creek Ballroom in Roseville (Spacious suburban venue for regional corporate gatherings)"
            ]
        },
        "callout": {
            "sub": "CALIFORNIA IN-STATE LOGISTICAL EASE",
            "title": "Direct Sacramento (SMF) Access • Reliable California In-State Mobility",
            "p": "Based in California, Adrian Saint travels seamlessly to Sacramento with direct flights or quick drives from Southern California. Event planners enjoy zero international border delays, prompt communication, and turnkey delivery."
        },
        "faqs": [
            {
                "q": "CAN ADRIAN HEADLINE ASSOCIATION CONFERENCES AT SAFE CREDIT UNION CONVENTION CENTER?",
                "a": "Yes! Adrian frequently headlines annual conferences, trade association banquets, and corporate general sessions at the SAFE Credit Union Convention Center for crowds of 150 to over 2,500."
            },
            {
                "q": "HOW DO TRAVEL LOGISTICS WORK FOR SACRAMENTO CORPORATE EVENTS?",
                "a": "Adrian flies directly into Sacramento International Airport (SMF), just 15 minutes north of Downtown Sacramento, or coordinates quick in-state flights from Southern California airports."
            },
            {
                "q": "IS ADRIAN'S CORPORATE SHOW APPROPRIATE FOR GOVERNMENT & ASSOCIATION AUDIENCES?",
                "a": "Yes, 100%. Adrian's corporate presentation is completely clean, dignified, and HR-safe. He engages attendees with intelligence and humor without putting anyone on the spot."
            },
            {
                "q": "WHAT ARE ADRIAN'S TECHNICAL AUDIO REQUIREMENTS AT HYATT REGENCY SACRAMENTO?",
                "a": "Adrian requires only a wireless handheld or lavalier microphone connected to house sound. He works smoothly with hotel AV staff to execute rapid sound checks before doors open."
            },
            {
                "q": "DOES ADRIAN PERFORM FOR PRIVATE LEGISLATIVE OR EXECUTIVE DINNERS IN SACRAMENTO?",
                "a": "Yes! Adrian regularly performs strolling close-up mentalism for cocktail receptions and intimate after-dinner shows for executive board dinners at venues like The Sutter Club and The Citizen."
            }
        ]
    },
    {
        "slug": "raleigh",
        "city": "Raleigh",
        "state": "NC",
        "state_full": "North Carolina",
        "country": "US",
        "phone": "(833) 570-5966",
        "phone_clean": "18335705966",
        "phone_e164": "+18335705966",
        "badge": "📍 RESEARCH TRIANGLE & RALEIGH CONVENTION COVERAGE",
        "h1": "Corporate Magician &amp; Mentalist in <span class=\"hero-headline-highlight\">Raleigh</span> for Research Triangle Summits, Tech Galas &amp; Conferences",
        "subhead": "Delivering sophisticated psychological mentalism and interactive mind reading for corporate conventions, life sciences summits, and tech banquets across Raleigh and the Research Triangle.",
        "lat": 35.7796,
        "lon": -78.6382,
        "areas": ["Raleigh", "Wake County", "Downtown Raleigh", "Research Triangle Park", "RTP", "North Hills", "Cary", "Durham", "North Carolina"],
        "venue_h2": "Serving Raleigh's Research Triangle Tech Hub &amp; Premier Convention Facilities",
        "venue_p": "At the nexus of technology, healthcare, and higher education, Raleigh offers state-of-the-art convention infrastructure and luxury retreat resorts throughout the Research Triangle.",
        "card1": {
            "sub": "CONVENTION HUBS & CIVIC VENUES",
            "title": "National Conventions & Tech Summits",
            "items": [
                "Raleigh Convention Center (500,000 sq ft modern facility with shimmering Cree Shimmer Wall)",
                "Raleigh Convention Center Grand Ballroom (32,000 sq ft space for national conference banquets)",
                "Martin Marietta Center for the Performing Arts (Four dedicated theaters for major corporate keynotes)",
                "Lenovo Center (Formerly PNC Arena - arena-scale corporate celebrations and suites)"
            ]
        },
        "card2": {
            "sub": "LUXURY CONFERENCE RESORTS & HOTELS",
            "title": "Executive Summits & Corporate Banquets",
            "items": [
                "The Umstead Hotel and Spa (Five-Star luxury sanctuary in Cary for elite executive retreats)",
                "Raleigh Marriott City Center (Connected directly to Raleigh Convention Center)",
                "The StateView Hotel, Autograph Collection (Scenic lakeside corporate retreat on NC State campus)",
                "Renaissance Raleigh North Hills Hotel (Upscale mixed-use district hotel with premier ballrooms)"
            ]
        },
        "card3": {
            "sub": "DISTINCTIVE TRIANGLE EVENT SPACES",
            "title": "Private Banquets & Cultural Venues",
            "items": [
                "Angus Barn Pavilions (Legendary Lakeside Pavilion for Southern hospitality corporate banquets)",
                "Contemporary Art Museum (CAM Raleigh - dramatic open gallery space for modern corporate galas)",
                "North Carolina Museum of Art (West Building & park amphitheater for architectural receptions)",
                "Prestonwood Country Club in Cary (Championship golf clubhouse for executive corporate outings)"
            ]
        },
        "callout": {
            "sub": "RESEARCH TRIANGLE FLY-IN EXPERTISE",
            "title": "Direct RDU International Airport Access • Seamless Midwest & East Coast Travel",
            "p": "Adrian Saint brings turnkey entertainment to Raleigh and Research Triangle events. Flying directly into Raleigh-Durham International Airport (RDU) just 15 minutes from downtown, Adrian ensures effortless logistics, guaranteed punctuality, and zero production stress."
        },
        "faqs": [
            {
                "q": "CAN ADRIAN HEADLINE TECH CONFERENCES AT RALEIGH CONVENTION CENTER?",
                "a": "Yes! Adrian frequently headlines major corporate summits, life sciences galas, and technology conferences at Raleigh Convention Center for crowds from 150 to over 3,000 attendees."
            },
            {
                "q": "HOW DO TRAVEL LOGISTICS WORK FOR RALEIGH & RESEARCH TRIANGLE EVENTS?",
                "a": "Adrian flies directly into Raleigh-Durham International Airport (RDU), centrally located between Raleigh, Durham, and RTP. All travel arrangements are self-contained and turnkey."
            },
            {
                "q": "IS ADRIAN'S PERFORMANCE FIT FOR TECH AND SCIENTIFIC EXECUTIVES?",
                "a": "Absolutely. Adrian's demonstrations explore human psychology, influence, and intuition, resonating powerfully with analytical, tech, and engineering minds while remaining 100% clean and HR-safe."
            },
            {
                "q": "WHAT ARE ADRIAN'S AV REQUIREMENTS AT THE UMSTEAD OR MARRIOTT CITY CENTER?",
                "a": "Adrian requires only a wireless handheld or lavalier microphone plugged into the venue audio system. There are no heavy props or complicated staging requirements."
            },
            {
                "q": "DOES ADRIAN PERFORM STROLLING MIND READING FOR RESEARCH TRIANGLE MIXERS?",
                "a": "Yes! Adrian's strolling mentalism is in high demand for cocktail hours, VIP networking mixers, and vendor receptions, engaging small groups with mind-boggling interactive demonstrations."
            }
        ]
    },
    {
        "slug": "richmond",
        "city": "Richmond",
        "state": "VA",
        "state_full": "Virginia",
        "country": "US",
        "phone": "(833) 570-5966",
        "phone_clean": "18335705966",
        "phone_e164": "+18335705966",
        "badge": "📍 GREATER RICHMOND & CONVENTION CENTER COVERAGE",
        "h1": "Corporate Magician &amp; Mentalist in <span class=\"hero-headline-highlight\">Richmond</span> for Convention Summits, Historic Galas &amp; Banquets",
        "subhead": "Delivering world-class psychological entertainment and interactive mind reading for corporate conventions, Fortune 500 summits, and leadership banquets across Richmond and Central Virginia.",
        "lat": 37.5407,
        "lon": -77.4360,
        "areas": ["Richmond", "Henrico County", "Chesterfield County", "Downtown Richmond", "Shockoe Slip", "Shockoe Bottom", "Short Pump", "Central Virginia"],
        "venue_h2": "Serving Virginia's Premier Convention Facilities &amp; Historic Grand Venues",
        "venue_p": "With the state's largest convention center, multiple Fortune 500 headquarters, and iconic historic hotels, Richmond provides a magnificent setting for corporate conferences and executive events.",
        "card1": {
            "sub": "CONVENTION CENTERS & CIVIC HUBS",
            "title": "State Conventions & Regional Summits",
            "items": [
                "Greater Richmond Convention Center (700,000 sq ft, the largest meeting facility in Virginia)",
                "Exhibit Hall Pavilion at GRCC (178,000 sq ft pillarless space for major trade shows and galas)",
                "Main Street Station Train Shed (Breathtaking 100,000 sq ft glass-enclosed historic event space)",
                "Altria Theater (Historic 3,500-seat theater in Monroe Park for flagship corporate presentations)"
            ]
        },
        "card2": {
            "sub": "HISTORIC 5-STAR HOTELS & RESORTS",
            "title": "Executive Summits & Awards Banquets",
            "items": [
                "The Jefferson Hotel (Historic Five-Star landmark with Rotunda, Palm Court, and Grand Ballroom)",
                "Omni Richmond Hotel (Prime Shockoe Slip location with James River Ballroom suites)",
                "Hilton Richmond Downtown (Historic Miller & Rhoads building with stylish event halls)",
                "The Commonwealth (Boutique hotel across from the Virginia State Capitol for executive dinners)"
            ]
        },
        "card3": {
            "sub": "DISTINCTIVE ESTATES & CULTURAL CENTERS",
            "title": "Private Banquets & Leadership Retreats",
            "items": [
                "Dover Hall Estate in Goochland (Tudor mansion estate for premier executive leadership retreats)",
                "Virginia Museum of Fine Arts (VMFA Marble Hall and sculpture garden corporate receptions)",
                "Science Museum of Virginia Dewey Gottwald Center (Modern architectural event pavilion)",
                "Country Club of Virginia (Historic Westhampton and James River clubhouse galas)"
            ]
        },
        "callout": {
            "sub": "MID-ATLANTIC FLY-IN MOBILITY",
            "title": "Direct Richmond International (RIC) Access • Effortless Turnkey Production",
            "p": "Adrian Saint provides seamless fly-in delivery for Richmond events. Arriving via Richmond International Airport (RIC) just 15 minutes from downtown, Adrian ensures guaranteed on-time arrival and zero production headaches."
        },
        "faqs": [
            {
                "q": "CAN ADRIAN HEADLINE EVENTS AT GREATER RICHMOND CONVENTION CENTER?",
                "a": "Yes! Adrian frequently headlines annual corporate conventions, trade shows, and awards banquets at Greater Richmond Convention Center for groups from 150 to over 2,500 guests."
            },
            {
                "q": "HOW DO TRAVEL LOGISTICS WORK FOR RICHMOND CORPORATE GATHERINGS?",
                "a": "Adrian flies directly into Richmond International Airport (RIC), located 15 minutes from downtown Richmond hotels. Turnkey travel coordination means no logistical stress for meeting planners."
            },
            {
                "q": "IS ADRIAN'S CORPORATE SHOW 100% CLEAN AND APPROPRIATE FOR EXECUTIVES?",
                "a": "Yes, absolutely. Adrian's corporate show is 100% clean, polished, and HR-safe. He engages company leadership respectfully without ever embarrassing participants."
            },
            {
                "q": "WHAT ARE ADRIAN'S AUDIOVISUAL SPECIFICATIONS AT THE JEFFERSON HOTEL?",
                "a": "Adrian's rider requires only a wireless handheld or lavalier mic patched into room sound. He coordinates directly with hotel AV teams for rapid sound checks."
            },
            {
                "q": "DOES ADRIAN PERFORM AT PRIVATE EXECUTIVE RETREATS AT DOVER HALL OR COUNTRY CLUBS?",
                "a": "Yes! Adrian frequently performs close-up mentalism for cocktail receptions and intimate after-dinner shows for executive board retreats at venues like Dover Hall and The Country Club of Virginia."
            }
        ]
    },
    {
        "slug": "memphis",
        "city": "Memphis",
        "state": "TN",
        "state_full": "Tennessee",
        "country": "US",
        "phone": "(833) 570-5966",
        "phone_clean": "18335705966",
        "phone_e164": "+18335705966",
        "badge": "📍 MEMPHIS METRO & RENASANT CONVENTION COVERAGE",
        "h1": "Corporate Magician &amp; Mentalist in <span class=\"hero-headline-highlight\">Memphis</span> for Renasant Convention Summits, Galas &amp; Banquets",
        "subhead": "Delivering unforgettable psychological mentalism and interactive mind reading for corporate conventions, logistics summits, and executive banquets across Memphis and the Mid-South.",
        "lat": 35.1495,
        "lon": -90.0490,
        "areas": ["Memphis", "Shelby County", "Downtown Memphis", "Beale Street", "East Memphis", "Germantown", "Mid-South Tennessee"],
        "venue_h2": "Serving Memphis's Riverfront Convention Centers &amp; Iconic Southern Landmarks",
        "venue_p": "As America's global distribution hub and a cultural icon along the Mississippi River, Memphis features premier convention spaces, legendary historic hotels, and vibrant entertainment venues.",
        "card1": {
            "sub": "CONVENTION HUBS & RIVERFRONT VENUES",
            "title": "National Conventions & Flagship Galas",
            "items": [
                "Renasant Convention Center (Modernized 350,000 sq ft facility overlooking the Mississippi River)",
                "Grand Ballroom at Renasant Center (28,000 sq ft space with floor-to-ceiling riverfront views)",
                "Cannon Center for the Performing Arts (Acoustically superior 2,100-seat corporate keynote hall)",
                "FedExForum Hospitality Suites & Arenas (Corporate keynote productions & executive suites)"
            ]
        },
        "card2": {
            "sub": "LEGENDARY LUXURY HOTELS & CLUBS",
            "title": "Executive Summits & Corporate Banquets",
            "items": [
                "The Peabody Memphis (World-famous luxury landmark with Continental and Grand Ballrooms)",
                "The Guest House at Graceland (Upscale resort with 450-seat theater and grand ballroom)",
                "The Westin Memphis Beale Street (Located directly across from FedExForum in downtown)",
                "Hu. Hotel (Boutique downtown luxury hotel with stunning rooftop riverfront lounges)"
            ]
        },
        "card3": {
            "sub": "DISTINCTIVE BLUES CITY EVENT SPACES",
            "title": "Private Banquets & Cultural Receptions",
            "items": [
                "The Columns at One Commerce Square (Historic 1920s bank hall with soaring Ionic pillars)",
                "Memphis Botanic Garden (Hardin Hall and outdoor corporate banquet pavilions)",
                "National Civil Rights Museum Event Hall (Inspiring setting for corporate leadership dinners)",
                "Memphis Brooks Museum of Art (Contemporary corporate galas in Overton Park)"
            ]
        },
        "callout": {
            "sub": "LOGISTICS HUB FLY-IN ADVANTAGE",
            "title": "Direct Memphis International (MEM) Access • Turnkey Production Delivery",
            "p": "As the home of global logistics, Memphis is effortlessly accessible. Adrian Saint flies directly into Memphis International Airport (MEM) just 15 minutes from downtown, delivering turnkey corporate entertainment with guaranteed punctuality."
        },
        "faqs": [
            {
                "q": "CAN ADRIAN HEADLINE EVENTS AT RENASANT CONVENTION CENTER IN MEMPHIS?",
                "a": "Yes! Adrian frequently headlines corporate general sessions, trade show banquets, and annual conferences at Renasant Convention Center for audiences of 150 to over 3,000 attendees."
            },
            {
                "q": "HOW DO TRAVEL LOGISTICS WORK FOR MEMPHIS CORPORATE MEETINGS?",
                "a": "Adrian flies directly into Memphis International Airport (MEM), located just 15 minutes from downtown convention hotels. All travel is turnkey and self-contained."
            },
            {
                "q": "IS THE PERFORMANCE 100% CLEAN AND SAFE FOR CORPORATE AUDIENCES?",
                "a": "Yes, 100%. Adrian's corporate show is completely clean, intelligent, and HR-approved. He creates astonishment through psychology and mind reading without embarrassing anyone."
            },
            {
                "q": "WHAT ARE ADRIAN'S AUDIOVISUAL REQUIREMENTS AT THE PEABODY MEMPHIS?",
                "a": "Adrian requires only a wireless handheld or lavalier mic patched into house sound. He works smoothly with hotel AV staff, requiring minimal setup and sound check time."
            },
            {
                "q": "DOES ADRIAN PERFORM STROLLING CLOSE-UP MIND READING DURING COCKTAIL RECEPTIONS?",
                "a": "Yes! Adrian's strolling mentalism is perfect for corporate networking hours, cocktail receptions, and VIP hospitality suites, creating personal moments of wonder inches from guests."
            }
        ]
    },
    {
        "slug": "detroit",
        "city": "Detroit",
        "state": "MI",
        "state_full": "Michigan",
        "country": "US",
        "phone": "(833) 570-5966",
        "phone_clean": "18335705966",
        "phone_e164": "+18335705966",
        "badge": "📍 METRO DETROIT & HUNTINGTON PLACE CONVENTION COVERAGE",
        "h1": "Corporate Magician &amp; Mentalist in <span class=\"hero-headline-highlight\">Detroit</span> for Huntington Place Summits, Automotive Galas &amp; Banquets",
        "subhead": "Delivering electrifying psychological entertainment and interactive mind reading for automotive summits, corporate conventions, and executive galas across Detroit and Southeast Michigan.",
        "lat": 42.3314,
        "lon": -83.0458,
        "areas": ["Detroit", "Wayne County", "Downtown Detroit", "Midtown Detroit", "Corktown", "Dearborn", "Oakland County", "Southeast Michigan"],
        "venue_h2": "Serving Metro Detroit's World-Class Convention Centers &amp; Restored Architectural Gems",
        "venue_p": "With the iconic Huntington Place Convention Center, booming mobility and tech sectors, and revitalized Art Deco landmarks, Detroit stands as a powerhouse for national corporate gatherings.",
        "card1": {
            "sub": "WORLD-RENOWNED CONVENTION CENTERS",
            "title": "International Conventions & Automotive Summits",
            "items": [
                "Huntington Place Convention Center (2.4M sq ft global convention complex along the Detroit River)",
                "Grand Riverview Ballroom at Huntington Place (40,000 sq ft space with panoramic river views)",
                "Suburban Collection Showplace in Novi (Over 300,000 sq ft for suburban Detroit corporate expos)",
                "Fox Theatre Detroit (Spectacular 5,000-seat theater for flagship corporate presentations)"
            ]
        },
        "card2": {
            "sub": "HISTORIC LUXURY & BOUTIQUE HOTELS",
            "title": "Executive Summits & Corporate Banquets",
            "items": [
                "The Westin Book Cadillac Detroit (Restored historic landmark with Italian Renaissance ballrooms)",
                "Detroit Foundation Hotel (Iconic former fire department HQ turned luxury boutique retreat)",
                "Shinola Hotel (Chic downtown boutique hotel with Biddle Building event hall)",
                "MGM Grand Detroit Event Center (30,000 sq ft luxury ballroom for black-tie corporate galas)"
            ]
        },
        "card3": {
            "sub": "ICONIC MOTOR CITY EVENT SPACES",
            "title": "Private Banquets & Cultural Venues",
            "items": [
                "The Henry Ford Museum & Greenfield Village (Magnificent venue for automotive corporate galas)",
                "Detroit Institute of Arts (Diego Rivera Court for unforgettable corporate banquets)",
                "Gem Theatre & Century Club (Charming historic venue for executive meetings & entertainment)",
                "Detroit Athletic Club (Historic private business club overlooking Comerica Park)"
            ]
        },
        "callout": {
            "sub": "GLOBAL HUB FLY-IN ADVANTAGE",
            "title": "Direct Detroit Metro (DTW) Access • Turnkey Production Delivery",
            "p": "Adrian Saint provides turnkey entertainment delivery for Detroit corporate events. Flying directly into Detroit Metropolitan Wayne County Airport (DTW), Adrian ensures effortless travel, reliable timing, and zero production stress."
        },
        "faqs": [
            {
                "q": "CAN ADRIAN HEADLINE MAJOR SESSIONS AT HUNTINGTON PLACE IN DETROIT?",
                "a": "Yes! Adrian frequently headlines major corporate general sessions, automotive industry banquets, and national conventions at Huntington Place for crowds from 150 to over 3,500."
            },
            {
                "q": "HOW DO TRAVEL LOGISTICS WORK FOR DETROIT CORPORATE EVENTS?",
                "a": "Adrian flies directly into Detroit Metropolitan Wayne County Airport (DTW), one of the nation's premier hubs, providing rapid 20-minute highway access to Downtown Detroit."
            },
            {
                "q": "IS ADRIAN'S SHOW 100% CLEAN AND APPROPRIATE FOR AUTOMOTIVE & TECH EXECUTIVES?",
                "a": "Yes, absolutely. Adrian's show is 100% clean, intelligent, and HR-approved. He showcases incredible mental demonstrations that captivate engineers, executives, and leaders alike."
            },
            {
                "q": "WHAT ARE ADRIAN'S TECHNICAL AV REQUIREMENTS AT THE WESTIN BOOK CADILLAC?",
                "a": "Adrian requires only a wireless handheld or lavalier microphone connected to house audio. His streamlined setup allows for quick sound checks without disrupting event schedules."
            },
            {
                "q": "DOES ADRIAN PERFORM STROLLING MIND READING FOR DETROIT NETWORKING RECEPTIONS?",
                "a": "Yes! Adrian's strolling close-up mentalism is in high demand for cocktail hours, VIP lounges, and automotive VIP receptions, performing impossible mind-reading feats up close."
            }
        ]
    },
    {
        "slug": "tucson",
        "city": "Tucson",
        "state": "AZ",
        "state_full": "Arizona",
        "country": "US",
        "phone": "(833) 570-5966",
        "phone_clean": "18335705966",
        "phone_e164": "+18335705966",
        "badge": "📍 TUCSON RESORT & CONVENTION COVERAGE",
        "h1": "Corporate Magician &amp; Mentalist in <span class=\"hero-headline-highlight\">Tucson</span> for Resort Summits, Desert Galas &amp; Executive Retreats",
        "subhead": "Delivering world-class psychological entertainment and interactive mind reading for corporate conferences, luxury resort retreats, and executive banquets across Tucson and Southern Arizona.",
        "lat": 32.2226,
        "lon": -110.9747,
        "areas": ["Tucson", "Pima County", "Downtown Tucson", "Catalina Foothills", "Oro Valley", "Marana", "Southern Arizona"],
        "venue_h2": "Serving Tucson's Luxury Sonoran Desert Resorts &amp; Modern Convention Center",
        "venue_p": "Framed by the majestic Santa Catalina Mountains, Tucson is renowned for its world-class luxury golf resorts and expanded convention facilities, hosting premier corporate meetings year-round.",
        "card1": {
            "sub": "CONVENTION HUBS & CIVIC VENUES",
            "title": "Conventions & Regional Summits",
            "items": [
                "Tucson Convention Center (205,000 sq ft exhibition and arena complex in Downtown Tucson)",
                "TCC Grand Ballroom & Leo Rich Theater (Intimate theater & spacious banquet spaces)",
                "Fox Tucson Theatre (Historic 1,164-seat Southwestern Art Deco theater for keynote events)",
                "Linda Ronstadt Music Hall (2,200-seat performing arts hall for large corporate productions)"
            ]
        },
        "card2": {
            "sub": "LUXURY DESERT RESORTS & RETREATS",
            "title": "Executive Summits & Corporate Banquets",
            "items": [
                "JW Marriott Tucson Starr Pass Resort & Spa (88,000 sq ft indoor/outdoor mountain-view meeting space)",
                "Loews Ventana Canyon Resort (Catalina Foothills luxury resort with 37,000 sq ft of event space)",
                "The Ritz-Carlton, Dove Mountain in Marana (Forbes Five-Star desert luxury for elite leadership retreats)",
                "The Westin La Paloma Resort & Spa (Stunning Sonoran golf resort with spacious ballrooms)"
            ]
        },
        "card3": {
            "sub": "DISTINCTIVE SONORAN EVENT DESTINATIONS",
            "title": "Private Banquets & Cultural Receptions",
            "items": [
                "Omni Tucson National Resort (Championship golf resort hosting executive corporate banquets)",
                "Westward Look Wyndham Grand Resort & Spa (Historic 80-acre foothills retreat)",
                "Arizona-Sonora Desert Museum Event Grounds (Unique outdoor corporate galas under desert skies)",
                "Pima Air & Space Museum Event Hangars (Spectacular aviation backdrops for major corporate dinners)"
            ]
        },
        "callout": {
            "sub": "SOUTHWEST REGIONAL FLY-IN MOBILITY",
            "title": "Direct Tucson (TUS) Access • 90 Minutes from Phoenix Sky Harbor (PHX)",
            "p": "Adrian Saint frequently performs throughout Arizona. With direct flights into Tucson International Airport (TUS) or quick transfers from Phoenix Sky Harbor (PHX), logistics are simple, reliable, and turnkey."
        },
        "faqs": [
            {
                "q": "CAN ADRIAN HEADLINE RESORT CONFERENCES AT JW MARRIOTT STARR PASS OR LOEWS VENTANA CANYON?",
                "a": "Yes! Adrian frequently headlines corporate conferences, annual incentive trips, and evening banquets at Tucson's premier Sonoran resorts for audiences from 100 to over 1,500."
            },
            {
                "q": "HOW DO TRAVEL LOGISTICS WORK FOR TUCSON CORPORATE EVENTS?",
                "a": "Adrian flies directly into Tucson International Airport (TUS) or Phoenix Sky Harbor (PHX) with convenient ground transfer. Turnkey travel ensures prompt arrival without hassle."
            },
            {
                "q": "IS THE PERFORMANCE 100% CLEAN AND APPROPRIATE FOR EXECUTIVES & SPOUSES?",
                "a": "Yes, 100%. Adrian's corporate show is completely clean, intelligent, and HR-safe. It is particularly popular for executive retreats and spouse-inclusive evening galas."
            },
            {
                "q": "WHAT ARE ADRIAN'S AV REQUIREMENTS AT THE RITZ-CARLTON DOVE MOUNTAIN?",
                "a": "Adrian requires only a wireless handheld or lavalier microphone patched into room audio. His setup is completely self-contained, allowing for rapid sound checks."
            },
            {
                "q": "DOES ADRIAN PERFORM STROLLING CLOSE-UP MENTALISM FOR TUCSON PATIO MIXERS?",
                "a": "Yes! Adrian's strolling mentalism is perfect for outdoor Sonoran desert terrace receptions, cocktail mixers, and VIP hospitality gatherings, delivering jaw-dropping mind reading up close."
            }
        ]
    },
    {
        "slug": "oklahoma-city",
        "city": "Oklahoma City",
        "state": "OK",
        "state_full": "Oklahoma",
        "country": "US",
        "phone": "(833) 570-5966",
        "phone_clean": "18335705966",
        "phone_e164": "+18335705966",
        "badge": "📍 OKC METRO & CONVENTION CENTER COVERAGE",
        "h1": "Corporate Magician &amp; Mentalist in <span class=\"hero-headline-highlight\">Oklahoma City</span> for Convention Summits, Galas &amp; Energy Banquets",
        "subhead": "Delivering interactive psychological entertainment and high-impact mind reading for corporate conventions, energy summits, and executive galas across Oklahoma City and Central Oklahoma.",
        "lat": 35.4676,
        "lon": -97.5164,
        "areas": ["Oklahoma City", "Oklahoma County", "Downtown OKC", "Bricktown", "Scissortail Park", "Midtown OKC", "Edmond", "Central Oklahoma"],
        "venue_h2": "Serving Oklahoma City's State-of-the-Art Convention Campus &amp; Downtown Venues",
        "venue_p": "With the modern $288M Oklahoma City Convention Center, the Omni OKC headquarters hotel, and vibrant Bricktown entertainment, OKC has become a premier destination for national corporate events.",
        "card1": {
            "sub": "MODERN CONVENTION CENTERS & CIVIC HUBS",
            "title": "National Conventions & Flagship Galas",
            "items": [
                "Oklahoma City Convention Center (Brand new 500,000 sq ft state-of-the-art convention complex)",
                "OKCCC Grand Ballroom (30,000 sq ft space with floor-to-ceiling glass overlooking Scissortail Park)",
                "Paycom Center (Arena-scale corporate rallies and private executive suites in Downtown OKC)",
                "The Criterion in Bricktown (Modern multi-level event center for large corporate gatherings)"
            ]
        },
        "card2": {
            "sub": "FLAGSHIP LUXURY HOTELS & RESORTS",
            "title": "Executive Summits & Corporate Banquets",
            "items": [
                "Omni Oklahoma City Hotel (Flagship 605-room convention hotel with 76,000 sq ft of meeting space)",
                "The Skirvin Hilton Oklahoma City (Historic luxury landmark with the ornate Venetian Ballroom)",
                "Colcord Hotel (Downtown boutique luxury hotel in a historic 1910 skyscraper)",
                "Renaissance Waterford Oklahoma City Hotel (Premier suburban corporate retreat in Northwest OKC)"
            ]
        },
        "card3": {
            "sub": "DISTINCTIVE OKC EVENT SPACES",
            "title": "Private Banquets & Cultural Venues",
            "items": [
                "National Cowboy & Western Heritage Museum (Majestic Great Hall for iconic corporate galas)",
                "First Americans Museum (FAM - striking contemporary architecture for VIP corporate dinners)",
                "Oklahoma City Museum of Art (Chihuly glass atrium for elegant corporate receptions)",
                "The Jones Assembly (Spacious industrial-chic venue in Film Row for dynamic corporate events)"
            ]
        },
        "callout": {
            "sub": "CENTRAL US FLY-IN CONVENIENCE",
            "title": "Direct Will Rogers World Airport (OKC) Access • Turnkey Production Delivery",
            "p": "Adrian Saint provides turnkey entertainment delivery for Oklahoma City corporate events. Flying directly into Will Rogers World Airport (OKC) just 15 minutes from downtown, Adrian ensures effortless travel, guaranteed timing, and zero production stress."
        },
        "faqs": [
            {
                "q": "CAN ADRIAN HEADLINE EVENTS AT OKLAHOMA CITY CONVENTION CENTER?",
                "a": "Yes! Adrian frequently headlines national corporate conferences, annual energy summits, and evening banquets at OKCCC for crowds ranging from 150 to over 3,000 attendees."
            },
            {
                "q": "HOW DO TRAVEL LOGISTICS WORK FOR OKLAHOMA CITY CORPORATE EVENTS?",
                "a": "Adrian flies directly into Will Rogers World Airport (OKC), located only 15 minutes from downtown convention hotels. His travel arrangements are turnkey and completely self-managed."
            },
            {
                "q": "IS ADRIAN'S PERFORMANCE 100% CLEAN AND HR-SAFE?",
                "a": "Yes, absolutely. Adrian's show is 100% clean, professional, and HR-safe. He never embarrasses audience members, making him the ideal choice for corporate banquets and executive retreats."
            },
            {
                "q": "WHAT ARE ADRIAN'S AV REQUIREMENTS AT THE OMNI OKC OR THE SKIRVIN?",
                "a": "Adrian requires only a wireless handheld or lavalier microphone patched into room audio. His setup is completely self-contained, allowing for rapid sound checks."
            },
            {
                "q": "DOES ADRIAN PERFORM STROLLING CLOSE-UP MENTALISM FOR OKC RECEPTIONS?",
                "a": "Yes! Adrian's strolling mentalism is in high demand for cocktail mixers, VIP receptions, and trade show booths, delivering personal mind-reading demonstrations right in guests' hands."
            }
        ]
    },
    {
        "slug": "omaha",
        "city": "Omaha",
        "state": "NE",
        "state_full": "Nebraska",
        "country": "US",
        "phone": "(833) 570-5966",
        "phone_clean": "18335705966",
        "phone_e164": "+18335705966",
        "badge": "📍 OMAHA METRO & CHI HEALTH CENTER COVERAGE",
        "h1": "Corporate Magician &amp; Mentalist in <span class=\"hero-headline-highlight\">Omaha</span> for CHI Health Center Summits, Shareholder Galas &amp; Banquets",
        "subhead": "Delivering world-class psychological entertainment and interactive mind reading for corporate conventions, executive shareholder summits, and awards galas across Omaha and Eastern Nebraska.",
        "lat": 41.2565,
        "lon": -95.9345,
        "areas": ["Omaha", "Douglas County", "Downtown Omaha", "Old Market", "Capitol District", "Blackstone District", "West Omaha", "Eastern Nebraska"],
        "venue_h2": "Serving Omaha's Renowned Convention Center &amp; Vibrant Downtown Districts",
        "venue_p": "Famed as the home of Fortune 500 giants and the annual Berkshire Hathaway gathering, Omaha boasts world-class convention infrastructure, historic Old Market charm, and premier luxury hotels.",
        "card1": {
            "sub": "CONVENTION CENTERS & CIVIC HUBS",
            "title": "National Conventions & Shareholder Summits",
            "items": [
                "CHI Health Center Omaha (1.1M sq ft convention center and arena hosting national summits)",
                "CHI Health Center Grand Ballroom (30,900 sq ft space for flagship corporate banquets)",
                "Mid-America Center in Council Bluffs (Suburban metro convention center with 64,000 sq ft)",
                "Holland Performing Arts Center (Acoustically pristine hall for corporate keynote events)"
            ]
        },
        "card2": {
            "sub": "DOWNTOWN LUXURY & BOUTIQUE HOTELS",
            "title": "Executive Summits & Corporate Banquets",
            "items": [
                "Omaha Marriott Downtown at the Capitol District (Over 20,000 sq ft of meeting space)",
                "The Farnam, Autograph Collection (Chic luxury hotel in Downtown Omaha for executive retreats)",
                "The Cottonwood Hotel, Kimpton (Historic Blackstone District landmark with Schimmel Ballroom)",
                "Hilton Omaha (Skywalk-connected to CHI Health Center with expansive conference ballrooms)"
            ]
        },
        "card3": {
            "sub": "DISTINCTIVE OMAHA EVENT SPACES",
            "title": "Private Banquets & Cultural Receptions",
            "items": [
                "The Durham Museum (Historic Union Station Art Deco Grand Concourse for spectacular galas)",
                "Lauritzen Gardens (Botanical garden visitor center and floral display hall for private dinners)",
                "Omaha's Henry Doorly Zoo Desert Dome & Aquarium (Unique world-renowned corporate banquet settings)",
                "Happy Hollow Club (Private country club for executive golf outings & leadership banquets)"
            ]
        },
        "callout": {
            "sub": "MIDWEST CROSSROADS FLY-IN ADVANTAGE",
            "title": "Direct Eppley Airfield (OMA) Access • Turnkey Production Delivery",
            "p": "Adrian Saint provides turnkey entertainment delivery for Omaha corporate events. Flying directly into Eppley Airfield (OMA) just 8 minutes from downtown hotels, Adrian ensures effortless travel, guaranteed timing, and zero production stress."
        },
        "faqs": [
            {
                "q": "CAN ADRIAN HEADLINE EVENTS AT CHI HEALTH CENTER OMAHA?",
                "a": "Yes! Adrian frequently headlines national corporate conferences, annual shareholder summits, and evening awards banquets at CHI Health Center for audiences from 150 to over 3,000."
            },
            {
                "q": "HOW DO TRAVEL LOGISTICS WORK FOR OMAHA CORPORATE GATHERINGS?",
                "a": "Adrian flies directly into Eppley Airfield (OMA), located only 8 minutes from downtown Omaha convention hotels. All travel logistics are self-managed and turnkey."
            },
            {
                "q": "IS ADRIAN'S PERFORMANCE FIT FOR FINANCE AND FORTUNE 500 EXECUTIVES?",
                "a": "Yes, absolutely. Adrian's demonstrations of intuition, memory, and influence captivate finance, insurance, and Fortune 500 corporate leaders while remaining 100% clean and HR-safe."
            },
            {
                "q": "WHAT ARE ADRIAN'S AV REQUIREMENTS AT THE MARRIOTT CAPITOL DISTRICT OR THE FARNAM?",
                "a": "Adrian requires only a wireless handheld or lavalier microphone patched into room audio. His setup is completely self-contained, allowing for rapid sound checks."
            },
            {
                "q": "DOES ADRIAN PERFORM STROLLING MIND READING FOR OMAHA COCKTAIL RECEPTIONS?",
                "a": "Yes! Adrian's strolling mentalism is in high demand for corporate cocktail hours, VIP receptions, and executive dinners, creating personal moments of wonder inches from guests."
            }
        ]
    },
    {
        "slug": "tulsa",
        "city": "Tulsa",
        "state": "OK",
        "state_full": "Oklahoma",
        "country": "US",
        "phone": "(833) 570-5966",
        "phone_clean": "18335705966",
        "phone_e164": "+18335705966",
        "badge": "📍 TULSA METRO & COX CONVENTION COVERAGE",
        "h1": "Corporate Magician &amp; Mentalist in <span class=\"hero-headline-highlight\">Tulsa</span> for Cox Convention Summits, Energy Galas &amp; Banquets",
        "subhead": "Delivering electrifying psychological mentalism and interactive mind reading for corporate conventions, energy summits, and executive banquets across Tulsa and Green Country Oklahoma.",
        "lat": 36.1540,
        "lon": -95.9928,
        "areas": ["Tulsa", "Tulsa County", "Downtown Tulsa", "Tulsa Arts District", "Deco District", "Blue Dome", "Broken Arrow", "Green Country Oklahoma"],
        "venue_h2": "Serving Tulsa's Modern Convention Facilities &amp; Art Deco Architectural Landmarks",
        "venue_p": "Celebrated for its world-class Art Deco architecture, vibrant energy economy, and modern meeting infrastructure, Tulsa is an exceptional host city for regional and national corporate gatherings.",
        "card1": {
            "sub": "CONVENTION HUBS & CIVIC VENUES",
            "title": "National Conventions & Energy Summits",
            "items": [
                "Cox Business Convention Center (310,000 sq ft modern convention facility in Downtown Tulsa)",
                "Grand Hall at CBCC (Oklahoma's largest banquet ballroom at over 41,000 sq ft)",
                "BOK Center (Renowned César Pelli-designed arena for major corporate rallies & keynote events)",
                "Tulsa Performing Arts Center (Four-theater complex for major corporate presentations)"
            ]
        },
        "card2": {
            "sub": "HISTORIC ART DECO & LUXURY HOTELS",
            "title": "Executive Summits & Corporate Banquets",
            "items": [
                "The Mayo Hotel (Legendary 1920s Art Deco luxury landmark with the ornate Crystal Ballroom)",
                "Ambassador Hotel Tulsa, Autograph Collection (Boutique luxury for executive leadership retreats)",
                "Tulsa Club Hotel, Curio Collection by Hilton (Historic 1927 Art Deco building in Deco District)",
                "Hyatt Regency Tulsa Downtown (Full-service convention hotel directly adjacent to arts districts)"
            ]
        },
        "card3": {
            "sub": "DISTINCTIVE GREEN COUNTRY EVENT SPACES",
            "title": "Private Banquets & Cultural Venues",
            "items": [
                "Philbrook Museum of Art (Villa Philbrook Italian Renaissance gardens & villa for elite galas)",
                "Southern Hills Country Club (Championship golf clubhouse for executive corporate outings)",
                "Gilcrease Museum Event Spaces (Western art museum grounds for private corporate banquets)",
                "The Campbell Hotel (Historic boutique venue on Route 66 for intimate corporate dinners)"
            ]
        },
        "callout": {
            "sub": "CENTRAL REGIONAL FLY-IN MOBILITY",
            "title": "Direct Tulsa International (TUL) Access • Turnkey Production Delivery",
            "p": "Adrian Saint provides turnkey entertainment delivery for Tulsa corporate events. Flying directly into Tulsa International Airport (TUL) just 12 minutes from downtown, Adrian ensures effortless travel, guaranteed timing, and zero production stress."
        },
        "faqs": [
            {
                "q": "CAN ADRIAN HEADLINE GENERAL SESSIONS AT COX BUSINESS CONVENTION CENTER IN TULSA?",
                "a": "Yes! Adrian frequently headlines corporate general sessions, energy industry banquets, and regional conferences at Cox Business Convention Center for audiences from 150 to over 3,000 attendees."
            },
            {
                "q": "HOW DO TRAVEL LOGISTICS WORK FOR TULSA CORPORATE EVENTS?",
                "a": "Adrian flies directly into Tulsa International Airport (TUL), located just 12 minutes from downtown hotels. His travel is completely turnkey and hassle-free for meeting planners."
            },
            {
                "q": "IS ADRIAN'S PERFORMANCE 100% CLEAN AND HR-SAFE?",
                "a": "Yes, absolutely. Adrian's corporate show is 100% clean, intelligent, and HR-safe. He engages attendees with humor and astonishment without ever embarrassing participants."
            },
            {
                "q": "WHAT ARE ADRIAN'S AV REQUIREMENTS AT THE MAYO HOTEL OR HYATT REGENCY?",
                "a": "Adrian requires only a wireless handheld or lavalier microphone patched into room audio. His setup is completely self-contained, allowing for rapid sound checks."
            },
            {
                "q": "DOES ADRIAN PERFORM STROLLING CLOSE-UP MENTALISM FOR TULSA RECEPTIONS?",
                "a": "Yes! Adrian's strolling mentalism is in high demand for cocktail mixers, VIP receptions, and executive dinners at venues like Philbrook and Southern Hills Country Club."
            }
        ]
    },
    {
        "slug": "birmingham",
        "city": "Birmingham",
        "state": "AL",
        "state_full": "Alabama",
        "country": "US",
        "phone": "(833) 570-5966",
        "phone_clean": "18335705966",
        "phone_e164": "+18335705966",
        "badge": "📍 BIRMINGHAM METRO & BJCC CONVENTION COVERAGE",
        "h1": "Corporate Magician &amp; Mentalist in <span class=\"hero-headline-highlight\">Birmingham</span> for BJCC Summits, Healthcare Galas &amp; Banquets",
        "subhead": "Delivering world-class psychological entertainment and interactive mind reading for corporate conventions, healthcare summits, and executive banquets across Birmingham and Central Alabama.",
        "lat": 33.5186,
        "lon": -86.8104,
        "areas": ["Birmingham", "Jefferson County", "Downtown Birmingham", "Uptown", "Mountain Brook", "Homewood", "Central Alabama"],
        "venue_h2": "Serving Birmingham's Modernized Convention Campus &amp; Historic Event Venues",
        "venue_p": "With the expansive Birmingham-Jefferson Convention Complex (BJCC), vibrant Uptown entertainment district, and premier medical and banking sectors, Birmingham is an ideal corporate meeting destination.",
        "card1": {
            "sub": "CONVENTION CENTERS & ENTERTAINMENT HUBS",
            "title": "National Conventions & Regional Summits",
            "items": [
                "Birmingham-Jefferson Convention Complex (BJCC - 300,000 sq ft exhibition and meeting complex)",
                "Legacy Arena at the BJCC (State-of-the-art arena for major corporate keynotes and rallies)",
                "BJCC Concert Hall (2,800-seat theater for flagship corporate presentations)",
                "Protective Stadium Club Suites (Modern stadium hospitality lounges for corporate receptions)"
            ]
        },
        "card2": {
            "sub": "PREMIER LUXURY & BOUTIQUE HOTELS",
            "title": "Executive Summits & Corporate Banquets",
            "items": [
                "Grand Bohemian Hotel Mountain Brook, Autograph Collection (Luxury art hotel for VIP retreats)",
                "The Westin Birmingham (Connected directly to BJCC in the heart of Uptown)",
                "Sheraton Birmingham Hotel (Alabama's largest hotel with extensive convention ballrooms)",
                "Elyton Hotel, Autograph Collection (Historic Empire Building with Moon Shine rooftop bar)"
            ]
        },
        "card3": {
            "sub": "DISTINCTIVE MAGIC CITY EVENT SPACES",
            "title": "Private Banquets & Cultural Venues",
            "items": [
                "The Florentine (Exquisitely restored 1920s historic ballroom in Downtown Birmingham)",
                "Regions Field Banquet Suites & Club Lounge (Downtown views overlooking the ballpark)",
                "Birmingham Museum of Art (Contemporary corporate galas surrounded by world-class art)",
                "The Harbert Center (Dedicated downtown executive meeting facility & Beeson Hall)"
            ]
        },
        "callout": {
            "sub": "SOUTHEAST REGIONAL FLY-IN MOBILITY",
            "title": "Direct Birmingham-Shuttlesworth (BHM) Access • Turnkey Production Delivery",
            "p": "Adrian Saint provides turnkey entertainment delivery for Birmingham corporate events. Flying directly into Birmingham-Shuttlesworth International Airport (BHM) just 10 minutes from downtown, Adrian ensures effortless travel, guaranteed timing, and zero production stress."
        },
        "faqs": [
            {
                "q": "CAN ADRIAN HEADLINE EVENTS AT THE BJCC IN BIRMINGHAM?",
                "a": "Yes! Adrian frequently headlines corporate general sessions, healthcare conferences, and evening banquets at the BJCC for audiences from 150 to over 3,000 attendees."
            },
            {
                "q": "HOW DO TRAVEL LOGISTICS WORK FOR BIRMINGHAM CORPORATE GATHERINGS?",
                "a": "Adrian flies directly into Birmingham-Shuttlesworth International Airport (BHM), located just 10 minutes from downtown hotels. His travel arrangements are turnkey and completely self-contained."
            },
            {
                "q": "IS ADRIAN'S SHOW 100% CLEAN AND HR-SAFE?",
                "a": "Yes, absolutely. Adrian's corporate show is 100% clean, intelligent, and HR-safe. He engages attendees with humor and astonishment without ever embarrassing participants."
            },
            {
                "q": "WHAT ARE ADRIAN'S AV REQUIREMENTS AT THE GRAND BOHEMIAN OR THE WESTIN?",
                "a": "Adrian requires only a wireless handheld or lavalier microphone patched into room audio. His setup is completely self-contained, allowing for rapid sound checks."
            },
            {
                "q": "DOES ADRIAN PERFORM STROLLING CLOSE-UP MENTALISM FOR BIRMINGHAM RECEPTIONS?",
                "a": "Yes! Adrian's strolling mentalism is in high demand for cocktail mixers, VIP receptions, and executive dinners, creating personal moments of wonder inches from guests."
            }
        ]
    },
    {
        "slug": "providence",
        "city": "Providence",
        "state": "RI",
        "state_full": "Rhode Island",
        "country": "US",
        "phone": "(833) 570-5966",
        "phone_clean": "18335705966",
        "phone_e164": "+18335705966",
        "badge": "📍 PROVIDENCE METRO & CONVENTION CENTER COVERAGE",
        "h1": "Corporate Magician &amp; Mentalist in <span class=\"hero-headline-highlight\">Providence</span> for Convention Summits, Galas &amp; Executive Banquets",
        "subhead": "Delivering sophisticated psychological mentalism and interactive mind reading for corporate conventions, leadership retreats, and annual banquets across Providence and Rhode Island.",
        "lat": 41.8240,
        "lon": -71.4128,
        "areas": ["Providence", "Providence County", "Downtown Providence", "College Hill", "Federal Hill", "Warwick", "Newport", "Rhode Island"],
        "venue_h2": "Serving Providence's Premier Convention Facilities &amp; Historic Ocean State Venues",
        "venue_p": "Blending historic New England elegance with a vibrant culinary and arts culture, Providence features modern convention facilities and luxury historic hotels ideal for corporate meetings.",
        "card1": {
            "sub": "CONVENTION HUBS & CIVIC AUDITORIUMS",
            "title": "Regional Conventions & Flagship Galas",
            "items": [
                "Rhode Island Convention Center (RICC - 100,000 sq ft exhibition hall and 20,000 sq ft ballroom)",
                "Amica Mutual Pavilion (Connected arena hosting large-scale corporate rallies & assemblies)",
                "Providence Performing Arts Center (PPAC - Historic 3,100-seat theater for major corporate keynotes)",
                "WaterFire Arts Center (Historic 37,000 sq ft open hall for creative corporate galas)"
            ]
        },
        "card2": {
            "sub": "HISTORIC LUXURY & BOUTIQUE HOTELS",
            "title": "Executive Summits & Corporate Banquets",
            "items": [
                "Omni Providence Hotel (Connected directly via skybridge to Rhode Island Convention Center)",
                "Graduate Providence (Historic 1922 Biltmore landmark with the iconic Biltmore Ballroom)",
                "Renaissance Providence Downtown Hotel (Historic 1920s Masonic temple turned luxury hotel)",
                "The Beatrice (Boutique luxury hotel in Downtown Providence for executive board dinners)"
            ]
        },
        "card3": {
            "sub": "DISTINCTIVE NEW ENGLAND EVENT SPACES",
            "title": "Private Banquets & Waterfront Venues",
            "items": [
                "Squantum Association in Riverside (Historic private oceanfront club with panoramic bay views)",
                "Aldrich Mansion in Warwick (Historic 70-room French chateau for elite corporate retreats)",
                "RISD Museum Grand Gallery (Surrounded by world-class art for sophisticated corporate dinners)",
                "The Dorrance (Historic federal reserve bank architecture with ornate ceilings)"
            ]
        },
        "callout": {
            "sub": "NORTHEAST CORRIDOR FLY-IN MOBILITY",
            "title": "Direct Rhode Island T.F. Green (PVD) Access • 50 Minutes from Boston Logan (BOS)",
            "p": "Adrian Saint provides turnkey entertainment delivery for Providence corporate events. Flying directly into Rhode Island T.F. Green International Airport (PVD) just 10 minutes from downtown, Adrian ensures effortless travel, guaranteed timing, and zero production stress."
        },
        "faqs": [
            {
                "q": "CAN ADRIAN HEADLINE EVENTS AT RHODE ISLAND CONVENTION CENTER?",
                "a": "Yes! Adrian frequently headlines corporate general sessions, trade show banquets, and annual conferences at RICC for audiences ranging from 150 to over 2,500 attendees."
            },
            {
                "q": "HOW DO TRAVEL LOGISTICS WORK FOR PROVIDENCE CORPORATE MEETINGS?",
                "a": "Adrian flies directly into Rhode Island T.F. Green International Airport (PVD), only 10 minutes from downtown, or connects via Boston Logan (BOS). All travel logistics are turnkey."
            },
            {
                "q": "IS ADRIAN'S PERFORMANCE 100% CLEAN AND APPROPRIATE FOR EXECUTIVES?",
                "a": "Yes, absolutely. Adrian's corporate show is 100% clean, intelligent, and HR-safe. He engages company leadership respectfully without ever embarrassing participants."
            },
            {
                "q": "WHAT ARE ADRIAN'S AV REQUIREMENTS AT THE OMNI PROVIDENCE OR GRADUATE?",
                "a": "Adrian requires only a wireless handheld or lavalier microphone patched into room audio. His setup is completely self-contained, allowing for rapid sound checks."
            },
            {
                "q": "DOES ADRIAN PERFORM STROLLING CLOSE-UP MENTALISM FOR PROVIDENCE RECEPTIONS?",
                "a": "Yes! Adrian's strolling mentalism is in high demand for cocktail mixers, VIP receptions, and executive dinners at venues like the Squantum Association and The Beatrice."
            }
        ]
    },
    {
        "slug": "des-moines",
        "city": "Des Moines",
        "state": "IA",
        "state_full": "Iowa",
        "country": "US",
        "phone": "(833) 570-5966",
        "phone_clean": "18335705966",
        "phone_e164": "+18335705966",
        "badge": "📍 DES MOINES METRO & IOWA EVENTS CENTER COVERAGE",
        "h1": "Corporate Magician &amp; Mentalist in <span class=\"hero-headline-highlight\">Des Moines</span> for Iowa Events Center Summits, Insurance Galas &amp; Banquets",
        "subhead": "Delivering world-class psychological entertainment and interactive mind reading for corporate conventions, insurance summits, and executive banquets across Des Moines and Central Iowa.",
        "lat": 41.5868,
        "lon": -93.6250,
        "areas": ["Des Moines", "Polk County", "Downtown Des Moines", "Historic East Village", "Western Gateway", "West Des Moines", "Central Iowa"],
        "venue_h2": "Serving Des Moines's Premier Convention Facilities &amp; Downtown Skywalk Network",
        "venue_p": "As one of the world's leading insurance and financial capitals, Des Moines features the massive Iowa Events Center, an extensive 4-mile skywalk system, and beautifully restored historic hotels.",
        "card1": {
            "sub": "CONVENTION HUBS & ARENAS",
            "title": "National Conventions & Insurance Summits",
            "items": [
                "Iowa Events Center (Includes Hy-Vee Hall & Wells Fargo Arena with 250,000 sq ft of space)",
                "Hy-Vee Hall Ballroom (Iowa's largest ballroom at 28,800 sq ft for major corporate galas)",
                "Wells Fargo Arena (Arena-scale corporate rallies and private executive suites)",
                "Community Choice Convention Center (Modernized ballroom and meeting rooms connected to arena)"
            ]
        },
        "card2": {
            "sub": "SKYWALK-CONNECTED & BOUTIQUE HOTELS",
            "title": "Executive Summits & Corporate Banquets",
            "items": [
                "Hilton Des Moines Downtown (Connected directly to Iowa Events Center via skywalk)",
                "Des Moines Marriott Downtown (Prime central location with spacious grand ballroom)",
                "Hotel Fort Des Moines, Curio Collection by Hilton (Historic 1919 landmark with Grand Ballroom)",
                "The Surety Hotel (Historic 1913 bank building turned chic boutique hotel in downtown)"
            ]
        },
        "card3": {
            "sub": "DISTINCTIVE CAPITAL CITY EVENT SPACES",
            "title": "Private Banquets & Cultural Venues",
            "items": [
                "World Food Prize Hall of Laureates (Magnificent Beaux-Arts building for elite corporate galas)",
                "Temple for Performing Arts (Historic downtown venue with Grand Hall for elegant dinners)",
                "Des Moines Art Center (World-class architecture and galleries for private corporate receptions)",
                "Glen Oaks Country Club in West Des Moines (Championship golf clubhouse for executive retreats)"
            ]
        },
        "callout": {
            "sub": "MIDWEST CAPITAL FLY-IN ADVANTAGE",
            "title": "Direct Des Moines International (DSM) Access • Turnkey Production Delivery",
            "p": "Adrian Saint provides turnkey entertainment delivery for Des Moines corporate events. Flying directly into Des Moines International Airport (DSM) just 10 minutes from downtown, Adrian ensures effortless travel, guaranteed timing, and zero production stress."
        },
        "faqs": [
            {
                "q": "CAN ADRIAN HEADLINE GENERAL SESSIONS AT IOWA EVENTS CENTER IN DES MOINES?",
                "a": "Yes! Adrian frequently headlines corporate general sessions, insurance industry summits, and annual banquets at Iowa Events Center for audiences from 150 to over 3,000 attendees."
            },
            {
                "q": "HOW DO TRAVEL LOGISTICS WORK FOR DES MOINES CORPORATE GATHERINGS?",
                "a": "Adrian flies directly into Des Moines International Airport (DSM), located just 10 minutes from downtown hotels. His travel is completely turnkey and hassle-free for meeting planners."
            },
            {
                "q": "IS ADRIAN'S PERFORMANCE FIT FOR INSURANCE AND FINANCIAL EXECUTIVES?",
                "a": "Yes, absolutely. Adrian's demonstrations of psychology, decision-making, and mind reading resonate powerfully with insurance and financial leaders while remaining 100% clean and HR-safe."
            },
            {
                "q": "WHAT ARE ADRIAN'S AV REQUIREMENTS AT HILTON DES MOINES OR HOTEL FORT DES MOINES?",
                "a": "Adrian requires only a wireless handheld or lavalier microphone patched into room audio. His setup is completely self-contained, allowing for rapid sound checks."
            },
            {
                "q": "DOES ADRIAN PERFORM STROLLING CLOSE-UP MENTALISM FOR DES MOINES RECEPTIONS?",
                "a": "Yes! Adrian's strolling mentalism is in high demand for cocktail mixers, VIP receptions, and executive dinners at venues like the Hall of Laureates and The Surety Hotel."
            }
        ]
    }
]

created_files = []

for c in GROUP_B_CITIES:
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

print(f"\nSuccessfully generated all {len(created_files)} Group B location pages!")
