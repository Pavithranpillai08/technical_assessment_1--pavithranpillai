from selenium.webdriver.common.by import By
import time
from config import RAPIDAPI_KEY
import requests
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def run_test(driver):

    driver.get("https://elpais.com/")
    driver.implicitly_wait(10)
    driver.maximize_window()

    time.sleep(5)

    # accepting the cookies here
   # driver.find_element(By.ID, "didomi-notice-agree-button").click()
   
# accepting cookies safely
    try:
        WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "didomi-notice-agree-button"))
        ).click()
        print("Cookies accepted.")
    except:
     print("Cookie popup not found or already accepted.")

    # going to opinion section
    driver.find_element(By.LINK_TEXT, "Opinión").click()

    time.sleep(5)

    # finding the articles and the length of same
    articles = driver.find_elements(By.TAG_NAME, "article")
    print(len(articles))

    # scraping starting 5 articles
    scraped_articles = []

    for i, article in enumerate(articles[:5]):
        print(f"\nArticle {i+1}:")

        try:
            h2 = article.find_element(By.TAG_NAME, "h2")
            title = h2.text.strip()
        except Exception:
            title = "No title found"
            h2 = None

        try:
            link = h2.find_element(By.TAG_NAME, "a").get_attribute("href") if h2 else None
        except Exception:
            link = None

        print(f"  Title  : {title}")
        print(f"  Link   : {link}")

        scraped_articles.append({
            "index": i + 1,
            "title": title,
            "link": link,
            "content": ""
        })

    # opening each article and scrapping content
    for article_data in scraped_articles:

        link = article_data["link"]

        if link:
            driver.get(link)
            time.sleep(3)

            paragraphs = driver.find_elements(By.TAG_NAME, "p")

            content_text = ""

            for p in paragraphs:
                text = p.text.strip()
                if text:
                    content_text += text + " "

            article_data["content"] = content_text

            print("\nContent preview:")
            print(content_text[:300])  # print first 300 chars only

    # translating the header titles of 5 articles
    translated_titles = []

    for article_data in scraped_articles:
        title = article_data["title"]
        idx = article_data["index"]

        print(f"\n  - Article {idx} - ")
        print(f"Spanish : {title}")

        try:
            url = "https://rapid-translate-multi-traduction.p.rapidapi.com/t"

            headers = {
                "Content-Type": "application/json",
                "X-RapidAPI-Key": RAPIDAPI_KEY,
                "X-RapidAPI-Host": "rapid-translate-multi-traduction.p.rapidapi.com"
            }

            payload = {
                "from": "es",
                "to": "en",
                "q": title
            }

            response = requests.post(url, json=payload, headers=headers, timeout=10)
            response.raise_for_status()

            translated = response.json()[0]

            print(f"English : {translated}")

            translated_titles.append(translated)

        except Exception as e:
            print(f"Translation failed: {e}")
            translated_titles.append(title)

    # --------- Repeated Word Analysis ---------

    print("\nRepeated Words (appearing more than twice):")

    all_text = " ".join(translated_titles).lower()

    # remove simple punctuation
    for ch in [",", ".", ":", ";", "!", "?", "-", "(", ")"]:
        all_text = all_text.replace(ch, "")

    words = all_text.split()

    word_count = {}

    for word in words:
        if len(word) > 2:   # ignore very small words like 'a', 'to'
            word_count[word] = word_count.get(word, 0) + 1

    for word, count in word_count.items():
        if count > 2:
            print(f"{word} : {count}")

    return translated_titles


