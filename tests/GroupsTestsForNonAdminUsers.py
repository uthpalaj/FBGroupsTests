import unittest
import json
from selenium import webdriver
from pages.homepage import FacebookHomePage
from pages.loginPage import FacebookLoginPage
from pages.grouppage import FacebookGroupsPage
from locators.locators import GroupLocators

class TestFacebookGroupPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.facebook_homepage = FacebookHomePage(self.driver)
        self.login_page = FacebookLoginPage(self.driver)
        self.groups_page = FacebookGroupsPage(self.driver)

    def tearDown(self):
        self.driver.quit()


# As a non admin user 
# When I go to the groups page
# Then I should able to see the posts
# And the like, comment , report options
    def test_user_view_group_post_as_a_non_admin(self):
        self.login_page.open()
        with open("data.json", "r") as f:
            data = json.load(f)
        self.login_page.login(data.username, data.password)
        self.facebook_homepage.go_to_group_page(data.groupurl)
        self.assertTrue(self.facebook_homepage.is_group_page_opened())
        self.assert_element(GroupLocators.likeBtn)
        self.assert_element(GroupLocators.comment)
        self.assert_element(GroupLocators.report)

# As a non admin user 
# When I add a reaction to the post
# Then I should see it as a success
    def test_user_add_reaction_to_a_post_as_a_non_admin(self):
        self.login_page.open()
        with open("data.json", "r") as f:
            data = json.load(f)
        self.login_page.login(data.username, data.password)
        self.facebook_homepage.go_to_group_page(data.groupurl)
        self.assertTrue(self.facebook_homepage.is_group_page_opened())
        self.groups_page.addReaction('like')
        self.assert_element(GroupLocators.reactionSuccess)

# As a non admin user 
# When I add a comment to the post
# Then I should see it as a success
    def test_user_add_comment_to_a_post_as_a_non_admin(self):
        self.login_page.open()
        with open("data.json", "r") as f:
            data = json.load(f)
        self.login_page.login(data.username, data.password)
        self.facebook_homepage.go_to_group_page(data.groupurl)
        self.assertTrue(self.facebook_homepage.is_group_page_opened())
        self.groups_page.addComment(data.comment)
        self.assert_element(GroupLocators.commentSuccess)

# As a non admin user 
# When I report a post
# Then I should see it as a success
    def test_user_report_a_post_as_a_non_admin(self):
        self.login_page.open()
        with open("data.json", "r") as f:
            data = json.load(f)
        self.login_page.login(data.username, data.password)
        self.facebook_homepage.go_to_group_page(data.groupurl)
        self.assertTrue(self.facebook_homepage.is_group_page_opened())
        self.groups_page.reportPost()
        self.assert_element(GroupLocators.reportSucess)

# As a non admin user 
# When I add a new post
# Then it should goes to admin review
    def test_user_add_new_post_as_a_non_admin(self):
        self.login_page.open()
        with open("data.json", "r") as f:
            data = json.load(f)
        self.login_page.login(data.username, data.password)
        self.facebook_homepage.go_to_group_page(data.groupurl)
        self.assertTrue(self.facebook_homepage.is_group_page_opened())
        self.groups_page.addNewPost()
        self.assert_element(GroupLocators.addReportSuccess)
      
        

if __name__ == "__main__":
    unittest.main()
