# Website Scraping

Scrape structured data from web pages (static or lightly dynamic) into a reproducible dataset.

**Points: 8**

---

## Task

1. **Target & legality (2 pts)** — Choose a public site or sandbox suitable for scraping. Document:
   - URL(s),
   - what you checked in `robots.txt` / terms,
   - polite crawl policy (delay, user-agent).
2. **Extractor (4 pts)** — Implement a scraper (`requests` + BeautifulSoup, Scrapy, or equivalent). Handle pagination or multiple pages if available. Save **raw HTML/JSON** and a parsed table (CSV/Parquet).
3. **Cleaning & schema (2 pts)** — Define column types; drop duplicates; handle missing fields; timestamp each run.
4. **Reliability (2 pts)** — Add basic error handling (timeouts, retries with backoff). Make a second run and show that outputs remain consistent or versioned by run id.

## Deliverables

- Scraper code + sample outputs (small sample committed; large dumps gitignored)
- Short ethics / ToS note
- Schema of the parsed dataset

## Acceptable alternatives

- Locally saved HTML fixtures + scraper that works offline (must still demonstrate real parsing logic).
- Official public API used **in addition** to HTML parsing is fine, but HTML extraction should remain part of the submission.
