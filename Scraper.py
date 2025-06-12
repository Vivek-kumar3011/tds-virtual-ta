import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
import time

# Example TDS Discourse topic URL
BASE_URL = "https://discourse.onlinedegree.iitm.ac.in/t/"
TOPIC_IDS = [
    "ga4-data-sourcing-discussion-thread-tds-jan-2025/165959",
    "ga5-question-8-clarification/155939"
]  # replace with the topics you want

all_posts = []

for topic_id in TOPIC_IDS:
    full_url = BASE_URL + topic_id
    print(f"Scraping: {full_url}")

    try:
        response = requests.get(full_url)
        if response.status_code != 200:
            print(f"Failed to fetch {full_url}")
            continue

        soup = BeautifulSoup(response.content, 'html.parser')

        # Get title
        title_tag = soup.find("title")
        title = title_tag.text.strip() if title_tag else "No Title"

        # Get all posts in the topic
        posts_divs = soup.find_all("div", class_="cooked")  # 'cooked' class contains post content

        for post_div in posts_divs:
            post_text = post_div.get_text(separator=' ', strip=True)
            all_posts.append({
                "title": title,
                "post_text": post_text,
                "url": full_url
            })

        time.sleep(1)  # Be gentle to the server

    except Exception as e:
        print(f"Error scraping {full_url}: {e}")

# Save as JSON
with open("discourse_posts.json", "w", encoding='utf-8') as f:
    json.dump(all_posts, f, ensure_ascii=False, indent=4)

# Optional: Save as CSV
df = pd.DataFrame(all_posts)
df.to_csv("discourse_posts.csv", index=False, encoding='utf-8')

print("Scraping complete. Data saved to discourse_posts.json and discourse_posts.csv.")

