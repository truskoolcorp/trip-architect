from pathlib import Path

path = Path('index.html')
html = path.read_text(encoding='utf-8')

if 'id="dot-ecosystem-footer"' not in html:
    block = '''\n\n<!-- ============================== DALLASITE ON TOUR ECOSYSTEM ============================== -->\n<footer id="dot-ecosystem-footer" style="background:#120f0c;border-top:1px solid rgba(196,113,53,.22);padding:28px 20px;color:#c9b9aa;font-family:'DM Sans',sans-serif;">\n  <div style="max-width:1180px;margin:0 auto;display:flex;flex-wrap:wrap;gap:14px 24px;align-items:center;justify-content:space-between;">\n    <div style="font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:#E8A06A;">Dallasite on Tour Network</div>\n    <nav aria-label="Dallasite on Tour network" style="display:flex;flex-wrap:wrap;gap:16px;font-size:13px;">\n      <a href="https://dallasiteontour.org" style="color:inherit;text-decoration:none;">Dallasite on Tour</a>\n      <a href="https://passport.dallasiteontour.org" style="color:inherit;text-decoration:none;">Passport</a>\n      <a href="https://canaryspanish.dallasiteontour.org" style="color:inherit;text-decoration:none;">Canary Spanish</a>\n      <a href="https://wanderlustfashionstore.com" style="color:inherit;text-decoration:none;">Wanderlust™</a>\n    </nav>\n  </div>\n</footer>\n'''
    if '</body>' not in html:
        raise SystemExit('body marker not found')
    html = html.replace('</body>', block + '\n</body>', 1)

path.write_text(html, encoding='utf-8')
