/* ==========================================================================
   ADRIAN SAINT - CORPORATE MENTALIST & AI SEO LEAD GENERATION PLATFORM
   Main JavaScript Controller - Clean Image Card Edition
   ========================================================================== */

import { CITIES_DATA } from './data/cities.js?v=20260821_v3';
import { SERVICES_DATA } from './data/services.js?v=20260821_v3';
import { TESTIMONIALS_DATA } from './data/testimonials.js?v=20260821_v3';
import { GENERAL_FAQS } from './data/faqs.js?v=20260821_v3';
import { renderCityPage } from './components/cityRenderer.js?v=20260821_v3';
import { setupBookingModal } from './components/bookingModal.js?v=20260821_v3';
import { generateSchema, updateDOMSchema } from './components/schemaGenerator.js?v=20260821_v3';

document.addEventListener("DOMContentLoaded", () => {
  initApp();
});

function initApp() {
  setupHeroBackgroundVideo();
  setupBookingModal();
  setupVideoModal();
  setupHeroForm();
  setupInquiryForm();
  setupLocationTabs();
  setupRouter();
  setupSearchFilter();
  setupFaqAccordion();

  // Initial global schema setup
  const globalSchemas = generateSchema({ faqs: GENERAL_FAQS });
  updateDOMSchema(globalSchemas);
}

function setupHeroBackgroundVideo() {
  const container = document.getElementById("hero-yt-player");
  if (!container) return;

  const initPlayer = () => {
    try {
      const player = new window.YT.Player("hero-yt-player", {
        videoId: "jnwJ1-k-dU8",
        playerVars: {
          autoplay: 1,
          mute: 1,
          loop: 1,
          start: 67,
          end: 93,
          playlist: "jnwJ1-k-dU8",
          controls: 0,
          showinfo: 0,
          modestbranding: 1,
          rel: 0,
          playsinline: 1,
          enablejsapi: 1,
          disablekb: 1,
          fs: 0
        },
        events: {
          onReady: (event) => {
            event.target.mute();
            event.target.seekTo(67, true);
            event.target.playVideo();

            // Precise loop watcher: checks every 200ms and loops when reaching 1:33 (93s)
            setInterval(() => {
              if (player && typeof player.getCurrentTime === 'function' && typeof player.getPlayerState === 'function') {
                if (player.getPlayerState() === 1) { // Currently playing
                  const current = player.getCurrentTime();
                  if (current >= 93 || current < 66) {
                    player.seekTo(67, true);
                  }
                }
              }
            }, 200);
          },
          onStateChange: (event) => {
            if (event.data === 0) { // Video ended -> loop back to 1:07 (67s)
              event.target.seekTo(67, true);
              event.target.playVideo();
            }
          }
        }
      });
    } catch (err) {
      console.warn("YouTube API init fallback", err);
    }
  };

  if (window.YT && window.YT.Player) {
    initPlayer();
  } else {
    // Load YouTube Iframe API
    if (!document.getElementById("yt-iframe-api-script")) {
      const tag = document.createElement("script");
      tag.id = "yt-iframe-api-script";
      tag.src = "https://www.youtube.com/iframe_api";
      const firstScriptTag = document.getElementsByTagName("script")[0];
      firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);
    }
    window.onYouTubeIframeAPIReady = initPlayer;
  }
}

function setupHeroForm() {
  const heroForm = document.getElementById("hero-fast-track-form");
  if (heroForm) {
    heroForm.addEventListener("submit", (e) => {
      e.preventDefault();
      const btn = heroForm.querySelector("button[type='submit']");
      if (btn) {
        btn.disabled = true;
        btn.innerHTML = "<span>⚡ Reserving Priority Hold...</span>";
      }

      setTimeout(() => {
        heroForm.innerHTML = `
          <div style="text-align: center; padding: 1.75rem 0.5rem; color: #FFFFFF;">
            <div style="font-size: 2.75rem; margin-bottom: 0.75rem;">🎉</div>
            <h3 style="font-family: var(--font-heading); font-size: 1.35rem; font-weight: 800; color: var(--accent-gold); margin-bottom: 0.5rem;">Event Date Hold Initiated!</h3>
            <p style="color: var(--text-silver); font-size: 0.9rem; line-height: 1.5; margin-bottom: 1.25rem;">
              Thank you! Our management team has received your event details. We will respond within <strong>2 business hours</strong> with custom package and fee options.
            </p>
            <div style="display: inline-flex; align-items: center; justify-content: center; gap: 0.5rem; background: rgba(212, 175, 55, 0.12); border: 1px solid var(--border-gold-glow); padding: 0.6rem 1.1rem; border-radius: 9999px; font-size: 0.82rem; color: var(--accent-gold); font-weight: 700; max-width: 100%;">
              <span>📞 Immediate Question? Call <a href="tel:18335705966" style="color: #FFF; text-decoration: underline;">(833) 570-5966</a></span>
            </div>
          </div>
        `;
      }, 850);
    });
  }
}

