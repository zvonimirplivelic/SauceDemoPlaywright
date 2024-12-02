from playwright.sync_api import Page, expect


def test_log_in_and_log_out(page: Page) -> None:
    page.goto("https://www.saucedemo.com/")
    
    ## Check login form
    expect(page.locator("[data-test=\"login-container\"] div").filter(has_text="Login").first).to_be_visible()
    expect(page.locator("[data-test=\"username\"]")).to_be_empty();
    expect(page.locator("[data-test=\"password\"]")).to_be_empty();
   
    ## Fill the log in form
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"username\"]").press("Tab")
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()
    
    ## Check elements of inventory page
    page.wait_for_url("https://www.saucedemo.com/inventory.html")
    expect(page.locator("[data-test=\"title\"]")).to_contain_text("Products")
    expect(page.locator("[data-test=\"inventory-container\"]")).to_be_visible()
    
    ## Open Hamburger Menu
    page.get_by_role("button", name="Open Menu").click()
    
    ## Click Logout
    page.locator("[data-test=\"logout-sidebar-link\"]").click()
    
    ## Check elements of login page
    page.wait_for_url("https://www.saucedemo.com/")
    expect(page.locator("[data-test=\"login-container\"] div").filter(has_text="Login").first).to_be_visible()

def test_log_in_with_empty_username(page: Page) -> None:
    page.goto("https://www.saucedemo.com/")

    ## Check elements state
    expect(page.locator("[data-test=\"error\"]")).not_to_be_visible()
    expect(page.locator("[data-test=\"username\"]")).to_be_empty();
    expect(page.locator("[data-test=\"password\"]")).to_be_empty();
    
    ## Login with empty username
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    expect(page.locator("[data-test=\"password\"]")).to_have_value("secret_sauce");
    page.locator("[data-test=\"login-button\"]").click()
    
    ## Verify error message
    expect(page.locator("[data-test=\"error\"]")).to_be_visible()
    expect(page.locator("[data-test=\"error\"]")).to_contain_text("Epic sadface: Username is required")
    
    ## Close and verify error message
    page.locator("[data-test=\"error-button\"]").click()
    expect(page.locator("[data-test=\"error\"]")).not_to_be_visible()
    
def test_log_in_with_empty_password(page: Page) -> None:
    page.goto("https://www.saucedemo.com/")

    ## Setup and check prerequisites
    expect(page.locator("[data-test=\"error\"]")).not_to_be_visible()
    page.locator("[data-test=\"username\"]").fill("standard_user")
    expect(page.locator("[data-test=\"username\"]")).not_to_be_empty();
    expect(page.locator("[data-test=\"password\"]")).to_be_empty();
    
    ## Try to login with empty credentials
    page.locator("[data-test=\"login-button\"]").click()
    
    ## Verify error message
    expect(page.locator("[data-test=\"error\"]")).to_be_visible()
    expect(page.locator("[data-test=\"error\"]")).to_contain_text("Epic sadface: Password is required")


def test_log_in_with_empty_credentials(page: Page) -> None:
    page.goto("https://www.saucedemo.com/")

    ## Check prerequisites
    expect(page.locator("[data-test=\"error\"]")).not_to_be_visible()
    expect(page.locator("[data-test=\"username\"]")).to_be_empty();
    expect(page.locator("[data-test=\"password\"]")).to_be_empty();
    
    ## Try to login with empty credentials
    page.locator("[data-test=\"login-button\"]").click()
    
    ## Verify error message
    expect(page.locator("[data-test=\"error\"]")).to_be_visible()
    expect(page.locator("[data-test=\"error\"]")).to_contain_text("Epic sadface: Username is required")
    
def test_log_in_with_locked_out_user(page: Page) -> None:
    page.goto("https://www.saucedemo.com/")
    
    ## Check login form
    expect(page.locator("[data-test=\"login-container\"] div").filter(has_text="Login").first).to_be_visible()
    expect(page.locator("[data-test=\"username\"]")).to_be_empty();
    expect(page.locator("[data-test=\"password\"]")).to_be_empty();
    expect(page.locator("[data-test=\"error\"]")).not_to_be_visible()

   
    ## Fill the log in form
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill("locked_out_user")
    page.locator("[data-test=\"username\"]").press("Tab")
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()
    
    ## Verify error message
    expect(page.locator("[data-test=\"error\"]")).to_be_visible()
    expect(page.locator("[data-test=\"error\"]")).to_contain_text("Epic sadface: Sorry, this user has been locked out.")
