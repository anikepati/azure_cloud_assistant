from utils.azure_auth import get_graph_client

class IAMAgent:
    def assign_role(self, user_a_id, user_b_id, role_id, scope):
        client = get_graph_client()
        result = client.post(
            url='https://graph.microsoft.com/v1.0/roleManagement/directory/roleAssignments',
            json={
                "principalId": user_b_id,
                "roleDefinitionId": role_id,
                "directoryScopeId": scope
            }
        )
        return result.json()