import os

ROOT = os.path.dirname(os.path.abspath(__file__))
os.makedirs(os.path.join(ROOT, "products"), exist_ok=True)

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
    "messenger": '<svg viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2"><path d="M12 2C6.5 2 2 6.1 2 11.2c0 2.9 1.5 5.5 3.8 7.2V22l3.5-1.9c1 .3 2.1.4 3.2.4 5.5 0 10-4.1 10-9.3S17.5 2 12 2z"/><path d="M7 13l3-3 2.5 2 3.5-4"/></svg>',
    "instagram": '<svg viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1"/></svg>',
    "crm": '<svg viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2"><circle cx="12" cy="8" r="4"/><path d="M4 21c0-4 4-6 8-6s8 2 8 6"/></svg>',
    "builder": '<svg viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/></svg>',
    "automation": '<svg viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2"><circle cx="12" cy="12" r="3"/><path d="M12 2v3M12 19v3M4.2 4.2l2.1 2.1M17.7 17.7l2.1 2.1M2 12h3M19 12h3M4.2 19.8l2.1-2.1M17.7 6.3l2.1-2.1"/></svg>',
    "shop": '<svg viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2"><path d="M3 9l1-5h16l1 5"/><path d="M3 9a2 2 0 004 0 2 2 0 004 0 2 2 0 004 0 2 2 0 004 0"/><path d="M5 9v10h14V9"/></svg>',
    "gift": '<svg viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2"><rect x="3" y="8" width="18" height="13"/><path d="M3 8h18M12 8v13M12 8c-1.5-4-6-4-6-1s3 1 6 1zM12 8c1.5-4 6-4 6-1s-3 1-6 1z"/></svg>',
    "calendar": '<svg viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2"><rect x="3" y="5" width="18" height="16" rx="2"/><path d="M16 3v4M8 3v4M3 10h18"/></svg>',
    "chart": '<svg viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2"><path d="M4 20V10M12 20V4M20 20v-7"/></svg>',
    "folder": '<svg viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2"><path d="M3 7a2 2 0 012-2h4l2 2h8a2 2 0 012 2v9a2 2 0 01-2 2H5a2 2 0 01-2-2z"/></svg>',
    "radio": '<svg viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2"><circle cx="12" cy="12" r="2"/><path d="M8.5 8.5a5 5 0 000 7M15.5 15.5a5 5 0 000-7M5.5 5.5a9 9 0 000 13M18.5 18.5a9 9 0 000-13"/></svg>',
    "grid": '<svg viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/></svg>',
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
    {
        "slug": "facebook-messenger",
        "name": "Facebook Messenger",
        "cat": "Beyond WhatsApp",
        "tag": "Automate conversations on Messenger",
        "icon": "messenger",
        "body": [
            "Bring the same automation and shared inbox you use on WhatsApp over to Facebook Messenger — automated replies, chatbots, and full conversation history in one unified view.",
            "Track engagement across every Messenger conversation and let your whole team collaborate on replies from a single workspace."
        ],
    },
    {
        "slug": "instagram-automation",
        "name": "Instagram Automation",
        "cat": "Beyond WhatsApp",
        "tag": "Turn DMs and comments into conversations",
        "icon": "instagram",
        "body": [
            "Automatically respond to Instagram DMs, track comments and story mentions, and never miss a lead that comes in through social engagement.",
            "Every Instagram conversation lands in the same shared inbox as your WhatsApp and Messenger chats, so your team never has to juggle apps."
        ],
    },
    {
        "slug": "smart-crm",
        "name": "Smart CRM",
        "cat": "Beyond WhatsApp",
        "tag": "Understand and segment every customer",
        "icon": "crm",
        "body": [
            "A CRM built specifically for conversation-driven businesses — segment customers automatically, tag and filter contacts, and track the full customer journey from first message to repeat purchase.",
            "Every channel feeds into the same customer profile, so your team always has full context no matter where the conversation started."
        ],
    },
    {
        "slug": "visual-bot-builder",
        "name": "Visual Bot Builder",
        "cat": "Beyond WhatsApp",
        "tag": "Build chatbots with zero code",
        "icon": "builder",
        "body": [
            "Design multi-step conversation flows with a drag-and-drop builder — no developers required. Start from ready-made templates or build entirely custom logic.",
            "Deploy the same bot across WhatsApp, Messenger, and Instagram, with support for multiple languages built in."
        ],
    },
    {
        "slug": "automation-builder",
        "name": "Automation Builder",
        "cat": "Beyond WhatsApp",
        "tag": "Automate workflows end-to-end",
        "icon": "automation",
        "body": [
            "Go beyond simple chatbot replies with a visual workflow builder that connects triggers, conditions, and actions across your whole business — no complex code needed.",
            "Connect to your existing tools and let entire processes run automatically once a conversation hits a certain condition."
        ],
    },
]

CATS = ["Capture Leads", "Qualify Leads", "Nurture Leads", "Close Deals", "Beyond WhatsApp"]

BASE_URL = "https://fameinbox.com"

def head(title, desc, depth="", path=""):
    canonical = f"{BASE_URL}/{path}"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">
<link rel="icon" type="image/svg+xml" href="{depth}favicon.svg">

<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:site_name" content="Fame Inbox">

<meta name="twitter:card" content="summary">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">

<link rel="stylesheet" href="{depth}style.css">

