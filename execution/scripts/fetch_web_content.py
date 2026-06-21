"""
Fetch and clean web page content.

Usage:
    python fetch_web_content.py <url>

Output:
    Saves cleaned content to .tmp/source-content.md

Dependencies:
    pip install requests beautifulsoup4 markdownify

TODO: Implementare al primo utilizzo con Claude Code
"""

import sys
import os

def fetch_and_clean(url: str) -> str:
    """Fetch web page and extract main content as markdown."""
    # TODO: Implementare con requests + BeautifulSoup
    # 1. Fetch pagina
    # 2. Estrarre contenuto principale (rimuovere nav, footer, sidebar, ads)
    # 3. Convertire in Markdown pulito
    # 4. Rimuovere link tracking, utm params
    raise NotImplementedError("Da implementare al primo utilizzo")


def save_content(text: str, output_path: str = ".tmp/source-content.md"):
    """Save content to file."""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Content saved to {output_path}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python fetch_web_content.py <url>")
        sys.exit(1)
    
    content = fetch_and_clean(sys.argv[1])
    save_content(content)
