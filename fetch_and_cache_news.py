import feedparser
import time
from feeds import FEEDS, is_relevant, detect_topic
from db_utils import get_connection, create_tables
import requests

def clear_articles():
    conn = get_connection()
    c = conn.cursor()
    c.execute("DELETE FROM articles")
    conn.commit()
    conn.close()

def insert_article(article):
    conn = get_connection()
    c = conn.cursor()
    c.execute('''
        INSERT INTO articles (title, link, source, country, region, topic)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (article['title'], article['link'], article['source'], article['country'], article['region'], article['topic']))
    conn.commit()
    conn.close()

def fetch_and_cache():
    print("Starting fetch_and_cache...")
    create_tables()
    clear_articles()

    headers = {'User-Agent': 'Mozilla/5.0 (compatible; MyNewsBot/1.0)'}
    total_articles = 0

    for feed_info in FEEDS:
        try:
            print(f"Fetching feed: {feed_info['source']}")
            # Fetch feed content with timeout
            response = requests.get(feed_info["url"], headers=headers, timeout=10)
            response.raise_for_status()  # Raise error for bad HTTP status
            parsed = feedparser.parse(response.content)

            count = 0
            for entry in parsed.entries:
                if is_relevant(entry.title):
                    article = {
                        "title": entry.title,
                        "link": entry.link,
                        "source": feed_info.get("source", "Unknown"),
                        "country": feed_info.get("country", "Unknown"),
                        "region": feed_info.get("region", "Unknown"),
                        "topic": detect_topic(entry.title)
                    }
                    insert_article(article)
                    count += 1

            print(f"✓ Done: {feed_info['source']}, articles: {count}")
            total_articles += count
            time.sleep(1)
        except Exception as e:
            print(f"Error fetching {feed_info['source']}: {e}")

    print(f"Fetched total {total_articles} articles.")

if __name__ == "__main__":
    fetch_and_cache()
