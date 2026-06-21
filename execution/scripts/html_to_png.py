"""
Convert HTML/CSS design to PNG image.

Usage:
    python html_to_png.py <input.html> <output.png> [--width 1200] [--height 630]

Output:
    PNG file at specified dimensions

Dependencies:
    pip install playwright
    playwright install chromium
"""

import sys
import argparse
from playwright.sync_api import sync_playwright


def html_to_png(html_path: str, output_path: str, width: int = 1200, height: int = 630):
    """Convert an HTML file to PNG screenshot at specified dimensions."""
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": width, "height": height})
        page.goto(f"file://{html_path}")
        page.screenshot(path=output_path, full_page=False)
        browser.close()
    print(f"Saved: {output_path} ({width}x{height})")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert HTML to PNG")
    parser.add_argument("input", help="Path to HTML file")
    parser.add_argument("output", help="Path to output PNG")
    parser.add_argument("--width", type=int, default=1200, help="Width in px")
    parser.add_argument("--height", type=int, default=630, help="Height in px")
    args = parser.parse_args()

    html_to_png(args.input, args.output, args.width, args.height)
