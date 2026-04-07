import streamlit as st
import pickle

# Load model

model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# Page config
st.set_page_config(page_title="Fake News Detector", page_icon="📰")

# Title
st.title("📰 Fake News Detector")
st.markdown("Detect whether a news article is **Fake or Real** using Machine Learning.")

# Input box
input_text = st.text_area("✍️ Enter news text here:")

# Button
if st.button("🔍 Analyze"):
    if input_text.strip() == "":
        st.warning("Please enter some text to analyze.")
    else:
        transformed_text = vectorizer.transform([input_text])
        prediction = model.predict(transformed_text)

        st.subheader("Result:")

        if prediction[0] == 0:
            st.error("🚨 This looks like Fake News")
        else:
            st.success("✅ This appears to be Real News")

# Footer
st.markdown("---")
st.caption("Built with Streamlit | NLP Project")
if st.button("Try Sample Fake News"):
    st.write("Breaking: Secret government plan revealed...")

if st.button("Try Sample Real News"):
    st.write("The government announced new economic policies today...")
