# 🎬 Movie Recommender System using Machine Learning

A **content-based movie recommender system** built using **Python** and **Flask**. Just enter a movie name and get 20 similar recommendations based on metadata such as genres, cast, crew, and keywords.

---

## 🚀 Features

- 🔍 Input any movie title and get **20 similar movie recommendations**
- 🖥️ User-friendly web interface built with **Flask**
- ⚙️ Backend logic powered by **cosine similarity**
- 💾 Movie data handled via CSV file

---

## 🧠 How It Works

1. **Preprocessing**:
   - Loads metadata like `genres`, `cast`, `crew`, `keywords` from the dataset
   - Combines them into a single feature called `tags`

2. **Vectorization**:
   - Applies `CountVectorizer` to transform text data into numerical vectors

3. **Similarity Matching**:
   - Uses `cosine_similarity` to find the most relevant movies

4. **Returns**:
   - Top 20 movies sorted by similarity score

---

## 🛠️ Tech Stack

- **Python 3**
- **Flask** – web app framework
- **Pandas, Scikit-learn** – data handling and ML
- **HTML/CSS** – frontend interface

---

## 📁 Project Structure

```bash
movie_recommender_system_using_ML/
│
├── app.py                        # Flask app entry point
├── Movie_recommender.ipynb       # Jupyter notebook (exploration)
├── movie_recommender.py          # Core recommendation logic
├── requirements.txt              # Python dependencies
├── README.md                     # Project documentation
│
├── csv/
│   └── movie.csv                 # Movie dataset
│
├── templates/
│   └── index.html                # Web interface (HTML)
│
└── __pycache__/, .vscode/        # Cache and editor configs
````

---

## ⚙️ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/tirthosaha69/movie_recommender_system_using_ML.git
cd movie_recommender_system_using_ML
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

> Or install manually:

```bash
pip install flask pandas scikit-learn
```

### 3. Run the Flask App

```bash
python app.py
```

### 4. Open in browser

```
http://127.0.0.1:5000
```

---

## 📸 Screenshots

> Add screenshots of your working application here (homepage, recommendations, etc.)

---

## 📌 To-Do

* [ ] 🚀 Deploy on Render/Heroku
* [ ] 🎞️ Add movie posters using TMDb API
* [ ] ⭐ Add filters for popularity or rating

---

## 💡 Inspiration

Inspired by the concept of **content-based filtering** in recommendation engines, this project showcases a simplified ML-driven app to recommend movies based on textual similarity.

---

## 📝 License

This project is licensed under the **MIT License** – feel free to use and improve it!
