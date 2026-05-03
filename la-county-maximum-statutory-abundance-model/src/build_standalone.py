"""
Build a single self-contained HTML file (dashboard_standalone.html)
by inlining all PNGs as base64 data URIs. The output can be downloaded
or emailed as one file with no broken images.
"""

from __future__ import annotations
import base64
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC_HTML = ROOT / "outputs" / "dashboard.html"
OUT_HTML = ROOT / "outputs" / "dashboard_standalone.html"


def encode_png(path: Path) -> str:
    data = path.read_bytes()
    b64 = base64.b64encode(data).decode("ascii")
    return f"data:image/png;base64,{b64}"


def main():
    html = SRC_HTML.read_text()
    base_dir = SRC_HTML.parent

    def replace_src(m: re.Match) -> str:
        src_path = m.group(1)
        png = (base_dir / src_path).resolve()
        if not png.exists():
            return m.group(0)
        return f'src="{encode_png(png)}"'

    html = re.sub(r'src="(dashboard/[^"]+\.png)"', replace_src, html)

    OUT_HTML.write_text(html)
    size_kb = OUT_HTML.stat().st_size // 1024
    print(f"Wrote {OUT_HTML} ({size_kb} KB)")


if __name__ == "__main__":
    main()
