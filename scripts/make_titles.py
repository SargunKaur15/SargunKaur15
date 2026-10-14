"""Generate the animated section-title SVGs in assets/titles/.

Run from the repository root:  python scripts/make_titles.py
"""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "assets" / "titles"

# (file slug, title, accent colour, icon markup drawn around a 48x48 box at the origin)
SECTIONS = [
    ("security-ai", "Security First, Powered by AI", "#ff6b35", """
      <path d="M24 9 L37 14 V24 C37 32 31 37 24 40 C17 37 11 32 11 24 V14 Z" fill="none" stroke="{c}" stroke-width="2.5" stroke-linejoin="round"/>
      <circle cx="24" cy="21" r="2.6" fill="{c}"/><circle cx="18" cy="28" r="2.2" fill="{c}"/><circle cx="30" cy="28" r="2.2" fill="{c}"/>
      <path d="M24 21 L18 28 M24 21 L30 28 M18 28 H30" stroke="{c}" stroke-width="1.5"/>"""),
    ("tech-stack", "Tech Stack", "#22d3ee", """
      <path d="M24 11 L38 18 L24 25 L10 18 Z" fill="none" stroke="{c}" stroke-width="2.5" stroke-linejoin="round"/>
      <path d="M10 24 L24 31 L38 24" fill="none" stroke="{c}" stroke-width="2.5" stroke-linejoin="round" opacity=".75"/>
      <path d="M10 30 L24 37 L38 30" fill="none" stroke="{c}" stroke-width="2.5" stroke-linejoin="round" opacity=".5"/>"""),
    ("projects", "Featured Projects · Security × AI", "#ff6b35", """
      <path d="M9 16 a3 3 0 0 1 3 -3 H20 L23 16 H36 a3 3 0 0 1 3 3 V33 a3 3 0 0 1 -3 3 H12 a3 3 0 0 1 -3 -3 Z" fill="none" stroke="{c}" stroke-width="2.5" stroke-linejoin="round"/>
      <path d="M20 22 L16 26 L20 30 M28 22 L32 26 L28 30" fill="none" stroke="{c}" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>"""),
    ("education", "Education", "#10b981", """
      <path d="M24 13 L41 20 L24 27 L7 20 Z" fill="none" stroke="{c}" stroke-width="2.5" stroke-linejoin="round"/>
      <path d="M14 23.5 V31 C14 34 34 34 34 31 V23.5" fill="none" stroke="{c}" stroke-width="2.5"/>
      <path d="M41 20 V29" stroke="{c}" stroke-width="2.5" stroke-linecap="round"/>"""),
    ("activity", "GitHub Activity", "#22d3ee", """
      <path class="beat" d="M7 26 H15 L19 16 L25 34 L29 22 L32 26 H41" fill="none" stroke="{c}" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>"""),
    ("connect", "Let's Connect", "#ff6b35", """
      <path d="M8 23 L39 11 L31 38 L23 28 Z" fill="none" stroke="{c}" stroke-width="2.5" stroke-linejoin="round"/>
      <path d="M23 28 L39 11" stroke="{c}" stroke-width="2"/>"""),
]

TEMPLATE = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 72" width="1000" height="72" role="img" aria-label="{title}">
  <title>{title}</title>
  <defs>
    <linearGradient id="sheen" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="600" y2="0" spreadMethod="repeat">
      <stop offset="0" stop-color="#e6edf3"/>
      <stop offset="0.42" stop-color="#e6edf3"/>
      <stop offset="0.5" stop-color="{c}"/>
      <stop offset="0.58" stop-color="#e6edf3"/>
      <stop offset="1" stop-color="#e6edf3"/>
      <animateTransform attributeName="gradientTransform" type="translate" from="0 0" to="600 0" dur="6s" repeatCount="indefinite"/>
    </linearGradient>
    <linearGradient id="rule" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="{c}"/>
      <stop offset="1" stop-color="{c}" stop-opacity="0"/>
    </linearGradient>
  </defs>
  <style>
    .icon {{ animation: glow 3s ease-in-out infinite; }}
    .dot {{ animation: run 4s ease-in-out infinite; }}
    .caret {{ animation: blink 1s steps(1) infinite; }}
    .beat {{ stroke-dasharray: 70; animation: beat 2.4s linear infinite; }}
    @keyframes glow {{ 0%, 100% {{ stroke-opacity: .45; }} 50% {{ stroke-opacity: 1; }} }}
    @keyframes run {{ 0% {{ transform: translateX(0); opacity: 0; }} 10% {{ opacity: 1; }} 90% {{ opacity: 1; }} 100% {{ transform: translateX(900px); opacity: 0; }} }}
    @keyframes blink {{ 50% {{ opacity: 0; }} }}
    @keyframes beat {{ from {{ stroke-dashoffset: 140; }} to {{ stroke-dashoffset: 0; }} }}
    @media (prefers-reduced-motion: reduce) {{ .icon, .dot, .caret, .beat {{ animation: none; }} .dot {{ display: none; }} }}
  </style>
  <rect x="0.5" y="0.5" width="999" height="71" rx="14" fill="#0b0d12" stroke="#ffffff" stroke-opacity="0.06"/>
  <rect class="icon" x="14" y="12" width="48" height="48" rx="12" fill="{c}" fill-opacity="0.12" stroke="{c}" stroke-width="1.5"/>
  <g transform="translate(14 12)">{icon}
  </g>
  <text x="80" y="46" font-family="'Segoe UI', 'Helvetica Neue', Ubuntu, Arial, sans-serif" font-size="26" font-weight="700" fill="url(#sheen)">{title_xml}</text>
  <text x="972" y="44" text-anchor="end" font-family="'Cascadia Code', 'Fira Code', Consolas, 'Courier New', monospace" font-size="13" fill="#8b949e">// {idx:02d}</text>
  <rect class="caret" x="976" y="32" width="7" height="14" fill="{c}"/>
  <rect x="80" y="58" width="880" height="2" rx="1" fill="url(#rule)" opacity="0.6"/>
  <circle class="dot" cx="80" cy="59" r="3" fill="{c}"/>
</svg>
"""


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for idx, (slug, title, colour, icon) in enumerate(SECTIONS, start=1):
        svg = TEMPLATE.format(
            title=title.replace("&", "&amp;"),
            title_xml=title.replace("&", "&amp;"),
            c=colour,
            idx=idx,
            icon=icon.format(c=colour),
        )
        (OUT / f"{slug}.svg").write_text(svg, encoding="utf-8", newline="\n")
        print("wrote", slug)


if __name__ == "__main__":
    main()
