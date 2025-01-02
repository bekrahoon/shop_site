# shop_site

This is a Django-based e-commerce application.

## Requirements
- Python 3.x
- Django 4.x
- PostgreSQL (or use SQLite for development)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/bekrahoon/shop_site.git
   cd shop_site
    ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
    ```
3. **Activate the virtual environment:**
* On Windows: 
    ```bash
    venv\Scripts\activate
    ```
* On Unix or MacOS:
  ```bash
  source venv/bin/activate
  ```
4. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```
5. Set up the database:

    If you are using SQLite (default for development), no additional setup is required. Otherwise, set up your PostgreSQL database in settings.py (DATABASES section).

6. **Run migrations:**
    ```bash
    python manage.py migrate
    ```
7. **Create a superuser:**
   
    To access the admin panel:
    ```bash
    python manage.py createsuperuser
    ```

8. Run the development server:
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
