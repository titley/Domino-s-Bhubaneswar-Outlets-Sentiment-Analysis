import pandas as pd
from textblob import TextBlob
from collections import Counter
import matplotlib.pyplot as plt
import seaborn as sns

# Load your CSV file

print ('SURYANAGAR')
df = pd.read_csv("C:/Users/HAPPY/Downloads/Domino's Bhubaneswar Reviews/SuryaNagar_Dominos.csv")
df.columns = df.columns.str.strip()
# Apply sentiment analysis
df['Polarity'] = df['Review Text'].apply(lambda x: TextBlob(str(x)).sentiment.polarity)
df['Subjectivity'] = df['Review Text'].apply(lambda x: TextBlob(str(x)).sentiment.subjectivity)
# Calculate average sentiment
print("Average Sentiment Polarity:", df['Polarity'].mean())
print("Average Sentiment Subjectivity:", df ['Subjectivity'].mean())


# Sort reviews by polarity (ascending = most negative first)
most_negative = df.sort_values(by='Polarity', ascending=True)

# Show top 10 most negative reviews
for i, row in most_negative[['Name of Reviewer', 'Review Text', 'Polarity', 'Business Response']].head(10).iterrows():
    print(f"\nReviewer: {row.get('Name of Reviewer', 'N/A')}")
    print(f"Polarity: {row.get('Polarity', 'N/A')}")
    print(f"Review Text: {str(row.get('Review Text', '')).strip()}")
    print(f"Business Response: {str(row.get('Business Response', 'No response')).strip()}")
    print("-" * 80)

print("\033[95m" + "="*80 + "\033[0m")
def sentiment_label(p):
    if p > 0.1:
        return "Positive"
    elif p < -0.1:
        return "Negative"
    else:
        return "Neutral"

df['Sentiment Category'] = df['Polarity'].apply(sentiment_label)
df['Sentiment Category'].value_counts().plot.pie(autopct='%1.1f%%', colors=['green', 'red', 'orange'])
plt.title("Review Sentiment Breakdown - SuryaNagar")
plt.ylabel('')
plt.show()

#Nextlocation

print ('RAGHUNATHPUR')

df = pd.read_csv(r"C:\Users\HAPPY\Downloads\Domino's Bhubaneswar Reviews\Raghunathpur.csv")
df.columns = df.columns.str.strip()
# Apply sentiment analysis
df['Polarity'] = df['Review Text'].apply(lambda x: TextBlob(str(x)).sentiment.polarity)
df['Subjectivity'] = df['Review Text'].apply(lambda x: TextBlob(str(x)).sentiment.subjectivity)
# Calculate average sentiment
print("Average Sentiment Polarity:", df['Polarity'].mean())
print("Average Sentiment Subjectivity:", df ['Subjectivity'].mean())


# Sort reviews by polarity (ascending = most negative first)
most_negative = df.sort_values(by='Polarity', ascending=True)

# Show top 10 most negative reviews
for i, row in most_negative[['Name of Reviewer', 'Review Text', 'Polarity', 'Business Response']].head(10).iterrows():
    print(f"\nReviewer: {row.get('Name of Reviewer', 'N/A')}")
    print(f"Polarity: {row.get('Polarity', 'N/A')}")
    print(f"Review Text: {str(row.get('Review Text', '')).strip()}")
    print(f"Business Response: {str(row.get('Business Response', 'No response')).strip()}")
    print("-" * 80)

print("\033[95m" + "="*80 + "\033[0m")
print("\033[95m" + "="*80 + "\033[0m")
def sentiment_label(p):
    if p > 0.1:
        return "Positive"
    elif p < -0.1:
        return "Negative"
    else:
        return "Neutral"

df['Sentiment Category'] = df['Polarity'].apply(sentiment_label)
df['Sentiment Category'].value_counts().plot.pie(autopct='%1.1f%%', colors=['green', 'red', 'orange'])
plt.title("Review Sentiment Breakdown - Raghunathpur")
plt.ylabel('')
plt.show()

#NextLocation
print ("Chandrasekharpur")

