# Inside the Context Window

A bilingual (EN/FR), scroll-driven guide to what actually happens when you press send
in Claude or Gemini, and how to use either one well.

**Live:** https://joris-decombe.github.io/context-window/

Written for people who are not engineers: family, friends, personal and academic work.
The main thread assumes no technical background; anything technical lives in collapsed
"going further" panels, including a playbook for people who write software.

## Contents

Tokens · The context window · Caching · Who is giving the orders ·
The machinery around the model · Memory · Giving it hands · The Claude side ·
The Gemini side · Side by side · How to actually use it

## Features

- **Two languages**, switchable at any time. The choice travels in the URL, so a link
  shared as `?lang=fr` opens in French.
- **Per-section deep links.** The `§` button beside each heading copies a link straight
  to that section, e.g. `?lang=fr#caching`.
- **Light and dark**, following the operating system by default, with a manual override.
- **Scroll-driven figures** (the instruction stack, the context budget, the loop) that
  advance as you read. They respect `prefers-reduced-motion`.
- **Two interactive demos**: a tokenizer you can type into, and a caching cost calculator.

## Accessibility notes

Colour choices were measured rather than eyeballed:

- Text contrast is validated against **APCA** (Lc), not only WCAG 2, because WCAG's
  formula overstates contrast on dark backgrounds. Body text clears Lc 75 in both themes;
  small monospace labels clear Lc 60 at 12-13px and weight 500-700.
- The instruction stack encodes **rank**, so it uses one hue in stepped lightness rather
  than seven hues. Lightness survives every form of colour vision deficiency.
- The one genuinely categorical figure uses a palette validated for deuteranopia and
  protanopia separation, with visible labels as a secondary channel.
- Colour never carries meaning on its own; every coloured element has a text label.
- The light theme is warm paper (`#FAF7F1`) rather than a tinted grey; every ink, rule
  and accent was re-solved against it rather than carried over.
- Touch targets are 44px on coarse pointers, and the seven-column comparison table
  becomes one card per product on phones.

## Repository layout

```
index.html        the built site, which is what GitHub Pages serves
.nojekyll         tells Pages to serve the file as-is
build.py          rebuilds index.html from src/
src/artifact.html the source, as published on claude.ai
```

`src/artifact.html` has no `<!doctype>`, `<head>` or `<body>` of its own, because the
claude.ai Artifact host supplies those. `build.py` adds them back, along with the page
metadata a shared link needs. To rebuild after editing the source:

```sh
python3 build.py
```

## A note on fonts

The page loads Bricolage Grotesque, Newsreader and JetBrains Mono from Google Fonts.
Every face has a real fallback stack, so the page is readable if that request is
blocked, but it does mean one third-party request. To remove it, download the woff2
files into `fonts/`, replace the `<link>` in `build.py` with `@font-face` rules, and
rebuild.

## Licence

Text and design: CC BY 4.0. Reuse it, adapt it, credit it.

Product details were accurate in September 2026 and will date quickly; every factual
claim is sourced in the article's Sources section.
