import os

ROOT = os.path.dirname(os.path.abspath(__file__))

ICONS = {
    "ad": '<svg viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2"><path d="M4 4l8 8-8 8M20 4v16"/></svg>',
    "qr": '<svg viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/><path d="M14 14h3v3h-3zM20 14v3M14 20h3M20 20h.01"/></svg>',
    "link": '<svg viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2"><path d="M9 15l6-6M8 12l-3 3a3 3 0 004 4l3-3M16 12l3-3a3 3 0 00-4-4l-3 3"/></svg>',
    "widget": '<svg viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2"><path d="M21 11.5a8.38 8.38 0 01-.9 3.8 8.5 8.5 0 01-7.6 4.7 8.38 8.38 0 01-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 01-.9-3.8 8.5 8.5 0 014.7-7.6 8.38 8.38 0 013.8-.9h.5a8.48 8.48 0 018 8v.5z"/></svg>',
    "bot": '<svg viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2"><rect x="4" y="8" width="16" height="12" rx="2"/><path d="M9 13v1M15 13v1M12 8V4M9 4h6"/></svg>',
    "form": '<svg viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2"><path d="M9 3H6a2 2 0 00-2 2v14a2 2 0 002 2h12a2 2 0 002-2V9l-6-6H9z"/><path d="M13 3v6h6M8 13h8M8 17h5"/></svg>',
    "broadcast": '<svg viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2"><circle cx="12" cy="12" r="2"/><path d="M8.5 8.5a5 5 0 000 7M15.5 8.5a5 5 0 010 7M5.5 5.5a9 9 0 000 13M18.5 5.5a9 9 0 010 13"/></svg>',
    "sequence": '<svg viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2"><path d="M17 2l4 4-4 4M3 11V9a4 4 0 014-4h14M7 22l-4-4 4-4M21 13v2a4 4 0 01-4 4H3"/></svg>',
    "inbox": '<svg viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2"><path d="M22 12h-6l-2 3h-4l-2-3H2"/><path d="M5.45 5.11L2 12v6a2 2 0 002 2h16a2 2 0 002-2v-6l-3.45-6.89A2 2 0 0016.76 4H7.24a2 2 0 00-1.79 1.11z"/></svg>',
    "payments": '<svg viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2"><rect x="2" y="5" width="20" height="14" rx="2"/><path d="M2 10h20M6 15h4"/></svg>',
}

