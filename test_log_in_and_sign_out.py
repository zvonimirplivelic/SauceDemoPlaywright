import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.saucedemo.com/")

    # FILL USERNAME
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill("standard_user")

    # FILL PASSWORD
    page.locator("[data-test=\"password\"]").click()
    page.locator("[data-test=\"password\"]").fill("secret_sauce")

    # CLICK LOGIN BUTTON
    page.locator("[data-test=\"login-button\"]").click()

    # OPEN HAMBURGER MENU
    page.get_by_role("button", name="Open Menu").click()

    # CLICK LOGOUT
    page.locator("[data-test=\"logout-sidebar-link\"]").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
