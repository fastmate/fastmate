import io, os, sys
OUT = sys.argv[1]
UPDATED = 'October 11, 2026'
UPDATED_VI = '15/10/2026'

# Two language editions: English at the root (global products: HireMate), Vietnamese under /vi/ (VNeInvoiceMate,
# Vietnam only). VNeInvoiceMate never appears in the English edition.
VNI_CHECKOUT = 'https://fastmate.lemonsqueezy.com/checkout/buy/e2bd491d-acda-4799-8593-6019b564d2b3'
VNI_STORE = '#'  # Chrome Web Store link once published

def header(p, lang='en', alt=None):
    if lang == 'vi':
        return f'''<header class="site-header">
  <div class="wrap">
    <a class="brand" href="{p}vi/index.html"><img class="logo" src="{p}assets/fastmate-logo.png" alt="FastMate"></a>
    <nav class="nav">
      <a href="{p}vi/index.html#san-pham">Sản phẩm</a>
      <a href="{p}vi/vneinvoicemate/">VNeInvoiceMate</a>
      <a href="{p}vi/hiremate/">HireMate</a>
      <a href="{p}vi/vneinvoicemate/#bang-gia">Bảng giá</a>
      <a href="{p}vi/contact.html">Liên hệ</a>
      <a class="lang" href="{p}{alt or 'index.html'}" hreflang="en" lang="en">English</a>
      <a class="btn btn-primary btn-sm" href="{VNI_STORE}">Thêm vào Chrome</a>
    </nav>
  </div>
</header>'''
    return f'''<header class="site-header">
  <div class="wrap">
    <a class="brand" href="{p}index.html"><img class="logo" src="{p}assets/fastmate-logo.png" alt="FastMate"></a>
    <nav class="nav">
      <a href="{p}index.html#products">Products</a>
      <a href="{p}hiremate/">HireMate</a>
      <a href="{p}hiremate/#pricing">Pricing</a>
      <a href="{p}contact.html">Contact</a>
      <a class="lang" href="{p}{alt or 'vi/index.html'}" hreflang="vi" lang="vi">Tiếng Việt</a>
      <a class="btn btn-primary btn-sm" href="#">Add to Chrome</a>
    </nav>
  </div>
</header>'''

def footer(p, lang='en'):
    if lang == 'vi':
        return f'''<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div>
        <a class="brand" href="{p}vi/index.html"><img class="logo" src="{p}assets/fastmate-logo.png" alt="FastMate"></a>
        <p class="muted" style="max-width:320px;margin:10px 0 0">Những công cụ nhỏ giúp bạn làm việc nhanh hơn.</p>
      </div>
      <div class="footer-links">
        <div><strong>Sản phẩm</strong><a href="{p}vi/vneinvoicemate/">VNeInvoiceMate</a><a href="{p}vi/hiremate/">HireMate</a></div>
        <div><strong>Pháp lý</strong><a href="{p}vi/privacy.html">Chính sách quyền riêng tư</a><a href="{p}vi/terms.html">Điều khoản sử dụng</a><a href="{p}vi/refund.html">Chính sách hoàn tiền</a></div>
        <div><strong>FastMate</strong><a href="{p}vi/contact.html">Liên hệ</a><a href="mailto:fastmate.support@gmail.com">fastmate.support@gmail.com</a></div>
      </div>
    </div>
    <p class="disclaimer">© 2026 FastMate. VNeInvoiceMate là sản phẩm độc lập, không liên kết với Tổng cục Thuế hay Bộ Tài chính. Thanh toán do Lemon Squeezy (đơn vị bán hàng chính thức — merchant of record) xử lý.</p>
  </div>
</footer>'''
    return f'''<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div>
        <a class="brand" href="{p}index.html"><img class="logo" src="{p}assets/fastmate-logo.png" alt="FastMate"></a>
        <p class="muted" style="max-width:320px;margin:10px 0 0">Small, focused tools that help people work faster.</p>
      </div>
      <div class="footer-links">
        <div><strong>Products</strong><a href="{p}hiremate/">HireMate</a><a href="{p}hiremate/#pricing">Pricing</a></div>
        <div><strong>Legal</strong><a href="{p}privacy.html">Privacy Policy</a><a href="{p}terms.html">Terms of Service</a><a href="{p}refund.html">Refund Policy</a></div>
        <div><strong>Company</strong><a href="{p}contact.html">Contact</a><a href="mailto:fastmate.support@gmail.com">fastmate.support@gmail.com</a></div>
      </div>
    </div>
    <p class="disclaimer">© 2026 FastMate. LinkedIn is a trademark of LinkedIn Corporation. HireMate is an independent product and is not affiliated with, endorsed by or sponsored by LinkedIn. Payments are processed by Lemon Squeezy, our merchant of record.</p>
  </div>
</footer>'''

