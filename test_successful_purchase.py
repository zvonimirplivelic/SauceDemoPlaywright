from playwright.sync_api import Page, expect

def test_successfull_purchase(page: Page) -> None:
    page.goto("https://www.saucedemo.com/")
    
    