FEATURES = [
    {
        "slug": "click-to-whatsapp-ads",
        "name": "Click-to-WhatsApp Ads",
        "cat": "Capture Leads",
        "tag": "Turn ad clicks into live conversations",
        "icon": "ad",
        "body": [
            "Click-to-WhatsApp Ads take someone from a Facebook or Instagram ad straight into a live chat with your business \u2014 no landing page, no form to fill, no waiting for a callback.",
            "The moment a person taps your ad, a WhatsApp conversation opens automatically. You can pre-fill a greeting message so the chat starts warm instead of blank, and every conversation is logged in your Fame Inbox so your team sees exactly which ad brought the lead in."
        ],
    },
    {
        "slug": "qr-to-whatsapp",
        "name": "QR-to-WhatsApp",
        "cat": "Capture Leads",
        "tag": "Scan a code, open a chat instantly",
        "icon": "qr",
        "body": [
            "Generate a scannable code that opens a WhatsApp chat with your business the moment someone points their camera at it \u2014 perfect for storefronts, packaging, print ads, or event booths.",
            "Each code can carry its own pre-filled greeting, so you always know where a conversation started, whether that's a shop counter, a flyer, or a product box."
        ],
    },
    {
        "slug": "link-to-whatsapp",
        "name": "Link-to-WhatsApp",
        "cat": "Capture Leads",
        "tag": "Share a link that opens a chat",
        "icon": "link",
        "body": [
            "Create a simple link that opens a WhatsApp conversation the instant someone clicks it \u2014 drop it in an email signature, a bio link, an SMS campaign, or anywhere else a normal link would go.",
            "No app switching confusion, no phone number to copy and paste \u2014 one tap and the customer is already chatting with you."
        ],
    },
    {
        "slug": "web-widget-to-whatsapp",
        "name": "Web Widget-to-WhatsApp",
        "cat": "Capture Leads",
        "tag": "Chat button on your website",
        "icon": "widget",
        "body": [
            "Add a floating chat button to your website that opens a WhatsApp conversation instead of a generic contact form \u2014 visitors reach a real person (or your bot) in one click, right where their intent is highest.",
            "Customize the button's color, position, and greeting message to match your site, and every chat started from the widget lands directly in your shared Fame Inbox."
        ],
    },
    {
        "slug": "whatsapp-chatbots",
        "name": "WhatsApp Chatbots",
        "cat": "Qualify Leads",
        "tag": "Automate responses and qualify leads at scale",
        "icon": "bot",
        "body": [
            "Build a chatbot that greets every incoming conversation, asks the right qualifying questions, and routes the customer to the right next step \u2014 without a human needing to type the first reply.",
            "Design flows visually with no code, branch based on what the customer says, and hand off to a live agent automatically once a lead is qualified and ready."
        ],
    },
    {
        "slug": "whatsapp-forms",
        "name": "WhatsApp Forms",
        "cat": "Qualify Leads",
        "tag": "Collect customer details within the chat",
        "icon": "form",
        "body": [
            "Collect structured information \u2014 name, order details, preferences, appointment times \u2014 directly inside the WhatsApp conversation instead of redirecting customers to an external form.",
            "Responses are saved automatically against the customer's chat history, so your team has full context the moment they pick up the conversation."
        ],
    },
    {
        "slug": "whatsapp-broadcasts",
        "name": "WhatsApp Broadcasts",
        "cat": "Nurture Leads",
        "tag": "Send campaigns to your customer list at once",
        "icon": "broadcast",
        "body": [
            "Send a single message to a segmented list of customers at once \u2014 offers, restock alerts, event reminders \u2014 using approved WhatsApp message templates.",
            "Track delivery, read rates, and replies from one dashboard, and let interested replies flow straight back into your shared team inbox for follow-up."
        ],
    },
    {
        "slug": "whatsapp-sequences",
        "name": "WhatsApp Sequences",
        "cat": "Nurture Leads",
        "tag": "Automate scheduled follow-up messages",
        "icon": "sequence",
        "body": [
            "Set up a series of automated follow-up messages that go out on a schedule you define \u2014 a reminder two days after someone browses, a check-in a week after purchase, a re-engagement nudge for quiet leads.",
            "Sequences stop automatically the moment a customer replies, so no one gets a message that no longer makes sense."
        ],
    },
    {
        "slug": "whatsapp-team-inbox",
        "name": "WhatsApp Team Inbox",
        "cat": "Close Deals",
        "tag": "Manage all conversations together in one place",
        "icon": "inbox",
        "body": [
            "Give your whole team access to one shared WhatsApp number, with conversations assignable to specific agents so nothing gets answered twice or missed entirely.",
            "Leave private internal notes on a chat, tag teammates for input, and see full conversation history the moment a customer messages back."
        ],
    },
    {
        "slug": "whatsapp-payments",
        "name": "WhatsApp Payments",
        "cat": "Close Deals",
        "tag": "Accept payments directly inside the chat",
        "icon": "payments",
        "body": [
            "Send a payment link directly inside a WhatsApp conversation and let customers pay without leaving the chat \u2014 no separate checkout page, no extra app.",
            "Payment confirmations post back into the same conversation automatically, so both your team and the customer have a clear record in one thread."
        ],
    },
]

CATS = ["Capture Leads", "Qualify Leads", "Nurture Leads", "Close Deals"]

def head(title, desc, depth=""):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="stylesheet" href="{depth}style.css">
</head>
<body>
"""

def header(depth=""):
    cols = {c: [f for f in FEATURES if f["cat"] == c] for c in CATS}
    mega_cols = ""
    for c in CATS:
        items = ""
        for f in cols[c]:
            items += f"""
              <a class="mega-item" href="{depth}features/{f['slug']}.html">
                <div class="icon">{ICONS[f['icon']]}</div>
                <div><h4>{f['name']}</h4><p>{f['tag']}</p></div>
              </a>"""
        mega_cols += f"""
            <div>
              <p class="mega-col-title">{c}</p>{items}
            </div>"""
    return f"""<header>
  <div class="nav-wrap">
    <a href="{depth}index.html" class="logo">FAME <span>INBOX</span></a>
    <nav class="primary">
      <ul>
        <li><a href="{depth}index.html">Home</a></li>
        <li class="has-mega" id="featuresLi">
          <button class="navtop" id="featuresBtn" aria-expanded="false">Features <span class="caret">&#9662;</span></button>
          <div class="mega">{mega_cols}
          </div>
        </li>
        <li><a href="{depth}features/index.html">All Features</a></li>
        <li><a href="{depth}pricing.html">Pricing</a></li>
        <li><a href="{depth}about.html">About Us</a></li>
        <li><a href="{depth}contact.html">Contact</a></li>
        <li><a href="https://app.fameinbox.com/">Login</a></li>
      </ul>
      <a href="https://getamohan.zohobookings.in/#/407269000000044006?bookedFrom=ShortenURL" class="cta-header" target="_blank" rel="noopener">Book a Demo</a>
    </nav>
  </div>
