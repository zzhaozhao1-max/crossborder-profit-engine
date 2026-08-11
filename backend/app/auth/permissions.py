"""Role permission definitions."""

ROLES = {
    "owner": ["manage_store", "view_profit", "upload_data"],
    "admin": ["view_profit", "upload_data"],
    "analyst": ["view_profit"],
}


def has_permission(role, permission):
    return permission in ROLES.get(role, [])
