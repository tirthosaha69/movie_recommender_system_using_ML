# 🎬 Movie Recommender System

A content-based Movie Recommender System built using Python and Flask. Enter a movie name and instantly get 20 similar movie recommendations based on their textual metadata.

## 🚀 Features
- Input any movie name and get 20 similar movies.
- Simple and responsive web interface using Flask.
- Built using cosine similarity on movie metadata.

## 🧠 How It Works
- Extracts features like genres, cast, keywords, and crew.
- Uses `sklearn`'s `CountVectorizer` and `cosine_similarity` to compute similarity scores.
- Returns top 20 most similar movies.

## 🛠 Tech Stack
- Python
- Pandas, Scikit-learn
- Flask
- HTML/CSS

## 📁 Project Structure
```

├── app.py
├── movie\_recommender.py
├── templates/
│   └── index.html
├── static/
│   └── style.css (optional)
├── movies.csv (or your dataset)
└── README.md

````

## ⚙️ How to Run Locally

1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/movie-recommender.git
   cd movie-recommender
````

2. Install dependencies:

   ```bash
   pip install flask pandas scikit-learn
   ```

3. Run the app:

   ```bash
   python app.py
   ```

4. Open your browser and visit:
   `http://127.0.0.1:5000`

## 📷 Screenshots

> Add the screenshots of your web app here.

## 📌 To-Do

* [ ] Deploy on Render/Heroku
* [ ] Add movie posters using TMDb API
* [ ] Add popularity/rating filter

## 💡 Inspiration

This project is inspired by the content-based filtering technique and aims to demonstrate a simple recommendation engine in action.

## 📝 License

This project is open-source under the MIT License.