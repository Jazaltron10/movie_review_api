# **Movie Review API**

Welcome to the **Movie Review API**, a Django-based REST API that allows users to register, authenticate, and submit reviews for various movies. This project is designed to provide a secure, scalable, and user-friendly platform for managing movie reviews, leveraging Django's robust framework, token authentication, and the Django REST Framework (DRF) for API management.

---

## **Table of Contents**
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Project Structure](#project-structure)
5. [Installation and Setup](#installation-and-setup)
6. [Authentication](#authentication)
7. [Endpoints](#endpoints)
8. [Pagination and Filtering](#pagination-and-filtering)
9. [Contributing](#contributing)
10. [License](#license)

---

## **Project Overview**
The **Movie Review API** is designed to allow users to:
- **Create an account** and **authenticate** using token-based authentication.
- **Submit reviews** for movies, rate them, and view reviews by others.
- **Search, filter**, and **paginate** through the list of movies and reviews efficiently.

The project uses a custom **User model**, integrates **Django REST Framework** for API management, and supports **token authentication** for secure access. The API is flexible, making it easy for developers to integrate it into different client applications such as mobile apps, websites, or other frontend systems.

---

## **Features**
- **User Registration and Authentication**: Users can register and authenticate using tokens.
- **Movie Management**: Manage a collection of movies with title, genre, and release date.
- **Review System**: Users can submit reviews and ratings (1 to 5) for movies.
- **Filtering and Searching**: Find movies and reviews through search queries and filters.
- **Pagination**: Efficiently paginate through large datasets.
- **Admin Panel**: Admin users can manage movies, reviews, and user accounts via Django's admin interface.
- **Secure**: Token-based authentication ensures that only authorized users can perform certain actions (e.g., submit reviews).

---

## **Technologies Used**
This project leverages the following technologies:
- **Python 3.12.x**: Programming language for building the backend logic.
- **Django 5.x**: Web framework for rapid development and clean design.
- **Django REST Framework**: A powerful toolkit for building Web APIs in Django.
- **PostgreSQL** (optional): Database used in production environments for data storage.
- **SQLite**: Default database used for development.
- **Django-Allauth**: For handling user registration and social authentication.
- **WhiteNoise**: For static file management in production.
- **Docker** (optional): Containerization tool to deploy the project easily.
  
---

## **Project Structure**
Here's a quick look at the main folders and files:
```
├── movie_review_api/
│   ├── settings.py              # Main Django settings file
│   ├── urls.py                  # Project-level URL configuration
│   ├── wsgi.py                  # WSGI configuration for production
├── reviews/
│   ├── models.py                # Models for Movie and Review
│   ├── views.py                 # API views for handling movie and review requests
│   ├── serializers.py           # DRF serializers for data validation
│   ├── urls.py                  # URL routing for movie and review endpoints
├── users/
│   ├── models.py                # Custom User model and Profile
│   ├── admin.py                 # Custom admin registration for User and Profile
│   ├── serializers.py           # User serializers for DRF
│   ├── views.py                 # API views for handling user requests
├── manage.py                    # Django's management script
└── README.md                    # Project documentation
```

---

## **Installation and Setup**

### **1. Clone the repository:**
```bash
git clone https://github.com/yourusername/movie-review-api.git
cd movie-review-api
```

### **2. Create a virtual environment and activate it:**
```bash
python3 -m venv env
source env/bin/activate  # On Windows, use `env\Scripts\activate`
```

### **3. Install the project dependencies:**
```bash
pip install -r requirements.txt
```

### **4. Set up environment variables:**
You will need to create a `.env` file in the root of your project to store secret keys and database credentials:
```bash
SECRET_KEY=your-secret-key
DB_NAME=your-database-name
DB_USER=your-database-user
DB_PASSWORD=your-database-password
DB_HOST=localhost
DB_PORT=5432
```

### **5. Set up the database:**
If using PostgreSQL, ensure the database is running, then run the following commands to apply the migrations:
```bash
python manage.py migrate
```

### **6. Create a superuser (admin account):**
```bash
python manage.py createsuperuser
```

### **7. Run the development server:**
```bash
python manage.py runserver
```

Now, you can access the API at `http://127.0.0.1:8000/`.

---

## **Authentication**
This project uses **Token Authentication** provided by Django REST Framework. After registration, users can obtain their authentication token by logging in through the `/dj-rest-auth/login/` endpoint. Once the token is obtained, it should be included in the Authorization header of all requests.

Example of how to include the token in your request header:
```http
Authorization: Token <your-token-here>
```

---

## **Endpoints**
Below are the key endpoints in the API:

### **User Endpoints**:
- **POST** `/dj-rest-auth/registration/` – Register a new user
- **POST** `/dj-rest-auth/login/` – Log in and get a token
- **POST** `/dj-rest-auth/logout/` – Log out the user

### **Movie Endpoints**:
- **GET** `/api/movies/` – Retrieve the list of movies
- **GET** `/api/movies/{id}/` – Get details of a specific movie
- **POST** `/api/movies/` – Add a new movie (admin only)

### **Review Endpoints**:
- **GET** `/api/reviews/` – Retrieve the list of reviews
- **POST** `/api/reviews/` – Submit a new review (authenticated users)
- **GET** `/api/reviews/{id}/` – Retrieve a specific review

---

## **Pagination and Filtering**
The API supports **pagination**, **filtering**, and **searching** to efficiently handle large sets of data. Pagination is enabled by default and can be controlled via query parameters.

- **Pagination**: `http://127.0.0.1:8000/api/movies/?limit=5&offset=10`
- **Filtering**: Filter movies by title: `http://127.0.0.1:8000/api/movies/?title=Inception`
- **Search**: Search reviews by rating: `http://127.0.0.1:8000/api/reviews/?search=5`

---

## **Contributing**
Contributions to this project are welcome! Please follow the steps below:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

---

## **License**
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## **Contact**
If you have any questions or suggestions regarding the project, feel free to reach out via email at `jazaltron.jan@gmail.com`.

---