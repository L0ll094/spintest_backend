
import requests
from flask import Flask, render_template, make_response,jsonify,request


app = Flask(__name__)

a={'first':3,'second':4}

#Preparing containers to store incoming data
#Fluid properties
densityfeed=0
densityParticle=0
kinviscosity=0

#Equipment properties
L1=0
L2=0
V1=0
V2=0

#Spintest Data
Nstart1=0
Nstart2=0
Nstart3=0
Nstart4=0

spintime1=0
spintime2=0
spintime3=0
spintime4=0

speed1=0
speed2=0
speed3=0
speed4=0

residualSolids1=0
residualSolids2=0
residualSolids3=0
residualSolids4=0

tempSpinTest=0
neededQ=0



def _build_cors_preflight_response():
    response = make_response()
    response.headers.add('Access-Control-Allow-Origin', "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    return response

def _corsify_actual_response(response):
    response.headers.add("Access-Control-Allow-Origin", "*")

# After many tests now we seem to be able to force the incoming data into json format

# ________I contain this data_________
# b'{"densityParticle":2,"densityFeed":4,"kinviscosity":32}'
# _______which is of the type_________
# <class 'bytes'>
# ________Or you can look at it this way_________
# b'{"densityParticle":2,"densityFeed":4,"kinviscosity":32}'
# _______which is of the type_________
# <class 'bytes'>
# ______Testing request.args
# ImmutableMultiDict([])
# ______Testing request.form
# ImmutableMultiDict([])
# ________Testing request.values
# CombinedMultiDict([ImmutableMultiDict([]), ImmutableMultiDict([])])
# ______Testing request.json with get_json(force=true):
# {'densityParticle': 2, 'densityFeed': 4, 'kinviscosity': 32}
# Therefore I shall force it to be json and then try and access it as a dictionary
    print("\n________I contain this data, printed as request.get_data()_________")
    print(request.get_data())

    incomingData=request.get_json(force=True)

    print("_______Saving request.get_json(force=true as incomingData and printing 'incomingData' below:________\n")
    print(incomingData)
    print("\nType of 'incomingData'")
    print(type(incomingData))
    

    



    return response



@app.route('/')
def hello_world():
    return "hello world"




#This is a get Endpoint, since it is accessed through a URL. 
# #Because i send hidden payloads in the body when posting. 
@app.route('/testpage')
def resopond_to_get_request():
    if request.method == "OPTIONS":
        return _build_cors_preflight_response()
    if request.method == "GET":
        return _corsify_actual_response(jsonify(a))

@app.route('/testpagepost', methods = ['POST'])
def respond_to_post_request():
    if request.method == "OPTIONS":
        print("\n\n The request method was indeed Options first\n\n")
        return _build_cors_preflight_response()
    if request.method == "POST":
        print("\n\n The request method was then POST\n\n")
        #It seems to only go post never options anymore. Shall try to do without the corsify
        #Nope doesn't work we need it.
        return _corsify_actual_response(jsonify(a))
    




app.run()

