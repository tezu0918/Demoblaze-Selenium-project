from Demoblaze.Server.API.Constant import home_constant
from random import randint

class HomeConstant(home_constant):
    num = randint(1, 2500)
    URL = "https://www.demoblaze.com/index.html"
    data_valid = {'birthDate': "2000-02-02",
                  'email': f"yoss{num}@ss.com",
                  'lastName': "Meshuulam",
                  'name': "Avi",
                  'password': "123456"}
    data_invalid = {'birthDate': "2000-02-02",
                    'email': "yossi111@ss.com",
                    'lastName': "Meshuulam",
                    'name': "Avi",
                    'password': "123456"}