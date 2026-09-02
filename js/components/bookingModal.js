/* ==========================================================================
   ADRIAN SAINT - CORPORATE MENTALIST & AI SEO LEAD GENERATION PLATFORM
   Interactive Dynamic Booking & Live Video Modal Engine (Real YouTube Stream)
   ========================================================================== */

export function setupBookingModal() {
  // Global event delegation for modal trigger buttons
  document.addEventListener("click", (e) => {
    const trigger = e.target.closest(".open-booking-modal");
    if (trigger) {
      e.preventDefault();
      const cityAttr = trigger.getAttribute("data-city") || "";
      openBookingModalDynamic(cityAttr);
    }

    const videoTrigger = e.target.closest(".open-video-modal");
    if (videoTrigger) {
      e.preventDefault();
      const videoId = videoTrigger.getAttribute("data-video-id") || "jnwJ1-k-dU8";
      openVideoModalDynamic(videoId);
    }
  });
}

function openBookingModalDynamic(cityName = "") {
  let modalEl = document.getElementById("booking-modal");
  if (!modalEl) {
    modalEl = document.createElement("div");
    modalEl.className = "modal-overlay";
    modalEl.id = "booking-modal";
    modalEl.innerHTML = `
      <div class="modal-content">
        <button class="modal-close" id="modal-close-btn">&times;</button>
        <div id="quote-form-container">
          <h2 class="text-gradient-gold" style="margin-bottom: 0.5rem;">Check Availability & Fees</h2>
          <p style="font-size: 0.95rem; margin-bottom: 1.5rem;">Fill out the form below to receive pricing and availability for your event.</p>

          <form id="quote-form">
            <div class="grid-2">
              <div class="form-group">
                <label class="form-label">Your Name *</label>
                <input type="text" class="form-input" required placeholder="e.g. Sarah Jenkins">
              </div>
              <div class="form-group">
                <label class="form-label">Company / Organization *</label>
                <input type="text" class="form-input" required placeholder="e.g. Deloitte / Google">
              </div>
            </div>

            <div class="grid-2">
              <div class="form-group">
                <label class="form-label">Email Address *</label>
                <input type="email" class="form-input" required placeholder="sarah@company.com">
              </div>
              <div class="form-group">
                <label class="form-label">Phone Number *</label>
                <input type="tel" class="form-input" required placeholder="(555) 000-0000">
              </div>
            </div>

            <div class="grid-2">
              <div class="form-group">
                <label class="form-label">Event Date *</label>
                <input type="date" class="form-input" required>
              </div>
              <div class="form-group">
                <label class="form-label">Event Location / City *</label>
                <input type="text" id="event-city-input" class="form-input" required value="${cityName}" placeholder="e.g. San Francisco, CA">
              </div>
            </div>

            <div class="form-group">
              <label class="form-label">Event Type & Details *</label>
              <textarea class="form-textarea" rows="3" required placeholder="Please describe your event format (Stage Show, Strolling, Trade Show, Custom Hybrid), guest count, or schedule..."></textarea>
            </div>

            <button type="submit" class="btn btn-gold" style="width: 100%; margin-top: 1rem;">
              <span>Submit Availability Request</span>
            </button>
          </form>

          <div id="quote-success-message" style="display: none; text-align: center; padding: 2rem 0;">
            <div style="font-size: 3.5rem; margin-bottom: 1rem;">🎉</div>
            <h3 class="text-gradient-gold" style="margin-bottom: 0.5rem;">Availability Request Submitted!</h3>
            <p style="color: var(--text-muted);">Thank you! Adrian's event team will review your details and send fee & booking information within 2 business hours.</p>
          </div>
        </div>
      </div>
    `;
    document.body.appendChild(modalEl);

    modalEl.querySelector(".modal-close").addEventListener("click", () => closeModal(modalEl));
    modalEl.addEventListener("click", (e) => { if (e.target === modalEl) closeModal(modalEl); });

    const formEl = modalEl.querySelector("#quote-form");
    const successEl = modalEl.querySelector("#quote-success-message");
    formEl.addEventListener("submit", (e) => {
      e.preventDefault();
      const submitBtn = formEl.querySelector("button[type='submit']");
      submitBtn.disabled = true;
      submitBtn.innerHTML = "<span>Processing Quote Request...</span>";
      setTimeout(() => {
        formEl.style.display = "none";
        successEl.style.display = "block";
        submitBtn.disabled = false;
        submitBtn.innerHTML = "<span>Submit Availability Request</span>";
      }, 1000);
    });
  }

  if (cityName && modalEl.querySelector("#event-city-input")) {
    modalEl.querySelector("#event-city-input").value = cityName;
  }

  modalEl.classList.add("active");
}

function openVideoModalDynamic(videoId = "jnwJ1-k-dU8") {
  let modalEl = document.getElementById("video-modal");
  if (!modalEl) {
    modalEl = document.createElement("div");
    modalEl.className = "modal-overlay";
    modalEl.id = "video-modal";
    document.body.appendChild(modalEl);
  }

  modalEl.innerHTML = `
    <div class="modal-content" style="max-width: 960px; padding: 1.75rem; background: #11131c;">
      <button class="modal-close" id="video-modal-close">&times;</button>
      <h3 class="text-gradient-gold" style="margin-bottom: 1rem; font-size: 1.35rem;">Adrian Saint — Live Performance & Mind Reading Reel</h3>
      <div style="position: relative; aspect-ratio: 16/9; background: #000; border-radius: 12px; overflow: hidden; border: 1px solid var(--border-gold-glow); box-shadow: 0 10px 40px rgba(0,0,0,0.9);">
        <iframe 
          src="https://www.youtube-nocookie.com/embed/${videoId}?autoplay=1&rel=0&modestbranding=1" 
          title="Adrian Saint Performance Video"
          style="position: absolute; top:0; left:0; width:100%; height:100%; border:0;" 
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
          allowfullscreen>
        </iframe>
      </div>
      <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 1.25rem; flex-wrap: wrap; gap: 1rem;">
        <p style="color: var(--text-silver); font-size: 0.9rem; margin: 0;">Recorded live at Fortune 500 summits, corporate galas & executive retreats.</p>
        <button class="btn btn-gold open-booking-modal" onclick="document.getElementById('video-modal').classList.remove('active');">
          <span>Check Availability & Fees</span>
        </button>
      </div>
    </div>
  `;

  modalEl.querySelector(".modal-close").addEventListener("click", () => {
    modalEl.innerHTML = ""; // Stop video playback on close
    closeModal(modalEl);
  });
  
  modalEl.addEventListener("click", (e) => { 
    if (e.target === modalEl) {
      modalEl.innerHTML = ""; // Stop video playback on close
      closeModal(modalEl);
    }
  });

  modalEl.classList.add("active");
}

function closeModal(modalEl) {
  if (modalEl) {
    modalEl.classList.remove("active");
  }
}
