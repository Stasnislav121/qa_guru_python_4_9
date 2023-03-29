import pytest
from selene import be, by
from selene.support.shared import browser


@pytest.fixture(scope='function', autouse=True)
def browser_setup():
    browser.config.window_height = '1440'
    browser.config.window_width = '1080'


def test_issue_tab(browser_setup):
    browser.open('https://github.com/')

    browser.element('.header-search-input').click()
    browser.element('.header-search-input').send_keys('Stasnislav121/qa_guru_python_4_8').submit()

    browser.element(by.link_text('Stasnislav121/qa_guru_python_4_8')).click()

    browser.element('#issues-tab').click()

    browser.element(by.partial_text('#1')).should(be.visible)
