# Use the official Python 3.8 image as the base image
FROM python:3.8

# Set the working directory inside the container
WORKDIR /app

# Copy the local directory contents to the container at /app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Define the default command to run the application
CMD ["python", "./manage.py"]