<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Fame Inbox",
  "url": "{BASE_URL}",
  "description": "WhatsApp business messaging platform for capturing, qualifying, nurturing and closing leads in one shared inbox.",
  "sameAs": ["https://wa.me/918939888107"]
}}
</script>
</head>
<body>
"""

PRODUCTS = [
    {"slug": "ecommerce", "name": "Ecommerce", "cat": "Commerce & Loyalty",
     "tag": "Sell products directly through WhatsApp", "icon": "shop",
     "body": ["A complete storefront inside WhatsApp — customers browse your catalog, add to cart, and check out without leaving the conversation."]},
    {"slug": "rewardz", "name": "Rewardz", "cat": "Commerce & Loyalty",
     "tag": "Turn repeat customers into loyal ones", "icon": "gift",
     "body": ["Track loyalty points and distribute rewards automatically, right inside the same conversations you're already having with customers."]},
    {"slug": "whatsapp-miniapps", "name": "WhatsApp MiniApps", "cat": "Commerce & Loyalty",
     "tag": "Rich in-chat experiences beyond plain text", "icon": "widget",
     "body": ["Build interactive mini-apps that run directly inside WhatsApp — for bookings, catalogs, or custom flows your business needs."]},
    {"slug": "dynamic-experiences", "name": "Dynamic Experiences", "cat": "Automation & Scheduling",
     "tag": "Personalized, interactive content at scale", "icon": "automation",
     "body": ["Generate personalized images, PDFs, and interactive content on the fly for each customer — automatically, without manual design work."]},
    {"slug": "calendar", "name": "Calendar", "cat": "Automation & Scheduling",
     "tag": "Automated appointment scheduling", "icon": "calendar",
     "body": ["Sync with Google and Outlook calendars to let customers book, reschedule, and get reminders — all inside WhatsApp."]},
    {"slug": "crm-analytics", "name": "CRM Analytics", "cat": "CRM & Operations",
     "tag": "See what's actually happening with your customers", "icon": "chart",
     "body": ["Real-time dashboards showing customer segments, conversation volume, and team performance — so decisions aren't based on guesswork."]},
    {"slug": "departments", "name": "Departments", "cat": "CRM & Operations",
     "tag": "Route conversations to the right team", "icon": "inbox",
     "body": ["Organize your team into departments — sales, support, billing — so conversations reach the right people automatically."]},
    {"slug": "media-manager", "name": "Media Manager", "cat": "CRM & Operations",
     "tag": "Organize every image, video, and file in one place", "icon": "folder",
     "body": ["A central library for all the media your team sends across conversations — no more hunting for the right file every time."]},
    {"slug": "channels", "name": "Channels", "cat": "CRM & Operations",
     "tag": "Manage every connected channel in one place", "icon": "grid",
     "body": ["One dashboard to manage every messaging channel connected to your account — add, configure, and monitor without switching tools."]},
    {"slug": "rcs-applications", "name": "RCS Applications", "cat": "Advanced Channels",
     "tag": "Rich messaging beyond WhatsApp and SMS", "icon": "radio",
     "body": ["Reach customers through RCS (Rich Communication Services) — rich media messaging built into Android's native messaging app."]},
    {"slug": "qr-ticketing", "name": "QR Ticketing", "cat": "Advanced Channels",
     "tag": "End-to-end event ticketing with QR check-in", "icon": "qr",
     "body": ["Generate digital tickets with secure QR validation, and track attendance in real time — built for conferences, meetups, and events."]},
]
PRODUCT_CATS = ["Commerce & Loyalty", "Automation & Scheduling", "CRM & Operations", "Advanced Channels"]

def build_product(p):
    icon_svg = ICONS[p["icon"]].replace('stroke="white"', 'stroke="#6E1E42"')
    body_html = "".join(f"<p>{b}</p>" for b in p["body"])
    html = head(f"{p['name']} — Fame Inbox", p["tag"], depth="../", path=f"products/{p['slug']}.html")
    html += header(depth="../")
    html += f"""
<section class="page-hero">
  <span class="eyebrow">{p['cat']}</span>
  <h1>{p['name']}</h1>
  <p class="sub">{p['tag']}</p>
</section>
<div class="detail-body">
  <div class="detail-illustration">
    <svg viewBox="0 0 24 24" style="width:64px;height:64px;">{icon_svg}</svg>
  </div>
  <div class="detail-section">
    {body_html}
  </div>
  <div class="detail-cta">
    <h3>See {p['name']} in action</h3>
    <p>Book a short demo and we'll walk you through it live.</p>
    <a href="https://zbooking.in/OEgH9" class="btn-primary" target="_blank" rel="noopener">Book a Demo</a>
  </div>
