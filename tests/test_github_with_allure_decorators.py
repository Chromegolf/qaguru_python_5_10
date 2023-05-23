import allure

from allure_commons.types import Severity

from page.github_page_with_allure_decorators import GitHubPages


@allure.tag("Web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "Ruslan Antipov")
@allure.feature("Задачи в репозитории")
@allure.story("Поиск issue в существующем репозитории")
@allure.description("Заходим на гит. Оп-оп-считай, и нашли issue")
@allure.testcase("PROJECT-1234")

def test_github_with_decorators_steps():

    page = GitHubPages()
    page.open()
    page.set_search_value('eroshenkoam/allure-example')
    page.get_search_result('eroshenkoam/allure-example')
    page.click_on_personal_git()
    page.search_issue_on_page('80')