df = pd.read_csv(r"C:\Users\HAPPY\Downloads\Domino's Bhubaneswar Reviews\Chandrasekharpur.csv")
df.columns = df.columns.str.strip()
# Apply sentiment analysis
df['Polarity'] = df['Review Text'].apply(lambda x: TextBlob(str(x)).sentiment.polarity)
df['Subjectivity'] = df['Review Text'].apply(lambda x: TextBlob(str(x)).sentiment.subjectivity)
# Calculate average sentiment
print("Average Sentiment Polarity:", df['Polarity'].mean())
print("Average Sentiment Subjectivity:", df ['Subjectivity'].mean())


# Sort reviews by polarity (ascending = most negative first)
most_negative = df.sort_values(by='Polarity', ascending=True)

# Show top 10 most negative reviews
for i, row in most_negative[['Name of Reviewer', 'Review Text', 'Polarity', 'Business Response']].head(10).iterrows():
    print(f"\nReviewer: {row.get('Name of Reviewer', 'N/A')}")
    print(f"Polarity: {row.get('Polarity', 'N/A')}")
    print(f"Review Text: {str(row.get('Review Text', '')).strip()}")
    print(f"Business Response: {str(row.get('Business Response', 'No response')).strip()}")
    print("-" * 80)

print("\033[95m" + "="*80 + "\033[0m")

#NextLocation
print ("Shaheed Nagar")

df = pd.read_csv(r"C:\Users\HAPPY\Downloads\Domino's Bhubaneswar Reviews\Shaheed Nagar- Dom.csv")
df.columns = df.columns.str.strip()
# Apply sentiment analysis
df['Polarity'] = df['Review Text'].apply(lambda x: TextBlob(str(x)).sentiment.polarity)
df['Subjectivity'] = df['Review Text'].apply(lambda x: TextBlob(str(x)).sentiment.subjectivity)
# Calculate average sentiment
print("Average Sentiment Polarity:", df['Polarity'].mean())
print("Average Sentiment Subjectivity:", df ['Subjectivity'].mean())


# Sort reviews by polarity (ascending = most negative first)
most_negative = df.sort_values(by='Polarity', ascending=True)

# Show top 10 most negative reviews
for i, row in most_negative[['Name of Reviewer', 'Review Text', 'Polarity', 'Business Response']].head(10).iterrows():
    print(f"\nReviewer: {row.get('Name of Reviewer', 'N/A')}")
    print(f"Polarity: {row.get('Polarity', 'N/A')}")
    print(f"Review Text: {str(row.get('Review Text', '')).strip()}")
    print(f"Business Response: {str(row.get('Business Response', 'No response')).strip()}")
    print("-" * 80)

print("\033[95m" + "="*80 + "\033[0m")


#NextLocation
print ("Janpath")

df = pd.read_csv(r"C:\Users\HAPPY\Downloads\Domino's Bhubaneswar Reviews\Janpath-Dominos.csv")
df.columns = df.columns.str.strip()
# Apply sentiment analysis
df['Polarity'] = df['Review Text'].apply(lambda x: TextBlob(str(x)).sentiment.polarity)
df['Subjectivity'] = df['Review Text'].apply(lambda x: TextBlob(str(x)).sentiment.subjectivity)
# Calculate average sentiment
print("Average Sentiment Polarity:", df['Polarity'].mean())
print("Average Sentiment Subjectivity:", df ['Subjectivity'].mean())


# Sort reviews by polarity (ascending = most negative first)
most_negative = df.sort_values(by='Polarity', ascending=True)

# Show top 10 most negative reviews
for i, row in most_negative[['Name of Reviewer', 'Review Text', 'Polarity', 'Business Response']].head(10).iterrows():
    print(f"\nReviewer: {row.get('Name of Reviewer', 'N/A')}")
    print(f"Polarity: {row.get('Polarity', 'N/A')}")
    print(f"Review Text: {str(row.get('Review Text', '')).strip()}")
    print(f"Business Response: {str(row.get('Business Response', 'No response')).strip()}")
    print("-" * 80)

print("\033[95m" + "="*80 + "\033[0m")

#NextLocation

