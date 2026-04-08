import streamlit as st
import pickle
import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

# Load model
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# Text cleaning function (same as training)
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z]', ' ', text)
    words = text.split()
    words = [w for w in words if w not in stop_words]
    return " ".join(words)

# Page config
st.set_page_config(page_title="Fake News Detector", page_icon="📰")

# Title
st.title("📰 Fake News Detector")
st.markdown("Detect whether a news article is **Fake or Real** using Machine Learning.")


# Input
input_text = st.text_area("✍️ Enter news text here:")
if len(input_text.split()) < 20:
        st.warning("Please enter a longer news article for better prediction.")


# Button
if st.button("🔍 Analyze"):
    if input_text.strip() == "":
        st.warning("Please enter some text to analyze.")
    else:
        # ✅ CLEAN TEXT BEFORE PREDICTION
        cleaned = clean_text(input_text)

        transformed_text = vectorizer.transform([cleaned])
        prediction = model.predict(transformed_text)
    
        st.subheader("Result:")

        if prediction[0] == 0:
            st.error("🚨 This looks like Fake News")
        else:
            st.success("✅ This appears to be Real News")

# Footer
st.markdown("---")
st.caption("Built with Streamlit | NLP Project")