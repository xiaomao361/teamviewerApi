# coding:utf-8

import redis


class Database:  
    def __init__(self):  
        self.host = 'localhost'  
        self.port = 6379  

    def write(self, key, val):
        try:  
            key = key
            val = val
            r = redis.StrictRedis(host=self.host, port=self.port)
            r.set(key, val)
        except Exception, exception:  
            print exception  

    def read(self, key):
        try:  
            key = key
            r = redis.StrictRedis(host=self.host, port=self.port)
            value = r.get(key)  
            print value  
            return value  
        except Exception, exception:  
            print exception  