SITE = 'https://fastmate.github.io/fastmate/'
PAGES = []  # every generated page (path, lang) -> sitemap.xml
import json as _json

ORG = {'@type': 'Organization', 'name': 'FastMate', 'url': SITE, 'logo': SITE + 'assets/fastmate-mark.png',
       'email': 'fastmate.support@gmail.com'}

# Per product: share image + schema.org SoftwareApplication (Chrome extension, Free + Premium offers).
PRODUCTS = {
    'hiremate': {
        'image': 'assets/og-hiremate.png',
        'app': {'name': 'HireMate', 'alternateName': 'HireMate - Export LinkedIn Profiles to Excel',
                'applicationCategory': 'BusinessApplication', 'applicationSubCategory': 'Recruiting',
                'operatingSystem': 'Google Chrome',
                'offers': [{'@type': 'Offer', 'name': 'Free', 'price': '0', 'priceCurrency': 'USD'},
                           {'@type': 'Offer', 'name': 'Premium (monthly)', 'price': '4.99', 'priceCurrency': 'USD'},
                           {'@type': 'Offer', 'name': 'Premium (quarterly)', 'price': '11.98', 'priceCurrency': 'USD'},
                           {'@type': 'Offer', 'name': 'Premium (yearly)', 'price': '41.92', 'priceCurrency': 'USD'}]}},
    'vneinvoicemate': {
        'image': 'assets/og-vneinvoicemate.png',
        'app': {'name': 'VNeInvoiceMate', 'applicationCategory': 'FinanceApplication',
                'applicationSubCategory': 'Accounting', 'operatingSystem': 'Google Chrome',
                'offers': [{'@type': 'Offer', 'name': 'Free', 'price': '0', 'priceCurrency': 'USD'},
                           {'@type': 'Offer', 'name': 'Premium (monthly)', 'price': '1.99', 'priceCurrency': 'USD'},
                           {'@type': 'Offer', 'name': 'Premium (yearly)', 'price': '19.99', 'priceCurrency': 'USD'}]}},
}

def seo_head(path, title, desc, lang):
    url = SITE + path.replace('index.html', '')
    product = next((k for k in PRODUCTS if '/' + k + '/' in '/' + path), None)
    image = SITE + (PRODUCTS[product]['image'] if product else 'assets/og-fastmate.png')
    esc = lambda t: t.replace('&', '&amp;').replace('"', '&quot;')
    tags = [
        f'<link rel="canonical" href="{url}">',
        '<meta property="og:site_name" content="FastMate">',
        f'<meta property="og:type" content="{"product" if product else "website"}">',
        f'<meta property="og:locale" content="{"vi_VN" if lang == "vi" else "en_US"}">',
        f'<meta property="og:title" content="{esc(title)}">',
        f'<meta property="og:description" content="{esc(desc)}">',
        f'<meta property="og:url" content="{url}">',
        f'<meta property="og:image" content="{image}">',
        '<meta property="og:image:width" content="1200">',
        '<meta property="og:image:height" content="630">',
        '<meta name="twitter:card" content="summary_large_image">',
        f'<meta name="twitter:title" content="{esc(title)}">',
        f'<meta name="twitter:description" content="{esc(desc)}">',
        f'<meta name="twitter:image" content="{image}">',
    ]
    data = None
    if product:
        data = dict({'@context': 'https://schema.org', '@type': 'SoftwareApplication', 'url': url,
                     'description': desc, 'image': image, 'inLanguage': lang, 'publisher': ORG}, **PRODUCTS[product]['app'])
    elif path in ('index.html', 'vi/index.html'):
        data = dict({'@context': 'https://schema.org'}, **ORG)
    if data:
        tags.append('<script type="application/ld+json">' + _json.dumps(data, ensure_ascii=False) + '</script>')
    return '\n' + '\n'.join(tags)

