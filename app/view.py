# coding:utf-8

from app import app
import data
from flask import request, session, redirect, url_for, flash, render_template
from decorators import async
import api

accessToken = False
clientId = '101234-eRtZu12OM5WfR3XTGfCe'
clientSecret = "ZIDP9wS9lw19KHbxXG5B"
authorizationCode = "h86LjcLm"
redirect_uri = "https://h.tongxinyiliao.com"

@app.route('/')
@app.route('/index')
def index():
    print 'with out web views'

@app.route('/new_meeting')
def new_meeting():
    db = data.Database()

    accessToken = db.read('accessToken')
    checkAccessToken = api.PingAPI(accessToken)

    if (checkAccessToken != 'true'):
        refreshToken = db.read('refreshToken')
        tokens = api.GetNewTokenWithRefreshToken(clientId, clientSecret, refreshToken)
        db.write('accessToken', tokens["access_token"])
        db.write('refreshToken', tokens['refresh_token'])
        accessToken = tokens["access_token"]

    meeting = api.CreateNewMeetingApi(accessToken)
    print meeting