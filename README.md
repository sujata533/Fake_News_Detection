🔍 Overview

This project is an end-to-end Machine Learning + NLP web application that classifies news articles as Fake or Real based on text content.

It includes:

Data preprocessing
Feature engineering (TF-IDF)
Model training
Evaluation
Web deployment using Streamlit

🎯 Objective

To detect misinformation in news articles using Natural Language Processing and supervised machine learning.

📊 Dataset

Fake & Real News Dataset (Kaggle)

Contains labeled news articles:

Fake (0)

Real (1)

⚙️ ML Pipeline

Data → Cleaning → EDA → TF-IDF → Model Training → Evaluation → Deployment

🧠 Models Used

Logistic Regression (Best Performance)

Multinomial Naive Bayes

📈 Performance


| Model               | Accuracy |
| ------------------- | -------- |
| Logistic Regression | XX%      |
| Naive Bayes         | XX%      |


🧹 Text Processing Steps

Lowercasing

Removing punctuation

Removing stopwords

Tokenization

📦 Tech Stack

Python

Scikit-learn

Pandas

NLTK

Streamlit

💡 Key Learnings

NLP preprocessing pipeline

Feature extraction using TF-IDF

Model evaluation metrics

Deployment using Streamlit

🔮 Future Improvements

Add BERT-based classification

Improve accuracy with deep learning

Add confidence score

Deploy on cloud permanently
