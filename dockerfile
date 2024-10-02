# Use the official Python image from the Docker Hub
FROM python:3.11.4

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt ./

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the dataset to the container
COPY App/chatbot/data/dataset.xlsx App/chatbot/data/

# Copy the application code to the container
COPY App/ App/
COPY api.py ./
COPY main.py ./

# Expose the port your app runs on
EXPOSE 5000

# Command to run the application
CMD ["python", "api.py"]
