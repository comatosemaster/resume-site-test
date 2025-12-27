from playwright.sync_api import expect

base_url = "https://davit-resume.com/skills"

def test_skills_title(page):
    page.goto(base_url)
    expect(page).to_have_title("Skills – Davit Mujirishvili")


def test_skills_name(page):
    page.goto(base_url)
    expect(page.locator("div.page-title")).to_be_visible()
    expect(page.locator("div.page-title")).to_have_text("Skills")


def test_skills_subtitle(page):
    page.goto(base_url)
    expect(page.locator("div.page-subtitle")).to_be_visible()
    expect(page.locator("div.page-subtitle")).not_to_have_text("")


def test_skills_main_sections(page):
    page.goto(base_url)
    expect(page.locator("h3.section-title")).to_have_count(2)


def test_skills_sub_sections(page):
    page.goto(base_url)
    page.wait_for_selector("div.skill-group-title", state="attached")

    count = page.locator("div.skill-group-title").count()
    assert count > 1


def test_skills_skill_box(page):
    page.goto(base_url)
    page.wait_for_selector("div.skill-pill", state="attached")

    count = page.locator("div.skill-pill").count()
    assert count > 1