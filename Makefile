run:
	python manage.py runserver

makemig:
	python manage.py makemigrations team_app

migrate:
	python manage.py migrate team_app

reapply:
	python manage.py migrate team_app zero
	python manage.py makemigrations
	python manage.py migrate