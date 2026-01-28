# QA Automation Case Study: WorkFlow Pro

A professional test automation framework built with Python, Pytest, and Playwright for a multi-tenant B2B SaaS platform.

## 🚀 Features
- **Multi-Tenant Support**: Dynamically handles multiple subdomains and client-specific data.
- **Cross-Platform**: Support for Web (Chromium, Firefox, Webkit) and Mobile emulation (iPhone/Android).
- **Hybrid Testing**: Combines API-driven setup with UI-driven validation for efficient E2E flows.
- **Page Object Model (POM)**: Highly maintainable and readable code structure.
- **Security Validation**: Explicit checks for tenant data isolation.

## 🛠️ Tech Stack
- **Language**: Python 3.x
- **Test Runner**: Pytest
- **Automation Engine**: Playwright
- **API Requests**: Requests library
- **Reporting**: Allure Framework (Configured)

## 📁 Repository Structure
- `tests/`: UI and API test scripts.
- `pages/`: Page Object classes for UI components.
- `utils/`: API clients, configuration loaders, and helpers.
- `docs/`: Technical documentation, Test Plan, and Analysis.
- `data/`: Placeholder for external test data.

## ⚙️ Setup & Execution
1. **Clone the repo**: `git clone <repo-url>`
2. **Setup virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   playwright install
   ```
4. **Run Tests**:
   - **All Tests**: `pytest`
   - **Web UI Specific**: `pytest tests/test_user_login.py`
   - **Mobile Emulation**: `MOBILE=true pytest tests/test_project_creation.py`
   - **API + UI Integration**: `pytest tests/test_project_creation.py`

## 📝 Part Analysis
- [Part 1: Debugging Analysis](docs/part1_analysis.md)
- [Part 2: Framework Design](docs/framework_design.md)
- [Part 3: Integration Test Logic](tests/test_project_creation.py)

---
*Created by Dhruv Pal as part of the Bynry Intern Case Study.*
