# coding:utf-8


from app import app
from werkzeug.contrib.fixers import ProxyFix


app.wsgi_app = ProxyFix(app.wsgi_app)
# app.run(debug=True, host='192.168.1.6')
app.run(debug=True)
