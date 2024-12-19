# Base image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    DJANGO_SETTINGS_MODULE=library_management_system.settings

# Set working directory inside the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && apt-get clean

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Collect static files
RUN python /app/manage.py collectstatic --no-input

# Install Nginx and copy the Nginx configuration file
RUN apt-get update && apt-get install -y nginx
COPY nginx.conf /etc/nginx/nginx.conf

# Copy the collected static files to the appropriate location for Nginx
COPY static /app/static/

# Expose application port
EXPOSE 8000

# Start the application (gunicorn can be used for production)
CMD ["gunicorn", "--workers", "3", "--bind", "0.0.0.0:8000", "library_management_system.wsgi:application"]
