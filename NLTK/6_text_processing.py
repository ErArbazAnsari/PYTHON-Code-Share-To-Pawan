import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download VADER lexicon (if not already downloaded)
nltk.download('vader_lexicon')

# Initialize VADER sentiment analyzer
sid = SentimentIntensityAnalyzer()

# Sample text data
texts = [
    "I love this product! It's amazing.",
    "The service was terrible, very disappointed.",
    "The movie was okay, not great but not terrible either."
]

# Analyze sentiment for each text
for text in texts:
    print("Text:", text)
    # Get sentiment scores
    scores = sid.polarity_scores(text)
    # Print sentiment scores
    print("Sentiment Scores:", scores)
    # Determine sentiment label based on compound score
    if scores['compound'] >= 0.05:
        sentiment = 'Positive'
    elif scores['compound'] <= -0.05:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'
    print("Sentiment:", sentiment)
    print()  # Empty line for readability
