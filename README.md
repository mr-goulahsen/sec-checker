# Simple Security & Utility Checker 🛡️

A lightweight Python script designed to quickly check HTTP security headers of URLs and calculate SHA-256 hashes for files. Perfect for basic reconnaissance and file integrity verification.

## Features
- **URL Header Inspection:** Check status codes, server info, and missing security headers (like `X-Frame-Options`).
- **File Integrity:** Generate SHA-256 hashes for files quickly.

## Usage
- For URLs:
  ```bash
  python sec_checker.py url [https://example.com](https://example.com)