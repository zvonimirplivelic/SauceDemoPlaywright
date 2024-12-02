from playwright.sync_api import Page, expect

    
"""
###
    There is already log in and log out test created in test_log_in.py, 
    therefore it will be ommited in this file
###
    There is a bug fully described in test_reset_app_state.py, 
    therefore Reset App State hamburger menu option is also ommited
"""
    
def test_about_link(page: Page) -> None:
    page.goto("https://www.saucedemo.com/")  

    ## Log In as Standard User
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"username\"]").press("Tab")
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()
    
    ## Open the Hamburger Menu
    page.get_by_role("button", name="Open Menu").click()
    
    ## Test About Link
    page.locator("[data-test=\"about-sidebar-link\"]").click()
    page.wait_for_url("https://saucelabs.com/")
    
def test_all_items_link(page: Page) -> None:
    page.goto("https://www.saucedemo.com/")  

    ## Log In as Standard User
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"username\"]").press("Tab")
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()
    
    ## Open an inventory item (Sauce Labs Backpack) 
    page.locator("[data-test=\"item-4-title-link\"]").click()
    ## Open hamburger menu and click All Items
    page.get_by_role("button", name="Open Menu").click()
    page.locator("[data-test=\"inventory-sidebar-link\"]").click()
    
    ## Verify Inventory Page
    page.wait_for_url("https://www.saucedemo.com/inventory.html")
    expect(page.locator("[data-test=\"title\"]")).to_contain_text("Products")
    expect(page.locator("[data-test=\"inventory-container\"]")).to_be_visible()
    
def test_cart_icon_click(page: Page):
    page.goto("https://www.saucedemo.com/")  

    ## Log In as Standard User
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"username\"]").press("Tab")
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()
    
    expect(page.locator("[data-test=\"title\"]")).to_contain_text("Products")
    expect(page.locator("[data-test=\"inventory-container\"]")).to_be_visible()

    page.locator("[data-test=\"shopping-cart-link\"]").click()
    page.wait_for_url("https://www.saucedemo.com/cart.html")
    expect(page.locator("[data-test=\"title\"]")).to_contain_text("Your Cart")
    expect(page.locator("[data-test=\"cart-contents-container\"]")).to_be_visible()

    page.locator("[data-test=\"continue-shopping\"]").click()
    page.wait_for_url("https://www.saucedemo.com/inventory.html")
    expect(page.locator("[data-test=\"title\"]")).to_contain_text("Products")
    expect(page.locator("[data-test=\"inventory-container\"]")).to_be_visible()
