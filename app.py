from flask import Flask, render_template, request
from movie_recommender import recommend

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    recommendations = []
    movie_name = ""

    if request.method == 'POST':
        movie_name = request.form['movie']
        recommendations = recommend(movie_name)

    return render_template('index.html', recommendations=recommendations, movie_name=movie_name)

if __name__ == '__main__':
    app.run(debug=True)
