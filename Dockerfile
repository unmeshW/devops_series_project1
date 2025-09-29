# Use a lightweight Python image
FROM redhat/ubi8

# Set working directory
WORKDIR /app

# Copy dependency file
COPY requirements.txt .

# Install dependencies
RUN dnf install python3-pip -y && pip3 install --no-cache-dir -r requirements.txt

# Copy app files
COPY . .

# Expose Flask app port
EXPOSE 5000

# Run the Flask app
CMD ["python3", "app.py"]
