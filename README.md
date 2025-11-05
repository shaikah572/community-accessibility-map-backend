
# Community Accessibility Map

## Description
Community Accessibility Map is a web application built with React and Django that allows users to find, add, and comment on accessible locations within their area. It provides an interactive map interface to explore places with accessibility features.

## Tech stack
- **Python** 
- **Django** 
- **Django REST Framework (DRF)**
- **django-cors-headers** 
- **Pillow**
- **psycopg2-binary**

## Backend Repository Link
[Community Accessibility Map Frontend](https://github.com/shaikah572/community-accessibility-map-frontend)

## ERD diagram
![image](https://i.postimg.cc/W1pfVfWh/Screenshot-2025-11-05-at-9-58-20-PM.png)

## Routing Table

| Mathod | URL Pattern                   | Action                     |
|--------|-------------------------------|----------------------------|
| GET    | /api/user/                    | get a single user          |
| PUT    | /api/user/                    | edit user                  |
| DELETE | /api/users/delete/            | delete user                |
| POST   | /api/login/                   | user login                 |
| POST   | /api/signup/                  | user register              |
| GET    | /api/markers/                 | get all markers            |
| POST   | /api/merkers/                 | add a marker               |
| GET    | /api/markers/:id/             | get a single marker        |
| PUT    | /api/markers/:id/             | edit a marker              |
| DELETE | /api/markers/:id/             | delete a marker            |
| GET    | /api/marker/:id/comments/     | get all marker comments    |
| POST   | /api/marker/:id/comments/     | post a comment on a marker |
| DELETE | /api/marker/:id/comments/:id/ | delete a comment           |
| GET    | /api/categories/              | get all categories         |
| GET    | /api/categories/:id/          | get a single category      |
| POST   | /api/categories/              | add a category             |
| PUT    | /api/categories/:id/          | edit a category            |
| DELETE | /api/categories/:id/          | delete a category          |


## Installation
1. Clone repository
```bash
git clone https://github.com/shaikah572/community-accessibility-map-frontend
git clone https://github.com/shaikah572/community-accessibility-map-backend
```
2. Install backend dependencies
```bash
pip install -r requirements.txt
```
3. Run migrations and start the backend server
```bash
python manage.py migrate
python manage.py runserver
```
4.In frontend directory install dependencies
```bash
npm install
```
5.Start the frontend server
```bash
npm run dev
```


## IceBox Features
- Rating Model
- Profile Model
- ...
