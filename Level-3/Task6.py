import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse


def validate_url(url):
    """Check whether the URL is valid."""
    parsed_url = urlparse(url)

    return (
        parsed_url.scheme in ("http", "https")
        and bool(parsed_url.netloc)
        and "." in parsed_url.netloc
    )


def scrape_website(url):
    """Fetch and extract useful information from a website."""

    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; CognifyzStudentScraper/1.0)"
    }

    try:
        print("\nFetching website data...")

        response = requests.get(
            url,
            headers=headers,
            timeout=15
        )

        response.raise_for_status()

        # Parse webpage HTML
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract page title
        title = (
            soup.title.get_text(strip=True)
            if soup.title else "No title found"
        )

        # Extract meta description
        meta_description = soup.find(
            "meta",
            attrs={"name": "description"}
        )

        description = (
            meta_description.get("content", "No description found")
            if meta_description else "No description found"
        )

        # Extract headings
        headings = []

        for tag in soup.find_all(["h1", "h2", "h3"]):
            text = tag.get_text(" ", strip=True)

            if text:
                headings.append((tag.name, text))

        # Extract links
        links = []

        for tag in soup.find_all("a", href=True):
            link_text = tag.get_text(" ", strip=True)
            link_url = requests.compat.urljoin(url, tag["href"])

            if link_url.startswith(("http://", "https://")):
                links.append((link_text or "No link text", link_url))

        # Display extracted information
        print("\n" + "=" * 55)
        print("             WEBSITE SCRAPER RESULTS")
        print("=" * 55)

        print(f"\nWebsite URL: {url}")
        print(f"Page Title: {title}")
        print(f"\nDescription:\n{description}")

        print("\n--- HEADINGS ---")

        if headings:
            for index, (tag, heading) in enumerate(headings, 1):
                print(f"{index}. [{tag.upper()}] {heading}")
        else:
            print("No headings found.")

        print("\n--- LINKS (First 10) ---")

        if links:
            for index, (text, link) in enumerate(links[:10], 1):
                print(f"{index}. {text}")
                print(f"   URL: {link}")
        else:
            print("No links found.")

        print("\n" + "=" * 55)
        print("Scraping completed successfully!")
        print(f"Total headings: {len(headings)}")
        print(f"Total links: {len(links)}")
        print("=" * 55)

    except requests.exceptions.Timeout:
        print("Error: Website took too long to respond.")

    except requests.exceptions.ConnectionError:
        print("Error: Unable to connect to the website.")

    except requests.exceptions.HTTPError as error:
        print(f"HTTP Error: {error}")

    except requests.exceptions.RequestException as error:
        print(f"Request Error: {error}")

    except Exception as error:
        print(f"Unexpected Error: {error}")


def main():
    while True:
        print("\n========== INTERACTIVE WEB SCRAPER ==========")
        print("1. Scrape a website")
        print("2. Exit")

        choice = input("\nEnter your choice (1-2): ").strip()

        if choice == "1":
            url = input("\nEnter website URL: ").strip()

            if not validate_url(url):
                print("Invalid URL! Enter a valid HTTP or HTTPS URL.")
                continue

            scrape_website(url)

        elif choice == "2":
            print("\nThank you for using Interactive Web Scraper!")
            break

        else:
            print("Invalid choice! Please select 1 or 2.")


if __name__ == "__main__":
    main()
