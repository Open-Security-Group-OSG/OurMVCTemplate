"""
The VIEWS should call Functions from CONTROLLER Only
"""

from controller.dbControllers import connectdbController

def connectdbView():
    print(connectdbController())