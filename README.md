# Travel Blog API

A Django REST API for sharing travel experiences with features for creating posts, managing categories, uploading images, and engaging through comments and likes.

## Features

- **Authentication**: JWT-based user authentication and authorization
- **Posts**: Create, read, update, and delete travel blog posts with draft/published status
- **Categories**: Organize posts by travel categories (adventure, culture, food, etc.)
- **Images**: Upload and manage multiple images per post
- **Comments**: Add comments to posts with like functionality
- **Likes**: Like posts and comments
- **Travel Details**: Track places visited and dates for each post
- **Filtering**: Search and filter posts by category, tags, and other criteria

## Tech Stack

- **Backend**: Django 5.2 with Django REST Framework
- **Authentication**: JWT tokens with Simple JWT
- **Documentation**: Auto-generated API docs with drf-spectacular
- **Database**: SQLite (development)
- **File Storage**: Local media storage for images

## API Documentation

- **Swagger UI**: `/api/schema/swagger-ui/`
- **ReDoc**: `/api/schema/redoc/`

## Quick Start

1. Install dependencies: `pip install -r requirements.txt`
2. Run migrations: `python manage.py migrate`
3. Start server: `python manage.py runserver`
4. Access API docs at `http://localhost:8000/api/schema/swagger-ui/`
