from selene import browser, have, command, be, by

class GitHubPages:
    def open(self):
        browser.open('https://github.com')

    def set_search_value(self):
        if browser.element(".header-search-input").should(be.visible):
            browser.element(".header-search-input").clear()
            browser.element(".header-search-input").click()
            browser.element(".header-search-input").send_keys('eroshenkoam/allure-example').submit()
            return self
        else:
            print('Element not found')

    def get_search_result(self):
        browser.element(by.link_text('eroshenkoam/allure-example')).click()
        return self

    def click_on_personal_git(self):
        if browser.element("#issues-tab").should(be.visible):
            browser.element("#issues-tab").click()
            return self

    def search_issue_on_page(self):
        browser.element(by.partial_text('#80')).should(be.visible)
        return self

