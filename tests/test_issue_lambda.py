import json

import allure
import pytest
from allure import attachment_type
from allure_commons.types import Severity
from selene import be, by
from selene.support.shared import browser


@pytest.fixture(scope='function', autouse=True)
def browser_setup():
    browser.config.window_height = '1440'
    browser.config.window_width = '1080'


@allure.tag('web')
@allure.severity(Severity.BLOCKER)
@allure.feature('Задачи в репозиторий')
@allure.label('owner', 'Stanislav')
@allure.story('Поиск задачи неавторизованным пользователем')
@allure.link('https://github.com', name='Testing')
def test_issue_lambda():
    open_page(browser_setup)
    search_repository('Stasnislav121/qa_guru_python_4_8')
    link_click('Stasnislav121/qa_guru_python_4_8')
    click_for_issue()
    search_text('#1')


@allure.step('Открытие страницы GitHib')
def open_page(browser_setup):
    browser.open('https://github.com/')


@allure.step('Ввод названия репозитория {repo}')
def search_repository(repo):
    allure.attach("<h1>Hello, world</h1>", name="Html", attachment_type=attachment_type.HTML)
    browser.element('.header-search-input').click()
    browser.element('.header-search-input').send_keys(repo).submit()


@allure.step('Переход по найденной ссылке {repo}')
def link_click(repo):
    browser.element(by.link_text(repo)).click()
    allure.attach("Text content", name="Text", attachment_type=attachment_type.TEXT)


@allure.step('Переход во кладку "Issue"')
def click_for_issue():
    browser.element('#issues-tab').click()
    allure.attach(json.dumps({"first": 1, "second": 2}), name="Json", attachment_type=attachment_type.JSON)


@allure.step('Проверка наличия элемента с текстом {text}')
def search_text(text):
    browser.element(by.partial_text('#1')).should(be.visible)