</div>
"""
    html += footer(depth="../")
    with open(os.path.join(ROOT, "products", f"{p['slug']}.html"), "w") as f:
        f.write(html)

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
    mega_cols += f"""
            <div class="mega-viewall"><a href="{depth}features/index.html">View all features &#8594;</a></div>"""

    pcols = {c: [p for p in PRODUCTS if p["cat"] == c] for c in PRODUCT_CATS}
    product_cols = ""
    for c in PRODUCT_CATS:
        items = ""
        for p in pcols[c]:
            items += f"""
              <a class="mega-item" href="{depth}products/{p['slug']}.html">
                <div class="icon">{ICONS[p['icon']]}</div>
                <div><h4>{p['name']}</h4><p>{p['tag']}</p></div>
              </a>"""
        product_cols += f"""
            <div>
              <p class="mega-col-title">{c}</p>{items}
            </div>"""

    return f"""<header>
  <div class="nav-wrap">
    <a href="{depth}index.html" class="logo">FAME <span>INBOX</span></a>
    <button class="hamburger" id="navToggle" aria-label="Open menu" aria-expanded="false">
      <span></span><span></span><span></span>
    </button>
    <nav class="primary" id="primaryNav">
      <ul>
        <li class="has-mega">
          <button class="navtop" aria-expanded="false">Features <span class="caret">&#9662;</span></button>
          <div class="mega">{mega_cols}
          </div>
        </li>
        <li class="has-mega">
          <button class="navtop" aria-expanded="false">Products <span class="caret">&#9662;</span></button>
          <div class="mega">{product_cols}
          </div>
        </li>
        <li><a href="{depth}solutions.html">Solutions</a></li>
        <li><a href="{depth}resources.html">Resources</a></li>
        <li><a href="{depth}integrations.html">Integrations</a></li>
        <li><a href="{depth}pricing.html">Pricing</a></li>
        <li><a href="https://app.fameinbox.com/">Login</a></li>
      </ul>
      <div class="cta-group">
        <a href="https://app.fameinbox.com/" class="cta-header" target="_blank" rel="noopener">Start for FREE &#8594;</a>
        <a href="https://zbooking.in/OEgH9" class="cta-header-outline" target="_blank" rel="noopener">Book a Demo &#8594;</a>
      </div>
    </nav>
  </div>
</header>
"""

def footer(depth=""):
    return f"""<a class="wa-float" href="https://wa.me/918939888107?text=Hi%2C%20I%27m%20interested%20in%20Fame%20Inbox" target="_blank" rel="noopener" aria-label="Chat on WhatsApp">
  <svg viewBox="0 0 24 24" fill="white"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.39 1.26 4.82L2 22l5.44-1.43a9.86 9.86 0 004.6 1.17h.01c5.46 0 9.9-4.45 9.9-9.91C21.95 6.45 17.5 2 12.04 2zm5.8 14.13c-.24.68-1.42 1.3-1.96 1.38-.5.08-1.14.11-1.84-.12-.42-.13-.97-.32-1.66-.63-2.93-1.27-4.84-4.22-4.99-4.42-.15-.2-1.19-1.58-1.19-3.02 0-1.43.75-2.14 1.02-2.43.27-.29.58-.36.78-.36h.56c.18 0 .42-.03.65.5.24.55.83 1.98.9 2.13.07.15.11.32.02.5-.09.19-.14.31-.28.47-.14.16-.29.36-.42.48-.14.14-.28.28-.12.55.16.27.7 1.16 1.51 1.88 1.04.93 1.91 1.22 2.18 1.36.27.14.43.12.59-.07.16-.2.68-.79.86-1.06.18-.27.36-.22.6-.13.24.09 1.55.73 1.81.86.27.13.44.2.51.31.07.11.07.63-.17 1.31z"/></svg>
</a>
<footer>
  <div class="footer-links">
    <a href="{depth}partners.html">Partner Program</a>
    <a href="{depth}about.html">About Us</a>
    <a href="{depth}contact.html">Contact</a>
  </div>
  &copy; 2026 <span>Fame Inbox</span>. All rights reserved.
</footer>
<script src="{depth}menu.js"></script>
<script src="https://bookings.nimbuspop.com/assets/embed.js"></script>
<script>
  Bookings.buttonModal({{
    url: "https://getamohan.zohobookings.in/portal-embed#/fameinbox",
    text: "Book now",
    color: "#5646A5",
    textColor: "#ffffff",
    position: "bottom-left"
  }});
</script>
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
                "WhatsApp business messaging platform: capture, qualify, nurture and close leads in one shared inbox.", path="")
    html += header()
    html += f"""
<section class="page-hero">
  <span class="eyebrow">Trusted by growing businesses &middot; Official Meta Business Partner</span>
  <h1>Where conversations<br>become <span class="accent">customers</span></h1>
  <p class="sub">Capture, qualify, nurture and close every lead on the app your customers already have open — WhatsApp.</p>
  <div class="hero-cta">
    <a href="https://zbooking.in/OEgH9" class="btn-primary" target="_blank" rel="noopener">Book a Demo</a>
    <a href="https://app.fameinbox.com/" class="btn-secondary">Start Free Trial</a>
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
  <p>Powered by a platform trusted by 50,000+ businesses worldwide</p>
  <div class="trust-badges">
    <span class="trust-badge">Official Meta Business Partner</span>
    <span class="trust-badge">99.9% Uptime</span>
    <span class="trust-badge">SOC 2 Type II</span>
    <span class="trust-badge">GDPR Compliant</span>
    <span class="trust-badge">End-to-End Encrypted</span>
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
    html = head("All Features — Fame Inbox", "Every Fame Inbox feature for capturing, qualifying, nurturing and closing leads on WhatsApp.", depth="../", path="features/index.html")
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
WHO_MAP = {
    "click-to-whatsapp-ads": "Businesses running Meta ad campaigns who want ad clicks to convert into conversations, not just landing page visits.",
    "qr-to-whatsapp": "Retail stores, restaurants, and event booths that want an easy offline-to-chat path for walk-in customers.",
    "link-to-whatsapp": "Anyone with an email signature, social bio, or SMS campaign who wants a single tap to start a chat.",
    "web-widget-to-whatsapp": "Websites that want visitors to reach a real conversation instead of filling out a generic contact form.",
    "whatsapp-chatbots": "Teams getting a high volume of repetitive questions who want leads pre-qualified before a human joins in.",
    "whatsapp-forms": "Businesses that need structured details (orders, bookings, preferences) without sending customers to an external form.",
    "whatsapp-broadcasts": "Businesses with an existing customer list who want to announce offers, restocks, or updates in one send.",
    "whatsapp-sequences": "Sales teams tired of manually remembering to follow up — this automates the nudge.",
    "whatsapp-team-inbox": "Any team of 2+ people sharing one WhatsApp number who need to avoid double-replies and missed chats.",
    "whatsapp-payments": "Businesses that want to close the sale in the same conversation instead of redirecting to a separate checkout.",
    "facebook-messenger": "Businesses already active on Facebook who want the same automation they use on WhatsApp.",
    "instagram-automation": "Brands running Instagram content and ads who don't want DMs and comments falling through the cracks.",
    "smart-crm": "Growing teams that have outgrown spreadsheets and need real customer segmentation and history.",
    "visual-bot-builder": "Non-technical teams who want to build and adjust chatbot flows themselves, without waiting on developers.",
    "automation-builder": "Operations-minded teams who want conversations to trigger real business workflows automatically.",
}

