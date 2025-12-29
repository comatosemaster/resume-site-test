from playwright.sync_api import expect
import pytest

base_url = "https://davit-resume.com"

@pytest.fixture(autouse=True)
def open_page(page):
    page.goto(base_url)

def test_title(page):
    expect(page).to_have_title("About - Davit Mujirishvili")


def test_header_visible(page):
    expect(page.locator("header")).to_be_visible()


def test_nav_bar_sections_visible(page):
    nav_card = page.locator(".card")
    expect(nav_card.get_by_role("link", name="Experience")).to_be_visible()
    expect(nav_card.get_by_role("link", name="Skills")).to_be_visible()
    expect(nav_card.get_by_role("link", name="Projects")).to_be_visible()
    expect(nav_card.get_by_role("link", name="Education")).to_be_visible()
    expect(nav_card.get_by_role("link", name="Certificates")).to_be_visible()
    expect(nav_card.get_by_role("link", name="Languages")).to_be_visible()
    expect(nav_card.get_by_role("link", name="Contact Me")).to_be_visible()
    expect(nav_card.get_by_role("link", name="About")).to_be_visible()
    expect(nav_card.get_by_role("link", name="Favorite Animes")).to_be_visible()
    expect(nav_card.get_by_role("link", name="Favorite Movies")).to_be_visible()
    expect(nav_card.get_by_role("link", name="Favorite Bands")).to_be_visible()


def test_about_image_visible(page):
    expect(page.locator("img.about-photo")).to_be_visible()


def test_focus_label_visible(page):
    expect(page.locator("span.focus-label")).to_be_visible()


def test_stat_cards_four(page):
    expect(page.locator("div.stats-grid")).to_be_visible()
    expect(page.locator("div.stat-card")).to_have_count(4)


def test_about_box(page):
    expect(page.locator("div.about-bio-box")).to_be_visible()
    expect(page.locator("div.about-bio-title")).to_be_visible()
    expect(page.locator("div.about-bio-title")).not_to_have_text("")
    expect(page.locator("div.about-bio-text")).to_be_visible()
    expect(page.locator("div.about-bio-text")).not_to_have_text("")


def test_header_sections_visible(page):
    expect(page.locator(
        ".top-header-right div.top-chip", has_text="Georgia"
    )).to_be_visible()

    expect(page.locator(
        ".top-header-right div.top-chip", has_text="+995"
    )).to_be_visible()

    expect(page.get_by_role("link", name="Github")).to_be_visible()
    expect(page.get_by_role("link", name="Linkedin")).to_be_visible()
    expect(page.get_by_role("link", name="heyitsdavit@gmail.com")).to_be_visible()
    expect(page.get_by_role("link", name="Download CV")).to_be_visible()

def test_nav_links_correct(page):
    nav_card = page.locator(".card")

    expect(nav_card.get_by_role("link", name="Skills")).to_have_attribute("href", "/skills/")
    expect(nav_card.get_by_role("link", name="Experience")).to_have_attribute("href", "/experience/")
    expect(nav_card.get_by_role("link", name="Projects")).to_have_attribute("href", "/projects/")
    expect(nav_card.get_by_role("link", name="Education")).to_have_attribute("href", "/education/")
    expect(nav_card.get_by_role("link", name="Languages")).to_have_attribute("href", "/languages/")
    expect(nav_card.get_by_role("link", name="Certificates")).to_have_attribute("href", "/certificates/")
    expect(nav_card.get_by_role("link", name="Contact Me")).to_have_attribute("href", "/contact/")
    expect(nav_card.get_by_role("link", name="About")).to_have_attribute("href", "/")
    expect(nav_card.get_by_role("link", name="Favorite Animes")).to_have_attribute("href", "/animes/")
    expect(nav_card.get_by_role("link", name="Favorite Movies")).to_have_attribute("href", "/movies/")
    expect(nav_card.get_by_role("link", name="Favorite Bands")).to_have_attribute("href", "/bands/")

def test_header_links_correct(page):
    github = page.get_by_role("link", name="Github")
    linkedin = page.get_by_role("link", name="Linkedin")
    download = page.get_by_role("link", name="Download CV")
    expect(github).to_have_attribute("href", "https://github.com/comatosemaster/")
    expect(linkedin).to_have_attribute("href", "https://www.linkedin.com/in/davit-mujirishvili/")
    expect(download).to_have_attribute("href", "/media/resumes/Davit_Mujirishvili_Resume.pdf")
