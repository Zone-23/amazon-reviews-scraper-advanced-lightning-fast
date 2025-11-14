thonpython
import logging
import random
import time
from typing import List, Dict
from .utils_filters import filter_reviews

class AmazonReviewParser:
    def __init__(self, settings: dict):
        self.settings = settings

    def mock_fetch_page(self, asin: str, page: int) -> List[Dict]:
        """Simulated review fetcher."""
        time.sleep(0.1)
        return [
            {
                "reviewId": f"R{random.randint(100000, 999999)}",
                "reviewUrl": f"https://www.amazon.com/review/{asin}/{page}",
                "rating": random.choice([3,4,5]),
                "reviewer": random.choice(["Alice","Bob","Charlie","Dana"]),
                "title": f"Sample Review {page}",
                "date": "2025-03-28",
                "reviewedIn": "United States",
                "body": "Sample review text content.",
                "verifiedPurchase": random.choice([True, False]),
                "userImage": "",
                "reviewImages": [],
                "position": page,
                "variantDetails": ["Size: Medium"],
                "variantASIN": asin,
                "helpfulCounts": random.randint(0,15),
                "videoUrl": ""
            }
            for _ in range(3)
        ]

    def scrape_reviews(self, asin: str) -> List[Dict]:
        pages = self.settings.get("pagesToScrape", 3)
        collected = []

        for p in range(1, pages + 1):
            logging.info(f"Fetching page {p} for ASIN {asin}")
            page_reviews = self.mock_fetch_page(asin, p)
            filtered = filter_reviews(page_reviews, self.settings)
            collected.extend(filtered)

        # Remove duplicates by id
        unique = {r["reviewId"]: r for r in collected}
        return list(unique.values())