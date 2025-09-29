pytest

sudo docker build -t unmeshw/flaskwebapp:v1 .

sudo docker push unmeshw/flaskwebapp:v1

sudo docker rm -f flaskwebapp

sudo docker run -dit --name flaskwebapp -p 5000:5000 unmeshw/flaskwebapp:v1
