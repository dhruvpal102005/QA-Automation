import pytest
from playwright.sync_api import expect
from pages.pom_elements import LoginPage, DashboardPage
from utils.api_client import APIClient

def test_project_creation_flow(page, env_config):
    """
    1. Create project via API
    2. Verify in Web UI
    3. Verify Tenant Isolation
    """
    tenant_a = "company1"
    tenant_b = "company2"
    project_name = "Automation Test Project"
    
    # 1. API: Create project for Tenant A
    api = APIClient(env_config["api_url"], "test-token-tenant-a")
    project = api.create_project(tenant_a, project_name, "Created via API")
    project_id = project["id"]
    
    try:
        # 2. Web UI: Verify project display for Tenant A
        login_page = LoginPage(page)
        dashboard = DashboardPage(page)
        
        page.goto(f"https://{tenant_a}.workflowpro.com/login")
        login_page.login("admin@company1.com", "password123")
        
        # Verify it appears on dashboard
        expect(dashboard.project_cards).to_contain_text(project_name)
        
        # 3. Security: Verify tenant isolation (Tenant B should NOT see it)
        page.context.clear_cookies()
        page.goto(f"https://{tenant_b}.workflowpro.com/login")
        login_page.login("user@company2.com", "password123")
        
        # Verify it does NOT appear on Tenant B's dashboard
        texts = [card.inner_text() for card in dashboard.project_cards.all()]
        assert project_name not in texts, f"Project {project_name} leaked to {tenant_b}!"

    finally:
        # Cleanup: Delete the project via API
        api.delete_project(tenant_a, project_id)

def test_mobile_compatibility(page, env_config):
    """
    Simulate mobile access (Device emulation logic in conftest.py)
    """
    # This test would be run with MOBILE=true env variable
    page.goto(env_config["base_url"])
    expect(page.locator(".mobile-menu")).to_be_visible()
    # ... further mobile-specific validations