def build_feature(feat):
    icon_svg = ICONS[feat["icon"]].replace('stroke="white"', 'stroke="#6E1E42"')
    body_html = "".join(f"<p>{p}</p>" for p in feat["body"])
    who = WHO_MAP.get(feat["slug"], "")
    related = [f for f in FEATURES if f["cat"] == feat["cat"] and f["slug"] != feat["slug"]][:3]
    if len(related) < 3:
        related += [f for f in FEATURES if f["cat"] != feat["cat"] and f["slug"] != feat["slug"]][:3 - len(related)]
    related_html = "".join(f"""
<a class="hub-card" href="{r['slug']}.html">
  <div class="icon">{ICONS[r['icon']]}</div>
  <h4>{r['name']}</h4>
  <p>{r['tag']}</p>
</a>""" for r in related)
    html = head(f"{feat['name']} — Fame Inbox", feat["tag"], depth="../", path=f"features/{feat['slug']}.html")
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
    <p style="background:#F3E3EC;border-radius:10px;padding:16px 20px;font-size:14px;color:var(--wine);margin-top:24px;"><strong>Who it's for:</strong> {who}</p>
  </div>
  <div class="detail-cta">
    <h3>See {feat['name']} in action</h3>
    <p>Book a short demo and we'll walk you through it live.</p>
    <a href="https://zbooking.in/OEgH9" class="btn-primary" target="_blank" rel="noopener">Book a Demo</a>
  </div>
</div>
<div class="strip">
  <div class="strip-head">
    <span class="eyebrow">Explore more</span>
    <h2>Related features</h2>
  </div>
  <div class="hub-grid" style="padding:0;">
    {related_html}
  </div>
</div>
"""
    html += footer(depth="../")
    with open(os.path.join(ROOT, "features", f"{feat['slug']}.html"), "w") as f:
        f.write(html)

# ---------- About / Contact ----------
def build_about():
    html = head("About Us — Fame Inbox", "Fame Inbox helps businesses turn WhatsApp conversations into customers.", path="about.html")
    html += header()
    html += """
<section class="page-hero">
  <span class="eyebrow">About Us</span>
  <h1>Built for businesses<br><span class="accent">that live in the chat</span></h1>
  <p class="sub">Fame Inbox gives growing businesses one shared WhatsApp workspace to capture, qualify, nurture and close every conversation.</p>
</section>

<div class="hub-grid">
  <p class="hub-cat">What Fame Inbox Is Built On</p>
  <div class="hub-card">
    <div class="icon">""" + ICONS["ad"] + """</div>
    <h4>Official Meta Business Partner</h4>
    <p>Built on the official WhatsApp Business API, not an unofficial workaround.</p>
  </div>
  <div class="hub-card">
    <div class="icon">""" + ICONS["inbox"] + """</div>
    <h4>99.9% Uptime</h4>
    <p>Global infrastructure built to stay reliable at scale.</p>
  </div>
  <div class="hub-card">
    <div class="icon">""" + ICONS["form"] + """</div>
    <h4>SOC 2 &amp; GDPR</h4>
    <p>Bank-grade security and compliance standards behind every conversation.</p>
  </div>
  <div class="hub-card">
    <div class="icon">""" + ICONS["bot"] + """</div>
    <h4>End-to-End Encrypted</h4>
    <p>Your customer conversations stay protected in transit and at rest.</p>
  </div>
</div>

<div class="detail-body">
  <div class="detail-section">
    <h2>Why we built this</h2>
    <p>Most customers today would rather message a business than fill out a form or wait on hold. Fame Inbox exists so your team can meet them there — with automation that qualifies leads instantly and a shared inbox that keeps every conversation organized.</p>
    <h2>What we stand for</h2>
    <p>Fast responses, clear ownership of every conversation, and tools your team can actually set up without an engineer. That's the whole product philosophy.</p>
    <h2>Who we work with</h2>
    <p>From single-founder shops running their first WhatsApp campaign to growing teams managing thousands of conversations a month — plus agencies reselling the platform to their own clients through our <a href="partners.html">Partner Program</a>.</p>
    <h2>How we're different</h2>
    <p>Most tools give you WhatsApp automation and stop there. Fame Inbox connects WhatsApp, Facebook Messenger, and Instagram into one inbox, backed by a real CRM — so your team isn't juggling five different apps to talk to the same customer.</p>
  </div>
  <div class="detail-cta">
    <h3>See it for yourself</h3>
    <p>Book a demo and we'll walk you through the whole platform, live.</p>
    <a href="https://zbooking.in/OEgH9" class="btn-primary" target="_blank" rel="noopener">Book a Demo</a>
  </div>