</header>
"""

def footer(depth=""):
    return f"""<footer>
  &copy; 2026 <span>Fame Inbox</span>. All rights reserved. &middot; <a href="{depth}contact.html">Contact us</a>
</footer>
<script src="{depth}menu.js"></script>
</body>
</html>
"""

# ---------- Home page ----------
def build_home():
    strip_cards = ""
    for c in CATS:
        items = ""
        for f in [x for x in FEATURES if x["cat"] == c][:2]:
            items += f"""<div class="item"><div class="dot"></div><div><h4>{f['name']}</h4><p>{f['tag']}</p></div></div>"""
        strip_cards += f"""<div class="strip-card"><p class="cat">{c.split()[0]}</p>{items}</div>"""

    journey_data = [
        ("capture", "Capture", "Every inquiry captured in real time",
         "Leads from Click-to-WhatsApp ads, QR codes, links, or your website chat widget land in a live conversation instantly — no forms, no redirects, no waiting.",
         ICONS["ad"]),
        ("qualify", "Qualify", "Sales-ready before your team steps in",
         "Your chatbot asks the right questions and scores intent automatically, so your team inherits context instead of a cold lead.",
         ICONS["bot"]),
        ("nurture", "Nurture", "Most deals die from silence, not rejection",
         "Automated sequences and broadcasts follow up the moment a lead goes quiet — fully configurable, fully automatic.",
         ICONS["sequence"]),
        ("close", "Close", "From intent to commitment, no friction",
         "Your shared team inbox and in-chat payments mean a ready buyer can be closed without ever leaving the conversation.",
         ICONS["payments"]),
    ]
    tabs_html = "".join(
        f'<button class="journey-tab{" active" if i==0 else ""}" data-target="panel-{key}">{label}</button>'
        for i, (key, label, _, _, _) in enumerate(journey_data)
    )
    panels_html = "".join(f"""
    <div class="journey-panel{' active' if i==0 else ''}" id="panel-{key}">
      <div>
        <h3>{title}</h3>
        <p>{desc}</p>
        <a href="features/index.html" class="btn-secondary">See how it works</a>
      </div>
      <div class="journey-visual"><svg viewBox="0 0 24 24" style="stroke:#6E1E42">{icon.replace('stroke="white"','stroke="#6E1E42"')}</svg></div>
    </div>""" for i, (key, label, title, desc, icon) in enumerate(journey_data))

    html = head("Fame Inbox — Where conversations become customers",
                "WhatsApp business messaging platform: capture, qualify, nurture and close leads in one shared inbox.")
    html += header()
    html += f"""
<section class="page-hero">
  <span class="eyebrow">Trusted by growing businesses &middot; Official Meta Business Partner</span>
  <h1>Where conversations<br>become <span class="accent">customers</span></h1>
  <p class="sub">Capture, qualify, nurture and close every lead on the app your customers already have open — WhatsApp.</p>
  <div class="hero-cta">
    <a href="https://getamohan.zohobookings.in/#/407269000000044006?bookedFrom=ShortenURL" class="btn-primary" target="_blank" rel="noopener">Book a Demo</a>
    <a href="contact.html" class="btn-secondary">Start Free Trial</a>
  </div>
  <div class="hero-mockup">
    <div class="hero-mockup-head"><span class="dot"></span> Fame Inbox — Live Chat</div>
    <div class="hero-mockup-body">
      <div class="bubble in">Hi! I saw your ad — do you deliver to Chennai?</div>
      <div class="bubble out">Yes! Free delivery on orders over ₹999 🚚</div>
      <div class="bubble in">Perfect, I'd like to order 2 sarees</div>
      <div class="bubble out">Great choice — here's a payment link to complete your order ✅</div>
    </div>
  </div>
</section>

<section class="journey reveal">
  <div class="journey-tabs">{tabs_html}</div>
  {panels_html}
</section>

<section class="strip reveal">
  <div class="strip-head">
    <span class="eyebrow">What you get</span>
    <h2>One inbox, every stage of the journey</h2>
    <p>From the first ad click to the final payment — all inside a single WhatsApp workflow.</p>
  </div>
  <div class="strip-grid">{strip_cards}</div>
</section>

<section class="trust-row reveal">
  <p>Trusted by growing businesses</p>
  <div class="trust-badges">
    <span class="trust-badge">Meta Business Partner</span>
    <span class="trust-badge">Data Encrypted</span>
    <span class="trust-badge">99.9% Uptime</span>
  </div>
