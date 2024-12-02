from playwright.sync_api import Page, expect

def test_successfull_purchase(page: Page) -> None:
    page.goto("https://www.saucedemo.com/")
    
    ## Login to the application
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()
    
    ## Check inventory elements
    page.wait_for_url("https://www.saucedemo.com/inventory.html")
    expect(page.locator("[data-test=\"title\"]")).to_contain_text("Products")
    expect(page.locator("[data-test=\"inventory-container\"]")).to_be_visible()
    
    ## Check Button text and cart empty state
    expect(page.locator("[data-test=\"shopping-cart-badge\"]")).not_to_be_visible()
    expect(page.locator("[data-test=\"add-to-cart-sauce-labs-bolt-t-shirt\"]")).to_contain_text("Add to cart")

    ## Add item to the cart
    page.locator("[data-test=\"add-to-cart-sauce-labs-bolt-t-shirt\"]").click()
    
    ## Check button and cart state
    expect(page.locator("[data-test=\"shopping-cart-badge\"]")).to_be_visible()
    expect(page.locator("[data-test=\"shopping-cart-badge\"]")).to_contain_text("1")
    expect(page.locator("[data-test=\"remove-sauce-labs-bolt-t-shirt\"]")).to_contain_text("Remove")

    ## Open cart
    page.locator("[data-test=\"shopping-cart-link\"]").click()
    page.wait_for_url("https://www.saucedemo.com/cart.html")
    expect(page.locator("[data-test=\"shopping-cart-badge\"]")).to_contain_text("1")
    expect(page.locator("[data-test=\"inventory-item\"]")).to_be_visible()
    expect(page.locator("[data-test=\"inventory-item-name\"]")).to_contain_text("Sauce Labs Bolt T-Shirt")
    
    ## Checkout step one - Credentials
    page.locator("[data-test=\"checkout\"]").click()
    page.wait_for_url("https://www.saucedemo.com/checkout-step-one.html")
    expect(page.locator("[data-test=\"title\"]")).to_contain_text("Checkout: Your Information")
    expect(page.locator(".checkout_info")).to_be_visible()
    
    ## Fill the checkout credentials
    page.locator("[data-test=\"firstName\"]").fill("Fname")
    page.locator("[data-test=\"lastName\"]").fill("Lname")
    page.locator("[data-test=\"postalCode\"]").fill("123456")
    page.locator("[data-test=\"continue\"]").click()
    
    ## Checkout step two - Confirmation
    page.wait_for_url("https://www.saucedemo.com/checkout-step-two.html")
    expect(page.locator("[data-test=\"title\"]")).to_contain_text("Checkout: Overview")
    expect(page.locator("[data-test=\"cart-list\"]")).to_be_visible()

    ## Confirm purchase
    page.locator("[data-test=\"finish\"]").click()
    
    ## Thank you screen -> Get back to inventory
    page.wait_for_url("https://www.saucedemo.com/checkout-complete.html")
    expect(page.locator("[data-test=\"title\"]")).to_contain_text("Checkout: Complete!")
    expect(page.locator("[data-test=\"pony-express\"]")).to_be_visible()
    expect(page.locator("[data-test=\"checkout-complete-container\"]")).to_be_visible()

    page.locator("[data-test=\"back-to-products\"]").click()
    
    page.wait_for_url("https://www.saucedemo.com/inventory.html")
