import time
from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://davit-resume.com")

    page.wait_for_load_state("networkidle")

    nav_card = page.locator(".card")
    nav_card.get_by_role("link", name="Contact Me").click()
    page.wait_for_load_state("networkidle")
    page.locator('input[name="name"]').fill("Test Name")
    page.locator('input[name="email"]').fill("test@gmail.com")
    page.locator('textarea[name="message"]').fill("Test Message!")
    page.get_by_role("button", name="Send Message").click()

    page.wait_for_load_state("networkidle")

    page.get_by_text("Thanks! Your message has been sent.").highlight()
    time.sleep(5)