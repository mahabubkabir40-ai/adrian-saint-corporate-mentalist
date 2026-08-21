/* ==========================================================================
   ADRIAN SAINT - CORPORATE MENTALIST & AI SEO LEAD GENERATION PLATFORM
   Dynamic City Page Renderer - Pure Corporate Mentalist Positioning
   ========================================================================== */

import { CITIES_DATA } from '../data/cities.js';
import { generateSchema, updateDOMSchema } from './schemaGenerator.js';

export function renderCityPage(cityId, container) {
  const city = CITIES_DATA.find(c => c.id === cityId);

  if (!city) {
    container.innerHTML = `
      <div class="container section-padding text-center">
        <h2>City Page Not Found</h2>
        <p>Return to <a href="#">Homepage</a></p>
      </div>
    `;
    return;
  }

  // Update Dynamic Document Meta & Schema for GEO / SEO
  document.title = `Corporate Mentalist & Mind Reader ${city.name}, ${city.state} | Adrian Saint`;
  
  const citySchemas = generateSchema({ cityData: city });
  updateDOMSchema(citySchemas);

  // Render High-Converting City Landing Page
  container.innerHTML = `
    <!-- CITY HERO SECTION -->
    <section class="hero" style="min-height: 80vh; padding-top: 140px; background-color: var(--bg-hero);">
      <div class="hero-video-backdrop"></div>
      <div class="container">
        <div class="hero-grid">
          <div class="hero-text-content">
            <div class="section-badge">
              <span>📍 #1 Corporate Mentalist & Mind Reader in ${city.name}, ${city.state}</span>
            </div>
            
            <h1 class="hero-headline text-gradient-gold">
              Corporate Mentalist & Mind Reader in ${city.name}, ${city.state}
            </h1>

            <p class="hero-subheadline">
              Elevate your next corporate gala, executive retreat, or national convention in ${city.name} with Adrian Saint's world-class, 100% clean psychological mind reading show.
            </p>

            <div class="hero-actions">
              <button class="btn btn-gold open-booking-modal">
                <span>Check ${city.name} Date & Fees</span>
              </button>
              <a href="#city-details" class="btn btn-secondary">
                <span>Explore ${city.name} Venues</span>
              </a>
            </div>
          </div>

          <div class="glass-card gold-glow-card" style="padding: 2.2rem;">
            <h3 class="text-gradient-gold" style="margin-bottom: 1rem;">Why ${city.name} Event Planners Book Adrian Saint</h3>
            <ul class="service-features" style="margin-bottom: 1.5rem;">
              <li><strong>Major Venues Covered:</strong> ${city.venues.join(', ')}</li>
              <li><strong>Local Enterprise Experience:</strong> Performed for ${city.hqs.join(', ')} executive teams</li>
              <li><strong>Direct Travel Hub:</strong> ${city.airports.join(', ')} airport convenience</li>
              <li><strong>100% HR-Safe Guarantee:</strong> Zero embarrassing audience call-outs</li>
            </ul>
            <button class="btn btn-gold open-booking-modal" style="width: 100%;">
              <span>Request ${city.name} Quote</span>
            </button>
          </div>
        </div>
      </div>
    </section>

    <!-- CITY VENUES & CORPORATE EXPERIENCE -->
    <section id="city-details" class="section-padding section-divider" style="background-color: var(--bg-packages);">
      <div class="container">
        <div class="section-header">
          <div class="section-badge">${city.metro} Entertainment</div>
          <h2 class="text-gradient-gold">Serving ${city.name}'s Premier Venues</h2>
          <p>Adrian Saint regularly flies in to headline conferences, corporate galas, and executive retreats at ${city.name}'s top event spaces.</p>
        </div>

        <div class="grid-3" style="margin-bottom: 3rem;">
          <div class="glass-card">
            <h3 style="font-size: 1.25rem; margin-bottom: 0.5rem; color: #FFF;">🏛️ Convention Venues</h3>
            <p style="color: var(--text-silver); font-size: 0.95rem;">${city.venues.join('<br>• ')}</p>
          </div>

          <div class="glass-card">
            <h3 style="font-size: 1.25rem; margin-bottom: 0.5rem; color: #FFF;">🏢 Regional Corporate HQs</h3>
            <p style="color: var(--text-silver); font-size: 0.95rem;">${city.hqs.join('<br>• ')}</p>
          </div>

          <div class="glass-card">
            <h3 style="font-size: 1.25rem; margin-bottom: 0.5rem; color: #FFF;">✈️ Airport Logistics</h3>
            <p style="color: var(--text-silver); font-size: 0.95rem;">${city.airports.join('<br>• ')} (Fly-in turnkey show setup)</p>
          </div>
        </div>

        <!-- Call to Action -->
        <div class="glass-card gold-glow-card text-center" style="padding: 3rem; max-width: 800px; margin: 0 auto;">
          <h3 class="text-gradient-gold" style="margin-bottom: 1rem;">Planning a Corporate Event in ${city.name}?</h3>
          <p style="margin-bottom: 1.75rem; color: var(--text-silver);">Dates for ${city.name} corporate galas and Q1/Q4 retreats fill up fast. Reserve your date early to lock in availability.</p>
          <button class="btn btn-gold open-booking-modal">
            <span>Check ${city.name} Availability & Pricing</span>
          </button>
        </div>
      </div>
    </section>
  `;
}