def page(path, title, desc, body, lang='en', alt=None):
    # alt: the same page in the other language (path from the site root), for the language switch and hreflang
    depth = path.count('/')
    p = '../' * depth
    canon = lambda x: SITE + x.replace('index.html', '')
    hreflang = ''
    if alt:
        hreflang = f'\n<link rel="alternate" hreflang="{lang}" href="{canon(path)}">\n<link rel="alternate" hreflang="{"en" if lang == "vi" else "vi"}" href="{canon(alt)}">'
    html = f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">{hreflang}{seo_head(path, title, desc, lang)}
<link rel="icon" href="{p}assets/favicon.png" type="image/png">
<link rel="apple-touch-icon" href="{p}assets/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap">
<link rel="stylesheet" href="{p}assets/style.css">
</head>
<body>
{header(p, lang, alt)}
<main>
{body.replace('{P}', p)}
</main>
{footer(p, lang)}
</body>
</html>
'''
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    io.open(full, 'w', encoding='utf-8', newline='\n').write(html)
    PAGES.append(path)

ICON = {
 'table': '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18M3 15h18M9 3v18"/></svg>',
 'bolt': '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M13 2 4 14h7l-1 8 9-12h-7l1-8z"/></svg>',
 'chart': '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/></svg>',
 'board': '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="5" height="16" rx="1.5"/><rect x="10" y="4" width="5" height="11" rx="1.5"/><rect x="17" y="4" width="4" height="7" rx="1.5"/></svg>',
 'trend': '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m3 17 6-6 4 4 8-8M15 7h6v6"/></svg>',
 'shield': '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l8 4v5c0 4.5-3.4 8.3-8 9-4.6-.7-8-4.5-8-9V7l8-4z"/></svg>',
 'search': '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>',
 'refresh': '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12a9 9 0 1 1-3-6.7L21 8"/><path d="M21 3v5h-5"/></svg>',
}

# ---------------- FastMate home ----------------
page('index.html', 'FastMate — small tools that make work faster',
 'FastMate builds small, focused tools that save professionals hours every week. Our first product is HireMate for recruiters.',
f'''<section class="hero">
  <div class="wrap center" style="max-width:820px">
    <span class="eyebrow">FastMate</span>
    <h1>Small tools that make your work <span style="color:var(--green)">faster</span>.</h1>
    <p class="lead" style="margin:0 auto">FastMate builds focused, privacy-first tools for professionals — each one does one job well, right where you already work.</p>
    <div class="actions" style="justify-content:center">
      <a class="btn btn-primary" href="#products">See our products</a>
      <a class="btn btn-ghost" href="contact.html">Contact us</a>
    </div>
  </div>
</section>

<section id="products">
  <div class="wrap">
    <div class="section-head">
      <h2>Products</h2>
      <p class="lead">Start with HireMate. More tools are on the way.</p>
    </div>
    <div class="grid-2">
      <div class="card product">
        <div class="logo-row"><img src="assets/hiremate-icon.png" alt=""><div><h3>HireMate</h3><span class="tag">Available</span></div></div>
        <p>A Chrome extension for recruiters: turn the candidate profiles you view into a clean Excel shortlist, then organize your talent pool with a dashboard, talent map and hiring pipeline.</p>
        <div class="links"><a class="btn btn-primary btn-sm" href="hiremate/">Learn more</a><a class="btn btn-ghost btn-sm" href="hiremate/#pricing">Pricing</a></div>
      </div>
      <div class="card product soon">
        <div class="logo-row"><img src="assets/fastmate-mark.png" alt=""><div><h3>Next product</h3><span class="tag">Coming soon</span></div></div>
        <p>We are building more small tools for everyday professional work. Want to hear first? Drop us a line.</p>
        <div class="links"><a class="btn btn-ghost btn-sm" href="contact.html">Get notified</a></div>
      </div>
    </div>
  </div>
</section>

<section class="section-alt">
  <div class="wrap">
    <div class="section-head"><h2>How we build</h2></div>
    <div class="grid-3">
      <div class="card"><div class="icon">{ICON['bolt']}</div><h3>Fast by default</h3><p>Results in seconds, inside the tools you already use. No setup, no learning curve.</p></div>
      <div class="card"><div class="icon green">{ICON['shield']}</div><h3>Private by design</h3><p>Your work data stays on your device. We don’t run servers that collect it.</p></div>
      <div class="card"><div class="icon">{ICON['chart']}</div><h3>Useful insight</h3><p>Not just data in, data out — each tool helps you see what matters and decide faster.</p></div>
    </div>
  </div>
