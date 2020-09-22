# Security Introday Coding Challenge

## The challenge

Here is a badly written application with many flaws.

Your task is to:

1. Study the application **as a whole** and identify the flaws. Try to fix as many of them as possible*.
2. Containerize the application.
3. Present the improved application and show us the changes you made.

Notes: \*Some flaws cannot be fixed immediately. Document them and explain why they are bad and what will you change.

## Demo application

### Requirements

#### System

- GNU/Linux
- `python` >= 3.7
- `pip` >= 9.0

`>=` means any version of the package, above or equal to the specified version.

#### Application

This application requires `tornado` python package.

You can install them by using:

```bash
pip install tornado
```

Although things do not have to be this way :wink: 

### :rocket: Starting the application

Application can be found in `main.py` file. You can start the application by using:

```bash
python main.py
```

Visit http://localhost:8000. Login with **admin:letmein**.

#### Database

The application comes with a simple predefined sqlite3 database file `db`. There are two tables:

**users** table

| Column   | Type         | Null | Note        |
| -------- | ------------ | ---- | ----------- |
| id       | INTEGER      | No   | Primary key |
| username | VARCHAR(255) | No   |             |
| password | VARCHAR(255) | No   |             |

**fruits** table

| Column   | Type         | Null | Note        |
| -------- | ------------ | ---- | ----------- |
| id       | INTEGER      | No   | Primary key |
| name     | VARCHAR(255) | No   |             |
| quantity | INTEGER      | No   |             |
