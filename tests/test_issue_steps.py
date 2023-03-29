import allure
import pytest
from allure_commons.types import Severity, AttachmentType
from selene import be, by
from selene.support.shared import browser


@pytest.fixture(scope='function', autouse=True)
def browser_setup():
    browser.config.window_height = '1440'
    browser.config.window_width = '1080'


def test_issue_tab_steps(browser_setup):
    allure.dynamic.tag('web')
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature('Задачи в репозиторий')
    allure.dynamic.story('Поиск задачи неавторизованным пользователем')
    allure.dynamic.link('https://github.com', name='Testing')

    with allure.step('Открытие страницы GitHib'):
        browser.open('https://github.com/')

    with allure.step('Ввод названия репозитория'):
        browser.element('.header-search-input').click()
        browser.element('.header-search-input').send_keys('Stasnislav121/qa_guru_python_4_8').submit()

    with allure.step('Переход по найденной ссылке'):
        browser.element(by.link_text('Stasnislav121/qa_guru_python_4_8')).click()

    with allure.step('Переход во кладку "Issue"'):
        browser.element('#issues-tab').click()

    with allure.step('Проверка наличия элемента с текстом "#1"'):
        browser.element(by.partial_text('#1')).should(be.visible)
        allure.attach(browser.driver().get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