</section>

<section class="testimonials reveal">
  <div class="strip-head">
    <span class="eyebrow">Customers</span>
    <h2>What businesses are saying</h2>
    <p>Real quotes from your customers go here once available.</p>
  </div>
  <div class="testi-grid">
    <div class="testi-card"><span class="testi-placeholder-tag">Sample — replace with a real quote</span><p class="quote">"Add a short quote from a happy customer here."</p><p class="who">Customer Name</p><p class="role">Role, Company</p></div>
    <div class="testi-card"><span class="testi-placeholder-tag">Sample — replace with a real quote</span><p class="quote">"Add a short quote from a happy customer here."</p><p class="who">Customer Name</p><p class="role">Role, Company</p></div>
    <div class="testi-card"><span class="testi-placeholder-tag">Sample — replace with a real quote</span><p class="quote">"Add a short quote from a happy customer here."</p><p class="who">Customer Name</p><p class="role">Role, Company</p></div>
  </div>
</section>
"""
    html += footer()
    with open(os.path.join(ROOT, "index.html"), "w") as f:
        f.write(html)

# ---------- Features hub ----------
def build_hub():
    html = head("All Features — Fame Inbox", "Every Fame Inbox feature for capturing, qualifying, nurturing and closing leads on WhatsApp.", depth="../")
    html += header(depth="../")
    html += """
<section class="page-hero">
  <span class="eyebrow">Features</span>
  <h1>Everything you need, <span class="accent">in one WhatsApp inbox</span></h1>
  <p class="sub">From the first ad click to the final payment confirmation — browse every tool below.</p>
</section>
<div class="hub-grid">
"""
    for c in CATS:
        html += f'<p class="hub-cat">{c}</p>'
        for feat in [x for x in FEATURES if x["cat"] == c]:
            html += f"""
<a class="hub-card" href="{feat['slug']}.html">
  <div class="icon">{ICONS[feat['icon']]}</div>
  <h4>{feat['name']}</h4>
  <p>{feat['tag']}</p>
</a>"""
    html += "\n</div>\n"
    html += footer(depth="../")
    with open(os.path.join(ROOT, "features", "index.html"), "w") as f:
        f.write(html)

# ---------- Feature detail pages ----------
def build_feature(feat):
    icon_svg = ICONS[feat["icon"]].replace('stroke="white"', 'stroke="#6E1E42"')
    body_html = "".join(f"<p>{p}</p>" for p in feat["body"])
    html = head(f"{feat['name']} — Fame Inbox", feat["tag"], depth="../")
    html += header(depth="../")
    html += f"""
<section class="page-hero">
  <span class="eyebrow">{feat['cat']}</span>
  <h1>{feat['name']}</h1>
  <p class="sub">{feat['tag']}</p>
</section>
<div class="detail-body">
  <div class="detail-illustration">
    <svg viewBox="0 0 24 24" style="width:64px;height:64px;">{icon_svg}</svg>
  </div>
  <div class="detail-section">
    {body_html}
  </div>
  <div class="detail-cta">
    <h3>See {feat['name']} in action</h3>
    <p>Book a short demo and we'll walk you through it live.</p>
    <a href="https://getamohan.zohobookings.in/#/407269000000044006?bookedFrom=ShortenURL" class="btn-primary" target="_blank" rel="noopener">Book a Demo</a>
  </div>
</div>
"""
    html += footer(depth="../")
    with open(os.path.join(ROOT, "features", f"{feat['slug']}.html"), "w") as f:
        f.write(html)

# ---------- About / Contact ----------
def build_about():
    html = head("About Us — Fame Inbox", "Fame Inbox helps businesses turn WhatsApp conversations into customers.")
    html += header()
    html += """
<section class="page-hero">
  <span class="eyebrow">About Us</span>
  <h1>Built for businesses<br><span class="accent">that live in the chat</span></h1>
  <p class="sub">Fame Inbox gives growing businesses one shared WhatsApp workspace to capture, qualify, nurture and close every conversation.</p>
</section>
<div class="detail-body">
  <div class="detail-section">
    <h2>Why we built this</h2>
    <p>Most customers today would rather message a business than fill out a form or wait on hold. Fame Inbox exists so your team can meet them there — with automation that qualifies leads instantly and a shared inbox that keeps every conversation organized.</p>
    <h2>What we stand for</h2>
    <p>Fast responses, clear ownership of every conversation, and tools your team can actually set up without an engineer. That's the whole product philosophy.</p>
  </div>
