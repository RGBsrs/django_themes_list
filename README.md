# django_themes_list
## App that shows themes list and generate pdf file with chosen themes
 
### If you want test this project on your local machine run the following commands:

> git init
> 
> git clone https://github.com/RGBsrs/flask_api_course.git

### Then create virtual enviroment:

> virtualenv env

### Activate this enviroment:

- On Linux/Mac
> env/bin/activate

- On Windows
> env/Scripts/activate

### Install all dependencies:
> pip install -r requirements.txt

## For PDFkit package need install additional package as written here link(https://pypi.org/project/pdfkit/)

### Than run migrations:

> python manage.py migrate

### And now you can start this app:

> python manage.py runserver
