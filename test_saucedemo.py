import playwright
from playwright.sync_api import Playwright, sync_playwright, Page


def test_saucedemo_login(page: Page):
    page.goto("https://www.saucedemo.com/")

    # 1. Login
    page.locator("[data-test='username']").fill("standard_user")
    page.locator("[data-test='password']").fill("secret_sauce")
    page.locator("[data-test='login-button']").click()

    # 2. Add to Cart & Navigate
    page.locator("[data-test='add-to-cart-sauce-labs-fleece-jacket']").click()
    page.locator("[data-test='shopping-cart-link']").click()
    page.locator("[data-test='checkout']").click()

    # 3. Form Fill
    page.locator("[data-test='firstName']").fill("John")
    page.locator("[data-test='lastName']").fill("Price")
    page.locator("[data-test='postalCode']").fill("110110")

    # 4. Finish flow
    page.locator("[data-test='continue']").click()
    page.locator("[data-test='finish']").click()
    page.locator("[data-test='back-to-products']").click()

