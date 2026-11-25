import markdown, os, pathlib
from datetime import date

ROOT=pathlib.Path(__file__).resolve().parent.parent
PREVIEW_NOTE = False
CO='DGFIX LTD'; NUM='10646551'; ADDR='13 Chestnut Road, Dartford DA1 2LB'
EMAIL='Holusa.d@seznam.cz'
PRIVACY_EMAIL='sulikovazena@gmail.com'
SITE='https://whizzed.uk'
NAV=[('Home','index.html',''),('Games','games/index.html','games'),('Contact','contact/index.html','contact'),('Privacy','privacy/index.html','privacy')]
PLAY={
    'stellar-run':'com.stellarrun.game',
    'flashsums':'com.whizzed.flashsums',
    'meridian':'com.whizzed.meridian',
}

def play_badge(pkg, r='{r}'):
    url=f'https://play.google.com/store/apps/details?id={pkg}'
    return (
        f'<a class="play-badge" href="{url}">'
        f'<img src="{r}assets/img/google-play-badge.png" alt="Get it on Google Play" width="646" height="250">'
        f'</a>'
    )

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
{'<meta name="robots" content="noindex, nofollow">' if PREVIEW_NOTE else ''}
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
<p><a href="{r}contact/index.html">Contact</a> · <a href="{r}privacy/index.html">Privacy</a></p>
<p class="play-legal">Google Play and the Google Play logo are trademarks of Google LLC.</p>
<p>© 2026 {CO}</p>
</div></footer>
</body>
</html>
'''
    out=ROOT/path; out.parent.mkdir(parents=True,exist_ok=True); out.write_text(html)

OPERATED=f'<p><strong>Whizzed is operated by {CO}, registered office {ADDR}.</strong> {CO} is a private limited company registered in England and Wales (company number {NUM}).</p>'

page('index.html','Whizzed — games by DGFIX LTD','Whizzed is an independent games studio operated by DGFIX LTD. Games include Stellar Run, Flashsums and Meridian, on Google Play.',f'''
<h1>Whizzed</h1>
<p class="lead">Whizzed is an independent games studio making small, friendly games for phones.</p>
<p><a href="{{r}}games/index.html">See our games</a> · <a href="{{r}}contact/index.html">Get in touch</a></p>
<h2>Our games</h2>
<div class="card game" id="home-stellar-run">
<img class="icon" src="{{r}}assets/img/stellar-run-icon.webp" width="72" height="72" alt="Stellar Run app icon">
<div>
<h3 style="margin-top:0">Stellar Run: Space Shooter</h3>
<p style="margin:0">A one-thumb arcade space shooter. Sectors, bosses, DRYDOCK upgrades and bombs.</p>
{play_badge(PLAY['stellar-run'])}
<p style="margin:8px 0 0"><a href="{{r}}games/stellar-run/index.html">More about Stellar Run</a></p>
</div>
</div>
<div class="card game" id="home-flashsums" style="margin-top:16px">
<img class="icon" src="{{r}}assets/img/flashsums-icon.webp" width="72" height="72" alt="Flashsums app icon">
<div>
<h3 style="margin-top:0">Flashsums</h3>
<p style="margin:0">11+ maths and reasoning practice: timed sums, verbal and non-verbal skills.</p>
{play_badge(PLAY['flashsums'])}
<p style="margin:8px 0 0"><a href="{{r}}games/flashsums/index.html">More about Flashsums</a></p>
</div>
</div>
<div class="card game" id="home-meridian" style="margin-top:16px">
<img class="icon" src="{{r}}assets/img/meridian-icon.webp" width="72" height="72" alt="Meridian app icon">
<div>
<h3 style="margin-top:0">Meridian: A Quiet Atlas</h3>
<p style="margin:0">A calm KS2 geography quiz. Name countries, flags and capitals on a globe.</p>
{play_badge(PLAY['meridian'])}
<p style="margin:8px 0 0"><a href="{{r}}games/meridian/index.html">More about Meridian</a></p>
</div>
</div>
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
''','')

page('games/index.html','Games — Whizzed','Games by Whizzed, now on Google Play: Stellar Run, Flashsums and Meridian.',f'''
<h1>Games</h1>
<p class="lead">Games made by Whizzed, available on Google Play.</p>

