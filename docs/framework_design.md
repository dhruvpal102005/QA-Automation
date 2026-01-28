# Part 2: Test Framework Design Document

## 1. Folder Structure
```text
QA_Automation_Repo/
├── tests/              # Test scripts (Login, Projects, etc.)
│   ├── conftest.py     # Global fixtures & configurations
│   └── test_*.py       # UI and API tests
├── pages/              # Page Object Model (POM) classes
│   └── *.py            # Selectors and page-specific actions
├── utils/              # Helper utilities
│   ├── api_client.py   # API wrapper for backend services
│   └── auth_helper.py  # 2FA / Token management
├── data/               # Test data (JSON/CSV/Env vars)
├── docs/               # Documentation & Test Plans
├── reports/            # Test execution results (Allure/HTML)
├── requirements.txt    # Project dependencies
└── pytest.ini          # Pytest execution settings
```

## 2. Configuration Management
- **Environment Variables**: We use `.env` files and OS environment variables to switch between `Production`, `Staging`, and `Dev` environments.
- **Tenant Handling**: The `base_url` is dynamically constructed based on the tenant ID (e.g., `{tenant}.workflowpro.com`).
- **BrowserStack Integration**: Added via a custom fixture in `conftest.py` that connects to the BrowserStack grid using specific capabilities for iOS/Android.

## 3. Missing Requirements & Clarifying Questions
To build a production-ready framework, I would ask the following questions:
1. **2FA Bypass**: For automated tests, do we have a "Master Secret" or a dedicated test-only 2FA bypass?
2. **Data Cleanup**: Is there a "Sandbox" database reset capability, or should we implement cleanup via API after every test run?
3. **Parallel Execution**: What is the target concurrency? (This informs how we design test data to avoid locking records).
4. **Reporting**: Do we need Jira/TestRail integration for test results?
5. **Secrets Management**: Where should API tokens and BrowserStack keys be stored? (Recommendation: GitHub Secrets or AWS Secrets Manager).
6. **Mobile Infrastructure**: Are we testing on physical devices or emulators for local development?
