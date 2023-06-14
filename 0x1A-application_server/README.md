# Application server

## 0. Set up development with Python
```
python3 -m web_flask.0-hello_route on window1
curl 127.0.0.1:5000/airbnb-onepage/ on window2
```

## 1. Set up production with Gunicorn
```
pip3 install gunicorn flask
sudo lsof -i :6000
gunicorn --bind 0.0.0.0:5000 web_flask.0-hello_route:app on terminal 1
curl 127.0.0.1:5000/airbnb-onepage/ on terminal 2
```
