import markdown, os, pathlib
ROOT=pathlib.Path(__file__).resolve().parent.parent
PREVIEW_NOTE=True
CO='DGFIX LTD'; NUM='10646551'; ADDR='13 Chestnut Road, Dartford DA1 2LB'
EMAIL='Holusa.d@seznam.cz'
NAV=[('Home','index.html',''),('Games','games/index.html','games'),('Contact','contact/index.html','contact'),('Privacy','privacy/index.html','privacy')]
def page(path,title,desc,body,active):
    depth=path.count('/')
    r='../'*depth
    nav=''.join(f'<a href="{r}{h}"{" aria-current=page" if k==active else ""}>{n}</a>' for n,h,k in NAV)
    note='<div class="preview-note">Preview draft — pending approval. Not yet the final published site.</div>' if PREVIEW_NOTE else ''
    html=f'''<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
{'<meta name="robots" content="noindex">' if PREVIEW_NOTE else ''}
<link rel="icon" type="image/png" href="{r}assets/img/favicon-32.png">
<link rel="apple-touch-icon" href="{r}assets/img/apple-touch-icon.png">
<link rel="stylesheet" href="{r}assets/site.css">
</head>
<body>
{note}
<header class="site"><div class="wrap">
<a class="brand" href="{r}index.html">Whizzed<span>.</span></a>
<nav aria-label="Main">{nav}</nav>
</div></header>
<main><div class="wrap">
{body.replace('{r}',r)}
</div></main>
<footer class="site"><div class="wrap">
<p><strong>Whizzed is operated by {CO}</strong>, registered office {ADDR}.</p>
<p>Registered in England and Wales, company number {NUM}.</p>
<p><a href="{r}contact/index.html">Contact</a> · <a href="{r}privacy/index.html">Privacy</a> · <a href="{r}privacy/meridian/index.html">Meridian privacy policy</a></p>
<p>© 2026 {CO}</p>
</div></footer>
</body>
</html>
'''
    out=ROOT/path; out.parent.mkdir(parents=True,exist_ok=True); out.write_text(html)

OPERATED=f'<p><strong>Whizzed is operated by {CO}, registered office {ADDR}.</strong> {CO} is a private limited company registered in England and Wales (company number {NUM}).</p>'

page('index.html','Whizzed — games by DGFIX LTD','Whizzed is an independent games studio operated by DGFIX LTD.',f'''
<h1>Whizzed</h1>
<p class="lead">Whizzed is an independent games studio making small, friendly games for phones.</p>
<p><a href="{{r}}games/index.html">See our games</a> · <a href="{{r}}contact/index.html">Get in touch</a></p>
<h2 id="about">About</h2>
<div class="card soft">
{OPERATED}
<dl class="facts">
<dt>Trading name</dt><dd>Whizzed</dd>
<dt>Company</dt><dd>{CO}</dd>
<dt>Company number</dt><dd>{NUM}</dd>
<dt>Registered office</dt><dd>13 Chestnut Road, Dartford, Kent, DA1 2LB, United Kingdom</dd>
<dt>Email</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd>
</dl>
</div>
<h2>Our first game</h2>
<div class="card game">
<img class="icon" src="{{r}}assets/img/meridian-icon.webp" width="72" height="72" alt="Meridian app icon">
<div><h3 style="margin-top:0">Meridian</h3><span class="badge">Coming soon to Google Play</span>
<p style="margin:0">A quiet atlas. Spin the world. Know it a little better.</p>
<p style="margin:8px 0 0"><a href="{{r}}games/index.html#meridian">More about Meridian</a></p></div>
</div>
''','')

