# ShortUrls

<img src="static/assets/short-urls.png" alt="logo" width="100"/>

[Click Here To Visit](https://github.com/kushagra-aa/shorturls)

A Fast URL Shortener,

It shortens The given URL using UUID.

> Made using JavaScript and Django

Built with 🤍 For You!

## Screenshots
![image](https://user-images.githubusercontent.com/68841296/134166828-b14f8c94-ae17-4120-ba94-3c29706842df.png)
![image](https://user-images.githubusercontent.com/68841296/134166838-39c775f7-b3a0-47b2-85ea-89a671eecfc2.png)
![image](https://user-images.githubusercontent.com/68841296/134166845-f56e6f58-84c0-45d4-8172-bfd4ab771252.png)
![image](https://user-images.githubusercontent.com/68841296/134166847-384bbf6d-7f98-4dde-a43b-b1bcf09227e6.png)
## Run Locally

Clone the project

```bash
  git clone https://github.com/kushagra-aa/shorturls.git
```

Go to the project directory

```bash
  cd shorturls
```

Install dependencies

```bash
  pip install -r requirements.txt
```

then run

```bash
python manage.py migrate
```

create admin account

```bash
python manage.py createsuperuser
```

then

```bash
python manage.py makemigrations
```

to makemigrations for the app

then again run

```bash
python manage.py migrate
```

to start the development server

```bash
python manage.py runserver
```

and open localhost:8000 on your browser to view the app.
