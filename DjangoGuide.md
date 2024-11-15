# Django Project Basic Guide

This guide provides a simple, step-by-step overview of how to work on a Django project. It covers setting up your project, handling URLs, creating views, and managing templates. Whether you're new to Django or need a refresher, this guide will help you get started.

---

## Table of Contents

1. [Setting Up a Django Project](#1-setting-up-a-django-project)
   - [Install Django](#install-django)
   - [Create a New Project](#create-a-new-project)
   - [Create a New App](#create-a-new-app)
2. [Handling URLs](#2-handling-urls)
   - [Project-Level URLs](#project-level-urls)
   - [App-Level URLs](#app-level-urls)
3. [Creating Views](#3-creating-views)
   - [Function-Based Views](#function-based-views)
   - [Class-Based Views](#class-based-views)
4. [Template Handling](#4-template-handling)
   - [Setting Up Templates Directory](#setting-up-templates-directory)
   - [Creating Templates](#creating-templates)
   - [Rendering Templates in Views](#rendering-templates-in-views)
5. [Additional Tips](#5-additional-tips)

---

## 1. Setting Up a Django Project

Before you can handle URLs, views, and templates, you need to set up your Django project and application.

### Install Django

1. **Ensure Python is Installed:**

   Make sure you have Python installed. You can check by running:

   ```bash
   python3 --version
   ```

2. **Install Django Using pip:**

   It's recommended to use a virtual environment.

   ```bash
   # Install virtualenv if not already installed
   pip install virtualenv

   # Create a virtual environment
   virtualenv venv

   # Activate the virtual environment
   source venv/bin/activate

   # Install Django
   pip install django
   ```

### Create a New Project

1. **Start a New Django Project:**

   Replace `myproject` with your desired project name.

   ```bash
   django-admin startproject myproject
   ```

2. **Navigate to Project Directory:**

   ```bash
   cd myproject
   ```

### Create a New App

1. **Start a New App:**

   Replace `myapp` with your desired app name.

   ```bash
   python manage.py startapp myapp
   ```

2. **Register the App in `settings.py`:**

   Open `myproject/settings.py` and add `'myapp'` to the `INSTALLED_APPS` list.

   ```python
   INSTALLED_APPS = [
       # ...
       'myapp',
   ]
   ```

---

## 2. Handling URLs

URLs are how users navigate through your Django application. You'll define URL patterns that map to views.

### Project-Level URLs

1. **Open `myproject/urls.py`:**

   This file defines the root URL configurations.

2. **Include App URLs:**

   Modify `myproject/urls.py` to include URLs from your app.

   ```python
   from django.contrib import admin
   from django.urls import path, include

   urlpatterns = [
       path('admin/', admin.site.urls),
       path('', include('myapp.urls')),  # Include app URLs
   ]
   ```

### App-Level URLs

1. **Create `urls.py` in Your App:**

   If not already present, create a `urls.py` file inside `myapp`.

   ```bash
   touch myapp/urls.py
   ```

2. **Define URL Patterns in `myapp/urls.py`:**

   ```python
   from django.urls import path
   from . import views

   urlpatterns = [
       path('', views.home, name='home'),
       path('about/', views.about, name='about'),
   ]
   ```

   - `''`: The root URL of the app.
   - `'about/'`: A URL for the about page.

---

## 3. Creating Views

Views handle the logic behind each URL. They process requests and return responses.

### Function-Based Views

1. **Open `myapp/views.py`:**

2. **Define Views:**

   ```python
   from django.shortcuts import render

   def home(request):
       return render(request, 'home.html')

   def about(request):
       return render(request, 'about.html')
   ```

   - **`home` View:** Renders the `home.html` template.
   - **`about` View:** Renders the `about.html` template.

### Class-Based Views

Alternatively, you can use class-based views for more complex functionalities.

1. **Import Generic Views:**

   ```python
   from django.views import View
   from django.shortcuts import render
   ```

2. **Define a Class-Based View:**

   ```python
   class HomeView(View):
       def get(self, request):
           return render(request, 'home.html')

   class AboutView(View):
       def get(self, request):
           return render(request, 'about.html')
   ```

3. **Update `myapp/urls.py` to Use Class-Based Views:**

   ```python
   from django.urls import path
   from .views import HomeView, AboutView

   urlpatterns = [
       path('', HomeView.as_view(), name='home'),
       path('about/', AboutView.as_view(), name='about'),
   ]
   ```

---

## 4. Template Handling

Templates define the HTML structure of your web pages.

### Setting Up Templates Directory

1. **Create a `templates` Directory:**

   Inside your app (`myapp`), create a `templates` directory.

   ```bash
   mkdir myapp/templates
   ```

2. **Organize Templates:**

   It's good practice to create a subdirectory with your app's name to avoid naming conflicts.

   ```bash
   mkdir myapp/templates/myapp
   ```

   - Example: `myapp/templates/myapp/home.html`

3. **Configure Template Settings:**

   Ensure Django knows where to find your templates. In `myproject/settings.py`, verify the `TEMPLATES` setting.

   ```python
   TEMPLATES = [
       {
           'BACKEND': 'django.template.backends.django.DjangoTemplates',
           'DIRS': [],  # Add global templates directory here if needed
           'APP_DIRS': True,  # Enables Django to look for templates inside app directories
           'OPTIONS': {
               'context_processors': [
                   'django.template.context_processors.debug',
                   'django.template.context_processors.request',
                   'django.contrib.auth.context_processors.auth',
                   'django.contrib.messages.context_processors.messages',
               ],
           },
       },
   ]
   ```

   - **`APP_DIRS: True`** allows Django to search for templates inside each app's `templates` folder.

### Creating Templates

1. **Create `home.html`:**

   ```html
   <!-- myapp/templates/myapp/home.html -->
   <!DOCTYPE html>
   <html>
   <head>
       <title>Home Page</title>
   </head>
   <body>
       <h1>Welcome to the Home Page</h1>
       <p>This is the home page of your Django application.</p>
       <a href="{% url 'about' %}">About</a>
   </body>
   </html>
   ```

2. **Create `about.html`:**

   ```html
   <!-- myapp/templates/myapp/about.html -->
   <!DOCTYPE html>
   <html>
   <head>
       <title>About Page</title>
   </head>
   <body>
       <h1>About Us</h1>
       <p>This page contains information about us.</p>
       <a href="{% url 'home' %}">Home</a>
   </body>
   </html>
   ```

### Rendering Templates in Views

As shown in the views section, use the `render` function to render templates.

```python
from django.shortcuts import render

def home(request):
    return render(request, 'myapp/home.html')

def about(request):
    return render(request, 'myapp/about.html')
```

- **`render(request, 'myapp/home.html')`:** Tells Django to render the `home.html` template located in `myapp/templates/myapp/`.

---

## 5. Additional Tips

- **Run the Development Server:**

  To see your changes, run the Django development server.

  ```bash
  python manage.py runserver
  ```

  Visit `http://127.0.0.1:8000/` in your web browser.

- **Migrate Database Changes:**

  Whenever you make changes to models, run migrations.

  ```bash
  python manage.py makemigrations
  python manage.py migrate
  ```

- **Create a Superuser:**

  To access the Django admin interface.

  ```bash
  python manage.py createsuperuser
  ```

- **Collect Static Files:**

  For serving static files in production.

  ```bash
  python manage.py collectstatic
  ```

- **Use Django’s Template Inheritance:**

  To avoid repeating HTML code, use base templates.

  ```html
  <!-- myapp/templates/myapp/base.html -->
  <!DOCTYPE html>
  <html>
  <head>
      <title>{% block title %}My Django Site{% endblock %}</title>
  </head>
  <body>
      <header>
          <h1>My Django Site</h1>
          <nav>
              <a href="{% url 'home' %}">Home</a>
              <a href="{% url 'about' %}">About</a>
          </nav>
      </header>
      <main>
          {% block content %}{% endblock %}
      </main>
      <footer>
          <p>&copy; 2024 My Django Site</p>
      </footer>
  </body>
  </html>
  ```

  Then, extend `base.html` in other templates.

  ```html
  <!-- myapp/templates/myapp/home.html -->
  {% extends 'myapp/base.html' %}

  {% block title %}Home - My Django Site{% endblock %}

  {% block content %}
  <h2>Welcome to the Home Page</h2>
  <p>This is the home page of your Django application.</p>
  {% endblock %}
  ```

- **Use URL Namespaces:**

  For larger projects with multiple apps, namespaces help organize URLs.

  ```python
  # myapp/urls.py
  from django.urls import path
  from . import views

  app_name = 'myapp'

  urlpatterns = [
      path('', views.home, name='home'),
      path('about/', views.about, name='about'),
  ]
  ```

  Update templates to use namespaces.

  ```html
  <a href="{% url 'myapp:about' %}">About</a>
  ```

- **Debugging:**

  If you encounter issues:

  - **Check URL Patterns:** Ensure URLs are correctly mapped.
  - **Verify Template Paths:** Ensure templates are in the right directories.
  - **Use Django’s Debug Mode:** Set `DEBUG = True` in `settings.py` during development to see detailed error pages.

---

## Conclusion

This basic guide provides the foundational steps to work on a Django project, including setting up the project, handling URLs, creating views, and managing templates. As you become more comfortable with Django, you can explore more advanced features and best practices to enhance your application's functionality and maintainability.

For further learning, consider exploring the [official Django documentation](https://docs.djangoproject.com/en/stable/).