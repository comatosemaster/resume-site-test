from playwright.sync_api import expect
import pytest

base_url = "https://davit-resume.com/contact"

@pytest.fixture(autouse=True)
def open_page(page):
    page.goto(base_url)

def test_send_message(page):
    page.locator('input[name="name"]').fill("Test Name")
    page.locator('input[name="email"]').fill("test@gmail.com")
    page.locator('textarea[name="message"]').fill("Test Message!")
    page.get_by_role("button", name="Send Message").click()

    page.wait_for_load_state("networkidle")

    expect(page.get_by_text("Thanks! Your message has been sent.")).to_be_visible()

def test_contact_page(page):
    expect(page).to_have_title("Contact – Davit Mujirishvili")
    expect(page.locator('input[name="name"]')).to_be_visible()
    expect(page.locator('input[name="email"]')).to_be_visible()
    expect(page.locator('textarea[name="message"]')).to_be_visible()
    expect(page.get_by_role("button", name="Send Message")).to_be_visible()