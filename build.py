#!/usr/bin/env python3
"""Compose the standalone GitHub Pages site from the artifact source.

The Artifact platform wraps the published file in its own <!doctype>/<head>/<body>
skeleton. A static host does not, so this script adds that skeleton back, plus the
metadata a shared link needs (title, description, social preview, theme colour,
favicon) which the artifact host supplied or did not need.

Run:  python3 build.py
Out:  index.html
"""
import pathlib, re, urllib.parse

SRC = pathlib.Path(__file__).parent / "src" / "artifact.html"
OUT = pathlib.Path(__file__).parent

TITLE = "Inside the Context Window"
DESC_EN = ("What actually happens when you press send, and how to use Claude and Gemini well. "
           "A bilingual, scroll-driven guide: tokens, context, caching, instructions, memory "
           "and the machinery around the model.")

FAVICON = (
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32">'
    '<rect width="32" height="32" rx="7" fill="#4139AB"/>'
    '<rect x="7" y="8" width="18" height="3.5" rx="1.75" fill="#fff"/>'
    '<rect x="7" y="14.25" width="18" height="3.5" rx="1.75" fill="#fff" opacity=".68"/>'
    '<rect x="7" y="20.75" width="18" height="3.5" rx="1.75" fill="#fff" opacity=".38"/></svg>'
)

def main():
    src = SRC.read_text(encoding="utf-8")
    split = src.index('<div id="progress">')
    head_src, body_src = src[:split], src[split:]
    head_src = re.sub(r"<title>.*?</title>\s*", "", head_src, count=1, flags=re.S)
    favicon_uri = "data:image/svg+xml," + urllib.parse.quote(FAVICON, safe="")

    reset = """  <style>
    :root{ padding-top:env(safe-area-inset-top,0px); padding-bottom:env(safe-area-inset-bottom,0px); }
    body{ margin:0 }
    img{ max-width:100% }
    [hidden]{ display:none !important }
  </style>"""

    page = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <title>{TITLE}</title>
  <meta name="description" content="{DESC_EN}">
  <meta name="color-scheme" content="light dark">
  <meta name="theme-color" media="(prefers-color-scheme: light)" content="#FAF7F1">
  <meta name="theme-color" media="(prefers-color-scheme: dark)" content="#141127">
  <link rel="icon" href="{favicon_uri}">
  <meta property="og:type" content="article">
  <meta property="og:title" content="{TITLE}">
  <meta property="og:description" content="{DESC_EN}">
  <meta property="og:locale" content="en">
  <meta property="og:locale:alternate" content="fr">
  <meta name="twitter:card" content="summary_large_image">
{reset}
{head_src.rstrip()}
</head>
<body>
{body_src.rstrip()}
</body>
</html>
"""
    (OUT / "index.html").write_text(page, encoding="utf-8")
    (OUT / ".nojekyll").write_text("", encoding="utf-8")
    print(f"wrote index.html ({(OUT/'index.html').stat().st_size/1024:.0f} KB)")

if __name__ == "__main__":
    main()
