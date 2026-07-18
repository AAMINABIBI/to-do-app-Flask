# To-Do App (Flask + SQLite)

A simple task tracker built with Flask, Flask-SQLAlchemy, and SQLite.
Users can register, log in, add tasks, cycle a task's status
(Pending → Working → Done), and clear all tasks.

## Features

- User registration and login (passwords hashed with Werkzeug)
- Session-based authentication
- Add, view, and clear tasks
- Toggle task status through Pending → Working → Done
- SQLite database, created automatically on first run

## Tech stack

- Python 3
- Flask
- Flask-SQLAlchemy
- SQLite
- Jinja2 templates

## Project structure