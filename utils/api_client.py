import requests

class APIClient:
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

    def create_project(self, tenant_id, name, description):
        endpoint = f"{self.base_url}/api/v1/projects"
        headers = self.headers.copy()
        headers["X-Tenant-ID"] = tenant_id
        
        payload = {
            "name": name,
            "description": description,
            "team_members": []
        }
        
        response = requests.post(endpoint, json=payload, headers=headers)
        response.raise_for_status()
        return response.json()

    def delete_project(self, tenant_id, project_id):
        # Implementation for cleanup
        endpoint = f"{self.base_url}/api/v1/projects/{project_id}"
        headers = self.headers.copy()
        headers["X-Tenant-ID"] = tenant_id
        requests.delete(endpoint, headers=headers)
