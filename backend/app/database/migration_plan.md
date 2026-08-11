# V3.6 Database Migration Plan

## Core Tables

- users
- workspaces
- stores
- platform_connections
- orders
- settlements
- profit_records
- sync_tasks

## Relationship

User -> Workspace -> Store -> Orders -> Profit Records

Platform connections belong to stores and provide API synchronization capability.

Future implementation:

- PostgreSQL
- SQLAlchemy ORM
- Alembic migrations
