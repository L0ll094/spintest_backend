
import requests
from flask import Flask, render_template, make_response,jsonify,request


app = Flask(__name__)

a={'first':3,'second':4}

#Preparing containers to store incoming data
#Fluid properties
densityParticle=0
densityfeed=0
kinviscosity=0

#Equipment properties
Rcentrifuge=0
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


#Below code was copied from a solution on stack overflow to resole the issue of not having appropriate CORS headers
def _build_cors_preflight_response():
    response = make_response()
    response.headers.add('Access-Control-Allow-Origin', "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    return response

def _corsify_actual_response(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response




def _process_fluid_properties(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    #Take the incoming data and turning it into a python recognized dictionary
    incomingData=request.get_json(force=True)
    print(incomingData)

    #We expect a certain order of incoming data, but try to avoid guessing the name right in case angular did something
    #The keys correspond to the names of the Formcontrols in angular
    save_fluid_properties(incomingData)
    return response

def save_fluid_properties(incomingData):
    list_of_the_keys=list(incomingData.keys())
    global densityParticle
    global densityfeed
    global kinviscosity
    densityParticle=incomingData[list_of_the_keys[0]]
    densityfeed=incomingData[list_of_the_keys[1]]
    kinviscosity=incomingData[list_of_the_keys[2]]




def _process_equipment_properties(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    #Take the incoming data and turning it into a python recognized dictionary
    incomingData=request.get_json(force=True)
    print(incomingData)
    #We expect a certain order of incoming data, but try to avoid guessing the name right in case angular did something
    #The keys correspond to the names of the Formcontrols in angular
    save_equipment_properties(incomingData)
    return response

def save_equipment_properties(incomingData):
    list_of_the_keys=list(incomingData.keys())
    
    global Rcentrifuge
    global L1
    global L2
    global V1
    global V2

    Rcentrifuge=incomingData[list_of_the_keys[0]]
    L1=incomingData[list_of_the_keys[1]]
    L2=incomingData[list_of_the_keys[2]]
    V1=incomingData[list_of_the_keys[3]]
    V2=incomingData[list_of_the_keys[4]]

    return

def _process_spintest_data(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    #Take the incoming data and turning it into a python recognized dictionary
    incomingData=request.get_json(force=True)
    print(incomingData)

    #We expect a certain order of incoming data, but try to avoid guessing the name right in case angular did something
    #The keys correspond to the names of the Formcontrols in angular
    save_spintest_data(incomingData)
    return response
    

def save_spintest_data(incomingData):
    list_of_the_keys=list(incomingData.keys())

    global Nstart1
    global Nstart2
    global Nstart3
    global Nstart4

    global spintime1
    global spintime2
    global spintime3
    global spintime4

    global speed1
    global speed2
    global speed3
    global speed4

    global residualSolids1
    global residualSolids2
    global residualSolids3
    global residualSolids4

    global tempSpinTest
    global neededQ
    
    
    Nstart1=incomingData[list_of_the_keys[0]]
    Nstart2=incomingData[list_of_the_keys[1]]
    Nstart3=incomingData[list_of_the_keys[2]]
    Nstart4=incomingData[list_of_the_keys[3]]

    spintime1=incomingData[list_of_the_keys[4]]
    spintime2=incomingData[list_of_the_keys[5]]
    spintime3=incomingData[list_of_the_keys[6]]
    spintime4=incomingData[list_of_the_keys[7]]

    speed1=incomingData[list_of_the_keys[8]]
    speed2=incomingData[list_of_the_keys[9]]
    speed3=incomingData[list_of_the_keys[10]]
    speed4=incomingData[list_of_the_keys[11]]

    residualSolids1=incomingData[list_of_the_keys[12]]
    residualSolids2=incomingData[list_of_the_keys[13]]
    residualSolids3=incomingData[list_of_the_keys[14]]
    residualSolids4=incomingData[list_of_the_keys[15]]

    tempSpinTest=incomingData[list_of_the_keys[16]]
    neededQ=incomingData[list_of_the_keys[17]]
    return


    
    





#routes and what happens when you send a request to them
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

@app.route('/send_fluid_properties', methods = ['POST'])
def respond_to_fluid_properties():
    if request.method == "OPTIONS":
        return _build_cors_preflight_response()
    if request.method == "POST":
        #It seems to only go post never options anymore. Shall try to do without the corsify
        #Nope doesn't work we need it.
        return _process_fluid_properties(jsonify(a))
    
@app.route('/send_equipment_properties', methods = ['POST'])
def respond_to_equipment_properties():
    if request.method == "OPTIONS":
        return _build_cors_preflight_response()
    if request.method == "POST":
        #It seems to only go post never options anymore. Shall try to do without the corsify
        #Nope doesn't work we need it.
        return _process_equipment_properties(jsonify(a))

   
@app.route('/send_spintest_data', methods = ['POST'])
def respond_to_spintest_data():
    if request.method == "OPTIONS":
        return _build_cors_preflight_response()
    if request.method == "POST":
        #It seems to only go post never options anymore. Shall try to do without the corsify
        #Nope doesn't work we need it, but it is now just added to my other processing.
        return _process_spintest_data(jsonify(a))
    




app.run()

