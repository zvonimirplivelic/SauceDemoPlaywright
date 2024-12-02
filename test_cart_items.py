from playwright.sync_api import Page, expect

""""
### This test will go through each item in the list 
### by clicking on the image and title.
### Odd items will be selected from the inventory list
### Even items will be selected from the item detail page
"""

def test_successfull_purchase(page: Page) -> None:
    page.goto("https://www.saucedemo.com/")
    
    ## Log In as Standard User
    page.locator("[data-test=\"username\"]").click()
    page.locator("[data-test=\"username\"]").fill("standard_user")
    page.locator("[data-test=\"username\"]").press("Tab")
    page.locator("[data-test=\"password\"]").fill("secret_sauce")
    page.locator("[data-test=\"login-button\"]").click()
    
    