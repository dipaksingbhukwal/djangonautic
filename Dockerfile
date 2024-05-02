# Use the official Python image as a base
FROM python:3.9

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    DJANGO_SETTINGS_MODULE=djangonautic.settings \
    DATABASE_URL=sqlite:///db.sqlite3

# Set up the working directory
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project files to the working directory
COPY . /app/

# Run migrations
RUN python manage.py makemigrations
RUN python manage.py migrate

# Expose port 8000
EXPOSE 8000

# Command to run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]