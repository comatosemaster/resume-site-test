from playwright.sync_api import expect
import pytest

base_url = "https://davit-resume.com/skills"

@pytest.fixture(autouse=True)
def open_page(page):
    page.goto(base_url)

def test_skills_title(page):
    expect(page).to_have_title("Skills - Davit Mujirishvili")


def test_skills_name(page):
    expect(page.locator("div.page-title")).to_be_visible()
    expect(page.locator("div.page-title")).to_have_text("Skills")


def test_skills_subtitle(page):
    expect(page.locator("div.page-subtitle")).to_be_visible()
    expect(page.locator("div.page-subtitle")).not_to_have_text("")


def test_skills_main_sections(page):
    expect(page.locator("h3.section-title")).to_have_count(2)
    expect(page.locator("h3.section-title").nth(0)).to_contain_text("Hard Skills")
    expect(page.locator("h3.section-title").nth(1)).to_contain_text("Soft Skills")


def test_skills_sub_sections(page):
    page.wait_for_selector("div.skill-group-title", state="attached")

    count = page.locator("div.skill-group-title").count()
    assert count > 1


def test_skills_skill_box(page):
    page.wait_for_selector("div.skill-pill", state="attached")

    count = page.locator("div.skill-pill").count()
    assert count > 1