import time
from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://davit-resume.com/skills")

    page.wait_for_load_state("networkidle")
    skill_one = page.locator("h3.section-title").nth(0).inner_text()
    skill_two = page.locator("h3.section-title").nth(1).inner_text()

    print(skill_one)
    print(skill_two)