import datetime as DT
import requests
import SpinTest.SpinTestClass as spintestModule
import SpinTest.test as importedModule #for testing purposes
from flask import Flask, render_template, make_response,jsonify,request
#Added this comment from company laptop to test if shit works

app = Flask(__name__)

a={'first':3,'second':4}

#Preparing containers to store incoming data. None of these should be 0, so if they're sent to python as 0 
#we know something's wrong.
#Fluid properties
densityParticle=0
densityFeed=0
kinViscosity=0

#Equipment properties
Rcentrifuge=0
V1=0
V2=0
L1=0
L2=0


#Spintest Data
Nstart1=0
Nstart2=0
Nstart3=0
Nstart4=0

spintime1=0
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






def do_calculations():
    #ensure spintimes are provided as number of minutes
    
    spintimes=[spintime1, spintime2, spintime3,spintime4]
    Nstarts=[Nstart1,Nstart2,Nstart3,Nstart4]
    Speeds=[speed1,speed2,speed3,speed4]
    ResidualSolids=[residualSolids1,residualSolids2,residualSolids3,residualSolids4]
    
    spintimes_min=[]
    refTime=DT.datetime(1900,1,1)
    print("\n\n\n\n")
    for time in spintimes:
        temp=DT.datetime.strptime(time,'%M:%S')
        time_in_minutes=(temp-refTime).total_seconds()/60
        spintimes_min.append(time_in_minutes)
        
        

    #remember to add TempSpinTest and Needed Q to below call once they have been added to form.
        
        
    spintest_object=spintestModule.SpinTest(spinTimes=spintimes_min,Nstart=Nstarts,speeds=Speeds,residualSol=ResidualSolids,\
                                            densityfeed=densityFeed,densityparticle=densityParticle,kinviscosity=kinViscosity,\
                                            L1=L1,L2=L2,V1=V1,V2=V2,rCentrifuge=Rcentrifuge,neededQ=NeededQ,tempSpinTest=TempSpinTest)
    print(spintest_object)
    return



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
   # print(incomingData)
   

    #We expect a certain order of incoming data, but try to avoid guessing the name right in case angular did something
    #The keys correspond to the names of the Formcontrols in angular
    save_fluid_properties(incomingData)
    do_calculations()
    return response

def save_fluid_properties(incomingData):
    list_of_the_keys=list(incomingData.keys())
    global densityParticle
    global densityFeed
    global kinViscosity
    densityParticle=incomingData[list_of_the_keys[0]]
    densityFeed=incomingData[list_of_the_keys[1]]
    kinViscosity=incomingData[list_of_the_keys[2]]
    




def _process_equipment_properties(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    #Take the incoming data and turning it into a python recognized dictionary
    incomingData=request.get_json(force=True)
    #print(incomingData)
    #We expect a certain order of incoming data, but try to avoid guessing the name right in case angular did something
    #The keys correspond to the names of the Formcontrols in angular
    save_equipment_properties(incomingData)
    return response

def save_equipment_properties(incomingData):
    list_of_the_keys=list(incomingData.keys())
    
    global Rcentrifuge
    global V1
    global V2
    global L1
    global L2

    Rcentrifuge=incomingData[list_of_the_keys[0]]
    
    V1=incomingData[list_of_the_keys[1]]
    V2=incomingData[list_of_the_keys[2]]
    L1=incomingData[list_of_the_keys[3]]
    L2=incomingData[list_of_the_keys[4]]

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

    global TempSpinTest
    global NeededQ
    
    
  
    spintime1=incomingData[list_of_the_keys[0]]
    print(spintime1)
    print(type(spintime1))
    spintime2=incomingData[list_of_the_keys[1]]
    spintime3=incomingData[list_of_the_keys[2]]
    spintime4=incomingData[list_of_the_keys[3]]
    
    Nstart1=incomingData[list_of_the_keys[4]]
    print(Nstart1)
    print(type(Nstart1))
    Nstart2=incomingData[list_of_the_keys[5]]
    Nstart3=incomingData[list_of_the_keys[6]]
    Nstart4=incomingData[list_of_the_keys[7]]


    speed1=incomingData[list_of_the_keys[8]]
    print(speed1)
    print(type(speed1))
    speed2=incomingData[list_of_the_keys[9]]
    speed3=incomingData[list_of_the_keys[10]]
    speed4=incomingData[list_of_the_keys[11]]

    residualSolids1=incomingData[list_of_the_keys[12]]
    print(residualSolids1)
    print(type(residualSolids1))
    residualSolids2=incomingData[list_of_the_keys[13]]
    residualSolids3=incomingData[list_of_the_keys[14]]
    residualSolids4=incomingData[list_of_the_keys[15]]

    TempSpinTest=incomingData[list_of_the_keys[16]]
    NeededQ=incomingData[list_of_the_keys[17]]
    return



def _generate_results():
    do_calculations()
    
    return



#routes and what happens when you send a request to them
@app.route('/')
def hello_world():
    return "This is the backend server. You can send post requests to /send_fluid_properties,/send_equipment_properties and /send_spintest_data."



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
    
@app.route('/fetch_results',methods=['GET'])
def respond_with_results():
    return _generate_results()



app.run()

