# coding:utf-8

import json
import httplib
import requests

apiVersion = "v1"
tvApiBaseUrl = "webapi.teamviewer.com"
tvApiPort = 443

def RequestOAuthAccessToken(strClientId, strClientSecret, strAuthorizationCode):
    print ""
    print "Get token..."
    print "Request [POST] /api/" + apiVersion + "/oauth2/token"
    result = False

    try:
        conn = httplib.HTTPSConnection(tvApiBaseUrl, tvApiPort)
        conn.connect()

        request = conn.putrequest('POST', '/api/' + apiVersion + '/oauth2/token')

        payload = "grant_type=authorization_code&code=" + strAuthorizationCode \
                  + "&client_id=" + strClientId \
                  + "&client_secret=" + strClientSecret

        headers = {}
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['Content-Length'] = "%d" % len(payload)
        for k in headers:
            conn.putheader(k, headers[k])
        conn.endheaders()

        print "Payload :" + payload
        conn.send(payload)

        resp = conn.getresponse()
        statusStr = resp.reason
        statusCode = resp.status

        print statusCode, statusStr

        if (statusCode != 200):
            print "Unexpected response code. Received content was:"
            print resp.read()
            result = False
            return result

        jsonResp = json.loads(resp.read())
        result = jsonResp

        print jsonResp
        print result
        print "Token received."

    except Exception as e:
        print "Request failed! The error was: ", e
        result = False

    return result

def PingAPI(accessToken):

    print ""
    print "Ping API..."
    print "Request [GET] /api/" + apiVersion + "/ping"
    result = False

    try:
        conn = httplib.HTTPSConnection(tvApiBaseUrl, tvApiPort)
        conn.connect()

        request = conn.putrequest('GET', '/api/' + apiVersion + '/ping')

        headers = {}
        headers['Authorization'] = 'Bearer ' + accessToken
        for k in headers:
            conn.putheader(k, headers[k])
        conn.endheaders()

        resp = conn.getresponse()
        statusStr = resp.reason
        statusCode = resp.status

        print statusCode, statusStr

        if (statusCode != 200):
            print "Unexpected response code. Received content was:"
            print resp.read()
            result = False
            return result

        jsonResp = json.loads(resp.read())
        tokenValue = jsonResp["token_valid"]

        if(tokenValue == True):
            print "Ping: Token is valid"
            result = True
        else:
            result = False

    except Exception, e:
        print "Request failed! The error was: ", e
        result = False

    return result

def GetMeetingApi(accessToken, meetingID):
    print ""
    print "get details meeting of " + meetingID
    print "Request [GET] /api/" + apiVersion + "/meetings"
    result = False

    try:
        conn = httplib.HTTPSConnection(tvApiBaseUrl, tvApiPort)
        conn.connect()

        request = conn.putrequest('GET', '/api/' + apiVersion + '/meetings/' + meetingID)


        headers = {}
        headers['Content-Type'] = 'application/json; charset=utf-8'
        headers['Authorization'] = 'Bearer ' + accessToken

        for k in headers:
            conn.putheader(k, headers[k])
        conn.endheaders()

        conn.send("")

        resp = conn.getresponse()
        statusStr = resp.reason
        statusCode = resp.status

        print statusCode, statusStr

        if (statusCode != 200):
            print "Unexpected response code. Received content was:"
            print resp.read()

            result = False
            return result

        result = json.loads(resp.read())
        print result["participant_web_link"]
        print "Request ok!"

    except Exception as e:
        print "Request failed! The error was: ", e
        result = False

    return result

def CreateNewMeetingApi(accessToken):
    try:
        data = '{"instant": "true"}'
        headers = {'Content-Type': 'application/json',
                   'Authorization': 'Bearer ' + accessToken}
        response =  requests.post('https://webapi.teamviewer.com/api/v1/meetings', data=data, headers=headers)
        result = response.text
        return result
    except Exception, e:
        print e
        result = False
        return result

def GetNewTokenWithRefreshToken(strClientId, strClientSecret, refreshToken):
    print ""
    print "Get token..."
    print "Request [POST] /api/" + apiVersion + "/oauth2/token"
    result = False

    try:
        conn = httplib.HTTPSConnection(tvApiBaseUrl, tvApiPort)
        conn.connect()

        request = conn.putrequest('POST', '/api/' + apiVersion + '/oauth2/token')

        payload = "grant_type=refresh_token&refresh_token=" + refreshToken \
                  + "&client_id=" + strClientId \
                  + "&client_secret=" + strClientSecret

        headers = {}
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        headers['Content-Length'] = "%d" % len(payload)
        for k in headers:
            conn.putheader(k, headers[k])
        conn.endheaders()

        print "Payload :" + payload
        conn.send(payload)

        resp = conn.getresponse()
        statusStr = resp.reason
        statusCode = resp.status

        print statusCode, statusStr

        if (statusCode != 200):
            print "Unexpected response code. Received content was:"
            print resp.read()
            result = False
            return result

        jsonResp = json.loads(resp.read())
        result = jsonResp

        print jsonResp
        print result
        print "Token received."

    except Exception as e:
        print "Request failed! The error was: ", e
        result = False

    return result

