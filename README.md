# 🎬 Movie Recommendation System

A content-based Movie Recommendation System built using **Python, Flask, Machine Learning, and TMDB API**. The application recommends movies similar to the one selected by the user and displays their posters in an interactive web interface.

🌐 **Live Demo:** https://movie-recommendation-system-1dar.onrender.com


---

## 📖 Overview

Finding movies that match your interests can be overwhelming with thousands of options available. This project solves that problem by recommending movies based on their content rather than user ratings.

The recommendation engine analyzes movie metadata such as:

- Genres
- Keywords
- Cast
- Crew
- Overview

These features are combined into textual representations and transformed using Natural Language Processing techniques. The similarity between movies is then computed using **Cosine Similarity**, allowing the system to recommend movies with similar characteristics.

The web application is built with **Flask** and retrieves movie posters dynamically from **The Movie Database (TMDB) API**.

---

## 🚀 Live Demo

🔗 **Application:**  
https://movie-recommendation-system-1dar.onrender.com

---

## ✨ Features

- 🎥 Content-Based Movie Recommendation
- 🎬 Displays movie posters using TMDB API
- 🔍 Search and select movies from the dataset
- ⚡ Fast recommendations using precomputed similarity matrix
- 🌐 Flask-based web application
- 📱 Responsive web interface
- 🚀 Deployed on Render

---

## 🛠 Tech Stack

### Backend
- Python
- Flask

### Machine Learning
- Pandas
- NumPy
- Scikit-learn

### Frontend
- HTML5
- CSS3
- JavaScript

### APIs
- TMDB (The Movie Database)

### Deployment
- Render

---

## 📊 Dataset

The project uses the following Kaggle datasets:

- TMDB 5000 Movies Dataset
- TMDB 5000 Credits Dataset

These datasets include:

- Movie titles
- Genres
- Keywords
- Cast
- Crew
- Overview
- Movie IDs

---

## ⚙️ Machine Learning Pipeline

The recommendation engine follows these steps:

1. Load movie and credits datasets
2. Merge datasets
3. Perform data preprocessing
4. Extract important textual features:
   - Genres
   - Keywords
   - Cast
   - Crew
   - Overview
5. Create a combined "tags" column
6. Text preprocessing
7. Vectorize text using **CountVectorizer**
8. Compute movie similarity using **Cosine Similarity**
9. Save processed data using Pickle
10. Serve recommendations through Flask

---

## 📂 Project Structure

```text
Movie_Recommendation_System/
│
├── app.py
├── recommend.py
├── requirements.txt
│
├── models/
│   ├── movie_list.pkl
│   └── similarity.pkl
│
├── data/
│   ├── tmdb_5000_movies.csv
│   └── tmdb_5000_credits.csv
│
├── notebooks/
│   └── movie-recommender.ipynb
│
├── templates/
│   └── index.html
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
└── README.md
```

---

## ⚡ Installation

### Clone the repository

```bash
git clone https://github.com/Pardhiv-07/Movie_Recommendation_System.git
```

### Navigate to the project

```bash
cd Movie_Recommendation_System
```

### Create a virtual environment

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the Flask application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```



---

## 🔮 Future Improvements

- Movie search autocomplete
- User authentication
- Favorite movies list
- Movie trailers
- Similar genres filtering
- IMDb ratings
- Streaming platform availability
- Collaborative Filtering
- Hybrid Recommendation System
- Recommendation explanations

---

## 📈 Learning Outcomes

This project helped me gain practical experience with:

- Machine Learning workflows
- NLP-based feature engineering
- Cosine Similarity
- Flask web development
- REST API integration
- Frontend-backend integration
- Model deployment
- Git & GitHub
- Render deployment

---

## 🤝 Contributing

Contributions are welcome.

If you'd like to improve the project:

1. Fork the repository
2. Create a new branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Added new feature"
```

4. Push to GitHub

```bash
git push origin feature-name
```

5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Sai Charan Chonga**

GitHub:
https://github.com/Pardhiv-07


---

⭐ If you found this project useful, consider giving it a **Star** on GitHub!