</div>
"""
    html += footer()
    with open(os.path.join(ROOT, "about.html"), "w") as f:
        f.write(html)

def build_contact():
    html = head("Contact — Fame Inbox", "Get in touch with Fame Inbox or book a demo.", path="contact.html")
    html += header()
    html += """
<section class="page-hero">
  <span class="eyebrow">Contact</span>
  <h1>Let's get you <span class="accent">set up</span></h1>
  <p class="sub">Send us your details on WhatsApp, or book a demo directly below.</p>
</section>
<div class="detail-body">
  <form class="contact-form" id="waContactForm">
    <label for="waName">Name</label>
    <input type="text" id="waName" required placeholder="Your name">
    <label for="waPhone">Phone number</label>
    <input type="tel" id="waPhone" required placeholder="Your WhatsApp number">
    <label for="waMessage">What are you looking for?</label>
    <textarea id="waMessage" placeholder="e.g. I want to know more about the WhatsApp API plan"></textarea>
    <button type="submit">Send on WhatsApp</button>
  </form>
  <p class="contact-note">This opens WhatsApp with your details pre-filled — just hit send and our team replies from there.</p>

  <div class="detail-cta">
    <h3>Prefer to talk it through?</h3>
    <p>Book a demo and we'll walk you through the full platform live.</p>
    <a href="https://zbooking.in/OEgH9" class="btn-primary" target="_blank" rel="noopener">Book a Demo</a>
  </div>
</div>
<script>
document.getElementById('waContactForm').addEventListener('submit', function (e) {
  e.preventDefault();
  var name = document.getElementById('waName').value.trim();
  var phone = document.getElementById('waPhone').value.trim();
  var message = document.getElementById('waMessage').value.trim();
  var text = "Hi, I'm " + name + " (" + phone + "). " + (message || "I'd like to know more about Fame Inbox.");
  window.open("https://wa.me/918939888107?text=" + encodeURIComponent(text), "_blank");
});
</script>
"""
    html += footer()
    with open(os.path.join(ROOT, "contact.html"), "w") as f:
        f.write(html)

def build_pricing():
    html = head("Pricing — Fame Inbox", "Fame Inbox pricing plans.", path="pricing.html")
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
    <div class="price-amount">Free<span> for 7 days</span></div>
    <ul>
      <li>WhatsApp + Instagram</li>
      <li>7-day trial of core features before you commit</li>
    </ul>
    <a href="https://app.fameinbox.com/" class="btn-secondary" target="_blank" rel="noopener">Start Free Trial</a>
  </div>

  <div class="price-card">
    <h3>WhatsApp Basic Chatbots &amp; Automations</h3>
    <div class="price-amount">₹2,999<span>/mo (or $199/mo)</span></div>
    <ul>
      <li>Connect 5 numbers to Official WhatsApp API</li>
      <li>Import & store up to 1 million contacts in CRM</li>
      <li>Send messages via APIs, receive via webhooks</li>
      <li>Custom fields & contact segments</li>
      <li>Send bulk campaigns</li>
      <li>WhatsApp chatbots without external API/apps</li>
      <li>WhatsApp automations without external API/apps</li>
      <li>WhatsApp ecom bot (manual product entry)</li>
      <li>WhatsApp native Forms / Mini Apps</li>
      <li>Collect payments via WhatsApp native payments</li>
    </ul>
    <a href="https://zbooking.in/OEgH9" class="btn-primary" target="_blank" rel="noopener">Book a Demo</a>
  </div>

  <div class="price-card">
    <h3>Instagram DM Chatbots &amp; Comment Automations</h3>
    <div class="price-amount">₹5,999<span>/mo (₹5,499 billed annually) — or $99/mo ($999/yr)</span></div>
    <ul>
      <li>Connect 1 Instagram Professional account</li>
      <li>Store & automate comments for 100,000 contacts</li>
      <li>DM multi-step automation bots with buttons</li>
      <li>Comment automation for Posts, Reels & Live</li>
      <li>Drip journeys within 24 hours of last DM</li>
    </ul>
    <a href="https://zbooking.in/OEgH9" class="btn-secondary" target="_blank" rel="noopener">Book a Demo</a>
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
    <a href="https://zbooking.in/OEgH9" class="btn-primary" target="_blank" rel="noopener">Book a Demo</a>
  </div>

</div>

<div class="detail-body">
  <div class="detail-section">
    <h2>Not included in the API &amp; Bulk Messaging plan</h2>
    <p>Team members for inbox &middot; other social channels (Facebook/Instagram) &middot; WhatsApp chatbots/automations &middot; WhatsApp native ecommerce store &middot; WhatsApp native Forms/Mini Apps Builder. Access on this plan is limited to CRM and Inbox.</p>
    <h2>Good to know</h2>
    <p>Support is available via support tickets with a 3-day SLA. WhatsApp conversation charges are prepaid via wallet deposit per channel, with a minimum recharge of $20 / ₹1000 per channel. Sending spam marketing to random numbers risks a Meta ban on your business account or numbers. All taxes and payment gateway fees are extra.</p>
  </div>
  <div class="detail-cta">
    <h3>Running an agency?</h3>
    <p>We also offer Sub-Agency Licensing — resell white-label panels to your own clients under your own brand. See our <a href="partners.html">Partner Program</a> for details.</p>
    <a href="https://zbooking.in/OEgH9" class="btn-primary" target="_blank" rel="noopener">Book a Demo</a>
  </div>
</div>
"""
    html += footer()
    with open(os.path.join(ROOT, "pricing.html"), "w") as f:
        f.write(html)

