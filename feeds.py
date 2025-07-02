import feedparser


FEEDS = [
    # Existing feeds
    {"source": "BBC", "url": "https://feeds.bbci.co.uk/news/world/rss.xml", "region": "Europe", "country": "UK"},
    {"source": "Reuters", "url": "http://feeds.reuters.com/reuters/worldNews", "region": "Global", "country": "International"},
    {"source": "AP News", "url": "https://apnews.com/rss", "region": "Americas", "country": "USA"},
    {"source": "The Guardian", "url": "https://www.theguardian.com/world/rss", "region": "Europe", "country": "UK"},
    {"source": "DW", "url": "https://rss.dw.com/rdf/rss-en-all", "region": "Europe", "country": "Germany"},
    {"source": "Al Jazeera", "url": "https://www.aljazeera.com/xml/rss/all.xml", "region": "Middle East", "country": "Qatar"},
    {"source": "NPR", "url": "https://feeds.npr.org/1001/rss.xml", "region": "Americas", "country": "USA"},
    {"source": "El País", "url": "https://feeds.elpais.com/mrss-s/pages/ep/site/elpais.com/section/international/eng/rss.xml", "region": "Europe", "country": "Spain"},
    {"source": "ABC España", "url": "https://www.abc.es/rss/feeds/abc_Internacional.xml", "region": "Europe", "country": "Spain"},
    {"source": "Gazeta Wyborcza", "url": "https://wyborcza.pl/pub/rss/wyborcza.pl/wiadomosci_english.xml", "region": "Europe", "country": "Poland"},
    {"source": "SBS Australia", "url": "https://www.sbs.com.au/news/rss", "region": "Oceania", "country": "Australia"},
    {"source": "NZ Herald", "url": "https://rss.nzherald.co.nz/rss/xml/worldnewssection.xml", "region": "Oceania", "country": "New Zealand"},
    {"source": "Le Monde", "url": "https://www.lemonde.fr/rss/une.xml", "region": "Europe", "country": "France"},
    {"source": "CBC", "url": "https://rss.cbc.ca/lineup/world.xml", "region": "Americas", "country": "Canada"}
]



UNWANTED_KEYWORDS = [
    "celebrity", "influencer", "gossip", "love island", "Kardashian"
]

def is_relevant(title):
    return not any(bad in title.lower() for bad in UNWANTED_KEYWORDS)

def fetch_news(filter_region=None, filter_country=None):
    stories = []
    for feed in FEEDS:
        if filter_region and feed["region"] != filter_region:
            continue
        if filter_country and feed["country"] != filter_country:
            continue

        parsed = feedparser.parse(feed["url"])
        for entry in parsed.entries[:6]:
            if is_relevant(entry.title):
                stories.append({
                    "title": entry.title,
                    "link": entry.link,
                    "source": feed["source"],
                    "region": feed["region"],
                    "country": feed["country"],
                    "topic": detect_topic(entry.title)
                })
    return stories

def detect_topic(title):
    title = title.lower()
    if any(keyword in title for keyword in ["election", "president", "parliament", "government", "minister", "vote"]):
        return "Politics"
    if any(keyword in title for keyword in ["stock", "economy", "inflation", "gdp", "debt", "market", "trade"]):
        return "Economy"
    if any(keyword in title for keyword in ["ai", "technology", "robot", "software", "data", "cyber", "startup"]):
        return "Technology"
    if any(keyword in title for keyword in ["war", "conflict", "army", "strike", "military"]):
        return "Conflict"
    if any(keyword in title for keyword in ["sport", "match", "tournament", "olympics", "championship", "goal"]):
        return "Sports"
    return "Other"
