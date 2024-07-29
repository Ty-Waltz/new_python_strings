reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
    ]
def keywords(reviews):
    keyword_list = ["good","excellent","bad","poor","average"]
    cap_reviews = []
    
    for review in reviews:
        lower_review = review.lower()
        
        for keyword in keyword_list:
            if keyword in lower_review:
                review = review.replace(keyword,keyword.upper())

        cap_reviews.append(review)
    
    return cap_reviews

def tally_words(reviews):
    positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
    negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

    def word_count(text):
        words = text.lower().split()
        positive_count = sum(word in positive_words for word in words)
        negative_count = sum(word in negative_words for word in words)
        return positive_count, negative_count
    
    return [word_count(review) for review in reviews]

def summary(reviews):
    if len(reviews) <= 30:
        return reviews
    else:
        summary_review = reviews[:30]
        if reviews[:30] != " ":
            index = 30
            while index > 0 and reviews[index] != " ":
                index -= 1
            if index > 0:
                summary_review = reviews[:index]
                return summary_review + "..."


cap_review = keywords(reviews)
for review in cap_review:
    print(review)

#I cant figure out why the negative count is working but the positive isnt
word_count = tally_words(cap_review)
for review, counts in zip(cap_review, word_count):
    print(f"Review: {review}")
    print(f"Positive words: {counts[0]} Negative words: {counts[1]}")  
for review in reviews:
    print(summary(review))