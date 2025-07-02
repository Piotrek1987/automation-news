Global News Digest

A simple Python Flask web app that aggregates and displays news articles from various RSS feeds worldwide. It supports filtering by region and country, and allows manual or scheduled refreshing of news.

Features:
- Fetches news from multiple global sources using RSS feeds.
- Filters news by region and country.
- Refresh news manually or automatically every day at 7 AM.
- Uses SQLite to store news articles locally.
- User-friendly interface styled with Bootstrap.


Getting Started

Prerequisites: Python 3.7+ and Git.

Installation:

1. Clone the repository:
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name

2. Create a virtual environment and activate it:
    python -m venv venv
    source venv/bin/activate (On Windows: venv\Scripts\activate)

3 Install dependencies:
    pip install -r requirements.txt

4. Run the app locally:
    python app.py
    Then open http://127.0.0.1:5000/ in your browser.

Usage:
- Use the dropdown filters on the homepage to filter news by region and country.
- Click the Refresh Now button to fetch the latest news manually.
- News automatically refreshes every day at 7 AM if deployed with the scheduler.

Deployment:
- Ready to deploy on platforms like Render or Heroku.
- Set environment variables and scheduled jobs as needed.
- SQLite database file (news.db) is excluded from version control; it will be created on deployment.


Project Structure:
- app.py: Main Flask application.
- feeds.py: RSS feed URLs and helper functions.
- fetch_and_cache_news.py: Script to fetch news and update the database.
- templates/: HTML templates.
- news.db: SQLite database file (ignored in Git).
- requirements.txt: Python dependencies.

License:

This project is licensed under the MIT License.

Feel free to contribute or raise issues!

Created by Piotrek1987
