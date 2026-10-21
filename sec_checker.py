import hashlib
import os
import sys
import requests


def check_url(url):
  print(f"\n[*] Checking URL: {url}")
  try:
    response = requests.get(url, timeout=5)
    print(f"[+] Status Code: {response.status_code}")
    print(f"[+] Server Header: {response.headers.get('Server', 'Not Found')}")
    print(
        "[+] X-Frame-Options:"
        f" {response.headers.get('X-Frame-Options', 'Not Set (Potentially vulnerable)')}"
    )
  except requests.exceptions.RequestException as e:
    print(f"[-] Error connecting to URL: {e}")


def check_file_hash(file_path):
  print(f"\n[*] Calculating SHA-256 for file: {file_path}")
  if not os.path.exists(file_path):
    print("[-] File not found!")
    return

  sha256_hash = hashlib.sha256()
  with open(file_path, "rb") as f:
    for byte_block in iter(lambda: f.read(4096), b""):
      sha256_hash.update(byte_block)
  print(f"[+] SHA-256: {sha256_hash.hexdigest()}")


if __name__ == "__main__":
  print("=== Simple Security & Utility Checker ===")
  if len(sys.argv) < 3:
    print("Usage: python sec_checker.py [url/file] [target]")
    print(
        "Example URL: python sec_checker.py url"
        " https://example.com"
    )
    print(
        "Example File: python sec_checker.py file"
        " path/to/file.txt"
    )
    sys.exit(1)

  mode = sys.argv[1].lower()
  target = sys.argv[2]

  if mode == "url":
    check_url(target)
  elif mode == "file":
    check_file_hash(target)
  else:
    print("[-] Unknown mode. Use 'url' or 'file'.")