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
    """Fixture to handle browser specifics, including mobile emulation."""
    with sync_playwright() as p:
        browser_type = getattr(p, env_config["browser"])
        
        # Check if mobile emulation is requested
        if os.getenv("MOBILE") == "true":
            device = p.devices["iPhone 13"]
            browser = browser_type.launch(headless=True)
            context = browser.new_context(**device)
        else:
            browser = browser_type.launch(headless=True)
            context = browser.new_context(viewport={'width': 1280, 'height': 720})
        
        yield context
        browser.close()

@pytest.fixture(scope="function")
def page(browser_context):
    page = browser_context.new_page()
    yield page
    page.close()
