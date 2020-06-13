"""
The Main should call Functions from VIEWS Only
"""

from view.dbViews import connectdbView

if __name__ == '__main__':
    connectdbView()


"""
The layers dialog

View: Hi Controller, The user just asked to access Facebook! Get his login data there.

Controller: OK. I'll send you the answer. Hey model, my bro, take this login data and check if it's right

Model: The data is valid. Sending the login response.

Controller: OK. View, the user entered the correct data. I will send you his data and you load the profile page.

View: Thanks, Controller. Displaying for the user.


- A story by A1S0N
"""