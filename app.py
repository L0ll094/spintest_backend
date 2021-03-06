"""
Created by: setulsnc, Louise Stjern

"""



import datetime as DT
import requests
import SpinTest.SpinTestClass as spintestModule

from flask import Flask, make_response,jsonify,request,json
import pdb



app = Flask(__name__)
#Setting the important variable "theAnswer" to something at the start, so that it exists. 
theAnswer={'first':3,'second':4}

#Preparing variables where incoming data will be stored. Not necessarily needed in python but is done to give a proper overview for the next coder to look at this. None of them should be 0, so if they remain 0 after communicating with frontend, we know something's wrong.

#Equipment properties for the centrifuge and the sample tubes
Rcentrifuge=0
V1=0
V2=0
L1=0
L2=0
Va=0
Vb=0

Acc_t_1=0
Acc_t_2=0
Acc_t_3=0
Acc_t_4=0
Acc_t_5=0
Acc_t_6=0

Acc_rpm_1=0
Acc_rpm_2=0
Acc_rpm_3=0
Acc_rpm_4=0
Acc_rpm_5=0
Acc_rpm_6=0

Ret_t_1=0
Ret_t_2=0
Ret_t_3=0
Ret_t_4=0
Ret_t_5=0
Ret_t_6=0

Ret_rpm_1=0
Ret_rpm_2=0
Ret_rpm_3=0
Ret_rpm_4=0
Ret_rpm_5=0
Ret_rpm_6=0 



#Spintest Data for the spintest that was just run.
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

spintest_setup_successfully=False
equipment_setup_successfully=False





