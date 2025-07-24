function_schema = [
    {
        "name": "assign_iam_role",
        "description": "Assign IAM role from one user to another",
        "parameters": {
            "type": "object",
            "properties": {
                "from_user": {
                    "type": "string",
                    "description": "The source user who has the IAM role"
                },
                "to_user": {
                    "type": "string",
                    "description": "The target user to assign the IAM role to"
                },
                "role_name": {
                    "type": "string",
                    "description": "The name of the IAM role to assign"
                }
            },
            "required": ["from_user", "to_user", "role_name"]
        }
    },
    {
        "name": "check_app_insights",
        "description": "Check App Insights for anomaly or health metrics",
        "parameters": {
            "type": "object",
            "properties": {
                "app_id": {
                    "type": "string",
                    "description": "Azure Application Insights App ID"
                },
                "api_key": {
                    "type": "string",
                    "description": "API key for accessing App Insights data"
                }
            },
            "required": ["app_id", "api_key"]
        }
    }
]
