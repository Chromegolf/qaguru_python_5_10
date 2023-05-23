import allure
from allure_commons.types import Severity
from selene import browser, have, command, be, by




class GitHubPages:


    @allure.step("Открываем главную страницу")
    def open(self):
        browser.open('')


    @allure.step("Ищем репозиторий {repo} с помощью поиска")
    def set_search_value(self, repo):
        browser.element(".header-search-input").clear()
        browser.element(".header-search-input").click()
        browser.element(".header-search-input").send_keys(repo).submit()


    @allure.step("Ищем репозиторий {repo} на странице результата поиска")
    def get_search_result(self, repo):
        browser.element(by.link_text(repo)).click()


    @allure.step("В найденном репозитории переходим на вкладку Issues")
    def click_on_personal_git(self):
        browser.element("#issues-tab").click()

    @allure.step("Ищем Issue #80")
    def search_issue_on_page(self, number):
        browser.element(by.partial_text('#' + number)).should(be.visible)