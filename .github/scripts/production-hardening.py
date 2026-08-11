from pathlib import Path

p = Path('index.html')
s = p.read_text(encoding='utf-8')

old = """const urlToken = new URLSearchParams(location.search).get('t');
const DEMO_MODE = !urlToken || urlToken === 'demo';"""
new = """const urlToken = new URLSearchParams(location.search).get('t');
// Production is fail-closed. Demo access must be explicitly requested and is
// limited to local/preview hosts so the public production URL cannot bypass payment.
const IS_LOCAL_PREVIEW = ['localhost', '127.0.0.1'].includes(location.hostname) || location.hostname.endsWith('.vercel.app');
const DEMO_MODE = urlToken === 'demo' && IS_LOCAL_PREVIEW;"""
if old in s:
    s = s.replace(old, new, 1)

old2 = """  } catch(e) {
    console.warn('Token validation error:', e);
    return { valid: true, demo: true }; // fail open so network issues don't break access
  }
}"""
new2 = """  } catch(e) {
    console.warn('Token validation error:', e);
    return { valid: false, reason: 'validation_error' }; // fail closed: paid access must be verifiable
  }
}"""
if old2 in s:
    s = s.replace(old2, new2, 1)

s = s.replace("\n  async send\n\n  async send() {", "\n  async send() {", 1)
p.write_text(s, encoding='utf-8')
