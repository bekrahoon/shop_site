# shop_site

This is a Django-based e-commerce application.

## Table of Contents
1. [Requirements](#requirements)
2. [Installation](#installation)
   1. [Clone the repository](#clone-the-repository)
   2. [Create a virtual environment](#create-a-virtual-environment)
   3. [Activate the virtual environment](#activate-the-virtual-environment)
   4. [Install the required packages](#install-the-required-packages)
   5. [Create a .env file](#create-a-env-file)
   6. [Set up the database](#set-up-the-database)
   7. [Run migrations](#run-migrations)
   8. [Create a superuser](#create-a-superuser)
   9. [Run the development server](#run-the-development-server)
3. [Testing Data](#testing-data)
4. [Running the Project with Docker](#running-the-project-with-docker)
   1. [Install Docker](#install-docker)
   2. [Clone the Repository](#clone-the-repository-1)
   3. [Create a .env file](#create-a-env-file-1)
   4. [Build and Run the Docker Containers](#build-and-run-the-docker-containers)
   5. [Run Migrations](#run-migrations-1)
   6. [Create a Superuser](#create-a-superuser-1)
   7. [Access the Application](#access-the-application)
   8. [Stopping the Containers](#stopping-the-containers)
   

## Requirements
- Python 3.x
- Django 4.x
- PostgreSQL (or use SQLite for development)

## Installation

1. #### **Clone the repository:**

   ```bash
   git clone https://github.com/bekrahoon/shop_site.git
   cd shop_site
    ```

2. #### **Create a virtual environment:**
   ```bash
   python -m venv venv
    ```
3. #### **Activate the virtual environment:**
* On Windows: 
    ```bash
    venv\Scripts\activate
    ```
* On Unix or MacOS:
  ```bash
  source venv/bin/activate
  ```
4. #### **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```
5. #### Create a .env file 
   like `env.examenv`

6. #### **Set up the database:**

    If you are using SQLite (default for development), no additional setup is required. Otherwise, set up your PostgreSQL database in settings.py (DATABASES section).

7. #### **Run migrations:**
    ```bash
    python manage.py migrate
    ```
8. #### **Create a superuser:**
   
    To access the admin panel:
    ```bash
    python manage.py createsuperuser
    ```

9.  #### Run the development server:
    ```bash
    python manage.py runserver
    ```
The project will be available at `http://127.0.0.1:8000/.`

## Testing Data
You can test the application by either using the default SQLite database or by manually adding data using the Django admin panel. If you need sample data for testing, you can use the following commands:
```bash
# To add sample categories and products
python manage.py shell
```
Inside the Django shell, you can add some example data like this:

```python
from shop.models import Category, Product

# Creating categories
electronics = Category.objects.create(name="Electronics")
smartphones = Category.objects.create(name="Smartphones", parent=electronics)

# Creating products
Product.objects.create(name="iPhone 13", description="Latest Apple iPhone", price=999.99, category=smartphones)
Product.objects.create(name="Samsung Galaxy S21", description="Latest Samsung smartphone", price=799.99, category=smartphones)
```

## Running the Project with Docker
To run your project with Docker, follow these steps:

1. ### Install Docker
   
Make sure Docker is installed on your machine. You can follow the installation guide for your operating system here: [Docker Installation](https://docs.docker.com/get-started/get-docker/)

2. ### Clone the Repository
If you haven't cloned the repository yet, run:
```bash
git clone https://github.com/bekrahoon/shop_site.git
cd shop_site
```
3. ### Create a .env file 
    **like `env.examenv`**

4. ### Build and Run the Docker Containers
Run the following command to build the Docker images and run the containers:
```bash
docker-compose up --build
```
1. ### Run Migrations
Once the containers are up and running, you need to apply database migrations. Open a terminal in the project root directory and run:
```bash
docker-compose exec web python manage.py migrate
```
This will apply all the migrations in the Django project.

1. ### Create a Superuser
To access the Django admin panel, create a superuser by running the following command:

```bash
docker-compose exec web python manage.py createsuperuser
```
Follow the prompts to set up the admin credentials.

7. ### Access the Application
After running the server, your application should be available at `http://localhost:8000/`.

8. ### Stopping the Containers
To stop the Docker containers, press Ctrl + C in the terminal and then run:
```bash
docker-compose down
```
This will stop and remove all containers.