<section id="stellar-run" class="card" style="margin-top:24px">
<div class="game">
<img class="icon" src="{{r}}assets/img/stellar-run-icon.webp" width="72" height="72" alt="Stellar Run app icon">
<div>
<h2 style="margin:0">Stellar Run: Space Shooter</h2>
<p style="margin:0">A one-thumb arcade space shooter. Sectors, bosses, DRYDOCK upgrades and bombs.</p>
{play_badge(PLAY['stellar-run'])}
</div>
</div>
<img class="feature" src="{{r}}assets/img/stellar-run-feature.webp" width="1024" height="500" alt="Stellar Run feature graphic: a space fighter above a planet">
<p>Stellar Run is a portrait arcade space shooter you can play with one thumb. Drag to fly, your guns fire on their own, and each sector ends in a boss. Spend coins in the DRYDOCK shop on weapons, thrusters, hull or a bigger ship.</p>
<div class="shots">
<img src="{{r}}assets/img/stellar-run-shot-boss.webp" width="360" height="640" alt="Stellar Run boss fight" loading="lazy">
<img src="{{r}}assets/img/stellar-run-shot-drydock.webp" width="360" height="640" alt="Stellar Run DRYDOCK upgrade shop" loading="lazy">
</div>
<p style="margin-top:16px"><a href="{{r}}games/stellar-run/index.html">Stellar Run page</a> · <a href="{{r}}privacy/stellar-run/index.html">Stellar Run privacy policy</a></p>
</section>

<section id="flashsums" class="card" style="margin-top:24px">
<div class="game">
<img class="icon" src="{{r}}assets/img/flashsums-icon.webp" width="72" height="72" alt="Flashsums app icon">
<div>
<h2 style="margin:0">Flashsums</h2>
<p style="margin:0">11+ maths and reasoning practice: timed sums, verbal and non-verbal skills.</p>
{play_badge(PLAY['flashsums'])}
</div>
</div>
<img class="feature" src="{{r}}assets/img/flashsums-feature.webp" width="1024" height="500" alt="Flashsums feature graphic">
<p>Flashsums is a neon maths and brain trainer for timed practice of the skills used in the UK 11+ and in KS2 maths. It is skill practice in a game, not an official 11+ exam, and it is not linked to any exam board.</p>
<div class="shots">
<img src="{{r}}assets/img/flashsums-shot-play.webp" width="360" height="640" alt="Flashsums timed sums with a streak" loading="lazy">
<img src="{{r}}assets/img/flashsums-shot-hard.webp" width="360" height="640" alt="Flashsums hard mode with the clock" loading="lazy">
</div>
<p style="margin-top:16px"><a href="{{r}}games/flashsums/index.html">Flashsums page</a> · <a href="{{r}}privacy/flashsums/index.html">Flashsums privacy policy</a></p>
</section>