def build_partners():
    html = head("Partner Program — Fame Inbox", "Become a Fame Inbox reseller partner and launch your own branded communication platform.", path="partners.html")
    html += header()
    html += """
<section class="page-hero">
  <span class="eyebrow">Partner Program</span>
  <h1>Sell Fame Inbox <span class="accent">under your own brand</span></h1>
  <p class="sub">Already work with agency clients or run your own SMS/marketing business? Resell the full Fame Inbox platform under your own name and build a recurring revenue stream.</p>
  <div class="hero-cta">
    <a href="https://wa.me/918939888107?text=Hi%2C%20I%27m%20interested%20in%20the%20Fame%20Inbox%20Partner%20Program%20%2F%20reselling%20opportunity.%20Can%20you%20share%20more%20details%3F" class="btn-primary" target="_blank" rel="noopener">Chat on WhatsApp About Partnering</a>
    <a href="https://zbooking.in/OEgH9" class="btn-secondary" target="_blank" rel="noopener">Book a Demo</a>
  </div>
</section>

<div class="hub-grid">
  <p class="hub-cat">Why Partner With Us</p>
  <div class="hub-card">
    <div class="icon">""" + ICONS["builder"] + """</div>
    <h4>Your Brand, Your Way</h4>
    <p>Onboard your own clients under your own name and identity — you own the relationship end to end.</p>
  </div>
  <div class="hub-card">
    <div class="icon">""" + ICONS["automation"] + """</div>
    <h4>No Development Needed</h4>
    <p>The full platform is already built — WhatsApp API, bots, CRM, automation — ready to hand to your clients.</p>
  </div>
  <div class="hub-card">
    <div class="icon">""" + ICONS["crm"] + """</div>
    <h4>Recurring Revenue</h4>
    <p>Build a subscription business on top of a platform your clients will keep using month after month.</p>
  </div>
  <div class="hub-card">
    <div class="icon">""" + ICONS["inbox"] + """</div>
    <h4>Your Own Client Workspaces</h4>
    <p>Give each client an isolated workspace to manage their own conversations, contacts, and automations.</p>
  </div>
</div>

<div class="detail-body">
  <div class="detail-section">
    <h2>Who this is for</h2>
    <p>Digital marketing agencies, SMS/messaging companies, and consultants already serving business clients who want to add a WhatsApp/social automation offering without building it themselves.</p>
    <h2>How it works</h2>
    <p>You get access to the full platform under your own branding, onboard your clients into their own workspaces, and set your own retail pricing. We handle the underlying infrastructure and support.</p>
  </div>
  <div class="detail-cta">
    <h3>Want the specifics?</h3>
    <p>Pricing and partnership terms are discussed directly — message us on WhatsApp and we'll walk you through it.</p>
    <a href="https://wa.me/918939888107?text=Hi%2C%20I%27m%20interested%20in%20the%20Fame%20Inbox%20Partner%20Program%20%2F%20reselling%20opportunity.%20Can%20you%20share%20more%20details%3F" class="btn-primary" target="_blank" rel="noopener">Chat on WhatsApp About Partnering</a>
  </div>
</div>
"""
    html += footer()
    with open(os.path.join(ROOT, "partners.html"), "w") as f:
        f.write(html)

SOLUTIONS = [
    ("Ecommerce & Retail", "Turn browsers into buyers on WhatsApp",
     "Recover abandoned carts, send order and delivery updates, and let customers complete purchases with in-chat payments — without ever leaving the conversation.",
     "crm"),
    ("Real Estate", "Qualify property leads before your team calls",
     "Let a chatbot ask budget, location, and timeline questions upfront, share listings and brochures instantly, and route serious buyers straight to your agents.",
     "form"),
    ("Education & Coaching", "Never lose a student inquiry to a missed call",
     "Answer course questions instantly, collect enrollment details through WhatsApp forms, and send automated reminders for classes, fees, and deadlines.",
     "bot"),
    ("Healthcare & Clinics", "Simplify appointments and patient follow-ups",
     "Let patients book and reschedule appointments via chat, send automated reminders to cut no-shows, and keep every patient conversation in one place.",
     "sequence"),
    ("Restaurants & Cloud Kitchens", "Take orders and manage feedback on WhatsApp",
     "Share your menu, take orders through a chatbot, send order-ready notifications, and follow up for reviews — all inside the same conversation.",
     "broadcast"),
]

def build_solutions():
    html = head("Solutions — Fame Inbox", "Fame Inbox solutions by industry: ecommerce, real estate, education, healthcare, and restaurants.", path="solutions.html")
    html += header()
    html += """
<section class="page-hero">
  <span class="eyebrow">Solutions</span>
  <h1>Built for <span class="accent">how your industry sells</span></h1>
  <p class="sub">The same platform, tuned to how conversations actually happen in your business.</p>
  <div class="hero-mockup">
    <div class="hero-mockup-head"><span class="dot"></span> Illustrative mockup — not a live screen recording</div>
    <div class="hero-mockup-body">
      <div class="bubble in">Hi, is the blue kurta set still available in size M?</div>
      <div class="bubble out">Yes! Here's a quick payment link to secure it 👇</div>
      <div class="bubble in">Perfect, paying now</div>
      <div class="bubble out">Order confirmed ✅ Shipping by tomorrow</div>
    </div>
  </div>
</section>
<div class="detail-body">
"""
    for name, headline, desc, icon in SOLUTIONS:
        html += f"""
  <div class="detail-illustration" style="margin-bottom:14px;">
    <svg viewBox="0 0 24 24" style="width:48px;height:48px;">{ICONS[icon].replace('stroke="white"', 'stroke="#6E1E42"')}</svg>
  </div>
  <div class="detail-section" style="margin-bottom:40px;">
    <h2 style="margin-top:0;">{name}</h2>
    <p style="font-weight:700;color:var(--ink);margin-bottom:6px;">{headline}</p>
    <p>{desc}</p>
  </div>
"""
    html += """
  <div class="detail-cta">
    <h3>Don't see your industry?</h3>
    <p>Fame Inbox adapts to almost any conversation-driven business. Let's talk about yours.</p>
    <a href="https://zbooking.in/OEgH9" class="btn-primary" target="_blank" rel="noopener">Book a Demo</a>
  </div>
</div>
"""
    html += footer()
    with open(os.path.join(ROOT, "solutions.html"), "w") as f:
        f.write(html)

