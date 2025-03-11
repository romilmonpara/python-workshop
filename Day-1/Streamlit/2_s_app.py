import streamlit as st
from transformers import pipeline
import pandas as pd

# Set up the page configuration
st.set_page_config(page_title="Real-Time Sentiment Analysis", layout="wide")
st.title("Real-Time Sentiment Analysis with Interactive Charts")
st.write('''
Enter multiple sentences below (one per line), and adjust the confidence threshold to see how 
the sentiment distribution changes in real time!
''')

# Cache the sentiment analysis model
@st.cache_resource
def load_sentiment_model():
    return pipeline("sentiment-analysis")

# Load model
sentiment_model = load_sentiment_model()

# Sidebar for confidence threshold
threshold = st.sidebar.slider(
    "Confidence Threshold",
    min_value=0.0,
    max_value=1.0,
    value=0.5,
    step=0.1,
    help="Any sentiment score below this is labeled 'UNDECIDED'."
)

# Text input area
user_text = st.text_area(
    "Enter text (one sentence per line):",
    height=200,
    placeholder="Example:\nI love building apps with Streamlit!\nSometimes coding is tough but rewarding."
)

if user_text:
    lines = [line.strip() for line in user_text.split("\n") if line.strip()]
    
    results = sentiment_model(lines)  # Use the correct variable

    data = []
    for sentence, result in zip(lines, results):
        label = result["label"]
        score = result["score"]

        if score < threshold:
            label = "UNDECIDED"  # Fix typo

        data.append({
            "Sentence": sentence,
            "Label": label,  # Fix variable assignment
            "Confidence": score
        })

    df = pd.DataFrame(data)
    st.write("Detailed Results")
    st.dataframe(df)

    # Compute label distribution
    label_counts = df["Label"].value_counts().reset_index()
    label_counts.columns = ["Label", "Count"]  # Fix column naming

    st.write("LABEL DISTRIBUTION")
    st.bar_chart(label_counts, x="Label", y="Count")  # Fix incorrect variable reference
else:
    st.write("Please enter some text.")