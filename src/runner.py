thonpython
import json
import logging
from pathlib import Path
from extractors.amazon_parser import AmazonReviewParser
from outputs.exporters import Exporter

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

def load_settings():
    config_path = Path(__file__).parent / "config" / "settings.example.json"
    with open(config_path, "r", encoding="utf-8") as f:
        return json.load(f)

def load_inputs():
    inputs_path = Path(__file__).resolve().parents[1] / "data" / "inputs.sample.txt"
    with open(inputs_path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

def main():
    settings = load_settings()
    asin_list = load_inputs()

    parser = AmazonReviewParser(settings=settings)
    all_reviews = []

    for asin in asin_list:
        logging.info(f"Scraping ASIN: {asin}")
        reviews = parser.scrape_reviews(asin)
        all_reviews.extend(reviews)

    if not all_reviews:
        logging.warning("No reviews collected.")
        return

    exporter = Exporter()
    out_path = Path(__file__).resolve().parents[1] / "data" / "sample.json"
    exporter.export_json(all_reviews, out_path)

    logging.info(f"Export complete: {out_path}")

if __name__ == "__main__":
    main()