</section>''', alt='vi/index.html')

# ---------------- HireMate product page ----------------
page('hiremate/index.html', 'HireMate — Export LinkedIn™ profiles to Excel & manage your talent pool',
 'HireMate is a Chrome extension for recruiters: save candidate profiles you view to a clean Excel shortlist, then manage your talent pool with a dashboard, talent map and hiring pipeline.',
f'''<section class="hero">
  <div class="wrap hero-grid">
    <div>
      <span class="eyebrow">HireMate · LinkedIn to Excel Chrome extension for recruiters</span>
      <h1>Build your candidate shortlist in minutes, not hours.</h1>
      <p class="lead">HireMate is a Chrome side panel for recruiters. Open a candidate’s profile, save it in one click, and export a clean Excel file with every role, company, industry and education — then manage your whole talent pool in one dashboard.</p>
      <div class="actions">
        <a class="btn btn-primary" href="#">Add to Chrome — it’s free</a>
        <a class="btn btn-ghost" href="#pricing">See pricing</a>
      </div>
      <div class="trust"><span>Data stays in your browser</span><span>No account needed</span><span>Works with your own login</span></div>
    </div>
    <div class="hero-art"><img src="{{P}}assets/hiremate-hero.jpg" alt="HireMate — profile to Excel"></div>
  </div>
</section>

<section id="features">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Features</span>
      <h2>Everything after “I found a good candidate”</h2>
      <p class="lead">Stop copying and pasting. Spend your time talking to candidates instead.</p>
    </div>
    <div class="grid-3">
      <div class="card"><div class="icon">{ICON['table']}</div><h3>One-click to Excel</h3><p>Every role, period, company, industry, description and school — numbered columns, ready to filter in Excel.</p></div>
      <div class="card"><div class="icon green">{ICON['search']}</div><h3>Search & shortlist</h3><p>Search people by title, location, company and industry, see current role and total experience at a glance, and save the ones you like.</p></div>
      <div class="card"><div class="icon">{ICON['chart']}</div><h3>Talent map</h3><p>See where your talent works, their industries, schools and experience — the snapshot to bring to every hiring-manager intake.</p></div>
      <div class="card"><div class="icon green">{ICON['trend']}</div><h3>Who is likely to move</h3><p>A transparent estimate of who may change jobs in the next months, based on career patterns in your own saved pool — with the reasons.</p></div>
      <div class="card"><div class="icon">{ICON['board']}</div><h3>Hiring pipeline</h3><p>One board per opening: drag candidates from Sourced to Hired, add notes and tags, and track your funnel.</p></div>
      <div class="card"><div class="icon green">{ICON['refresh']}</div><h3>Stay up to date</h3><p>Refresh saved profiles to pick up new roles and get flagged when a candidate changes jobs.</p></div>
    </div>
  </div>
</section>

<section class="section-alt">
  <div class="wrap">
    <div class="section-head"><h2>How it works</h2></div>
    <div class="grid-3 steps">
      <div class="step"><h3>Install & open</h3><p class="muted">Add HireMate to Chrome and pin it. Click the icon to open the side panel.</p></div>
      <div class="step"><h3>View & save</h3><p class="muted">Open a candidate’s profile — HireMate reads it for you. Edit anything, then save it to your list.</p></div>
      <div class="step"><h3>Export & act</h3><p class="muted">Export to Excel, or use the dashboard to map talent, track your pipeline and spot who may be open to a move.</p></div>
    </div>
  </div>
</section>

