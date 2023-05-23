import allure
from page.github_pages import GitHubPages

def test_github_with_dynamic_steps():
    page = GitHubPages()
    with allure.step("Открываем главную страницу"):
        page.open()

    with allure.step("Ищем репозиторий с помощью поиска"):
        page.set_search_value()

    with allure.step("Ищем репозиторий на странице результата поиска"):
        page.get_search_result()

    with allure.step("В найденном репозитории переходим на вкладку Issues"):
        page.click_on_personal_git()

    with allure.step("Ищем Issue #80"):
        page.search_issue_on_page()
