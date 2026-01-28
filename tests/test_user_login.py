import pytest
import re
from playwright.sync_api import Page, expect

# Corrected version with reliability improvements
def test_user_login(page: Page):
    """
    Refactored login test using web-first assertions and proper waiting logic.
    """
    # Navigate to login page
    page.goto("https://app.workflowpro.com/login")
    
    # Fill login form
    page.fill("#email", "admin@company1.com")
    page.fill("#password", "password123")
    
    # Click and wait for navigation or state change
    page.click("#login-btn")
    
    # RELIABILITY FIX: Use web-first assertions that automatically retry
    expect(page).to_have_url(re.compile(r".*/dashboard"), timeout=10000)
    
    # RELIABILITY FIX: Ensure the element is attached and visible before asserting
    welcome_msg = page.locator(".welcome-message")
    expect(welcome_msg).to_be_visible()
    expect(welcome_msg).to_contain_text("Welcome")

def test_multi_tenant_access(page: Page):
    """
    Improved multi-tenant test with proper list handling and scoping.
    """
    page.goto("https://app.workflowpro.com/login")
    page.fill("#email", "user@company2.com")
    page.fill("#password", "password123")
    page.click("#login-btn")
    
    # RELIABILITY FIX: Wait for the dashboard to load by checking a key element
    expect(page.locator(".dashboard-container")).to_be_visible()
    
    # RELIABILITY FIX: Ensure at least one project card exists before iterating
    project_cards = page.locator(".project-card")
    expect(project_cards.first).to_be_visible()
    
    # Check all project cards for correct tenant data
    cards_count = project_cards.count()
    for i in range(cards_count):
        expect(project_cards.nth(i)).to_contain_text("Company2")

# NOTE: 2FA handling would require a setup/fixture or a mock/totp utility 
# which is added in the framework design section.