<section id="pricing">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Pricing</span>
      <h2>Start free. Upgrade when it saves you hours.</h2>
    </div>
    <div class="billing" role="group" aria-label="Billing period">
      <button type="button" data-period="monthly" class="active">Monthly</button>
      <button type="button" data-period="quarterly">Quarterly <span class="save">−20%</span></button>
      <button type="button" data-period="yearly">Yearly <span class="save">−30%</span></button>
    </div>
    <div class="pricing">
      <div class="plan">
        <div><h3>Free</h3><p class="muted" style="margin:0">For occasional sourcing</p></div>
        <div class="price">$0<small> forever</small></div>
        <ul>
          <li>Save profiles from the side panel &amp; export to Excel</li>
          <li>Dashboard, talent map, notes &amp; tags</li>
          <li>Search: extract 10 profiles per run, up to 50 per day</li>
          <li>Up to 3 projects</li>
          <li>“Most likely to move”: preview of the top 3</li>
        </ul>
        <a class="btn btn-ghost" href="#">Add to Chrome</a>
      </div>
      <div class="plan featured">
        <div><h3>Premium</h3><p class="muted" style="margin:0">For recruiters who source every day</p></div>
        <div>
          <div class="price"><span id="pPrice">$4.99</span><small> / month</small></div>
          <div class="muted" id="pBilled" style="font-size:14px;margin-top:6px">Billed monthly</div>
        </div>
        <ul>
          <li>Everything in Free</li>
          <li><strong>Full “Most likely to move” list</strong> with reasons</li>
          <li><strong>Unlimited search extraction</strong> — no daily limit, 50 profiles per run</li>
          <li><strong>Current position, company &amp; total experience</strong> right in search results</li>
          <li><strong>Unlimited projects</strong></li>
        </ul>
        <a class="btn btn-green" href="https://fastmate.lemonsqueezy.com/checkout/buy/b649a58d-00c4-41a0-ad82-a3b9c0660f90" target="_blank" rel="noopener">Get Premium</a>
      </div>
    </div>
    <p class="billing-note muted">Prices in USD; taxes may apply. Cancel anytime. Secure checkout by Lemon Squeezy.</p>
  </div>
</section>
<script>
  // Billing toggle: $4.99/month; quarterly −20% ($11.98 every 3 months); yearly −30% ($41.92 per year).
  (function () {{
    var plans = {{
      monthly: {{ price: '$4.99', billed: 'Billed monthly' }},
      quarterly: {{ price: '$3.99', billed: '$11.98 billed every 3 months — save 20%' }},
      yearly: {{ price: '$3.49', billed: '$41.92 billed yearly — save 30%' }}
    }};
    var buttons = document.querySelectorAll('.billing button');
    buttons.forEach(function (b) {{
      b.addEventListener('click', function () {{
        buttons.forEach(function (x) {{ x.classList.toggle('active', x === b); }});
        var p = plans[b.dataset.period];
        document.getElementById('pPrice').textContent = p.price;
        document.getElementById('pBilled').textContent = p.billed;
      }});
    }});
  }})();
</script>

<section class="section-alt">
  <div class="wrap">
    <div class="section-head"><h2>Frequently asked questions</h2></div>
    <div class="faq">
      <details><summary>Where is my candidate data stored?</summary><p>Only in your own browser (Chrome’s local extension storage). HireMate has no server that receives your candidate data. You can export a backup or delete everything at any time from the dashboard.</p></details>
      <details><summary>Do I need a LinkedIn Recruiter account?</summary><p>No. HireMate works with the profiles you can already see with your own LinkedIn account. Free LinkedIn accounts have their own search limits, which HireMate respects.</p></details>
      <details><summary>Does HireMate send messages or connection requests?</summary><p>No. HireMate never sends messages, invitations or posts on your behalf. Bulk features are capped and throttled to protect your account.</p></details>
      <details><summary>How is “likely to move” calculated?</summary><p>From career patterns in your own saved pool: how long people usually stay before moving, how long this person usually stays per company, time without a promotion and similar signals. It is an estimate, shown with its reasons — not a fact about any person.</p></details>
      <details><summary>What do I get for free?</summary><p>Saving profiles, Excel export, the dashboard and talent map are free. The free plan lets you extract 10 search results per run and up to 50 per day, includes up to 3 projects and a preview of the top 3 people most likely to move. Premium removes these limits and adds current position, company and total experience to search results.</p></details>
      <details><summary>Can I cancel Premium?</summary><p>Yes, anytime from the link in your receipt email. You keep Premium until the end of the period you paid for. See our <a href="{{P}}refund.html">Refund Policy</a>.</p></details>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="cta">
      <div><h2>Save your next shortlist in minutes.</h2><p>Free to install. No account needed.</p></div>
      <a class="btn btn-ghost" href="#">Add HireMate to Chrome</a>
    </div>
  </div>
