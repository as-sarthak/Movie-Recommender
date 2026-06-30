# 🎬 Movie Recommender System

A content-based movie recommendation web app built with **Python**, **Streamlit**, and **The Movie Database (TMDB) API**. Select any movie and get 5 similar movie recommendations along with their posters.

## 🚀 Live Demo

[Add your deployed Streamlit app link here once deployed]

## 📌 Features

- Content-based filtering using cosine similarity
- Fetches real-time movie posters via TMDB API
- Clean, simple Streamlit UI
- Handles large similarity matrix via Google Drive (no GitHub file size limits)

## 🛠️ Tech Stack

- **Python**
- **Streamlit** — web app framework
- **Pandas** — data handling
- **Scikit-learn** — cosine similarity (used during model building)
- **TMDB API** — movie posters and metadata
- **gdown** — downloading large model files from Google Drive at runtime

## 📂 Project Structure

```
movie-recommender/
├── app.py              # Main Streamlit application
├── movie_dict.pkl       # Preprocessed movie metadata
├── requirements.txt     # Python dependencies
└── README.md             # Project documentation
```

> **Note:** `similarity.pkl` (~176 MB) is not stored in this repository due to GitHub's file size limits. It is automatically downloaded from Google Drive when the app runs for the first time, using `gdown`.

## ⚙️ How It Works

1. The app loads a preprocessed dataset (`movie_dict.pkl`) containing movie titles and IDs.
2. A precomputed cosine similarity matrix (`similarity.pkl`) is downloaded from Google Drive at runtime.
3. When a user selects a movie, the app finds the 5 most similar movies based on the similarity matrix.
4. Movie posters are fetched live from the TMDB API.

## 🖥️ Run Locally

1. Clone the repository
   ```bash
   git clone https://github.com/YOUR_USERNAME/movie-recommender.git
   cd movie-recommender
   ```

2. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app
   ```bash
   streamlit run app.py
   ```

The app will automatically download `similarity.pkl` from Google Drive on first run.

## ☁️ Deployment (Streamlit Community Cloud)

1. Push this repository to GitHub (without `similarity.pkl`)
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Sign in with GitHub
4. Click **New app**, select this repository and branch
5. Set the main file path to `app.py`
6. Click **Deploy**

The first load will take 1–2 minutes as the app downloads the similarity matrix from Google Drive. Subsequent loads are cached and fast.

## 🔑 API Key Note

This project uses TMDB's free API for fetching movie posters. You can get your own API key at [themoviedb.org](https://www.themoviedb.org/settings/api) and replace the `API_KEY` variable in `app.py`.

## 📜 License

This project is open source and available for personal and educational use.