INTEGRATIONS = [
    ("Ecommerce", "Shopify, WooCommerce — sync orders, products, and customers automatically"),
    ("Payments", "Razorpay, Stripe and other gateways for in-chat payment collection"),
    ("Calendars", "Google Calendar and Outlook for automated appointment scheduling"),
    ("Spreadsheets", "Google Sheets for simple data sync without extra tools"),
    ("Automation platforms", "Connect to Zapier/Make-style tools and 1,000+ other apps via API and webhooks"),
    ("CRM & Helpdesk", "Sync contacts and conversations with your existing CRM or support tools"),
]

def build_integrations():
    html = head("Integrations — Fame Inbox", "Fame Inbox integrates with your ecommerce, payments, calendar, and automation tools.", path="integrations.html")
    html += header()
    html += """
<section class="page-hero">
  <span class="eyebrow">Integrations</span>
  <h1>Connects with <span class="accent">the tools you already use</span></h1>
  <p class="sub">REST APIs, webhooks, and ready-made connections so Fame Inbox fits into your existing stack, not the other way around.</p>
</section>
<div class="hub-grid">
"""
    for name, desc in INTEGRATIONS:
        html += f"""
<div class="hub-card">
  <div class="icon">{ICONS['automation']}</div>
  <h4>{name}</h4>
  <p>{desc}</p>
</div>"""
    html += """
</div>
<div class="detail-body">
  <div class="detail-cta">
    <h3>Need a custom integration?</h3>
    <p>Our open REST APIs and webhooks mean most custom workflows are possible — ask us during your demo.</p>
    <a href="https://zbooking.in/OEgH9" class="btn-primary" target="_blank" rel="noopener">Book a Demo</a>
  </div>
</div>
"""
    html += footer()
    with open(os.path.join(ROOT, "integrations.html"), "w") as f:
        f.write(html)

build_home()
build_hub()
build_pricing()
build_partners()
build_solutions()
build_integrations()
for feat in FEATURES:
    build_feature(feat)
for prod in PRODUCTS:
    build_product(prod)
build_about()
build_contact()

USE_CASES = [
    ("recover-abandoned-carts", "How to Recover Abandoned Carts with WhatsApp Broadcasts",
     "For ecommerce sellers",
     [
        "A customer adds items to their cart, gets distracted, and leaves — this happens to roughly 70% of online shopping carts. Email reminders often go unread, but WhatsApp messages get opened within minutes.",
        "<strong>Step 1: Segment abandoned-cart customers.</strong> Use Fame Inbox's Smart CRM to tag customers who added items but didn't complete checkout, based on your store's order data.",
        "<strong>Step 2: Send a broadcast, not a generic blast.</strong> Use WhatsApp Broadcasts to send a personalized reminder — mention the specific item they left behind if your store integration supports it.",
        "<strong>Step 3: Make it one tap to finish.</strong> Include a WhatsApp Payments link directly in the message so they can complete the purchase without leaving the chat.",
        "<strong>Step 4: Automate the timing.</strong> Set up a WhatsApp Sequence to trigger this reminder automatically a few hours after cart abandonment, without your team lifting a finger each time.",
     ], ["whatsapp-broadcasts", "whatsapp-payments", "whatsapp-sequences"]),
    ("qualify-real-estate-leads", "How Real Estate Agents Qualify Leads Faster with a WhatsApp Chatbot",
     "For real estate agents",
     [
        "Property inquiries often come in at odd hours, and by the time an agent calls back, the lead has already spoken to three other agents. Speed and pre-qualification both matter.",
        "<strong>Step 1: Answer instantly, day or night.</strong> A WhatsApp Chatbot can respond the moment someone messages about a listing, sharing photos, price, and availability immediately.",
        "<strong>Step 2: Ask qualifying questions upfront.</strong> Use WhatsApp Forms to collect budget range, preferred location, and timeline before a human ever gets involved.",
        "<strong>Step 3: Route hot leads to the right agent.</strong> Once a lead is qualified, hand off the conversation inside your WhatsApp Team Inbox so the right agent picks it up with full context already visible.",
     ], ["whatsapp-chatbots", "whatsapp-forms", "whatsapp-team-inbox"]),
    ("instagram-comments-to-sales", "Turning Instagram Comments into Sales with Automated Replies",
     "For social-first brands",
     [
        "When a post goes viral, comments can pile up faster than any team can reply to manually — and every unanswered \"price?\" comment is a lead going cold.",
        "<strong>Step 1: Auto-reply to comments.</strong> Instagram Automation can detect keywords in comments (like \"price\" or \"available\") and trigger an automatic DM reply.",
        "<strong>Step 2: Move the conversation to DM.</strong> Once someone engages, continue the conversation privately, where you can share pricing, links, and answer questions directly.",
        "<strong>Step 3: Keep it all in one place.</strong> Every Instagram conversation lands in the same shared inbox as your WhatsApp chats, so nothing gets missed across channels.",
     ], ["instagram-automation", "whatsapp-team-inbox"]),
    ("followup-without-forgetting", "How to Follow Up on Leads Without Relying on Memory",
     "For any sales team",
     [
        "Most lost deals aren't lost to a competitor — they're lost to a follow-up that never happened. Manual follow-up depends on someone remembering, and that doesn't scale.",
        "<strong>Step 1: Map out your follow-up cadence.</strong> Decide when a lead should hear from you again if they go quiet — a day later, a week later, and so on.",
        "<strong>Step 2: Build it once with WhatsApp Sequences.</strong> Set up automated follow-up messages that go out on schedule, and stop automatically the moment the lead replies.",
        "<strong>Step 3: Let your CRM track who's where.</strong> The Smart CRM keeps every lead's stage visible, so your team always knows who's due for a human touch versus who's still in automated follow-up.",
     ], ["whatsapp-sequences", "smart-crm"]),
]