</section>''', alt='vi/hiremate/index.html')

# ---------------- Legal ----------------
def legal(path, title, desc, inner):
    page(path, title + ' — FastMate', desc, f'<article class="legal"><h1>{title}</h1><p class="updated">Last updated: {UPDATED}</p>{inner}</article>', alt='vi/' + path)

legal('privacy.html', 'Privacy Policy', 'How FastMate and HireMate handle your data.', '''
<p>This policy explains how FastMate (“we”, “us”), operated by Fast Mate, handles information in our products, including the HireMate Chrome extension, and on this website.</p>
<h2>Summary</h2>
<ul>
  <li>Candidate information you save with HireMate is stored <strong>only in your browser</strong> (Chrome’s local extension storage). We do not receive, store or sell it.</li>
  <li>HireMate does not use analytics or tracking cookies.</li>
  <li>When you buy Premium, payment is handled by Lemon Squeezy, our merchant of record.</li>
</ul>
<h2>Information HireMate processes</h2>
<p>When you open a profile and use HireMate, the extension reads the information shown to you on that page (such as name, profile URL, work history, education and profile photo link) using your own signed-in session, and saves the candidates you choose — together with notes, tags and project statuses you add — in your browser’s local storage. This data never leaves your device unless you export it (for example to an Excel file) or copy it yourself.</p>
<p>You are responsible for how you use and share the candidate information you collect, including complying with applicable data-protection laws (such as GDPR or Vietnam’s Decree 13/2023/ND-CP) and the terms of the websites you use. HireMate includes tools to help: automatic deletion after a retention period you choose, backup and delete-all.</p>
<h2>Purchases</h2>
<p>To activate Premium, HireMate sends your license key and a device label (for example “HireMate · Win32”) to Lemon Squeezy’s license service, and re-checks the key every few days so a cancelled or expired subscription returns to the free plan. No candidate data is ever sent.</p>
<p>Premium purchases are processed by <a href="https://www.lemonsqueezy.com/privacy" target="_blank" rel="noopener">Lemon Squeezy</a>, which acts as merchant of record and collects the billing details needed to process your payment, taxes and invoices. We receive order information from Lemon Squeezy (such as your name, email, license key and order status) to provide Premium and support. We never see your full card details.</p>
<h2>Website</h2>
<p>This website is hosted on GitHub Pages. GitHub may log technical data such as IP addresses for security purposes; see GitHub’s privacy statement. We do not use analytics or advertising cookies on this site. Fonts are loaded from Google Fonts.</p>
<h2>Permissions used by HireMate</h2>
<ul>
  <li><strong>Side panel, tabs, scripting, access to linkedin.com</strong> — to read the profile you are viewing and show it in the side panel.</li>
  <li><strong>Storage / unlimited storage</strong> — to keep your saved candidates on your device.</li>
  <li><strong>Access to api.lemonsqueezy.com</strong> — only to activate and check your Premium license key.</li>
</ul>
<h2>Your choices</h2>
<p>You can edit or delete any saved candidate, delete all data from the dashboard (Data &amp; privacy), or uninstall the extension, which removes its local data. For purchase data, contact us or Lemon Squeezy.</p>
<h2>Children</h2>
<p>Our products are intended for professionals and are not directed to children under 16.</p>
<h2>Changes</h2>
<p>We may update this policy. The “last updated” date shows the latest version.</p>
<h2>Contact</h2>
<p>Questions? Email <a href="mailto:fastmate.support@gmail.com">fastmate.support@gmail.com</a>.</p>''')

legal('terms.html', 'Terms of Service', 'Terms for using FastMate products, including HireMate.', '''
<p>These terms govern your use of FastMate products, including the HireMate Chrome extension and HireMate Premium (the “Service”), provided by Fast Mate (“FastMate”, “we”). By installing or using the Service you agree to these terms.</p>
<h2>1. The Service</h2>
<p>HireMate helps you organize information from profiles you view in your browser: saving candidates, exporting them to Excel and managing them in a dashboard. Features may change over time.</p>
<h2>2. Your responsibilities</h2>
<ul>
  <li>You use the Service with your own accounts and are responsible for complying with the terms of the websites you visit (including LinkedIn’s User Agreement) and with applicable laws, including data-protection and anti-spam laws.</li>
  <li>You are responsible for the candidate information you save, export and share, and for having a lawful basis to process it.</li>
  <li>You will not use the Service to send unsolicited messages, to harass anyone, or to resell personal data.</li>
