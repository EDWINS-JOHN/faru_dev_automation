import configparser
import email


config=configparser.RawConfigParser()
config.read("..\\configuration\\config.ini")


class ReadConfig:
    @staticmethod
    def getAppUrl():
        URL=config.get('common data', 'baseURL')
        return URL
        
    @staticmethod
    def getEmail():
        email=config.get('common data', 'email')
        return email
        
        
    @staticmethod
    def getPassword():
        password=config.get('common data','password')
        return password
        