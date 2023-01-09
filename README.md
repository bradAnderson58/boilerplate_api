
### To Run
This project was setup using Poetry, if you want to use the exact versions of everything, just run `poetry install` from the top level dir and it will install all the dependencies. Then you can start the poetry shell with `poetry shell` command. You can run the project locally with `python manage.py runserver`.
```bash
poetry install
poetry shell
> python manage.py runserver
```

If you dont want to mess with all that right now, as long as you are on some version of Python 3, you can probably just run

```bash
pip install django django-cors-headers django-restframework djangorestframework-simplejwt
python manage.py runserver
``` 

and it will probably work.

### API Docs
These are the endpoints I made (they will all be on `http://localhost:8000/` when running locally)

- `POST` `api/token`: This is the login endpoint, it returns a "token" and "refresh" which is a refresh token. For authenticated calls, add "Authentication": "Bearer [token]" to the header
- `POST` `api/token/refresh`: For refreshing authentication. I changed the token timeout to 2 days in the settings.py file because doing this manually in Postman is a pain.
- `GET` `api/profile`: This returns the profile of the currently logged in user.
- `GET` `api/book`: This returns all the books in the database
- `POST` `api/book`: Create a new Book. No Id provided because its a new book.
- `GET` `api/book/<book-id>`: This returns one book based on ID
- `PUT` `api/book/<book-id>`: This updates a book by Id. Note, all the fields are required because its not a Patch
- `PATCH` `api/book/<book-id>`: This updates a book by Id. Only the fields that are being changed need to be provided.
- `DELETE` `api/book/<book-id>`: Guess what

### Notes on SQL
By default Django kicks up a little SQLite DB and uses that, and I didn't change it. If you want to point it at a Postgres db, you can go into the settings.py and change the `DATABASES` field to point to it. I included `psycopg2` in the poetry dependencies, so which is the python postgres adapter.

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '<db name>',
        'USER': '<db_username>',
        'PASSWORD': '<password>',
        'HOST': '<hostname>',
        'PORT': '<port>'
    }
}
```

If you are setting up a new db, you will have to run `python manage.py migrate` to add the tables and such to the new db. Also, you will need to create at least one superuser (then you can go in and create other users in the /admin).
`python manage.py createsuperuser`
