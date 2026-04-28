from playwright.sync_api import Playwright, sync_playwright


def test_web_automation(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_role("textbox", name="Username:").fill("rahulshettyacademy")
    page.get_by_role("textbox", name="Password:").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("teach")
    page.get_by_role("checkbox", name="I Agree to the terms and").check()
    page.get_by_role("button", name="Sign In").click()
    page.locator("app-card").filter(has_text="iphone X $24.99 Lorem ipsum").get_by_role("button").click()
    page.get_by_text("Checkout ( 1 ) (current)").click()
    page.get_by_role("button", name="Checkout").click()

    # Wait for the delivery country textbox to appear and be visible
    page.wait_for_selector("#country", state="visible")
    page.click("#country")
    page.type("#country", "India", delay=100)

    # Wait explicitly for the dropdown suggestion to appear
    page.wait_for_selector("div.suggestions ul li a", timeout=7000)
    page.click("div.suggestions ul li a")  # Click on the first suggestion (India)

    # Tick the terms & conditions checkbox (after country selection, in case DOM reloads)
    page.get_by_text("I agree with the term &").click()

    # Complete the purchase
    page.get_by_role("button", name="Purchase").click()

    context.close()
    browser.close()


with sync_playwright() as playwright:
    test_web_automation(playwright)