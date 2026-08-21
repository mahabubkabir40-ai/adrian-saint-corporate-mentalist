/* ==========================================================================
   ADRIAN SAINT - CORPORATE MENTALIST & AI SEO LEAD GENERATION PLATFORM
   Schema.org JSON-LD Generator - Verified Social & Entity Linkage
   ========================================================================== */

export function generateSchema({ cityData, faqs }) {
  const schemas = [];

  // 1. Person Schema (Adrian Saint) with Verified Social Graph
  schemas.push({
    "@context": "https://schema.org",
    "@type": "Person",
    "@id": "https://adriansaint.com/#person",
    "name": "Adrian Saint",
    "jobTitle": "Corporate Mentalist & Mind Reader",
    "description": "Adrian Saint is an elite corporate mentalist and mind reader providing clean, HR-safe psychological entertainment for corporate galas, executive retreats, and national conventions.",
    "url": "https://adriansaint.com",
    "email": "adrian@saintmentalist.com",
    "telephone": "+1-949-484-5096",
    "sameAs": [
      "https://www.linkedin.com/in/adriansaintmentalist/",
      "https://www.instagram.com/ocmentalist/",
      "https://www.youtube.com/@ocmentalist",
      "https://www.facebook.com/ocmentalist/",
      "https://x.com/sainttwins",
      "https://www.yelp.com/biz/adrian-and-john-the-saint-twins-irvine",
      "https://www.ocmentalist.com"
    ],
    "alumniOf": {
      "@type": "EducationalOrganization",
      "name": "Psychology & Linguistics Degree"
    },
    "knowsAbout": [
      "Corporate Mentalism",
      "Mind Reading",
      "Non-Verbal Communication",
      "Subconscious Persuasion",
      "Executive Entertainment",
      "Corporate Keynotes"
    ]
  });

  // 2. LocalBusiness / EntertainmentBusiness Schema
  if (cityData) {
    schemas.push({
      "@context": "https://schema.org",
      "@type": "EntertainmentBusiness",
      "@id": `https://adriansaint.com/#business-${cityData.id}`,
      "name": `Adrian Saint - Corporate Mentalist ${cityData.name}`,
      "description": `Premier corporate mentalist and mind reader serving ${cityData.name}, ${cityData.state} corporate galas, trade shows, and executive retreats.`,
      "areaServed": {
        "@type": "City",
        "name": cityData.name,
        "containedInPlace": {
          "@type": "State",
          "name": cityData.state
        }
      },
      "priceRange": "$$$$",
      "telephone": "+1-949-484-5096",
      "email": "adrian@saintmentalist.com",
      "url": `https://adriansaint.com/#city/${cityData.id}`,
      "sameAs": [
        "https://www.linkedin.com/in/adriansaintmentalist/",
        "https://www.instagram.com/ocmentalist/",
        "https://www.youtube.com/@ocmentalist",
        "https://www.facebook.com/ocmentalist/",
        "https://x.com/sainttwins",
        "https://www.yelp.com/biz/adrian-and-john-the-saint-twins-irvine"
      ]
    });
  }

  // 3. FAQPage Schema for AI Engines (ChatGPT, Gemini, Perplexity)
  if (faqs && faqs.length > 0) {
    schemas.push({
      "@context": "https://schema.org",
      "@type": "FAQPage",
      "mainEntity": faqs.map(f => ({
        "@type": "Question",
        "name": f.question,
        "acceptedAnswer": {
          "@type": "Answer",
          "text": f.answer
        }
      }))
    });
  }

  return schemas;
}

export function updateDOMSchema(schemas) {
  let scriptEl = document.getElementById("geo-jsonld-script");
  if (!scriptEl) {
    scriptEl = document.createElement("script");
    scriptEl.id = "geo-jsonld-script";
    scriptEl.type = "application/ld+json";
    document.head.appendChild(scriptEl);
  }
  scriptEl.textContent = JSON.stringify(schemas, null, 2);
}
