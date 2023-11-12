import allure
import time
from selene import have, by


@allure.title("Проверка работы формы регистрации")
def test_hw14(setup_browser):
    browser = setup_browser

    with allure.step('Открываем форму регистрации'):
        browser.element(".practice-form-wrapper").should(have.text("Student Registration Form"))
        browser.driver.execute_script("$('footer').remove()")
        browser.driver.execute_script("$('#fixedban').remove()")

    with allure.step('Ввод имени и фамилии'):
        browser.element('//input[@placeholder="First Name"]').send_keys('Timir')
        browser.element('//input[@placeholder="Last Name"]').send_keys('Gazizov')

    with allure.step('Ввод электронного адреса и номер телефона'):
        browser.element('#userEmail').send_keys('my_mail@gmail.com')
        browser.element('//input[@placeholder="Mobile Number"]').send_keys('9999999999')

    with allure.step('Выбор пола'):
        browser.element('//label[text() = "Male"]').click()

    # with allure.step('Выбор дня рождения'):
    #     browser.registration_page.select_date_of_birth('june', 11, 1994)

    with allure.step('Выбор предметов и увлечений'):
        browser.element('#subjectsInput').type(f'math').press_enter()
        browser.element('//label[@for="hobbies-checkbox-1"]').click()
        browser.element('//label[@for="hobbies-checkbox-3"]').click()

    # with allure.step('Загрузка фотографии'):
    #     registration_page.upload_picture()

    with allure.step('Ввод адреса'):
        browser.element('//textarea[@placeholder="Current Address"]').send_keys('Shevchenko street')
        browser.element('//div[text()="Select State"]').click()
        browser.element('//*[text()="Haryana"]').click()
        browser.element('//div[text()="Select City"]').click()
        browser.element('//*[text()="Karnal"]').click()

    with allure.step('Нажатие "Submit"'):
        browser.registration_page.submit_button_click()

    with allure.step('Проверка введенных данных'):
        browser.element("#example-modal-sizes-title-lg").should(have.text("Thanks for submitting the form"))

    time.sleep(1)