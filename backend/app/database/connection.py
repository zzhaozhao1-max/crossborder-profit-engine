"""Database connection foundation for CrossBorder Profit Engine."""

DATABASE_CONFIG = {
    "engine": "postgresql",
    "status": "planned",
}


def get_database_status():
    return DATABASE_CONFIG
