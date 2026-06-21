"""
Fetch YouTube video transcript.

Usage:
    python fetch_youtube_transcript.py <youtube_url>

Output:
    Saves transcript to .tmp/transcript-raw.md

Dependencies:
    pip install youtube-transcript-api

TODO: Implementare al primo utilizzo con Claude Code
"""

import sys
import os

def fetch_transcript(url: str) -> str:
    """Fetch transcript from YouTube URL."""
    # TODO: Implementare con youtube-transcript-api
    # 1. Estrarre video_id dall'URL
    # 2. Provare trascrizione manuale (lingua italiana)
    # 3. Fallback su trascrizione automatica
    # 4. Fallback su auto-generated + traduzione
    raise NotImplementedError("Da implementare al primo utilizzo")


def save_transcript(text: str, output_path: str = ".tmp/transcript-raw.md"):
    """Save transcript to file."""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Transcript saved to {output_path}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python fetch_youtube_transcript.py <youtube_url>")
        sys.exit(1)
    
    transcript = fetch_transcript(sys.argv[1])
    save_transcript(transcript)
