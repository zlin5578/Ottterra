# Use the Python 3.12 base image suitable for Mac M1 (Apple Silicon)
FROM --platform=linux/arm64 python:3.12

# Set the working directory
WORKDIR /app
COPY ./Dockerfile/requirements.txt /app/requirements.txt

# Copy local code to the container
COPY ./otter_backend_impl /app/

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
# RUN ./thirds/google-cloud-sdk/install.sh -y

# Expose Django port 8006
EXPOSE 8006

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8006"]