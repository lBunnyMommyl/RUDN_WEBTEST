from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_login_with_pom(driver):

    login_page = LoginPage(driver).open()

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    inventory_page = InventoryPage(driver)

    assert inventory_page.get_title() == "Products"