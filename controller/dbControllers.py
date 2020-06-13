"""
The CONTROLLER should call Functions from MODELS Only

The CONTROLLER will be always between View and Models

Here we operate the data, in this example we make a data conversion, decoding from base64
"""
from model.dbModels import connectdbModel
from base64 import b64decode

def connectdbController():
    return b64decode(connectdbModel()).decode('utf-8', "ignore")