function setupFaqAccordion() {
  const faqContainer = document.getElementById('faq-container');
  if (faqContainer && !faqContainer.dataset.listenerAttached) {
    faqContainer.dataset.listenerAttached = "true";
    faqContainer.addEventListener('click', (e) => {
      const question = e.target.closest('.faq-question');
      if (question) {
        const item = question.closest('.faq-item');
        if (item) {
          item.classList.toggle('active');
        }
      }
    });
  }
}

function setupVideoModal() {
  const videoModal = document.getElementById("video-modal");
  const videoClose = document.getElementById("video-modal-close");

  document.querySelectorAll(".open-video-modal").forEach(btn => {
    btn.addEventListener("click", (e) => {
      e.preventDefault();
      if (videoModal) videoModal.classList.add("active");
    });
  });

  if (videoClose) {
    videoClose.addEventListener("click", () => {
      if (videoModal) videoModal.classList.remove("active");
    });
  }

  if (videoModal) {
    videoModal.addEventListener("click", (e) => {
      if (e.target === videoModal) videoModal.classList.remove("active");
    });
  }
}

function setupInquiryForm() {
  const formEl = document.getElementById("inquiry-form-main");
  const successEl = document.getElementById("inquiry-success-message");

  if (formEl) {
    formEl.addEventListener("submit", (e) => {
      e.preventDefault();
      const btn = formEl.querySelector("button[type='submit']");
      btn.disabled = true;
      btn.innerHTML = "<span>Submitting Request...</span>";

      setTimeout(() => {
        formEl.style.display = "none";
        successEl.style.display = "block";
        btn.disabled = false;
        btn.innerHTML = "<span>Submit Availability Request</span>";
      }, 1000);
    });
  }
}

function setupLocationTabs() {
  const tabBtns = document.querySelectorAll(".tab-btn");
  const tabContents = document.querySelectorAll(".tab-content");

  tabBtns.forEach(btn => {
    btn.addEventListener("click", () => {
      const target = btn.dataset.target;
      
      tabBtns.forEach(b => b.classList.remove("active"));
      tabContents.forEach(c => c.classList.remove("active"));

      btn.classList.add("active");
      const targetEl = document.getElementById(target);
      if (targetEl) targetEl.classList.add("active");
    });
  });
}

function setupSearchFilter() {
  const searchInput = document.getElementById("city-search-input");
  const citiesGrid = document.getElementById("cities-grid");

  if (searchInput && citiesGrid) {
    renderCitiesGrid(CITIES_DATA, citiesGrid);

    searchInput.addEventListener("input", (e) => {
      const query = e.target.value.toLowerCase().trim();
      const filtered = CITIES_DATA.filter(c => 
        c.name.toLowerCase().includes(query) || 
        c.state.toLowerCase().includes(query) ||
        c.metro.toLowerCase().includes(query)
      );
      renderCitiesGrid(filtered, citiesGrid);
    });
  }
}

function renderCitiesGrid(cities, container) {
  if (cities.length === 0) {
    container.innerHTML = `
      <div style="grid-column: 1 / -1; text-align: center; padding: 2rem; color: var(--text-muted);">
        <p>No convention markets found. Adrian travels anywhere in North America upon request.</p>
      </div>
    `;
    return;
  }

  container.innerHTML = cities.map(c => `
    <div class="glass-card" onclick="window.location.hash='#city/${c.id}'" style="cursor: pointer;">
      <h3 style="font-size: 1.15rem; color: #FFF; margin-bottom: 0.25rem;">${c.name}, ${c.state}</h3>
      <p style="font-size: 0.85rem; color: var(--accent-gold); margin-bottom: 0.75rem;">${c.metro}</p>
      <div style="font-size: 0.8rem; color: var(--text-silver);">
        <span>🏛️ ${c.venues[0]}</span>
      </div>
    </div>
  `).join('');
}

