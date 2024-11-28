import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://www.saucedemo.com/")

    # EMPTY CREDENTIALS LOGIN
    page.locator("[data-test=\"login-button\"]").click()

    # INCORRECT USERNAME LOGIN
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill("fakeusername")
    page.locator("[data-test=\"password\"]").click()
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()

    # INCORRECT PASSWORD LOGIN
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"username\"]").press("Tab")
    page.locator("[data-test=\"password\"]").fill("fakepassword")
    page.locator("[data-test=\"login-button\"]").click()

    # EMPTY CREDENTIALS LOGIN
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill("")
    page.locator("[data-test=\"password\"]").dblclick()
    page.locator("[data-test=\"password\"]").fill("")
    page.locator("[data-test=\"password\"]").press("Enter")
    page.locator("[data-test=\"login-button\"]").click()

    # STANDARD USER LOGIN
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"password\"]").click()
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"password\"]").press("Enter")
    
    page.locator("[data-test=\"login-button\"]").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
