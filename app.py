import json
from feeds import FEEDS
from flask import Flask, render_template, request, url_for, flash, redirect
import sqlite3
import os
import threading
from db_utils import create_tables, DB_PATH, get_connection


app = Flask(__name__)
create_tables()


def load_cached_news():
    conn = get_connection()
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("SELECT * FROM articles")
    rows = c.fetchall()
    conn.close()
    return [dict(row) for row in rows]

@app.route("/")
def home():
    region = request.args.get("region")
    country = request.args.get("country")


    articles = load_cached_news()
    if region:
        articles = [a for a in articles if a["region"] == region]
    if country:
        articles = [a for a in articles if a["country"] == country]


    regions = sorted(set(feed["region"] for feed in FEEDS))
    countries = sorted(set(feed["country"] for feed in FEEDS))


    return render_template(
        "news.html",
        articles=articles,
        regions=regions,
        countries=countries,
        selected_region=region,
        selected_country=country,
        )

@app.route("/refresh")
def refresh():
    def fetch_news():
        try:
            import fetch_and_cache_news
            fetch_and_cache_news.fetch_and_cache()
        except Exception as e:
            print(f"Error in background fetch: {e}")

    thread = threading.Thread(target=fetch_news)
    thread.start()
    flash("News refresh started in background!", "info")
    return redirect(url_for("home"))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
