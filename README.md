# 📚 Book Recommendation System

A machine learning–powered Book Recommendation System with two main features:

- **Popularity-Based Recommendations:** Discover trending books loved by many readers.
- **Collaborative Filtering:** Get personalized book suggestions based on your favorite reads.

🌐 **Live Demo:** [Book Recommender on Render](https://book-recommender-t58c.onrender.com/)  

---

## 🚀 Features

### 🏠 Home Page – Popularity-Based
- Displays the **Top 50 Most Popular Books**.
- Ranks books based on **average ratings** and **number of ratings**.
- Helps users quickly explore trending and highly rated books.

### 🔍 Recommendation Page – Collaborative Filtering
- Enter the name of a book you like.
- The system recommends **5 similar books** using collaborative filtering.
- Uses similarity algorithms (e.g., **Cosine Similarity**, **KNN**) to analyze user preferences.

---

## ⚙️ How It Works

### Data Processing
- Preprocessed dataset of books, ratings, and user interactions.
- Cleaned data stored as `.pkl` files for faster access.

### Popularity Model
- Books ranked by average rating and number of ratings.

### Collaborative Filtering
- Finds similar books using similarity scores.
- Provides personalized recommendations.

### User Interface
- Simple and interactive web interface.

---

## 🛠 Tech Stack

- **Python:** Pandas, NumPy, Scikit-learn
- **Flask:** Web app framework (served on Render)
- **Pickle:** To store preprocessed models/data
- **HTML/CSS:** For frontend styling

---

## ▶️ Run Locally

### Clone the repository:
```bash
git clone https://github.com/ADITHICJ/Book-Recommender.git
cd Book-Recommender
```

### Create a virtual environment and install dependencies:
```bash
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Run the app
```bash
python app.py
```

### Open in your browser
```
http://127.0.0.1:5000
```

---

## 📊 Example Screens

- **Home Page:** Displays top 50 trending books.
- **Recommendation Page:** Enter a favorite book to view personalized suggestions.

---

## 💡 Outcome

This project demonstrates how data-driven approaches can enhance user experience by providing recommendations similar to those on platforms like Goodreads or Amazon.

---

## 📚 References

- [Pandas Documentation](https://pandas.pydata.org/)
- [Scikit-learn Documentation](https://scikit-learn.org/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [NumPy Documentation](https://numpy.org/)


---

**Developed by [ADITHICJ](https://github.com/ADITHICJ)**
