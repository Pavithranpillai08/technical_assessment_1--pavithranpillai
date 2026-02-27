# technical_assessment_1--pavithranpillai

# El Pais Opinion Scraper – Selenium + BrowserStack
The script runs locally and also executes in parallel across multiple browsers using BrowserStack, it extracts the top 5 articles from opinion section.

browserstack.py   → BrowserStack remote driver configuration
scrapper.py       → Scraping logic
main.py           → Entry point
config.py         → Configuration management
requirements.txt  → Dependencies


## Setup Instructions

### 1. Clone the Repository

---

### 2. Create and Activate a Virtual Environment (Recommended)

---

### 3. Install Dependencies
pip install -r requirements.txt


---

### 4. Configure Environment Variables

Create a file named `.env` in the root directory and add:
RAPIDAPI_KEY:YOUR_KEY
BROWSERSTACK_USERNAME=your_browserstack_username
BROWSERSTACK_ACCESS_KEY=your_browserstack_access_key


