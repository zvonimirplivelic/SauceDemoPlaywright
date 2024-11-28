import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # A BUG IS BEING REPLICATED IN THIS TEST CASE
    page.goto("https://www.saucedemo.com/")

    # LOG IN TO APPLICATION
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill("standard_user")

    page.locator("[data-test=\"password\"]").click()
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()

    # ADD FLEECE JACKET TO THE CART AND CHECK CART
    page.locator("[data-test=\"add-to-cart-sauce-labs-fleece-jacket\"]").click()
    page.locator("[data-test=\"shopping-cart-link\"]").click()
    page.locator("[data-test=\"continue-shopping\"]").click()

    # RESET APP STATE
    page.get_by_role("button", name="Open Menu").click()
    page.locator("[data-test=\"reset-sidebar-link\"]").click()

    # CHECK CART
    page.locator("[data-test=\"shopping-cart-link\"]").click()
    page.locator("[data-test=\"continue-shopping\"]").click()

    # ADD FLEECE JACKET TO THE CART AND CHECK CART
    page.locator("[data-test=\"add-to-cart-sauce-labs-fleece-jacket\"]").click()
    page.locator("[data-test=\"shopping-cart-link\"]").click()
    page.locator("[data-test=\"continue-shopping\"]").click()

    # RESET APP STATE
    page.get_by_role("button", name="Open Menu").click()
    page.locator("[data-test=\"reset-sidebar-link\"]").click()

    # APP STATE RESETS, BUT BUTTON STATE REMAINS
    # WHEN INSPECTED WITH DEV TOOLS, THE BUTTON HAS TWO STATES PRIMARY AND SECONDARY
    # WHEN CART IS EMPTY BUTTON STATE IS PRIMARY(ADD TO CART), 
    # WHEN ITEM IS ADDED TO CART BUTTON STATE IS SECONDARY(REMOVE)
    # WHEN USER CLICKS ON THE BUTTON, BUTTON STATE CHANGES
    # BUT THIS BUTTON STATE CHANGE DOESN'T OCCUR WHEN RESETING APP STATE FROM THE HAMBURGER MENU
    page.locator("[data-test=\"remove-sauce-labs-fleece-jacket\"]").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)