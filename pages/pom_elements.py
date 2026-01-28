from playwright.sync_api import Page, expect

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self, path: str):
        # Base URL is expected to be provided via config/fixture
        self.page.goto(path)

    def wait_for_load_state(self):
        self.page.wait_for_load_state("networkidle")

class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.email_input = page.locator("#email")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#login-btn")

    def login(self, email, password):
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.login_button.click()

class DashboardPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.welcome_message = page.locator(".welcome-message")
        self.project_cards = page.locator(".project-card")
        self.create_project_btn = page.locator("#create-project-btn")

    def get_project_texts(self):
        expect(self.project_cards.first).to_be_visible()
        return self.project_cards.all()