</div>
"""
    html += footer()
    with open(os.path.join(ROOT, "about.html"), "w") as f:
        f.write(html)

def build_contact():
    html = head("Contact — Fame Inbox", "Get in touch with Fame Inbox or book a demo.")
    html += header()
    html += """
<section class="page-hero">
  <span class="eyebrow">Contact</span>
  <h1>Let's get you <span class="accent">set up</span></h1>
  <p class="sub">Book a demo and we'll walk you through Fame Inbox live, or reach out directly below.</p>
</section>
<div class="detail-body">
  <div class="detail-cta">
    <h3>Book a Demo</h3>
    <p>Pick a time that works and we'll show you the full platform.</p>
    <a href="https://getamohan.zohobookings.in/#/407269000000044006?bookedFrom=ShortenURL" class="btn-primary" target="_blank" rel="noopener">Book a Demo</a>
  </div>
</div>
"""
    html += footer()
    with open(os.path.join(ROOT, "contact.html"), "w") as f:
        f.write(html)

def build_pricing():
    html = head("Pricing — Fame Inbox", "Fame Inbox pricing plans.")
    html += header()
    html += """
<section class="page-hero">
  <span class="eyebrow">Pricing</span>
  <h1>Plans that <span class="accent">grow with you</span></h1>
  <p class="sub">Simple plans for every stage — from a free trial to full WhatsApp API access.</p>
</section>
<div class="pricing-grid">

  <div class="price-card">
    <h3>Free Trial</h3>
    <div class="price-amount">Free</div>
    <ul>
      <li>WhatsApp + Instagram</li>
      <li>Try core features before you commit</li>
    </ul>
    <a href="https://getamohan.zohobookings.in/#/407269000000044006?bookedFrom=ShortenURL" class="btn-secondary" target="_blank" rel="noopener">Start Free Trial</a>
  </div>

  <div class="price-card">
    <h3>WhatsApp Basic Chatbots &amp; Automations</h3>
    <div class="price-amount">Contact us<span> for pricing</span></div>
    <ul>
      <li>WhatsApp chatbot automation</li>
      <li>Full details on request</li>
    </ul>
    <a href="https://getamohan.zohobookings.in/#/407269000000044006?bookedFrom=ShortenURL" class="btn-secondary" target="_blank" rel="noopener">Book a Demo</a>
  </div>

  <div class="price-card">
    <h3>Instagram DM Chatbots &amp; Comment Automations</h3>
    <div class="price-amount">Contact us<span> for pricing</span></div>
    <ul>
      <li>Instagram DM + comment automation</li>
      <li>Full details on request</li>
    </ul>
    <a href="https://getamohan.zohobookings.in/#/407269000000044006?bookedFrom=ShortenURL" class="btn-secondary" target="_blank" rel="noopener">Book a Demo</a>
  </div>

  <div class="price-card featured">
    <h3>Official WhatsApp API &amp; Bulk Messaging</h3>
    <div class="price-amount">₹999<span>/mo (or $99/mo)</span></div>
    <ul>
      <li>Connect up to 5 numbers to Official WhatsApp API</li>
      <li>Import & store up to 1 million contacts in CRM</li>
      <li>Send messages via APIs, receive via webhooks</li>
      <li>Custom fields & contact segments</li>
      <li>Send bulk campaigns</li>
      <li>Collect payments via WhatsApp native payments</li>
      <li>Shared inbox for checking & replying to messages</li>
      <li>Connect external integrations via APIs/webhooks</li>
    </ul>
    <a href="https://getamohan.zohobookings.in/#/407269000000044006?bookedFrom=ShortenURL" class="btn-primary" target="_blank" rel="noopener">Book a Demo</a>
  </div>

</div>

<div class="detail-body">
  <div class="detail-section">
    <h2>Not included in the API &amp; Bulk Messaging plan</h2>
    <p>Team members for inbox &middot; other social channels (Facebook/Instagram) &middot; WhatsApp chatbots/automations &middot; WhatsApp native ecommerce store &middot; WhatsApp native Forms/Mini Apps Builder. Access on this plan is limited to CRM and Inbox.</p>
    <h2>Good to know</h2>
    <p>Support is available via support tickets with a 3-day SLA. WhatsApp conversation charges are prepaid via wallet deposit per channel, with a minimum recharge of $20 / ₹1000 per channel. Sending spam marketing to random numbers risks a Meta ban on your business account or numbers. All taxes and payment gateway fees are extra.</p>
  </div>
</div>
"""
    html += footer()
    with open(os.path.join(ROOT, "pricing.html"), "w") as f:
        f.write(html)

build_home()
build_hub()
build_pricing()
for feat in FEATURES:
    build_feature(feat)
build_about()
build_contact()
print("Build complete.")
