# AI: SQL to ORM Refactoring and Security Analysis

## Objective
Use an AI assistant to refactor a procedural Python script that uses raw SQL
(mysql.connector) into an object-oriented SQLAlchemy ORM solution, and analyze
the security and maintainability benefits.

## Files
- `original_script.py`: initial version using mysql.connector and raw SQL.
- `refactored_orm.py`: refactored version using a SQLAlchemy `User` model and Session.

## Prompt Used
I have a procedural Python script that uses mysql.connector and raw SQL to manage a `users` table in a MySQL database. I would like you to refactor it into a secure, professional, object-oriented solution using the SQLAlchemy Object-Relational Mapper (ORM), written in SQLAlchemy 2.0 style. The original code is in `original_script.py` (get_connection, create_user, get_user_by_username, update_user_email, delete_user, list_users).

Please refactor this script so that your response does all of the following. First, define the `User` class as a SQLAlchemy declarative model using `DeclarativeBase`, with an auto-incrementing integer primary key, plus a unique, non-nullable `username` and a unique, non-nullable `email`. Second, show how to create the database engine and session, and how to create the `users` table using the ORM through `Base.metadata.create_all`. Third, show how to add a new user using the ORM Session, including commit, error handling, and rollback on failure. Fourth, show how to query for that same user by username using the ORM Session and print the result. Fifth, convert the remaining functions (get user by username, update user email, delete user, and list users) into their ORM equivalents. Finally, explain in detail why the SQLAlchemy ORM version is a more professional and secure solution than using raw SQL with string formatting, covering SQL injection prevention, abstraction, readability, maintainability, database portability, and error handling. Please keep the code comments brief so that the complete refactored code and the full explanation fit in a single screenshot.

## What Changed
- The `users` table is now defined by a `User` declarative model.
- Tables are created with `Base.metadata.create_all`.
- Create, read, update, delete, and list operations use the ORM Session.
- Failed commits are rolled back with `session.rollback()`.

## Setup
```
pip install sqlalchemy mysql-connector-python
```
Update `DATABASE_URL` in `refactored_orm.py` with your own MySQL credentials.
For a quick test without MySQL, use `sqlite:///test.db` instead.

## Key Takeaways
- Security: the ORM parameterizes queries automatically, reducing SQL injection risk.
- Abstraction: code works with `User` objects (`user.email`) instead of tuples (`row[2]`).
- Maintainability: the model is a single source of truth for the table structure.
- Portability: switching databases mostly means changing the connection string.
