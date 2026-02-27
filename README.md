# GoldenBlogApplication

A Django-based blog application with user authentication, profiles, and blog management features.

## Overview

GoldenBlogApplication is a web application built with Django that provides a platform for users to create and manage blog posts. It includes user registration, authentication, profile management, and full blog functionality with posts, comments, categories, and tags.

## Features

- **User Management**: Custom user model with email-based authentication
- **User Profiles**: Extended user profiles with bio, profile picture, and website
- **Blog Posts**: Create, edit, and manage blog posts
- **Comments**: Users can comment on posts
- **Categories and Tags**: Organize posts with categories and tags
- **REST API**: Built with Django REST Framework for API endpoints
- **JWT Authentication**: Secure authentication using JSON Web Tokens
- **Docker Support**: Containerized deployment with Docker and Docker Compose

## Project Structure

```
GoldenBlogApplication/
├── core/                          # Main Django project directory
│   ├── core/                      # Project settings and configuration
│   │   ├── settings.py            # Django settings
│   │   ├── urls.py                # Main URL configuration
│   │   ├── asgi.py                # ASGI configuration
│   │   └── wsgi.py                # WSGI configuration
│   ├── accounts/                  # User accounts app
│   │   ├── models.py              # User and Profile models
│   │   ├── admin.py               # Admin interface configuration
│   │   ├── views.py               # API views
│   │   ├── urls.py                # URL patterns
│   │   ├── apps.py                # App configuration
│   │   ├── tests.py               # Unit tests
│   │   └── migrations/            # Database migrations
│   └── blog/                      # Blog functionality app
│       ├── models.py              # Post, Comment, Category, Tag models
│       ├── admin.py               # Admin interface
│       ├── views.py               # API views
│       ├── urls.py                # URL patterns
│       ├── apps.py                # App configuration
│       ├── tests.py               # Unit tests
│       └── migrations/            # Database migrations
├── requirements.txt               # Python dependencies
├── Dockerfile                     # Docker container configuration
├── docker-compose.yml             # Docker Compose setup
├── .gitignore                     # Git ignore rules
└── README.md                      # This file
```

## Technology Stack

- **Backend**: Django 6.0.2
- **Database**: PostgreSQL
- **API Framework**: Django REST Framework 3.15.2
- **Authentication**: Django REST Framework Simple JWT 5.3.1
- **Image Handling**: Pillow 10.4.0
- **Configuration**: Python Decouple 3.8
- **Containerization**: Docker, Docker Compose

## Models

### Accounts App
- **User**: Custom user model with email authentication
- **Profile**: User profile with bio, profile picture, and website

### Blog App
- **Post**: Blog posts with title, content, author, and creation date
- **Comment**: Comments on posts
- **Category**: Post categories
- **Tag**: Post tags
- **PostCategory**: Many-to-many relationship between posts and categories
- **PostTag**: Many-to-many relationship between posts and tags

## Setup and Installation

### Prerequisites
- Python 3.12+
- Docker and Docker Compose (for containerized setup)
- PostgreSQL (if running without Docker)

### Local Development Setup

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd GoldenBlogApplication
   ```

2. **Create environment variables**:
   Create a `.env` file in the root directory with:
   ```
   SECRET_KEY=your-secret-key-here
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1
   DATABASE_URL=postgresql://user:password@localhost:5432/dbname
   ```

3. **Using Docker Compose** (recommended):
   ```bash
   docker-compose up --build
   ```

4. **Manual setup**:
   ```bash
   # Install dependencies
   pip install -r requirements.txt

   # Run migrations
   cd core
   python manage.py migrate

   # Create superuser
   python manage.py createsuperuser

   # Run development server
   python manage.py runserver
   ```

### API Endpoints

- `/admin/` - Django admin interface
- `/api/accounts/` - User authentication and profile endpoints
- `/api/blog/` - Blog posts, comments, categories, and tags endpoints

## Usage

After setup, you can:
- Register new users via the API
- Authenticate users with JWT tokens
- Create and manage blog posts
- Add comments to posts
- Organize content with categories and tags
- Access the admin interface for content management

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests
5. Submit a pull request

## License

This project is licensed under the MIT License.