function setupRouter() {
  window.addEventListener("hashchange", handleRoute);
  handleRoute();
}

function handleRoute() {
  const hash = window.location.hash;
  if (hash.startsWith("#city/")) {
    const cityId = hash.replace("#city/", "").trim();
    const appRoot = document.getElementById("app-root");
    renderCityPage(cityId, appRoot);
    window.scrollTo({ top: 0, behavior: 'smooth' });
  } else {
    renderHomepageContent();
  }
}

const SERVICE_IMAGES = {
  "corporate-stage-show": "images/adrian_hyatt.jpg",
  "strolling-mind-reading": "images/adrian_strolling_headshot.jpg",
  "trade-show-lead-gen": "images/Image5.jpg",
  "executive-keynotes": "images/Image7.jpg"
};

function renderHomepageContent() {
  const appRoot = document.getElementById("app-root");
  
  if (!appRoot.querySelector(".hero")) {
    window.location.reload();
    return;
  }

  // 1. Render 4 Performance Packages Cards without Overlay Badges (Clean Image)
  const servicesGrid = document.getElementById("services-grid");
  if (servicesGrid) {
    servicesGrid.innerHTML = SERVICES_DATA.map(s => {
      const cardImage = s.image || SERVICE_IMAGES[s.id] || "images/adrian_stage_1.jpg";
      return `
        <div class="service-card-interactive gold-glow-card">
          <!-- Clean Service Header Image -->
          <div class="service-card-image-wrap" style="position: relative; width: 100%; height: 220px; overflow: hidden; background: #11131c;">
            <img src="${cardImage}" alt="${s.title}" class="service-card-image" style="width: 100%; height: 100%; object-fit: cover; display: block;" loading="lazy">
          </div>

          <div class="service-card-body">
            <div>
              <span class="service-badge">${s.duration}</span>
              <h3 style="font-size: 1.45rem; margin-bottom: 0.6rem; color: #FFFFFF;">${s.title}</h3>
              <p style="margin-bottom: 1.25rem; font-size: 0.95rem; color: var(--text-silver); line-height: 1.5;">${s.shortDesc}</p>
              
              <ul class="service-features" style="margin-bottom: 1.75rem;">
                ${s.features.map(f => `<li>${f}</li>`).join('')}
              </ul>
            </div>

            <button class="btn btn-secondary open-booking-modal" style="width: 100%;">
              <span>View Package Details →</span>
            </button>
          </div>
        </div>
      `;
    }).join('');
  }

  // 2. Render Masonry Testimonials Grid
  const testimonialsGrid = document.getElementById("testimonials-grid");
  if (testimonialsGrid) {
    testimonialsGrid.innerHTML = TESTIMONIALS_DATA.map(t => `
      <div class="masonry-card" style="display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <div style="color: #EF4444; font-size: 1.15rem; margin-bottom: 1rem; letter-spacing: 3px;">
            ${"★".repeat(t.rating || 5)}
          </div>
          <p style="font-size: 0.95rem; margin-bottom: 1.5rem; color: #E4E4E7; line-height: 1.6; font-weight: 400;">
            "${t.quote}"
          </p>
        </div>

        <div style="border-top: 1px solid rgba(255, 255, 255, 0.08); padding-top: 1rem; margin-top: 0.5rem;">
          <div style="font-weight: 800; font-size: 1rem; color: #FFFFFF; margin-bottom: 0.2rem;">
            ${t.author}
          </div>
          ${t.role ? `<div style="color: #EF4444; font-size: 0.8rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 0.25rem;">${t.role}</div>` : ''}
          ${t.company && t.company !== t.author ? `<div style="color: #A1A1AA; font-size: 0.82rem;">${t.company}</div>` : ''}
        </div>
      </div>
    `).join('');
  }
}
