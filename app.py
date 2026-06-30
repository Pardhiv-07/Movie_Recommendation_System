from flask import Flask, render_template, request

# Import our custom functions from recommend.py
from recommend import get_recommendations, get_movie_list

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    # Grab the list of movies for the dropdown
    movie_list = get_movie_list()
    recommendations = []
    selected_movie = ""

    # If the user submitted the form
    if request.method == 'POST':
        selected_movie = request.form.get('selected_movie')
        if selected_movie:
            # Trigger the engine
            recommendations = get_recommendations(selected_movie)

    # Render the frontend, passing along our variables
    return render_template(
        'index.html',
        movie_list=movie_list,
        recommendations=recommendations,
        selected_movie=selected_movie
    )


if __name__ == '__main__':
    app.run(debug=True)