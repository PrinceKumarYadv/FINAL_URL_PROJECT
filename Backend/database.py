from datetime import datetime

# In-memory database (temporary)
url_database = {}


def save_url(code: str, url: str):
    url_database[code] = {
        "original_url": url,
        "created_at": datetime.utcnow(),
        "clicks": 0
    }
