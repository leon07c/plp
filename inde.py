import requests
import os
from urllib.parse import urlparse
import hashlib

def get_filename_from_url(url):
    """Extract filename from URL or generate one if missing."""
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)
    if not filename:
        filename = "downloaded_image.jpg"
    return filename

def file_already_exists(content, folder):
    """Check for duplicate images using hash comparison."""
    file_hash = hashlib.md5(content).hexdigest()
    for existing_file in os.listdir(folder):
        existing_path = os.path.join(folder, existing_file)
        with open(existing_path, 'rb') as f:
            existing_hash = hashlib.md5(f.read()).hexdigest()
            if existing_hash == file_hash:
                return True, existing_file
    return False, None

def fetch_image(url, folder="Fetched_Images"):
    """Fetch an image from the web and save it safely."""
    try:
        # Ensure directory exists
        os.makedirs(folder, exist_ok=True)

        # Request with precautions: user-agent, timeout
        headers = {"User-Agent": "UbuntuFetcher/1.0 (Respectful Bot)"}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        # Check content-type before saving
        content_type = response.headers.get("Content-Type", "")
        if not content_type.startswith("image/"):
            print(f"✗ Skipped {url} (Not an image, Content-Type: {content_type})")
            return

        # Check for duplicates
        duplicate, existing_file = file_already_exists(response.content, folder)
        if duplicate:
            print(f"⚠ Duplicate detected: already saved as {existing_file}")
            return

        # Save image with safe filename
        filename = get_filename_from_url(url)
        filepath = os.path.join(folder, filename)

        with open(filepath, 'wb') as f:
            f.write(response.content)

        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")

    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error while fetching {url}: {e}")
    except Exception as e:
        print(f"✗ An error occurred: {e}")

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    # Get multiple URLs from user (comma-separated)
    urls = input("Please enter image URLs (comma separated): ").split(",")

    for url in [u.strip() for u in urls if u.strip()]:
        fetch_image(url)

    print("\nConnection strengthened. Community enriched.")
    print('"A person is a person through other persons." - Ubuntu Philosophy')

if __name__ == "__main__":
    main()