#The functions _build_cors_preflight_response()_corsify_actual_response() and addHeadersToResponse() were copied from a solution on stack overflow to resole the issue of not having appropriate CORS headers. The CORS headers seem to be a security measure regulating what requests this backend may or may not respond to.
def _build_cors_preflight_response():
    response = make_response()
    response.headers.add('Access-Control-Allow-Origin', "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    return response

def _corsify_actual_response(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

def addHeadersToResponse(response):
    #This is run after thaAnswer have been updated by the find_flowrate function
    #so that the response is something useful and not just the default value of theAnswer
    response.headers.add("Access-Control-Allow-Origin", "*")
    
    return response
    
    

# _process_equipment_properties()  is one of the two setup-functions. Once the user has filled out the information about their equipment (or chosen the defaults) and clicks "send", this function will take the info and save it in the respective global variable it belongs in.
#@input:-
#@output:-
def _process_equipment_properties():

    #Take the incoming data and turning it into a python recognized dictionary
    incomingData=request.get_json(force=True)

    print("\n\nThis is the incoming data from the equipment field")
    print("Incoming data:")
    print(incomingData)
    #We expect a certain order of incoming data, but try to avoid guessing the name right in case angular did something
    #The keys correspond to the names of the Formcontrols in angular
    list_of_the_keys=list(incomingData.keys())
    
    global Rcentrifuge
    global V1
    global V2
    global L1
    global L2
    global Va
    global Vb

    global Acc_t_1
    global Acc_t_2
    global Acc_t_3
    global Acc_t_4
    global Acc_t_5
    global Acc_t_6
    
    global Acc_rpm_1
    global Acc_rpm_2
    global Acc_rpm_3
    global Acc_rpm_4
    global Acc_rpm_5
    global Acc_rpm_6
    
    global Ret_t_1
    global Ret_t_2
    global Ret_t_3
    global Ret_t_4
    global Ret_t_5
    global Ret_t_6
    
    global Ret_rpm_1
    global Ret_rpm_2
    global Ret_rpm_3
    global Ret_rpm_4
    global Ret_rpm_5
    global Ret_rpm_6 
    
    

    Rcentrifuge=incomingData[list_of_the_keys[0]]
    

    L1=incomingData[list_of_the_keys[1]]
    L2=incomingData[list_of_the_keys[2]]
    V1=incomingData[list_of_the_keys[3]]
    V2=incomingData[list_of_the_keys[4]]

    Acc_t_1=incomingData[list_of_the_keys[5]]
    Acc_t_2=incomingData[list_of_the_keys[6]]
    Acc_t_3=incomingData[list_of_the_keys[7]]
    Acc_t_4=incomingData[list_of_the_keys[8]]
    Acc_t_5=incomingData[list_of_the_keys[9]]
    Acc_t_6=incomingData[list_of_the_keys[10]]
    
    Acc_rpm_1=incomingData[list_of_the_keys[11]]
    Acc_rpm_2=incomingData[list_of_the_keys[12]]
    Acc_rpm_3=incomingData[list_of_the_keys[13]]
    Acc_rpm_4=incomingData[list_of_the_keys[14]]
    Acc_rpm_5=incomingData[list_of_the_keys[15]]
    Acc_rpm_6=incomingData[list_of_the_keys[16]]
    
    Ret_t_1=incomingData[list_of_the_keys[17]]
    Ret_t_2=incomingData[list_of_the_keys[18]]
    Ret_t_3=incomingData[list_of_the_keys[19]]
    Ret_t_4=incomingData[list_of_the_keys[20]]
    Ret_t_5=incomingData[list_of_the_keys[21]]
    Ret_t_6=incomingData[list_of_the_keys[22]]
    
    Ret_rpm_1=incomingData[list_of_the_keys[23]]
    Ret_rpm_2=incomingData[list_of_the_keys[24]]
    Ret_rpm_3=incomingData[list_of_the_keys[25]]
    Ret_rpm_4=incomingData[list_of_the_keys[26]]
    Ret_rpm_5=incomingData[list_of_the_keys[27]]
    Ret_rpm_6=incomingData[list_of_the_keys[28]]
    Va=incomingData[list_of_the_keys[29]]
    Vb=incomingData[list_of_the_keys[30]]
    
    global theAnswer
    global equipment_setup_successfully
    equipment_setup_successfully=True
    outdata={'equipment_setup_successfully':equipment_setup_successfully}
    theAnswer=json.dumps(outdata)

    print("This is returned:")
    print(theAnswer)


    print("********************************************************************")
    
    return

# _process_spintest_data()  is the second of the two setup-functions. Once the user has filled out the information about their spintest such as the spintimes, the results etc and clicks "send", this function will take the info and save it in the respective global variable it belongs in. It also changes the setting ""
#@input:-
#@output:-
def _process_spintest_data():
    #Take the incoming data and turning it into a python recognized dictionary
    incomingData=request.get_json(force=True)
    print("********************************************************************")
    print("Incoming data:")
    print("This is the incoming data: from the spintest form")
    print(incomingData)

    #We expect a certain order of incoming data, but try to avoid guessing the name right in case angular did something
    #The keys correspond to the names of the Formcontrols in angular

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

    
  
    spintime1=incomingData[list_of_the_keys[0]]
    spintime2=incomingData[list_of_the_keys[1]]
    spintime3=incomingData[list_of_the_keys[2]]
    spintime4=incomingData[list_of_the_keys[3]]
    
    Nstart1=incomingData[list_of_the_keys[4]]
    Nstart2=incomingData[list_of_the_keys[5]]
    Nstart3=incomingData[list_of_the_keys[6]]
    Nstart4=incomingData[list_of_the_keys[7]]


    speed1=incomingData[list_of_the_keys[8]]
    speed2=incomingData[list_of_the_keys[9]]
    speed3=incomingData[list_of_the_keys[10]]
    speed4=incomingData[list_of_the_keys[11]]

    residualSolids1=incomingData[list_of_the_keys[12]]/100
    residualSolids2=incomingData[list_of_the_keys[13]]/100
    residualSolids3=incomingData[list_of_the_keys[14]]/100
    residualSolids4=incomingData[list_of_the_keys[15]]/100

    global theAnswer
    global spintest_setup_successfully
    spintest_setup_successfully=True
    
    outdata={'spintest_setup_successfully':spintest_setup_successfully}
    theAnswer=json.dumps(outdata)
    print("This is returned:")
    print(theAnswer)
    return


# create_spintest_object() will take all the above mentioned and now updated global variables and create an object of the type "SpinTestClass" with all the data from the user. 
#@input:-
#@output: Returns the SpinTestClass object. 
def create_spintest_object():
    global spintest_setup_successfully
    #In case the user declines to fill in the spintest data for whatever reason, I don't want anything to crash. The frontend will ensure that a message is sent letting the user know that they will be shown a default graph.
    if (spintest_setup_successfully==True):
        spintimes=[spintime1, spintime2, spintime3,spintime4]
        #ensure spintimes are provided as number of minutes
        #Can be changed in frontend, but due to difficulties finding a good way to enter a time that is not a time of day
        #THe decision was made to enter it as a number of minutes. 
        spintimes_min=spintimes
        Nstarts=[Nstart1,Nstart2,Nstart3,Nstart4]
        Speeds=[speed1,speed2,speed3,speed4]
        ResidualSolids=[residualSolids1,residualSolids2,residualSolids3,residualSolids4]
        AccTable=[[Acc_rpm_1, Acc_rpm_2, Acc_rpm_3, Acc_rpm_4, Acc_rpm_5, Acc_rpm_6],[Acc_t_1, Acc_t_2, Acc_t_3, Acc_t_4, Acc_t_5, Acc_t_6]]
        RetTable=[[Ret_rpm_1, Ret_rpm_2, Ret_rpm_3, Ret_rpm_4, Ret_rpm_5, Ret_rpm_6],[Ret_t_1, Ret_t_2, Ret_t_3, Ret_t_4, Ret_t_5, Ret_t_6]]
        local_spintest_object=spintestModule.SpinTest(spinTimes=spintimes_min,Nstart=Nstarts,speeds=Speeds,residualSol=ResidualSolids,\
                                                L1=L1,L2=L2,V1=V1,V2=V2,Va=Va, Vb=Vb, rCentrifuge=Rcentrifuge,\
                                                accelTab=AccTable, retardTab=RetTable)
    else:
        #if not, just make a default
        local_spintest_object=spintestModule.SpinTest()

        
        #ensure spintimes are provided as number of minutes
        #Can be changed in frontend, but due to difficulties finding a good way to enter a time that is not a time of day
        #THe decision was made to enter it as a number of minutes. 
        spintimes_min=spintimes
            
           
    
    
    
    return local_spintest_object


#When the endpoint /find_flowrate is accessed, this function will create a SpinTestClass object with the user data, and given some separator size KQ will call a method to return the corresponding flowrate to the user. The answer is saved in json format in the global variable "theAnswer" which is then accessed and sent to frontend in respond_to_find_flowrate()
#@input: Through endpoint, a capacity as KQ.
#@output: Through endpoint, a vector of 4 flowrates [m3/h] corresponding to the 4 different separation results the user got 
def find_flowrate():
    
    local_spintest_object=create_spintest_object()
    
    #For testing purposes:
  
    #local_spintest_object=spintestModule.SpinTest()
    
    incomingData=request.get_json(force=True)
    print("Got some incoming data! \n {0}".format(incomingData))
    list_of_the_keys=list(incomingData.keys())
    _KQ=incomingData[list_of_the_keys[0]]
    

    theQ=local_spintest_object.calcQ(KQ=_KQ)#m3 per h
    
    print("Ran find Q function.This is the Q")
    print(theQ)
    
    outdata={'The_Flows':theQ}
    global theAnswer
    theAnswer=json.dumps(outdata)
    print("Sent back to frontend from /find_flowrate:")
    print(theAnswer)

    return 

#When the endpoint /fulfill_criteria is accessed, this function will create a SpinTestClass object with the user data. Using a separator capacity (if given) and a desired criteria for the outlet result ("referred to commonly as residualSolids" but can be in whatever unit the user desires). Creates a vector of 4 KQ:s to produce a range, and then the function calculates a set of maximum flowrates that can go through each KQ in order to yield a result satisfying the criteria. The answer is saved in json format in the global variable "theAnswer" which is then accessed and sent to frontend in respond_to_fulfill_criteria()
#@input:Through endpoint, a criteria in the same unit as the result (referred to as residualSolids) and optionally a separator capacity KQ
#@output: Through endpoint, a vector of maximum allowable flowrates Qmax [L/h], a loadfactor [L/KQ*H]
def fulfill_criteria():



    local_spintest_object=create_spintest_object()
    #For testing purposes:
    #local_spintest_object=spintestModule.SpinTest()
    
    incomingData=request.get_json(force=True)
    
    list_of_the_keys=list(incomingData.keys())
    #can pass desiredQ,KQ or Ae and Criteria
    _criteria=incomingData[list_of_the_keys[0]]/100
    KQ=incomingData[list_of_the_keys[1]]
    
 
    if(KQ==None):
        vector_of_KQ=[100,200,300,400,500]
    else:
        vector_of_KQ=[KQ*0.1,KQ*0.5,KQ,KQ*1.5,KQ*2]
    
    LF,Qmax,KQ=local_spintest_object.resSolCrit(criteria=_criteria,KQ=vector_of_KQ)
    LF=LF*3600*1000#Liter per h
    LF=round(LF,4)


    for i in range(0,len(Qmax)):
        Qmax[i]=Qmax[i]*3600*1000#Liter per h
        Qmax[i]=round(Qmax[i],4)
    
    outdata={'LF':LF,'Qmax':Qmax,'KQ':KQ}
    global theAnswer
    theAnswer=json.dumps(outdata)
    print("Sent back to frontend from /fulfill_criteria:")
    print(theAnswer)
    return

#When the endpoint /find_capacity() is accessed, this function will find an appropriate separator size KQ ("capacity" is the wrong denomination, size is much more appropriate) for the desired flowrate and acceptable interval of separation results (referred to as "effluent conc" here). An upper and lower bound of acceptable results are given, a middle point is calculated. A loadfactor, and recommended size is given for each of the three separation results.The answer is saved in json format in the global variable "theAnswer" which is then accessed and sent to frontend in respond_to_find_capacity()
#@input: Via the endpoint, a desired flowrate Q [m3/h] and an upper and lower bound of acceptable separation results in whatever unit was used when setting up the spintest data.
#output: Via the endpoint, three separator sizes and three loadfactors to match the upper lower and middle separation results. 
def find_capacity():
    local_spintest_object=create_spintest_object()
    #For testing purposes:
    #local_spintest_object=spintestModule.SpinTest()

    
    incomingData=request.get_json(force=True)
    print(incomingData)

    
    
    list_of_the_keys=list(incomingData.keys())
    #can pass desiredQ and Criteria
    desiredQ=incomingData[list_of_the_keys[0]]

    #Criterias are sent as percentages, so division is requrired to get decimal form
    effluent_conc1=incomingData[list_of_the_keys[1]]/100
    effluent_conc2=incomingData[list_of_the_keys[2]]/100
    
    effluent_conc_mid=(effluent_conc1+effluent_conc2)/2
    

    #Enter Q as m3 per h
    ##LF unit is [m3/s*KQ]. To change it to L/h*KQ, it is multiplied by 3600 and 1000
    LF_1,temp,KQ_1=local_spintest_object.resSolCrit(KQ=0,criteria=effluent_conc1,Qdesired=desiredQ)
    LF_1=round(LF_1*3600*1000,3)
    KQ_1=round(KQ_1/1000,2)

    LF,temp,KQ=local_spintest_object.resSolCrit(KQ=0,criteria=effluent_conc_mid,Qdesired=desiredQ)
    LF=round(LF*3600*1000,3)
    KQ=round(KQ/1000,2)

    LF_2,temp,KQ_2=local_spintest_object.resSolCrit(KQ=0,criteria=effluent_conc2,Qdesired=desiredQ)
    LF_2=round(LF_2*3600*1000,3)
    KQ_2=round(KQ_2/1000,2)
    
    

    
    outdata={'LF_1':LF_1,'LF':LF,'LF_2':LF_2,'KQ_1':KQ_1,'KQ':KQ,'KQ_2':KQ_2}
    global theAnswer
    theAnswer=json.dumps(outdata)
    print("Sent back to frontend from /find_capacity:")
    print(theAnswer)

    return



#When the endpoint /calculate_spintimes is accessed, this function will create a SpinTestClass object with default spintesdata, and customized equipment data. The class method CalculateSpintimes is then accessed using this object. The user commonly knows both their separator size and their expected florwrates and wants to know what spintime in their centrifuge corresponds to a flowrate through their separator. Theoretically, these should yield similar separation results. 
#@input: Via the endpoint, an upper and lower bound of flowrate [m3/h] and a separator size is entered, as well as a centrifuge speed.
#output: Via the endpoint, the recommended spintimes in seconds for the lower Q, upper Q and the two flowrates in between is returned. 
def calculate_spintimes():
    
 
    #A SpinTestClass object with default spintestdata is created. 
    AccTable=[[Acc_rpm_1, Acc_rpm_2, Acc_rpm_3, Acc_rpm_4, Acc_rpm_5, Acc_rpm_6],[Acc_t_1, Acc_t_2, Acc_t_3, Acc_t_4, Acc_t_5, Acc_t_6]]
    RetTable=[[Ret_rpm_1, Ret_rpm_2, Ret_rpm_3, Ret_rpm_4, Ret_rpm_5, Ret_rpm_6],[Ret_t_1, Ret_t_2, Ret_t_3, Ret_t_4, Ret_t_5, Ret_t_6]]
    theCentrifugeRadius=Rcentrifuge
    theV1=V1
    theV2=V2
    theVa=Va
    theVb=Vb
    theL1=L1
    theL2=L2
    
    local_spintest_object=spintestModule.SpinTest(L1=theL1,L2=theL2,V1=theV1,V2=theV2,Va=theVa, Vb=theVb, rCentrifuge=theCentrifugeRadius,accelTab=AccTable, retardTab=RetTable)
    
    incomingData=request.get_json(force=True)
    print("\n\nThe incoming data is:")
    print(incomingData)


    
    
    list_of_the_keys=list(incomingData.keys())
    #can pass desiredQ,KQ or Ae and Criteria
    KQ=incomingData[list_of_the_keys[0]]
    Flow1=incomingData[list_of_the_keys[1]]
    Flow4=incomingData[list_of_the_keys[2]]
    SpinningSpeed=incomingData[list_of_the_keys[3]]
    #incoming as m3/h
    Flow2=Flow1+((Flow4-Flow1)/3)
    Flow3=Flow1+(2*(Flow4-Flow1)/3)
    
    Flow2=round(Flow2,3)
    Flow3=round(Flow3,3)
    #Getting recommended spintimes in seconds

    rec_spintimes=local_spintest_object.getSpinTimes(Qin=[Flow4,Flow3,Flow2,Flow1],w0=SpinningSpeed,Ae=KQ*38.2)

   

    outdata={"Recommended_spintimes":rec_spintimes}
    global theAnswer
    theAnswer=json.dumps(outdata)
    print("Sent back to frontend from /calculate_spintimes:")
    print(theAnswer)

    
    
    return
            
    
    


#routes and what happens when you send a request to them
@app.route('/')
def default():
    return "This is the backend server. You can send post requests to '/find_flowrate', \n /fulfill_criteria \n /find_capacity, \n /calculate_spintimes, \n /send_fluid_properties, \n /send_equipment_properties and \n/send_spintest_data."


    
@app.route('/send_equipment_properties', methods = ['POST'])
def respond_to_equipment_properties():
    if request.method == "OPTIONS":
        return _build_cors_preflight_response()
    if request.method == "POST":
        #It seems to only go post never options anymore. Shall try to do without the corsify
        #Nope doesn't work we need it.
        _process_equipment_properties()
        return addHeadersToResponse(jsonify(theAnswer))

   
@app.route('/send_spintest_data', methods = ['POST'])
def respond_to_spintest_data():
    if request.method == "OPTIONS":
        return _build_cors_preflight_response()
    if request.method == "POST":
        #It seems to only go post never options anymore. Shall try to do without the corsify
        #Nope doesn't work we need it, but it is now just added to my other processing.
        _process_spintest_data()
        return addHeadersToResponse(jsonify(theAnswer))
    
@app.route('/find_flowrate',methods=['POST'])
def respond_to_find_flowrate():
    if request.method == "OPTIONS":
        return _build_cors_preflight_response()
    if request.method == "POST":
        #It seems to only go post never options anymore. Shall try to do without the corsify
        #Nope doesn't work we need it, but it is now just added to my other processing.
        find_flowrate()
        return addHeadersToResponse(jsonify(theAnswer))


@app.route('/fulfill_criteria',methods=['POST'])
def respond_to_fulfill_criteria():
    if request.method == "OPTIONS":
        return _build_cors_preflight_response()
    if request.method == "POST":
        #It seems to only go post never options anymore. Shall try to do without the corsify
        #Nope doesn't work we need it, but it is now just added to my other processing.
        fulfill_criteria()
        return addHeadersToResponse(jsonify(theAnswer))
    
@app.route('/find_capacity',methods=['POST'])
def respond_to_find_capacity():
    if request.method == "OPTIONS":
        return _build_cors_preflight_response()
    if request.method == "POST":
        #It seems to only go post never options anymore. Shall try to do without the corsify
        #Nope doesn't work we need it, but it is now just added to my other processing.
        find_capacity()
        return addHeadersToResponse(jsonify(theAnswer))
    
@app.route('/calculate_spintimes',methods=['POST'])
def respond_to_calculate_spintimes():
    if request.method == "OPTIONS":
        return _build_cors_preflight_response()
    if request.method == "POST": 
        #It seems to only go post never options anymore. Shall try to do without the corsify
        #Nope doesn't work we need it, but it is now just added to my other processing.
        calculate_spintimes()
        return addHeadersToResponse(jsonify(theAnswer))






app.run()

