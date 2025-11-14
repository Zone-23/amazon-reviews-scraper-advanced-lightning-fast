thonpython
def filter_reviews(reviews, settings):
    """Apply simple filters."""
    min_rating = settings.get("minRating", 1)
    verified_only = settings.get("verifiedOnly", False)

    result = []
    for r in reviews:
        if r["rating"] < min_rating:
            continue
        if verified_only and not r["verifiedPurchase"]:
            continue
        result.append(r)
    return result