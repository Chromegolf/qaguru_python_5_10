from page.github_pages import GitHubPages

def test_github():
    page = GitHubPages()
    page.open()
    page.set_search_value()
    page.get_search_result()
    page.click_on_personal_git()
    page.search_issue_on_page()