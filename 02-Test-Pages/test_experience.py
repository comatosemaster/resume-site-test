from playwright.sync_api import expect
import pytest

base_url = "https://davit-resume.com/experience"

@pytest.fixture(autouse=True)
def open_page(page):
    page.goto(base_url)

def test_experience_title(page):
    expect(page).to_have_title("Experience – Davit Mujirishvili")


def test_experience_name(page):
    expect(page.locator("div.page-title")).to_be_visible()
    expect(page.locator("div.page-title")).to_have_text("Experience")


def test_experience_subtitle(page):
    expect(page.locator("div.page-subtitle")).to_be_visible()
    expect(page.locator("div.page-subtitle")).not_to_have_text("")


def test_experience_box(page):
    expect(page.locator("div.exp-wrapper")).to_be_visible()

    card_count = page.locator("div.exp-card").count()
    assert card_count > 0

    cards = page.locator("div.exp-card")
    count = cards.count()

    assert count > 0, "No experience cards found"

    for i in range(count):
        card = cards.nth(i)

        expect(card.locator(".exp-role")).to_be_visible()
        expect(card.locator(".exp-company")).to_be_visible()
        expect(card.locator(".exp-divider")).to_be_visible()
        expect(card.locator(".exp-desc")).to_be_visible()
        expect(card.locator(".exp-role")).not_to_have_text("")
        expect(card.locator(".exp-company")).not_to_have_text("")
        expect(card.locator(".exp-desc")).not_to_have_text("")
