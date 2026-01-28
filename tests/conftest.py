import pytest
import os
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def env_config():
    """Load environment specific configurations."""
    return {
        "base_url": os.getenv("BASE_URL", "https://app.workflowpro.com"),
        "api_url": os.getenv("API_URL", "https://api.workflowpro.com/v1"),
        "browser": os.getenv("BROWSER", "chromium"),
        "tenant_id": os.getenv("TENANT_ID", "company1")
    }

@pytest.fixture(scope="function")
def browser_context(env_config):
    """Fixture to handle browser specifics, including mobile emulation and BrowserStack."""
    with sync_playwright() as p:
        # Check if we are using BrowserStack
        if os.getenv("BROWSERSTACK") == "true":
            # BrowserStack capabilities
            caps = {
                'browser': 'chrome',
                'browser_version': 'latest',
                'os': 'osx',
                'os_version': 'Ventura',
                'name': 'WorkFlow Pro: Project Creation Flow',
                'build': 'Bynry-QA-Case-Study',
                'browserstack.user': os.getenv('BS_USER', 'your_username'),
                'browserstack.key': os.getenv('BS_KEY', 'your_key')
            }
            # Construct BrowserStack URL
            bs_url = f"wss://cdp.browserstack.com/playwright?caps={caps}"
            browser = p.chromium.connect(bs_url)
            context = browser.new_context()
        
        # Local Mobile Emulation
        elif os.getenv("MOBILE") == "true":
            device = p.devices["iPhone 13"]
            browser = p.chromium.launch(headless=True)
            context = browser.new_context(**device)
        
        # Local Desktop
        else:
            browser_type = getattr(p, env_config["browser"])
            browser = browser_type.launch(headless=True)
            context = browser.new_context(viewport={'width': 1280, 'height': 720})
        
        yield context
        browser.close()

@pytest.fixture(scope="function")
def page(browser_context):
    page = browser_context.new_page()
    yield page
    page.close()
