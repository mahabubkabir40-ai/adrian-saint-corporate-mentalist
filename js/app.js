/* ==========================================================================
   ADRIAN SAINT - CORPORATE MENTALIST & AI SEO LEAD GENERATION PLATFORM
   Main JavaScript Controller - Clean Image Card Edition
   ========================================================================== */

import { CITIES_DATA } from './data/cities.js?v=20260821_v3';
import { TESTIMONIALS_DATA, VIDEO_TESTIMONIALS_DATA } from './data/testimonials.js?v=20260911_v27';
import { GENERAL_FAQS } from './data/faqs.js?v=20260911_v19';
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
  setupVideoModalPlayer();
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
          fs: 0,
          cc_load_policy: 0,
          cc_lang_pref: 'none',
          iv_load_policy: 3
        },
        events: {
          onReady: (event) => {
            event.target.mute();
            event.target.seekTo(67, true);
            event.target.playVideo();

            const killCaptions = () => {
              try {
                if (player && typeof player.unloadModule === 'function') {
                  player.unloadModule("captions");
                  player.unloadModule("cc");
                }
                if (player && typeof player.setOption === 'function') {
                  player.setOption("captions", "track", {});
                  player.setOption("cc", "track", {});
                }
              } catch (e) {}
            };

            killCaptions();

            // Precise loop watcher: checks every 200ms and loops when reaching 1:33 (93s)
            setInterval(() => {
              killCaptions();
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
            try {
              if (player && typeof player.unloadModule === 'function') {
                player.unloadModule("captions");
                player.unloadModule("cc");
              }
            } catch (e) {}
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

  if (citiesGrid) {
    renderCitiesGrid(CITIES_DATA, citiesGrid);

    if (searchInput) {
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
}

function renderCitiesGrid(cities, container) {
  if (cities.length === 0) {
    container.innerHTML = `
      <div style="grid-column: 1 / -1; text-align: center; padding: 2.5rem; color: var(--text-muted);">
        <p style="font-size: 1rem; color: #E4E4E7; margin-bottom: 0.5rem;">No direct matching city found.</p>
        <p style="font-size: 0.88rem; color: #A1A1AA;">Adrian Saint travels anywhere in North America upon request for private corporate events.</p>
      </div>
    `;
    return;
  }

  container.innerHTML = cities.map(c => `
    <div class="glass-card gold-glow-card" onclick="window.location.hash='#city/${c.id}'" style="cursor: pointer; padding: 1.5rem; border-radius: 14px; transition: transform 0.25s ease, border-color 0.25s ease;">
      <div style="display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 0.35rem;">
        <h3 style="font-size: 1.15rem; color: #FFFFFF; font-weight: 700;">${c.name}, ${c.state}</h3>
        <span style="font-size: 0.72rem; color: #EF4444; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em;">Fly-In Ready</span>
      </div>
      <p style="font-size: 0.85rem; color: #EF4444; font-weight: 600; margin-bottom: 0.65rem;">${c.metro}</p>
      <div style="font-size: 0.82rem; color: #A1A1AA;">
        <span>🏛️ ${c.venues ? c.venues[0] : 'Convention Hub'}</span>
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
  const appRoot = document.getElementById("app-root") || document.querySelector("main") || document.body;
  if (!appRoot) return;

  // Render Written Reviews Carousel Cards if empty
  const testimonialsGrid = document.getElementById("testimonials-grid");
  if (testimonialsGrid && testimonialsGrid.children.length === 0) {
    testimonialsGrid.innerHTML = TESTIMONIALS_DATA.map(t => {
      return `
        <div class="review-carousel-card">
          <div class="review-card-body">
            <div class="review-stars">★★★★★</div>
            <p class="review-quote-text">
              "${t.quote}"
            </p>
          </div>
          <div class="review-card-footer">
            <div class="review-author-name">${t.author}</div>
            ${t.role ? `<div class="review-author-role">${t.role}</div>` : ''}
            ${t.company && t.company !== t.author ? `<div class="review-author-company">${t.company}</div>` : ''}
          </div>
        </div>
      `;
    }).join('');
  }

  setupVideoModalPlayer();
  setupVideoCarousel();
  setupWrittenReviewsCarousel();
}

function setupVideoModalPlayer() {
  const modal = document.getElementById("video-testimonial-modal");
  const closeBtn = document.getElementById("close-video-modal");
  const iframeContainer = document.getElementById("video-modal-iframe-container");
  const videoCards = document.querySelectorAll(".video-card-item");

  if (!modal || !iframeContainer) return;

  const closeModal = () => {
    modal.style.display = "none";
    document.body.style.overflow = "";
    iframeContainer.innerHTML = "";
  };

  videoCards.forEach(card => {
    const handleOpen = () => {
      if (window._isCarouselDragging) return;
      const videoId = card.dataset.videoid;
      const title = card.dataset.videotitle || "Client Testimonial";
      if (!videoId) return;

      iframeContainer.innerHTML = `
        <iframe 
          src="https://www.youtube-nocookie.com/embed/${videoId}?autoplay=1&rel=0&modestbranding=1" 
          title="${title}" 
          style="width: 100%; height: 100%; border: none;" 
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
          allowfullscreen>
        </iframe>
      `;
      modal.style.display = "flex";
      document.body.style.overflow = "hidden";
    };

    card.addEventListener("click", handleOpen);
    card.addEventListener("keydown", (e) => {
      if (e.key === "Enter" || e.key === " ") {
        e.preventDefault();
        handleOpen();
      }
    });
  });

  if (closeBtn) {
    closeBtn.addEventListener("click", closeModal);
  }

  modal.addEventListener("click", (e) => {
    if (e.target === modal) {
      closeModal();
    }
  });

  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape" && modal.style.display === "flex") {
      closeModal();
    }
  });
}

function setupVideoCarousel() {
  const wrapper = document.querySelector(".video-carousel-wrapper");
  const track = document.getElementById("video-carousel-track");
  const prevBtn = document.getElementById("video-carousel-prev");
  const nextBtn = document.getElementById("video-carousel-next");
  const dotsContainer = document.getElementById("video-carousel-dots");

  if (!wrapper || !track) return;

  const cards = Array.from(track.querySelectorAll(".video-card-item"));
  if (!cards.length) return;

  const getPageCount = () => {
    const cardWidth = cards[0].offsetWidth + 20;
    const visibleCount = Math.max(1, Math.round(track.clientWidth / cardWidth));
    return Math.max(1, Math.ceil(cards.length / visibleCount));
  };

  const renderDots = () => {
    if (!dotsContainer) return;
    dotsContainer.innerHTML = "";
    const count = getPageCount();
    for (let i = 0; i < count; i++) {
      const dot = document.createElement("button");
      dot.className = `video-carousel-dot ${i === 0 ? "active" : ""}`;
      dot.setAttribute("aria-label", `Slide ${i + 1}`);
      dot.addEventListener("click", () => {
        goToPage(i);
      });
      dotsContainer.appendChild(dot);
    }
  };

  const goToPage = (pageIndex) => {
    const cardWidth = cards[0].offsetWidth + 20;
    const visibleCount = Math.max(1, Math.round(track.clientWidth / cardWidth));
    const targetCardIndex = Math.min(cards.length - 1, pageIndex * visibleCount);
    const targetCard = cards[targetCardIndex];
    if (targetCard) {
      track.scrollTo({ left: targetCard.offsetLeft - track.offsetLeft, behavior: "smooth" });
    }
  };

  const updateActiveState = () => {
    const cardWidth = cards[0].offsetWidth + 20;
    const visibleCount = Math.max(1, Math.round(track.clientWidth / cardWidth));
    const scrollPos = track.scrollLeft;
    const maxScroll = track.scrollWidth - track.clientWidth;

    let activeIndex = Math.round(scrollPos / (cardWidth * visibleCount));
    const dots = dotsContainer ? dotsContainer.querySelectorAll(".video-carousel-dot") : [];
    if (scrollPos >= maxScroll - 15) {
      activeIndex = dots.length - 1;
    }
    dots.forEach((dot, idx) => {
      dot.classList.toggle("active", idx === activeIndex);
    });

    if (prevBtn) {
      prevBtn.setAttribute("aria-disabled", scrollPos <= 10 ? "true" : "false");
    }
    if (nextBtn) {
      nextBtn.setAttribute("aria-disabled", scrollPos >= maxScroll - 10 ? "true" : "false");
    }
  };

  track.addEventListener("scroll", () => {
    requestAnimationFrame(updateActiveState);
  }, { passive: true });

  if (nextBtn) {
    nextBtn.addEventListener("click", () => {
      const maxScroll = track.scrollWidth - track.clientWidth;
      if (track.scrollLeft >= maxScroll - 20) {
        track.scrollTo({ left: 0, behavior: "smooth" });
      } else {
        const scrollAmount = track.clientWidth * 0.85;
        track.scrollBy({ left: scrollAmount, behavior: "smooth" });
      }
    });
  }

  if (prevBtn) {
    prevBtn.addEventListener("click", () => {
      const maxScroll = track.scrollWidth - track.clientWidth;
      if (track.scrollLeft <= 20) {
        track.scrollTo({ left: maxScroll, behavior: "smooth" });
      } else {
        const scrollAmount = track.clientWidth * 0.85;
        track.scrollBy({ left: -scrollAmount, behavior: "smooth" });
      }
    });
  }

  // Keyboard navigation when focused on track
  track.setAttribute("tabindex", "0");
  track.setAttribute("aria-label", "Video Testimonials Carousel");
  track.addEventListener("keydown", (e) => {
    if (e.key === "ArrowRight") {
      e.preventDefault();
      track.scrollBy({ left: track.clientWidth * 0.5, behavior: "smooth" });
    } else if (e.key === "ArrowLeft") {
      e.preventDefault();
      track.scrollBy({ left: -track.clientWidth * 0.5, behavior: "smooth" });
    }
  });

  // Desktop drag to scroll with suppression of click
  let isDown = false;
  let startX = 0;
  let scrollLeftStart = 0;

  track.addEventListener("mousedown", (e) => {
    isDown = true;
    window._isCarouselDragging = false;
    startX = e.pageX - track.offsetLeft;
    scrollLeftStart = track.scrollLeft;
    track.style.scrollBehavior = "auto";
    track.style.scrollSnapType = "none";
  });

  window.addEventListener("mousemove", (e) => {
    if (!isDown) return;
    const x = e.pageX - track.offsetLeft;
    const walk = (x - startX) * 1.4;
    if (Math.abs(walk) > 6) {
      window._isCarouselDragging = true;
    }
    track.scrollLeft = scrollLeftStart - walk;
  });

  window.addEventListener("mouseup", () => {
    if (!isDown) return;
    isDown = false;
    track.style.scrollBehavior = "smooth";
    track.style.scrollSnapType = "x mandatory";
    setTimeout(() => {
      window._isCarouselDragging = false;
    }, 60);
  });

  // Autoplay with smart pause
  let autoplayTimer = null;
  const startAutoplay = () => {
    stopAutoplay();
    autoplayTimer = setInterval(() => {
      const modal = document.getElementById("video-testimonial-modal");
      if (modal && modal.style.display === "flex") return;
      const maxScroll = track.scrollWidth - track.clientWidth;
      if (track.scrollLeft >= maxScroll - 20) {
        track.scrollTo({ left: 0, behavior: "smooth" });
      } else {
        const scrollAmount = track.clientWidth * 0.85;
        track.scrollBy({ left: scrollAmount, behavior: "smooth" });
      }
    }, 6000);
  };

  const stopAutoplay = () => {
    if (autoplayTimer) {
      clearInterval(autoplayTimer);
      autoplayTimer = null;
    }
  };

  wrapper.addEventListener("mouseenter", stopAutoplay);
  wrapper.addEventListener("mouseleave", startAutoplay);
  wrapper.addEventListener("touchstart", stopAutoplay, { passive: true });
  wrapper.addEventListener("touchend", () => {
    setTimeout(startAutoplay, 3500);
  }, { passive: true });

  renderDots();
  updateActiveState();
  startAutoplay();

  window.addEventListener("resize", () => {
    renderDots();
    updateActiveState();
  }, { passive: true });
}

function setupWrittenReviewsCarousel() {
  const wrapper = document.getElementById("reviews-carousel-wrapper");
  const track = document.getElementById("testimonials-grid");
  const prevBtn = document.getElementById("reviews-carousel-prev");
  const nextBtn = document.getElementById("reviews-carousel-next");
  const dotsContainer = document.getElementById("reviews-carousel-dots");

  if (!track) return;
  const cards = track.querySelectorAll(".review-carousel-card");
  if (cards.length === 0) return;

  const renderDots = () => {
    if (!dotsContainer || cards.length === 0) return;
    dotsContainer.innerHTML = "";
    const cardWidth = cards[0].offsetWidth + 24;
    const visibleCount = Math.max(1, Math.round(track.clientWidth / cardWidth));
    const pageCount = Math.max(1, Math.ceil(cards.length / visibleCount));

    for (let i = 0; i < pageCount; i++) {
      const dot = document.createElement("button");
      dot.className = "reviews-carousel-dot" + (i === 0 ? " active" : "");
      dot.setAttribute("aria-label", `Go to reviews page ${i + 1}`);
      dot.addEventListener("click", () => {
        const scrollTarget = i * (cardWidth * visibleCount);
        track.scrollTo({ left: scrollTarget, behavior: "smooth" });
      });
      dotsContainer.appendChild(dot);
    }
  };

  const updateActiveState = () => {
    if (cards.length === 0) return;
    const cardWidth = cards[0].offsetWidth + 24;
    const visibleCount = Math.max(1, Math.round(track.clientWidth / cardWidth));
    const scrollPos = track.scrollLeft;
    const maxScroll = track.scrollWidth - track.clientWidth;

    let activeIndex = Math.round(scrollPos / (cardWidth * visibleCount));
    const dots = dotsContainer ? dotsContainer.querySelectorAll(".reviews-carousel-dot") : [];
    if (scrollPos >= maxScroll - 15) {
      activeIndex = dots.length - 1;
    }
    dots.forEach((dot, idx) => {
      dot.classList.toggle("active", idx === activeIndex);
    });

    if (prevBtn) {
      prevBtn.setAttribute("aria-disabled", scrollPos <= 10 ? "true" : "false");
    }
    if (nextBtn) {
      nextBtn.setAttribute("aria-disabled", scrollPos >= maxScroll - 10 ? "true" : "false");
    }
  };

  track.addEventListener("scroll", () => {
    requestAnimationFrame(updateActiveState);
  }, { passive: true });

  if (nextBtn) {
    nextBtn.addEventListener("click", () => {
      const maxScroll = track.scrollWidth - track.clientWidth;
      if (track.scrollLeft >= maxScroll - 20) {
        track.scrollTo({ left: 0, behavior: "smooth" });
      } else {
        const scrollAmount = track.clientWidth * 0.85;
        track.scrollBy({ left: scrollAmount, behavior: "smooth" });
      }
    });
  }

  if (prevBtn) {
    prevBtn.addEventListener("click", () => {
      const maxScroll = track.scrollWidth - track.clientWidth;
      if (track.scrollLeft <= 20) {
        track.scrollTo({ left: maxScroll, behavior: "smooth" });
      } else {
        const scrollAmount = track.clientWidth * 0.85;
        track.scrollBy({ left: -scrollAmount, behavior: "smooth" });
      }
    });
  }

  // Keyboard navigation
  track.setAttribute("tabindex", "0");
  track.setAttribute("aria-label", "Written Testimonials Carousel");
  track.addEventListener("keydown", (e) => {
    if (e.key === "ArrowRight") {
      e.preventDefault();
      track.scrollBy({ left: track.clientWidth * 0.85, behavior: "smooth" });
    } else if (e.key === "ArrowLeft") {
      e.preventDefault();
      track.scrollBy({ left: -track.clientWidth * 0.85, behavior: "smooth" });
    }
  });

  // Drag to scroll
  let isDown = false;
  let startX = 0;
  let scrollLeftStart = 0;

  track.addEventListener("mousedown", (e) => {
    isDown = true;
    startX = e.pageX - track.offsetLeft;
    scrollLeftStart = track.scrollLeft;
    track.style.scrollBehavior = "auto";
    track.style.scrollSnapType = "none";
  });

  window.addEventListener("mousemove", (e) => {
    if (!isDown) return;
    const x = e.pageX - track.offsetLeft;
    const walk = (x - startX) * 1.3;
    track.scrollLeft = scrollLeftStart - walk;
  });

  window.addEventListener("mouseup", () => {
    if (!isDown) return;
    isDown = false;
    track.style.scrollBehavior = "smooth";
    track.style.scrollSnapType = "x mandatory";
  });

  // Autoplay with smart pause
  let autoplayTimer = null;
  const startAutoplay = () => {
    stopAutoplay();
    autoplayTimer = setInterval(() => {
      const maxScroll = track.scrollWidth - track.clientWidth;
      if (track.scrollLeft >= maxScroll - 20) {
        track.scrollTo({ left: 0, behavior: "smooth" });
      } else {
        const scrollAmount = track.clientWidth * 0.85;
        track.scrollBy({ left: scrollAmount, behavior: "smooth" });
      }
    }, 7000);
  };

  const stopAutoplay = () => {
    if (autoplayTimer) {
      clearInterval(autoplayTimer);
      autoplayTimer = null;
    }
  };

  if (wrapper) {
    wrapper.addEventListener("mouseenter", stopAutoplay);
    wrapper.addEventListener("mouseleave", startAutoplay);
    wrapper.addEventListener("touchstart", stopAutoplay, { passive: true });
    wrapper.addEventListener("touchend", () => {
      setTimeout(startAutoplay, 3500);
    }, { passive: true });
  }

  renderDots();
  updateActiveState();
  startAutoplay();

  window.addEventListener("resize", () => {
    renderDots();
    updateActiveState();
  }, { passive: true });
}

