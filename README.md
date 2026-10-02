\# 🎬 Movie Recommendation System



A content-based movie recommendation system built with Python and Scikit-learn. The application recommends movies similar to a selected movie based on movie metadata such as genres, cast, crew, keywords, and overview.



The recommendation engine is integrated with a Streamlit interface and the TMDB API to display movie posters.



\## 🚀 Features



\- 🎥 Content-based movie recommendations

\- 🔍 Select a movie from the available dataset

\- 🤖 Cosine similarity for finding similar movies

\- 🧮 CountVectorizer for text feature extraction

\- 🖼️ TMDB API integration for movie posters

\- 🌐 Interactive Streamlit web interface

\- 📦 Precomputed recommendation data stored using Pickle



\## 🛠️ Technologies Used



\- Python

\- Pandas

\- NumPy

\- Scikit-learn

\- Streamlit

\- Requests

\- TMDB API

\- Git \& Git LFS



\## 🧠 How It Works



1\. Movie metadata is loaded and processed.

2\. Relevant movie information is combined into a `tags` feature.

3\. `CountVectorizer` converts the text data into numerical vectors.

4\. Cosine similarity calculates similarity between movies.

5\. The system finds the most similar movies.

6\. The TMDB API retrieves movie poster information.

7\. Recommendations are displayed through Streamlit.



\## 📂 Project Structure



```text

movie-recommender-system/

│

├── model/

│   ├── movie\_list.pkl

│   └── similarity.pkl

│

├── app.py

├── movie\_recommender.ipynb

├── requirements.txt

├── .gitignore

└── .gitattributes

