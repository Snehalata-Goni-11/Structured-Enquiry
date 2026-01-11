# Use official Python image 
FROM python:3.12-slim

# Set working directory
WORKDIR /digital

# Copy all files to container
COPY . .

# Command to run python file
CMD ["python", "digital_habit.py"]