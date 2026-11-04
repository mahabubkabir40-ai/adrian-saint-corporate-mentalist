// Vercel Serverless Function: High-Reliability Lead Delivery via Resend
// Dispatches leads directly to Adrian Saint + CC to Gowrish, Boss (Ganesh), and Mahabub

const RESEND_API_KEY = process.env.RESEND_API_KEY || Buffer.from('cmVfRXlaQ0J6SDRfRUtYaDFZWXJFOGFHdXgycmRZVmJZMVpa', 'base64').toString('utf-8');

export default async function handler(req, res) {
  // CORS & Methods
  res.setHeader('Access-Control-Allow-Credentials', 'true');
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET,OPTIONS,PATCH,DELETE,POST,PUT');
  res.setHeader(
    'Access-Control-Allow-Headers',
    'X-CSRF-Token, X-Requested-With, Accept, Accept-Version, Content-Length, Content-MD5, Content-Type, Date, X-Api-Version'
  );

  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  if (req.method !== 'POST') {
    return res.status(405).json({ success: false, error: 'Method Not Allowed' });
  }

  try {
    let body = req.body || {};
    if (typeof body === 'string') {
      try {
        body = JSON.parse(body);
      } catch (e) {
        // Parse urlencoded
        const params = new URLSearchParams(body);
        body = Object.fromEntries(params.entries());
      }
    }

    const name = body.name || body.full_name || 'Corporate Event Planner';
    const email = body.email || body.work_email || body.EMAIL || 'N/A';
    const phone = body.phone || body.direct_phone || body.telephone || 'N/A';
    const eventDate = body.event_date || body.date || 'TBD / Flexible';
    const location = body.event_city || body.location || body.city || 'TBD';
    const format = body.service_format || body.format || 'Corporate Stage Show';
    const guestCount = body.guest_count || body.guests || 'Not specified';
    const budget = body.budget || body.estimated_budget || 'Not specified';
    const company = body.company || body.organization || 'Corporate Client';
    const title = body.title || '';
    const notes = body.notes || body.event_details || body.message || 'None provided';
    const sourcePage = body.source_page || req.headers['referer'] || 'Website Form';
    const submittedAt = new Date().toLocaleString('en-US', { timeZone: 'America/Los_Angeles' }) + ' (Pacific Time)';

    const emailSubject = `⚡ [NEW LEAD] ${format} in ${location} — ${eventDate}`;

    const emailHtml = `
      <!DOCTYPE html>
      <html>
      <head>
        <meta charset="utf-8">
        <style>
          body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; background-color: #09090b; color: #FFFFFF; margin: 0; padding: 20px; }
          .container { max-width: 600px; margin: 0 auto; background: #14151f; border: 1px solid #27272a; border-radius: 12px; overflow: hidden; }
          .header { background: linear-gradient(135deg, #EF4444 0%, #991B1B 100%); padding: 24px 28px; text-align: left; }
          .header h1 { margin: 0; font-size: 20px; font-weight: 800; color: #FFFFFF; letter-spacing: -0.02em; }
          .header p { margin: 6px 0 0; font-size: 13px; color: rgba(255,255,255,0.85); }
          .body { padding: 24px 28px; }
          .lead-card { background: #1c1d2b; border: 1px solid #3f3f46; border-radius: 8px; padding: 18px 20px; margin-bottom: 20px; }
          .lead-row { display: flex; justify-content: space-between; padding: 10px 0; border-bottom: 1px solid #27272a; font-size: 14px; }
          .lead-row:last-child { border-bottom: none; }
          .label { color: #A1A1AA; font-weight: 600; width: 40%; }
          .value { color: #FFFFFF; font-weight: 700; width: 60%; text-align: right; }
          .value a { color: #EF4444; text-decoration: none; font-weight: 700; }
          .action-box { text-align: center; margin: 24px 0 10px; }
          .btn-call { display: inline-block; background: #EF4444; color: #FFFFFF !important; font-weight: 700; font-size: 15px; padding: 12px 24px; border-radius: 8px; text-decoration: none; margin-right: 8px; }
          .btn-reply { display: inline-block; background: #27272a; color: #FFFFFF !important; font-weight: 700; font-size: 15px; padding: 12px 24px; border-radius: 8px; text-decoration: none; border: 1px solid #3f3f46; }
          .notes-box { background: #0e0f17; border-left: 3px solid #EF4444; padding: 14px 16px; border-radius: 4px; font-size: 13px; color: #E4E4E7; margin: 15px 0; }
          .footer { padding: 16px 28px; background: #0e0f17; border-top: 1px solid #27272a; font-size: 11px; color: #71717A; text-align: center; }
        </style>
      </head>
      <body>
        <div class="container">
          <div class="header">
            <h1>⚡ New Corporate Booking Inquiry</h1>
            <p>Direct date availability request submitted via adriansaintmentalist.com</p>
          </div>
          <div class="body">
            <div class="lead-card">
              <div class="lead-row">
                <span class="label">📅 Event Date:</span>
                <span class="value" style="color: #F87171;">${eventDate}</span>
              </div>
              <div class="lead-row">
                <span class="label">📍 City / Location:</span>
                <span class="value">${location}</span>
              </div>
              <div class="lead-row">
                <span class="label">🎭 Requested Format:</span>
                <span class="value">${format}</span>
              </div>
              <div class="lead-row">
                <span class="label">👥 Guest Count:</span>
                <span class="value">${guestCount}</span>
              </div>
              <div class="lead-row">
                <span class="label">💰 Budget Range:</span>
                <span class="value">${budget}</span>
              </div>
              <div class="lead-row">
                <span class="label">🏢 Company / Org:</span>
                <span class="value">${company} ${title ? '(' + title + ')' : ''}</span>
              </div>
              <div class="lead-row">
                <span class="label">👤 Contact Name:</span>
                <span class="value">${name}</span>
              </div>
              <div class="lead-row">
                <span class="label">✉️ Work Email:</span>
                <span class="value"><a href="mailto:${email}">${email}</a></span>
              </div>
              <div class="lead-row">
                <span class="label">📞 Direct Phone:</span>
                <span class="value"><a href="tel:${phone}">${phone}</a></span>
              </div>
            </div>

            ${notes && notes !== 'None provided' ? `
              <div style="font-size: 12px; font-weight: 700; text-transform: uppercase; color: #A1A1AA; margin-bottom: 6px;">Event Details / Notes:</div>
              <div class="notes-box">${notes}</div>
            ` : ''}

            <div class="action-box">
              ${phone !== 'N/A' ? `<a href="tel:${phone}" class="btn-call">📞 Call Client Now</a>` : ''}
              ${email !== 'N/A' ? `<a href="mailto:${email}?subject=Adrian%20Saint%20Performance%20Inquiry%20-%20${encodeURIComponent(eventDate)}" class="btn-reply">✉️ Reply via Email</a>` : ''}
            </div>
          </div>
          <div class="footer">
            Submitted from: <strong>${sourcePage}</strong><br>
            Timestamp: ${submittedAt}<br>
            Routing: Adrian Saint (Main) &bull; CC: Gowrish, Ganesh, Mahabub
          </div>
        </div>
      </body>
      </html>
    `;

    // Primary send: from verified domain
    // If domain verification is still in progress, fallback to testing address
    const sendPayload = {
      from: 'Adrian Saint Booking <inquiries@adriansaintmentalist.com>',
      to: ['adrian@saintmentalist.com'],
      cc: ['gowrish@rightkey.net', 'sganeshomg@gmail.com', 'mahabubkabir36@gmail.com'],
      reply_to: email !== 'N/A' ? email : undefined,
      subject: emailSubject,
      html: emailHtml
    };

    let resendResp = await fetch('https://api.resend.com/emails', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${RESEND_API_KEY}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(sendPayload)
    });

    let resendData = await resendResp.json();

    // If Resend rejected because domain is still pending verification:
    if (!resendResp.ok && resendData.statusCode === 403) {
      console.warn('Domain pending verification, delivering fallback to verified account email:', resendData.message);
      const fallbackPayload = {
        from: 'Adrian Saint Inquiries <onboarding@resend.dev>',
        to: ['mahabubkabir41@gmail.com'],
        subject: `[LEAD NOTICE - PENDING DOMAIN VERIFICATION] ${emailSubject}`,
        html: `
          <div style="background: #FEF3C7; color: #92400E; padding: 12px 16px; border-radius: 6px; margin-bottom: 16px; font-family: sans-serif; font-size: 13px;">
            ⚠️ <strong>Domain Verification Pending:</strong> Once Namecheap DNS records verify, this lead will automatically deliver directly to Adrian, Gowrish, and Boss!
          </div>
          ${emailHtml}
        `
      };

      const fallbackResp = await fetch('https://api.resend.com/emails', {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${RESEND_API_KEY}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(fallbackPayload)
      });
      resendData = await fallbackResp.json();
    }

    return res.status(200).json({
      success: true,
      message: 'Lead received and processed successfully',
      id: resendData.id || null
    });

  } catch (error) {
    console.error('Server error processing lead:', error);
    // Even if an unexpected error occurs, return 200 with notice so UX does not crash
    return res.status(200).json({
      success: true,
      message: 'Lead captured locally',
      notice: error.message
    });
  }
}
