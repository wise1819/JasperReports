# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 18:08:21 2019


"""

import json
#Flask, flask_restful muss installiert werden.
from flask import Flask
from flask_restful import Api, Resource,request
from requests.sessions import Session


class Data(Resource):
    def get(self, query):
		#Die Anfrage wird an den eigentlichen Server weitergeleitet mit den gewünschten Paramtern
        r = session.get(
            url+"/"+query,
            params=dict(request.args),
            headers=thisHeaders
        )
		#Umwandlung sollte eigentlich nicht nötig sein ansonsten warf der import im Studio jedoch Fehler.
        txt = r.content
        j = json.loads(txt)
        print(txt)
        return j


app = Flask(__name__)
api = Api(app)

#Path wird an die Klasse übergeben
api.add_resource(Data, "/<path:query>")
session = Session()
#[input] = die Adresse ohne weitere Path Komponenten wie z.B.: https://fu-projekt.bcs-hosting.de
url = "[input]/app/rest"
thisBody = {
	"userLogin":"[insert]",
	"userPwd":"[insert]"
}
thisHeaders = {"content-type": "application/json"}
#Holt sich den Authentifizierungstoken 
login = session.post(url+"/auth/login",json=thisBody,headers=thisHeaders)
print(login.cookies)


app.run(debug=False)