FROM redhat/ubi8

WORKDIR /app

COPY requirements.txt .

# For dependencies
RUN dnf install python3-pip -y && pip3 install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python3", "app.py"]
