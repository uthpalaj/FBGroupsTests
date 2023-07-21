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

# As an admin user 
# When I go to the groups page
# Then I should able to moderate post
    def test_user_edit_a_post_as_an_admin(self):
        self.login_page.open()
        with open("data.json", "r") as f:
            data = json.load(f)
        self.login_page.login(data.usernameAdmin, data.passwordAdmin)
        self.facebook_homepage.go_to_group_page(data.groupurl)
        self.assertTrue(self.facebook_homepage.is_group_page_opened())
        self.groups_page.moderatePost(GroupLocators.post, data.text)
        self.assert_element(GroupLocators.postmodificationSuccess)


# As an admin user 
# When I go to the groups page
# Then I should able to delete a post
    def test_user_delete_a_post_as_an_admin(self):
        self.login_page.open()
        with open("data.json", "r") as f:
            data = json.load(f)
        self.login_page.login(data.usernameAdmin, data.passwordAdmin)
        self.facebook_homepage.go_to_group_page(data.groupurl)
        self.assertTrue(self.facebook_homepage.is_group_page_opened())
        self.groups_page.deletePost(GroupLocators.post)
        self.assert_element(GroupLocators.deleteSuccess)

# As an admin user 
# When I go to the groups page
# Then I should able to delete a comment
    def test_user_delete_a_comment_as_an_admin(self):
        self.login_page.open()
        with open("data.json", "r") as f:
            data = json.load(f)
        self.login_page.login(data.usernameAdmin, data.passwordAdmin)
        self.facebook_homepage.go_to_group_page(data.groupurl)
        self.assertTrue(self.facebook_homepage.is_group_page_opened())
        self.groups_page.deletePost(GroupLocators.comment)
        self.assert_element(GroupLocators.deleteCommentSuccess)

# As an admin user 
# When I go to the groups page
# Then I should able to moderate comment
    def test_user_edit_a_comment_as_an_admin(self):
        self.login_page.open()
        with open("data.json", "r") as f:
            data = json.load(f)
        self.login_page.login(data.usernameAdmin, data.passwordAdmin)
        self.facebook_homepage.go_to_group_page(data.groupurl)
        self.assertTrue(self.facebook_homepage.is_group_page_opened())
        self.groups_page.moderateComment(GroupLocators.comment, data.text)
        self.assert_element(GroupLocators.commentmodificationSuccess)

# As an admin user 
# When I go to the groups page
# Then I should able to review post and approve them
    def test_user_approve_a_post_as_an_admin(self):
        self.login_page.open()
        with open("data.json", "r") as f:
            data = json.load(f)
        self.login_page.login(data.usernameAdmin, data.passwordAdmin)
        self.facebook_homepage.go_to_group_page(data.groupurl)
        self.assertTrue(self.facebook_homepage.is_group_page_opened())
        self.groups_page.approvePost(GroupLocators.post)
        self.assert_element(GroupLocators.approvePostSuccess)

# As an admin user 
# When I go to the groups page
# Then I should able to review post and decline them
    def test_user_decline_a_post_as_an_admin(self):
        self.login_page.open()
        with open("data.json", "r") as f:
            data = json.load(f)
        self.login_page.login(data.usernameAdmin, data.passwordAdmin)
        self.facebook_homepage.go_to_group_page(data.groupurl)
        self.assertTrue(self.facebook_homepage.is_group_page_opened())
        self.groups_page.declinePost(GroupLocators.post)
        self.assert_element(GroupLocators.declinetSuccess)

# As an admin user 
# When I go to the groups page
# Then I should able to ban a user
    def test_user_ban_a_user_as_an_admin(self):
        self.login_page.open()
        with open("data.json", "r") as f:
            data = json.load(f)
        self.login_page.login(data.usernameAdmin, data.passwordAdmin)
        self.facebook_homepage.go_to_group_page(data.groupurl)
        self.assertTrue(self.facebook_homepage.is_group_page_opened())
        self.groups_page.banUser(GroupLocators.user)
        self.assert_element(GroupLocators.banUserSuccess)