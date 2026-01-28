# Part 1: Analysis of Flaky Test Code

## Identified Flakiness Issues
1. **Static URL Assertion**: `assert page.url == "..."` fails if the redirection takes a few milliseconds longer than the execution of the line. Playwright's execution is faster than the browser's network/rendering cycle.
2. **Lack of Dynamic Waits**: `page.click("#login-btn")` followed immediately by assertions doesn't account for the "loading state" of the dashboard.
3. **Implicit Timing Dependencies**: The test assumes `.welcome-message` is visible immediately. If there's an animation or secondary API call, the test will fail.
4. **Tenant Isolation Check**: In `test_multi_tenant_access`, `page.locator(".project-card").all()` might return an empty list if the cards haven't rendered yet, and the `for` loop would pass silently even if no data is shown.
5. **No Visual State Handling**: CI environments often have different viewport sizes, which can cause elements to be hidden or require scrolling.

## Root Causes: CI/CD vs. Local Environment
1. **Resource Constraints**: CI runners (GitHub Actions, Jenkins) usually have fewer CPU/RAM resources than a local developer machine, leading to slower page renders and API responses.
2. **Network Latency**: CI environments might have different DNS resolution times or proxy configurations, affecting `page.goto` and authentication speed.
3. **Headless Execution**: CI runs in "headless" mode. Some elements behave differently when not rendered in a physical window (e.g., hover effects, focus).
4. **Environment Consistency**: "Cold starts" of the application in a fresh CI environment can cause the first few tests to be significantly slower.

## Proposed Fixes
- Use **Web-First Assertions** (`expect(page).to_have_url`) which have built-in retry logic.
- Implement **Explicit Waits** for specific network responses or element states.
- Use **Page Object Model (POM)** to separate selectors from logic (implemented in Part 2).
- Add **Browser Context** configuration for consistent viewports.
