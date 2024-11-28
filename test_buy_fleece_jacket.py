import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.saucedemo.com/")

    # LOGIN AS STANDARD USER
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill("standard_user")

    page.locator("[data-test=\"password\"]").click()
    page.locator("[data-test=\"password\"]").fill("secret_sauce")

    page.locator("[data-test=\"login-button\"]").click()

    # ADD FLEECE JACKET TO CART
    page.locator("[data-test=\"add-to-cart-sauce-labs-fleece-jacket\"]").click()

    # OPEN SHOPPING CART
    page.locator("[data-test=\"shopping-cart-link\"]").click()

    # CLICK CHECKOUT BUTTON
    page.locator("[data-test=\"checkout\"]").click()

    # SUBMIT CHECKOUT FORM
    page.locator("[data-test=\"firstName\"]").click()
    page.locator("[data-test=\"firstName\"]").fill("TestFirst")

    page.locator("[data-test=\"lastName\"]").click()
    page.locator("[data-test=\"lastName\"]").fill("TestLast")

    page.locator("[data-test=\"postalCode\"]").click()
    page.locator("[data-test=\"postalCode\"]").fill("999899")

    page.locator("[data-test=\"continue\"]").click()

    # FINISH CHECKOUT
    page.locator("[data-test=\"finish\"]").click()

    # CLICK BACK HOME BUTTON
    page.locator("[data-test=\"back-to-products\"]").click()

    # OPEN THE HAMBURGER MENU
    page.get_by_role("button", name="Open Menu").click()

    # LOG OUT
    page.locator("[data-test=\"logout-sidebar-link\"]").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
