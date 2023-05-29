from selene import browser
from selene import be, have,by

def test_lesson_5():
    browser.open("https://edvibe.com/Account/Login")
    browser.driver.maximize_window()
    browser.element('[name="Email"]').should(be.blank).type('43@mail.ru').press_enter()
    browser.element('[name="Password"]').should(be.blank).type('liveUT00mPE8CB7Z').press_enter()
    browser.element(by.xpath("/html/body/div[1]/div/div[2]/form/button[2]")).click()
    ...