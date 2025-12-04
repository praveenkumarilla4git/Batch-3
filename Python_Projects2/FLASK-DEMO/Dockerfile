# 1. Base Image: We specifically ask for Python 3.13.2 (Slim version)
FROM python:3.13.2-slim

# 2. Work Directory: Create a folder inside the container called /app
WORKDIR /app

# 3. Install Dependencies: Run pip inside the container
RUN pip install flask

# 4. Copy Code: Copy app.py from Windows to the container
COPY app.py .

# 5. Command: Run the app when container starts
CMD ["python", "app.py"]