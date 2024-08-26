reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]

keywords = ["good", "excellent", "bad", "poor", "average"]

for review in reviews:
    for keyword in keywords:
        review = review.replace(keyword, keyword.upper())

    print(review)

#2
reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]

keywords = ["good", "excellent", "bad", "poor", "average"]
positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

def capitalize_keywords(reviews, keywords):
    print("Capitalized Reviews:")
    for review in reviews:
        for keyword in keywords:
            review = review.replace(keyword, keyword.upper())
        print(review)
    print("\n" + "-"*50 + "\n")

def sentiment_tally(reviews, positive_words, negative_words):
    total_positive_count = 0
    total_negative_count = 0

    for review in reviews:
        review_lower = review.lower()

        positive_amount = sum(review_lower.count(word) for word in positive_words)
        total_positive_count += positive_amount

        negative_amount = sum(review_lower.count(word) for word in negative_words)
        total_negative_count += negative_amount

        print(f"Review: {review}")
        print(f"Positive words: {positive_amount}, Negative words: {negative_amount}")
        print("-" * 50)

    return total_positive_count, total_negative_count  

capitalize_keywords(reviews, keywords)
    
total_positive, total_negative = sentiment_tally(reviews, positive_words, negative_words)
    
print(f"Total Positive Words: {total_positive}")
print(f"Total Negative Words: {total_negative}")

#3
reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]

def create_summary(review, max_length=30):

    if len(review) <= max_length:
        return review 
     
    end_pos = review.rfind(' ', 0, max_length)

    if end_pos == -1:
        end_pos = max_length

    summary = review[:end_pos].strip() + "…"
    return summary

def print_review_summaries(reviews):
    print("Review Summaries:")
    for review in reviews:
        summary = create_summary(review)
        print(summary)

print_review_summaries(reviews)