page('games/index.html','Games — Whizzed','Games by Whizzed: Meridian and Stellar Run.',f'''
<h1>Games</h1>
<p class="lead">Games made by Whizzed.</p>
<section id="meridian" class="card" style="margin-top:24px">
<div class="game">
<img class="icon" src="{{r}}assets/img/meridian-icon.webp" width="72" height="72" alt="Meridian app icon">
<div><h2 style="margin:0">Meridian</h2><span class="badge">Coming soon to Google Play</span>
<p style="margin:0"><em>A quiet atlas.</em> Spin the world. Know it a little better.</p></div>
</div>
<img class="feature" src="{{r}}assets/img/meridian-feature.webp" width="1024" height="500" alt="Meridian feature graphic: the Meridian globe, Quill and Sandglass on a study desk">
<p>Meridian is a geography quiz for Android. Learn countries through modes such as Globe (a country is lit, name it), Flags, Capitals, Find (tap the map), Which is bigger? and Beat the Clock, with a daily set of questions and a journey through the world’s regions. Play without an account; progress is saved on your device.</p>
<div class="shots">
<img src="{{r}}assets/img/meridian-shot-home.webp" width="360" height="720" alt="Meridian home screen" loading="lazy">
<img src="{{r}}assets/img/meridian-shot-modes.webp" width="360" height="720" alt="Meridian list of quiz modes" loading="lazy">
</div>
<p style="margin-top:16px"><a href="{{r}}privacy/meridian/index.html">Meridian privacy policy</a></p>
</section>
<section id="stellar-run" class="card" style="margin-top:24px">
<div class="game">
<img class="icon" src="{{r}}assets/img/stellar-run-icon.webp" width="72" height="72" alt="Stellar Run app icon">
<div><h2 style="margin:0">Stellar Run</h2><span class="badge later">Coming later</span>
<p style="margin:0">A portrait space shooter you can play with one thumb.</p></div>
</div>
</section>
''','games')

page('contact/index.html','Contact — Whizzed','Contact Whizzed (DGFIX LTD).',f'''
<h1>Contact</h1>
<p class="lead">Questions about our games, support or privacy? Email us and we will reply as soon as we can.</p>
<div class="card soft" style="margin-top:20px">
<dl class="facts">
<dt>Email</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd>
<dt>Company</dt><dd>{CO} (trading as Whizzed)</dd>
<dt>Company number</dt><dd>{NUM}</dd>
<dt>Registered office</dt><dd>13 Chestnut Road<br>Dartford<br>Kent<br>DA1 2LB<br>United Kingdom</dd>
</dl>
</div>
''','contact')

page('privacy/index.html','Privacy — Whizzed','Privacy information for Whizzed and its games.',f'''
<div class="policy">
<h1>Privacy</h1>
<p>Last updated: 11 November 2026</p>
<p>This page explains how Whizzed handles personal information on this website and points to the privacy policy for each of our games.</p>
<h2>Who we are</h2>
<p>Whizzed is a trading name of <strong>{CO}</strong>, company number {NUM}, registered office 13 Chestnut Road, Dartford, Kent, DA1 2LB, United Kingdom. {CO} is the data controller. Contact: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
<h2>Game privacy policies</h2>
<ul><li><a href="{{r}}privacy/meridian/index.html">Meridian privacy policy</a> (Android)</li></ul>
<p>Each game has its own policy because each one uses different services.</p>
<h2>This website</h2>
<p>This website is a set of static pages. It has no accounts, no contact forms, no advertising and no analytics, and it does not set cookies.</p>
<p>Like any website, the hosting provider that serves these pages processes technical information such as your IP address, browser type and the pages requested, so that the site can be delivered and protected against abuse. We do not use that information to identify you.</p>
<h2>If you email us</h2>
<p>If you email us, we use your email address and message only to reply and deal with any follow-up, and we delete the email when we no longer need it.</p>
<h2>Your rights</h2>
<p>If UK or EU data protection law applies to you, you may have the right to ask for a copy of your personal information, to ask for it to be corrected or deleted, to object to or restrict certain uses, and to complain to a regulator. In the United Kingdom that is the Information Commissioner’s Office (ICO): <a href="https://ico.org.uk">https://ico.org.uk</a>. To make a request, email <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
<h2>Changes</h2>
<p>If we change this page in a meaningful way, we will update the “Last updated” date.</p>
</div>
''','privacy')

md=(ROOT/'src/meridian-privacy.md').read_text()
html=markdown.markdown(md,extensions=['extra','sane_lists'])
html=html.replace('holusa.d@seznam.cz',f'<a href="mailto:{EMAIL}">{EMAIL}</a>').replace('<strong><a','<a').replace('</a></strong>','</a>')
page('privacy/meridian/index.html','Meridian privacy policy — Whizzed','Privacy policy for the Meridian app by Whizzed (DGFIX LTD).',f'''<div class="policy">
<h1>Privacy policy for Meridian</h1>
{html}
</div>''','privacy')
(ROOT/'.nojekyll').write_text('')
print('built')
