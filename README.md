# student-cli

![Python](https://img.shields.io/badge/Python-3.x-c9a227?style=flat-square)
![SQLite](https://img.shields.io/badge/Database-SQLite-7fae6f?style=flat-square)
![Status](https://img.shields.io/badge/Status-Practice_Project-c1666b?style=flat-square)

A command-line student management system with admin login and a SQLite backend — built to practice core Python and SQL before moving on to **FastAPI**.

```
$ python admin.py
gave your username: admin1234
enter password: ••••

school grade 7 to 9
 1. add student
 2. show student
 3. find student by name
 4. update students
 5. delete students
 6. exit
type the number: _
```

## About

This project is a small CLI tool for managing student records: names, grades, and a running grade history, stored in a local SQLite database. Access is gated behind a simple admin login. It's a deliberately hands-on exercise — reading input, validating it, and talking to a real database — rather than a polished product.

## Features

| Command | Description |
|---|---|
| **Add** | Register a new student with a name and grade level (7–9), rejecting duplicates |
| **Show** | List all students, or filter by grade level |
| **Find** | Look up a single student by name |
| **Update** | Edit a student's grade history, name, or grade level |
| **Delete** | Remove a student record |
| **Auth** | A separate `admin.py` entry point gates access before `start()` runs |

## Project structure

```
.
├── admin.py     # login gate, then calls start() from main.py
├── main.py      # CLI menu loop + all SQLite operations
└── full.db      # SQLite database (created on first run)
```

## Running it

```bash
python admin.py
```

Log in with the admin credentials, then use the numbered menu to manage student records. The database file is created automatically on first run if it doesn't exist.

## Fixed while building

- ✅ Database connection was being closed immediately after table creation, breaking every later menu option.
- ✅ Changes weren't committed after insert/update/delete — calls were left incomplete instead of calling `commit()`.
- ✅ Result rows were being indexed incorrectly, so records printed as scrambled fragments instead of full rows.
- ✅ A stray comma in an `INSERT` statement and a couple of typos in column names and method calls.
- ✅ A login check in `admin.py` used `and` where it needed `or`, letting a wrong password slip through silently.

## What's next

- Keep extending this CLI as practice: cleaner error handling, maybe a proper class-based structure around the database logic.
- Once this feels solid, move on to **learning FastAPI** — likely by rebuilding this same student-management idea as a real API with endpoints instead of a menu loop.

---
*A learning project — built to practice Python, SQL, and debugging real (self-inflicted) bugs.*