print ("Samantharapur")

df = pd.read_csv(r"C:\Users\HAPPY\Downloads\Domino's Bhubaneswar Reviews\Samantarapur - Domino's.csv")
df.columns = df.columns.str.strip()
# Apply sentiment analysis
df['Polarity'] = df['Review Text'].apply(lambda x: TextBlob(str(x)).sentiment.polarity)
df['Subjectivity'] = df['Review Text'].apply(lambda x: TextBlob(str(x)).sentiment.subjectivity)
# Calculate average sentiment
print("Average Sentiment Polarity:", df['Polarity'].mean())
print("Average Sentiment Subjectivity:", df ['Subjectivity'].mean())


# Sort reviews by polarity (ascending = most negative first)
most_negative = df.sort_values(by='Polarity', ascending=True)

# Show top 10 most negative reviews
for i, row in most_negative[['Name of Reviewer', 'Review Text', 'Polarity', 'Business Response']].head(10).iterrows():
    print(f"\nReviewer: {row.get('Name of Reviewer', 'N/A')}")
    print(f"Polarity: {row.get('Polarity', 'N/A')}")
    print(f"Review Text: {str(row.get('Review Text', '')).strip()}")
    print(f"Business Response: {str(row.get('Business Response', 'No response')).strip()}")
    print("-" * 80)

print("\033[95m" + "="*80 + "\033[0m")

#NextLocation

print ("Jaydev")

df = pd.read_csv(r"C:\Users\HAPPY\Downloads\Domino's Bhubaneswar Reviews\Jaidev.csv")
df.columns = df.columns.str.strip()
# Apply sentiment analysis
df['Polarity'] = df['Review Text'].apply(lambda x: TextBlob(str(x)).sentiment.polarity)
df['Subjectivity'] = df['Review Text'].apply(lambda x: TextBlob(str(x)).sentiment.subjectivity)
# Calculate average sentiment
print("Average Sentiment Polarity:", df['Polarity'].mean())
print("Average Sentiment Subjectivity:", df ['Subjectivity'].mean())


# Sort reviews by polarity (ascending = most negative first)
most_negative = df.sort_values(by='Polarity', ascending=True)

# Show top 10 most negative reviews
for i, row in most_negative[['Name of Reviewer', 'Review Text', 'Polarity', 'Business Response']].head(10).iterrows():
    print(f"\nReviewer: {row.get('Name of Reviewer', 'N/A')}")
    print(f"Polarity: {row.get('Polarity', 'N/A')}")
    print(f"Review Text: {str(row.get('Review Text', '')).strip()}")
    print(f"Business Response: {str(row.get('Business Response', 'No response')).strip()}")
    print("-" * 80)

print("\033[95m" + "="*80 + "\033[0m")

print ("Baramunda")

df = pd.read_csv(r"C:\Users\HAPPY\Downloads\Domino's Bhubaneswar Reviews\BaramundaDom.csv")
df.columns = df.columns.str.strip()
# Apply sentiment analysis
df['Polarity'] = df['Review Text'].apply(lambda x: TextBlob(str(x)).sentiment.polarity)
df['Subjectivity'] = df['Review Text'].apply(lambda x: TextBlob(str(x)).sentiment.subjectivity)
# Calculate average sentiment
print("Average Sentiment Polarity:", df['Polarity'].mean())
print("Average Sentiment Subjectivity:", df ['Subjectivity'].mean())


# Sort reviews by polarity (ascending = most negative first)
most_negative = df.sort_values(by='Polarity', ascending=True)

# Show top 10 most negative reviews
for i, row in most_negative[['Name of Reviewer', 'Review Text', 'Polarity', 'Business Response']].head(10).iterrows():
    print(f"\nReviewer: {row.get('Name of Reviewer', 'N/A')}")
    print(f"Polarity: {row.get('Polarity', 'N/A')}")
    print(f"Review Text: {str(row.get('Review Text', '')).strip()}")
    print(f"Business Response: {str(row.get('Business Response', 'No response')).strip()}")
    print("-" * 80)

print("\033[95m" + "="*80 + "\033[0m")