</ul>
<h2>3. Premium subscriptions</h2>
<p>Premium is sold through Lemon Squeezy, our merchant of record, whose <a href="https://www.lemonsqueezy.com/buyer-terms" target="_blank" rel="noopener">buyer terms</a> also apply to your purchase. Subscriptions renew automatically until cancelled. You can cancel anytime; access continues until the end of the paid period. Refunds follow our <a href="refund.html">Refund Policy</a>.</p>
<h2>4. Third-party websites</h2>
<p>HireMate works with third-party websites that we do not control. They may change at any time, which can temporarily affect features. LinkedIn is a trademark of LinkedIn Corporation; FastMate and HireMate are not affiliated with or endorsed by LinkedIn.</p>
<h2>5. Intellectual property</h2>
<p>The Service, its code and branding belong to FastMate. You receive a personal, non-transferable license to use it according to these terms.</p>
<h2>6. Disclaimers</h2>
<p>The Service is provided “as is”. Insights such as “likely to move” are statistical estimates and may be wrong; do not rely on them as facts about any person. We do not guarantee that the Service will be uninterrupted or error-free.</p>
<h2>7. Limitation of liability</h2>
<p>To the extent permitted by law, FastMate is not liable for indirect or consequential damages, loss of data or profits. Our total liability is limited to the amount you paid us in the 12 months before the claim.</p>
<h2>8. Termination</h2>
<p>You may stop using the Service at any time. We may suspend access if you breach these terms.</p>
<h2>9. Changes</h2>
<p>We may update these terms; continued use after changes means you accept them.</p>
<h2>10. Contact</h2>
<p><a href="mailto:fastmate.support@gmail.com">fastmate.support@gmail.com</a></p>''')

legal('refund.html', 'Refund Policy', 'Refund policy for HireMate Premium.', '''
<p>We want you to be happy with HireMate Premium.</p>
<h2>14-day money-back guarantee</h2>
<p>If Premium isn’t right for you, request a full refund within <strong>14 days</strong> of your first payment — no questions asked. Email <a href="mailto:fastmate.support@gmail.com">fastmate.support@gmail.com</a> with your order number, or reply to your Lemon Squeezy receipt.</p>
<h2>Renewals</h2>
<p>Renewal payments can be refunded within 7 days of the renewal date if you haven’t used Premium since then. You can cancel anytime to stop future renewals; access continues until the end of the paid period.</p>
<h2>How refunds are paid</h2>
<p>Refunds are processed by Lemon Squeezy, our merchant of record, to your original payment method. Depending on your bank, it can take 5–10 business days to appear.</p>''')

page('contact.html', 'Contact — FastMate', 'Contact FastMate.', alt='vi/contact.html', body='''
<article class="legal">
  <h1>Contact us</h1>
  <p class="updated">We usually reply within 1–2 business days.</p>
  <div class="grid-2">
    <div class="card"><h3>Support & questions</h3><p>Questions about HireMate, Premium, billing or refunds.</p><p style="margin-top:12px"><a class="btn btn-primary btn-sm" href="mailto:fastmate.support@gmail.com">fastmate.support@gmail.com</a></p></div>
    <div class="card"><h3>Billing</h3><p>Manage or cancel your subscription from the link in your Lemon Squeezy receipt email, or contact us and we’ll help.</p></div>
  </div>
  <p class="note" style="margin-top:24px">Operated by Fast Mate.</p>
</article>''')

exec(io.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'build_vi.py'), encoding='utf-8').read())

print('built')


# sitemap.xml (submit https://fastmate.github.io/fastmate/sitemap.xml in Google Search Console)
import datetime as _dt
_today = _dt.date.today().isoformat()
_urls = ''.join('<url><loc>' + SITE + x.replace('index.html', '') + '</loc><lastmod>' + _today + '</lastmod></url>' for x in PAGES)
io.open(os.path.join(OUT, 'sitemap.xml'), 'w', encoding='utf-8', newline='\n').write(
    '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + _urls + '</urlset>\n')
print('sitemap', len(PAGES), 'urls')