<section id="meridian" class="card" style="margin-top:24px">
<div class="game">
<img class="icon" src="{{r}}assets/img/meridian-icon.webp" width="72" height="72" alt="Meridian app icon">
<div>
<h2 style="margin:0">Meridian: A Quiet Atlas</h2>
<p style="margin:0">A calm KS2 geography quiz. Name countries, flags and capitals on a globe.</p>
{play_badge(PLAY['meridian'])}
</div>
</div>
<img class="feature" src="{{r}}assets/img/meridian-feature.webp" width="1024" height="500" alt="Meridian feature graphic: the Meridian globe, Quill and Sandglass on a study desk">
<p>Meridian is a calm geography quiz for Android. Learn countries through modes such as Globe, Flags, Capitals and Find, with a journey through the world’s regions. Play without an account; progress is saved on your device.</p>
<div class="shots">
<img src="{{r}}assets/img/meridian-shot-home.webp" width="360" height="720" alt="Meridian home screen" loading="lazy">
<img src="{{r}}assets/img/meridian-shot-modes.webp" width="360" height="720" alt="Meridian list of quiz modes" loading="lazy">
</div>
<p style="margin-top:16px"><a href="{{r}}games/meridian/index.html">Meridian page</a> · <a href="{{r}}privacy/meridian/index.html">Meridian privacy policy</a></p>
</section>
''','games')

MORE='''
<div class="more-games card soft">
<p style="margin:0 0 8px"><strong>More from Whizzed</strong></p>
<ul>
<li><a href="{r}games/stellar-run/index.html">Stellar Run: Space Shooter</a></li>
<li><a href="{r}games/flashsums/index.html">Flashsums</a></li>
<li><a href="{r}games/meridian/index.html">Meridian: A Quiet Atlas</a></li>
</ul>
</div>
'''

page('games/stellar-run/index.html','Stellar Run: Space Shooter — Whizzed','Stellar Run is a one-thumb arcade space shooter for Android, with sectors, bosses, DRYDOCK upgrades and bombs. Get it on Google Play.',f'''
<div class="game">
<img class="icon" src="{{r}}assets/img/stellar-run-icon.webp" width="72" height="72" alt="Stellar Run app icon">
<div>
<h1 style="margin:0">Stellar Run: Space Shooter</h1>
<p class="lead" style="margin:8px 0 0">A one-thumb arcade space shooter. Sectors, bosses, DRYDOCK upgrades and bombs.</p>
{play_badge(PLAY['stellar-run'])}
</div>
</div>
<img class="feature" src="{{r}}assets/img/stellar-run-feature.webp" width="1024" height="500" alt="Stellar Run feature graphic: a space fighter above a planet">
<p>Stellar Run is a fast portrait arcade space shooter you can play with one thumb. Drag anywhere to fly. Your guns fire on their own. Clear waves of enemies, survive the boss at the end of each sector, then spend coins in the DRYDOCK shop — upgrade your weapon, thrusters and hull, or buy a bigger ship. Double-tap or tap BOMB to clear the screen when the belt gets ugly.</p>
<p>Seven themed sectors wait, with a local high score to beat. On your first death in a run you can revive with coins, or by watching an optional rewarded ad. The game itself works offline, and no account is required.</p>
<p>Contains ads (a banner and full-screen ads). A one-time purchase (£0.99) removes those. Optional revive ads can still be watched if you choose. Ads need an internet connection.</p>
<div class="shots">
<img src="{{r}}assets/img/stellar-run-shot-boss.webp" width="360" height="640" alt="Stellar Run boss fight">
<img src="{{r}}assets/img/stellar-run-shot-bomb.webp" width="360" height="640" alt="Stellar Run bomb clearing the screen">
<img src="{{r}}assets/img/stellar-run-shot-drydock.webp" width="360" height="640" alt="Stellar Run DRYDOCK upgrade shop">
<img src="{{r}}assets/img/stellar-run-shot-sector.webp" width="360" height="640" alt="Stellar Run sector boss approach">
</div>
<p style="margin-top:16px"><a href="{{r}}privacy/stellar-run/index.html">Stellar Run privacy policy</a></p>
{MORE}
''','games')

page('games/flashsums/index.html','Flashsums — Whizzed','Flashsums is 11+ maths and reasoning practice for Android: timed sums, verbal and non-verbal skills. Get it on Google Play.',f'''
<div class="game">
<img class="icon" src="{{r}}assets/img/flashsums-icon.webp" width="72" height="72" alt="Flashsums app icon">
<div>
<h1 style="margin:0">Flashsums</h1>
<p class="lead" style="margin:8px 0 0">11+ maths and reasoning practice: timed sums, verbal and non-verbal skills.</p>
{play_badge(PLAY['flashsums'])}
</div>
</div>
<img class="feature" src="{{r}}assets/img/flashsums-feature.webp" width="1024" height="500" alt="Flashsums feature graphic">
<p>Flashsums is a fast neon maths and brain trainer for quick, timed practice of the skills used in the UK 11+ (eleven plus) and in KS2 maths. Race the clock on mental maths, from Easy to Expert, then switch to brain modes that practise verbal reasoning and non-verbal reasoning — word, letter, shape and sequence puzzles.</p>
<p>You can play in portrait or landscape. There are global Play Games leaderboards, and a local Top 10 on your device. No account is needed to play. Sign in to Play Games only if you want the global boards.</p>
<p>Flashsums is skill practice in a game. It is not an official 11+ exam, it does not include full mock papers, and it is not linked to any exam board.</p>
<p>Contains ads on the menu and after a finished round — never during a timed round. A one-time purchase (£0.99) removes them. You can restore the purchase from Settings.</p>
<div class="shots">
<img src="{{r}}assets/img/flashsums-shot-play.webp" width="360" height="640" alt="Flashsums timed sums with a streak">
<img src="{{r}}assets/img/flashsums-shot-hard.webp" width="360" height="640" alt="Flashsums hard mode with the clock">
<img src="{{r}}assets/img/flashsums-shot-results.webp" width="360" height="640" alt="Flashsums results after a round">
<img src="{{r}}assets/img/flashsums-shot-leaderboard.webp" width="360" height="640" alt="Flashsums leaderboard">
</div>
<p style="margin-top:16px"><a href="{{r}}privacy/flashsums/index.html">Flashsums privacy policy</a></p>
{MORE}
''','games')

page('games/meridian/index.html','Meridian: A Quiet Atlas — Whizzed','Meridian is a calm KS2 geography quiz for Android. Name countries, flags and capitals on a globe. Get it on Google Play.',f'''
<div class="game">
<img class="icon" src="{{r}}assets/img/meridian-icon.webp" width="72" height="72" alt="Meridian app icon">
<div>
<h1 style="margin:0">Meridian: A Quiet Atlas</h1>
<p class="lead" style="margin:8px 0 0">A calm KS2 geography quiz. Name countries, flags and capitals on a globe.</p>
{play_badge(PLAY['meridian'])}
</div>
</div>
<img class="feature" src="{{r}}assets/img/meridian-feature.webp" width="1024" height="500" alt="Meridian feature graphic: the Meridian globe, Quill and Sandglass on a study desk">
<p>Meridian is a calm, unhurried geography quiz. Quill, a small paper bird, keeps you company at the desk while you work your way around the world, one region at a time.</p>
<p>It is useful practice for KS2 geography: countries, flags, capitals and finding places on a map. The 11+ (eleven plus) does not usually include a geography paper, so this is general knowledge and map practice, not exam-paper prep.</p>
<p>Four ways to play: Globe (a country lights up — name it), Flags, Capitals, and Find (tap the right place on the map). Start in Europe and travel on through the world’s regions, earning stars and taking each Grand Tour. Beat the Clock, a daily round, a stamp book and souvenirs for Quill are there when you want them. There are 170 countries. No account and no sign-in. Your progress is saved on your device. The quiz works offline.</p>
<p>Contains ads that are suitable for children. A one-time purchase (£0.99) removes them, and a grown-up is asked to confirm before any purchase.</p>
<div class="shots">
<img src="{{r}}assets/img/meridian-shot-home.webp" width="360" height="720" alt="Meridian home screen">
<img src="{{r}}assets/img/meridian-shot-modes.webp" width="360" height="720" alt="Meridian list of quiz modes">
<img src="{{r}}assets/img/meridian-shot-flags.webp" width="360" height="640" alt="Meridian flags quiz">
<img src="{{r}}assets/img/meridian-shot-find.webp" width="360" height="640" alt="Meridian find-on-the-map quiz">
</div>
<p style="margin-top:16px"><a href="{{r}}privacy/meridian/index.html">Meridian privacy policy</a></p>
{MORE}
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
<p>Last updated: 25 November 2026</p>
<p>This page explains how Whizzed handles personal information on this website and points to the privacy policy for each of our apps.</p>
<h2>Who we are</h2>
<p>Whizzed is a trading name of <strong>{CO}</strong>, company number {NUM}, registered office 13 Chestnut Road, Dartford, Kent, DA1 2LB, United Kingdom. {CO} is the data controller. Contact: <a href="mailto:{PRIVACY_EMAIL}">{PRIVACY_EMAIL}</a>.</p>
<h2>App privacy policies</h2>
<ul>
<li><a href="{{r}}privacy/stellar-run/index.html">Stellar Run privacy policy</a> (Android)</li>
<li><a href="{{r}}privacy/flashsums/index.html">Flashsums privacy policy</a> (Android)</li>
<li><a href="{{r}}privacy/meridian/index.html">Meridian privacy policy</a> (Android)</li>
<li><a href="{{r}}privacy/printcost/index.html">Whizzed Print Cost privacy policy</a> (Android)</li>
</ul>
<p>Each app has its own policy because each one uses different services.</p>
<h2>This website</h2>
<p>This website is a set of static pages. It has no accounts, no contact forms, no advertising and no analytics, and it does not set cookies.</p>
<p>Like any website, the hosting provider that serves these pages processes technical information such as your IP address, browser type and the pages requested, so that the site can be delivered and protected against abuse. We do not use that information to identify you.</p>
<h2>If you email us</h2>
<p>If you email us, we use your email address and message only to reply and deal with any follow-up, and we delete the email when we no longer need it.</p>
<h2>Your rights</h2>
<p>If UK or EU data protection law applies to you, you may have the right to ask for a copy of your personal information, to ask for it to be corrected or deleted, to object to or restrict certain uses, and to complain to a regulator. In the United Kingdom that is the Information Commissioner’s Office (ICO): <a href="https://ico.org.uk">https://ico.org.uk</a>. To make a request, email <a href="mailto:{PRIVACY_EMAIL}">{PRIVACY_EMAIL}</a>.</p>
<h2>Changes</h2>
<p>If we change this page in a meaningful way, we will update the “Last updated” date.</p>
</div>
''','privacy')

def policy(src, dest, title, desc, heading):
    md=(ROOT/'src'/src).read_text()
    html=markdown.markdown(md,extensions=['extra','sane_lists'])
    for addr in ('holusa.d@seznam.cz', 'Holusa.d@seznam.cz', PRIVACY_EMAIL):
        html=html.replace(addr, '<a href="mailto:%s">%s</a>' % (PRIVACY_EMAIL, PRIVACY_EMAIL))
    html=html.replace('<strong><a','<a').replace('</a></strong>','</a>')
    body='<div class="policy">\n<h1>%s</h1>\n%s\n</div>' % (heading, html)
    page(dest,title,desc,body,'privacy')

policy('stellar-run-privacy.md','privacy/stellar-run/index.html','Stellar Run privacy policy — Whizzed','Privacy policy for the Stellar Run app by Whizzed (DGFIX LTD).','Privacy policy for Stellar Run')
policy('meridian-privacy.md','privacy/meridian/index.html','Meridian privacy policy — Whizzed','Privacy policy for the Meridian app by Whizzed (DGFIX LTD).','Privacy policy for Meridian')
policy('flashsums-privacy.md','privacy/flashsums/index.html','Flashsums privacy policy — Whizzed','Privacy policy for the Flashsums app by Whizzed (DGFIX LTD).','Privacy policy for Flashsums')
policy('printcost-privacy.md','privacy/printcost/index.html','Whizzed Print Cost privacy policy — Whizzed','Privacy policy for the Whizzed Print Cost app by Whizzed (DGFIX LTD).','Privacy policy for Whizzed Print Cost')

(ROOT/'.nojekyll').write_text('')

PUBLIC_PATHS=[
    '/',
    '/games/',
    '/games/stellar-run/',
    '/games/flashsums/',
    '/games/meridian/',
    '/contact/',
    '/privacy/',
    '/privacy/stellar-run/',
    '/privacy/flashsums/',
    '/privacy/meridian/',
    '/privacy/printcost/',
]
if PREVIEW_NOTE:
    (ROOT/'robots.txt').write_text('User-agent: *\nDisallow: /\n')
else:
    (ROOT/'robots.txt').write_text('User-agent: *\nAllow: /\n\nSitemap: https://whizzed.uk/sitemap.xml\n')
    today=date.today().isoformat()
    urls='\n'.join(
        f'  <url>\n    <loc>{SITE}{p}</loc>\n    <lastmod>{today}</lastmod>\n  </url>'
        for p in PUBLIC_PATHS
    )
    (ROOT/'sitemap.xml').write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f'{urls}\n'
        '</urlset>\n'
    )

print('built')
