import playwright
from playwright.sync_api import Playwright, sync_playwright, Page

def test_demoblaze_login(page:Page):
    page.goto("https://www.demoblaze.com/index.html")

    # 1. Login
    page.get_by_role("link", name="Log in").click()
    # Using the CSS ID selector (#) is much safer and cleaner
    page.locator("#loginusername").fill("John_Price")
    page.locator("#loginpassword").fill("@Ut0m@te@12")
    page.get_by_role("button", name="Log in").click()

    # 2. Select Product
    page.locator(".card-title > a").first.click()

    # 3. Handle Alert Dialog
    # This line tells Playwright: "When you see an alert, accept it (click OK)."
    page.once("dialog", lambda dialog: dialog.accept())
    page.get_by_role("link", name="Add to cart").click()

    # 4. Go to Cart & Checkout
    page.get_by_role("link", name="Cart", exact=True).click()
    page.get_by_role("button", name="Place Order").click()

    # 5. Order Form

    page.locator("#name").fill("John Price")
    page.locator("#country").fill("India")
    page.locator("#city").fill("Mumbai")
    page.locator("#card").fill("1111111111199")
    page.locator("#month").fill("09")
    page.locator("#year").fill("2029")

    page.get_by_role("button", name="Purchase").click()
    page.get_by_role("button", name="OK").click()