def build_resources():
    html = head("Resources — Fame Inbox", "Marketing use cases and how-to guides for getting more from WhatsApp and Instagram automation.", path="resources.html")
    html += header()
    html += """
<section class="page-hero">
  <span class="eyebrow">Resources</span>
  <h1>Marketing use cases, <span class="accent">not just features</span></h1>
  <p class="sub">Practical ways to actually use Fame Inbox to sell more — not just a list of what the product does.</p>
</section>
<div class="detail-body">
"""
    for slug, title, audience, paras, related_slugs in USE_CASES:
        body = "".join(f"<p>{p}</p>" for p in paras)
        links = "".join(
            f'<a href="features/{s}.html" style="display:inline-block;margin:0 8px 8px 0;font-size:12.5px;background:#F3E3EC;color:var(--wine);padding:6px 12px;border-radius:999px;font-weight:600;">{next(f["name"] for f in FEATURES if f["slug"]==s)}</a>'
            for s in related_slugs
        )
        html += f"""
  <div class="detail-section" style="margin-bottom:50px;padding-bottom:44px;border-bottom:1px solid var(--line);">
    <span class="eyebrow">{audience}</span>
    <h2 style="font-size:24px;margin:14px 0 16px;">{title}</h2>
    {body}
    <div style="margin-top:18px;">{links}</div>
  </div>
"""
    html += """
  <div class="detail-cta">
    <h3>Want help setting one of these up?</h3>
    <p>Book a demo and we'll walk through building your specific use case live.</p>
    <a href="https://zbooking.in/OEgH9" class="btn-primary" target="_blank" rel="noopener">Book a Demo</a>
  </div>
</div>
"""
    html += footer()
    with open(os.path.join(ROOT, "resources.html"), "w") as f:
        f.write(html)

def build_ads_landing():
    html = head("Start Free — Fame Inbox WhatsApp Automation", "Capture, qualify, and close leads on WhatsApp. Start your free 7-day trial today.", path="get-started.html")
    html += """
<header class="lp-header">
  <a href="index.html" class="logo">FAME <span>INBOX</span></a>
</header>

<section class="lp-hero">
  <h1>Turn WhatsApp Chats Into <span class="accent">Paying Customers</span></h1>
  <p class="sub">Capture leads from ads, qualify them with a chatbot, and close the sale — all inside one WhatsApp conversation.</p>
  <div class="lp-badge-row">
    <span class="lp-badge">Official Meta Business Partner</span>
    <span class="lp-badge">99.9% Uptime</span>
    <span class="lp-badge">7-Day Free Trial</span>
  </div>
  <div class="hero-cta">
    <a href="https://app.fameinbox.com/" class="btn-primary" target="_blank" rel="noopener">Start Free 7-Day Trial</a>
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

<div class="lp-benefits">
  <div class="lp-benefit">
    <div class="icon">""" + ICONS["ad"] + """</div>
    <h4>Capture</h4>
    <p>Ad clicks land straight in a live WhatsApp conversation — no landing page drop-off.</p>
  </div>
  <div class="lp-benefit">
    <div class="icon">""" + ICONS["bot"] + """</div>
    <h4>Qualify</h4>
    <p>A chatbot pre-screens every lead before your team spends a minute on it.</p>
  </div>
  <div class="lp-benefit">
    <div class="icon">""" + ICONS["payments"] + """</div>
    <h4>Close</h4>
    <p>Send a payment link in the same chat — no separate checkout page needed.</p>
  </div>
</div>

<div class="lp-final-cta">
  <h2>Try it free for 7 days</h2>
  <p>No commitment — see how fast leads move from chat to sale.</p>
  <a href="https://app.fameinbox.com/" class="btn-primary" target="_blank" rel="noopener">Start Free 7-Day Trial</a>
</div>

<footer>
  &copy; 2026 <span>Fame Inbox</span>. All rights reserved.
</footer>
</body>
</html>
"""
    with open(os.path.join(ROOT, "get-started.html"), "w") as f:
        f.write(html)

build_resources()
build_ads_landing()

def build_sitemap():
    pages = ["", "features/index.html", "pricing.html", "partners.html", "solutions.html",
             "integrations.html", "resources.html", "about.html", "contact.html"]
    pages += [f"features/{f['slug']}.html" for f in FEATURES]
    pages += [f"products/{p['slug']}.html" for p in PRODUCTS]
    urls = "".join(f"""  <url>
    <loc>{BASE_URL}/{p}</loc>
  </url>
""" for p in pages)
    xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{urls}</urlset>
"""
    with open(os.path.join(ROOT, "sitemap.xml"), "w") as f:
        f.write(xml)

build_sitemap()
print("Build complete.")
