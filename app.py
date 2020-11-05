import datetime as DT
import requests
import SpinTest.SpinTestClass as spintestModule
#import SpinTest.test as importedModule #for testing purposes
from flask import Flask, make_response,jsonify,request,json
import pdb
#Added this comment from company laptop to test if shit works

app = Flask(__name__)

theAnswer={'first':3,'second':4}

#Preparing containers to store incoming data.
#This is not needed, but is done for the next person looking at this code, to make it more understandable.
#None of these should be 0, so if they're sent to python as 0 
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

setup_has_been_completed=False





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
    
    list_of_the_keys=list(incomingData.keys())
    global densityParticle
    global densityFeed
    global kinViscosity
    densityParticle=incomingData[list_of_the_keys[0]]
    densityFeed=incomingData[list_of_the_keys[1]]
    kinViscosity=incomingData[list_of_the_keys[2]]
    
    return response
    



def _process_equipment_properties(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    #Take the incoming data and turning it into a python recognized dictionary
    incomingData=request.get_json(force=True)
    #print(incomingData)
    #We expect a certain order of incoming data, but try to avoid guessing the name right in case angular did something
    #The keys correspond to the names of the Formcontrols in angular
    list_of_the_keys=list(incomingData.keys())
    
    global Rcentrifuge
    global V1
    global V2
    global L1
    global L2
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
    
    V1=incomingData[list_of_the_keys[1]]
    V2=incomingData[list_of_the_keys[2]]
    L1=incomingData[list_of_the_keys[3]]
    L2=incomingData[list_of_the_keys[4]]
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
    print(incomingData)

    return response

def _process_spintest_data(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    #Take the incoming data and turning it into a python recognized dictionary
    incomingData=request.get_json(force=True)
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

    global TempSpinTest
    global NeededQ
    
    
  
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

    residualSolids1=incomingData[list_of_the_keys[12]]
    residualSolids2=incomingData[list_of_the_keys[13]]
    residualSolids3=incomingData[list_of_the_keys[14]]
    residualSolids4=incomingData[list_of_the_keys[15]]

    TempSpinTest=incomingData[list_of_the_keys[16]]
    NeededQ=incomingData[list_of_the_keys[17]]
    return response



def create_spintest_object():

    
    
    spintimes=[spintime1, spintime2, spintime3,spintime4]
    Nstarts=[Nstart1,Nstart2,Nstart3,Nstart4]
    Speeds=[speed1,speed2,speed3,speed4]
    ResidualSolids=[residualSolids1,residualSolids2,residualSolids3,residualSolids4]
    AccTable=[[Acc_rpm_1, Acc_rpm_2, Acc_rpm_3, Acc_rpm_4, Acc_rpm_5, Acc_rpm_6],[Acc_t_1, Acc_t_2, Acc_t_3, Acc_t_4, Acc_t_5, Acc_t_6]]
    RetTable=[[Ret_rpm_1, Ret_rpm_2, Ret_rpm_3, Ret_rpm_4, Ret_rpm_5, Ret_rpm_6],[Ret_t_1, Ret_t_2, Ret_t_3, Ret_t_4, Ret_t_5, Ret_t_6]]
    
    #ensure spintimes are provided as number of minutes
    spintimes_min=[]
    refTime=DT.datetime(1900,1,1)
    print("\n\n\n\n")
    for time in spintimes:
        temp=DT.datetime.strptime(time,'%M:%S')
        time_in_minutes=(temp-refTime).total_seconds()/60
        spintimes_min.append(time_in_minutes)
        
        

    #remember to add TempSpinTest and Needed Q to below call once they have been added to form.
        
        
    local_spintest_object=spintestModule.SpinTest(spinTimes=spintimes_min,Nstart=Nstarts,speeds=Speeds,residualSol=ResidualSolids,\
                                            densityfeed=densityFeed,densityparticle=densityParticle,kinviscosity=kinViscosity,\
                                            L1=L1,L2=L2,V1=V1,V2=V2,rCentrifuge=Rcentrifuge,neededQ=NeededQ,tempSpinTest=TempSpinTest,\
                                            accelTab=AccTable, retardTab=RetTable)
    
    global setup_has_been_completed
    setup_has_been_completed=True

    print(local_spintest_object)
    
    
    return local_spintest_object

def addHeadersToResponse(response):
    #This is run after thaAnswer have been updated by the find_flowrate function
    #so that the response is something useful and not just the default value of theAnswer
    response.headers.add("Access-Control-Allow-Origin", "*")
    
    return response
    
    

def find_flowrate():
  
    #local_spintest_object=create_spintest_object()
    
    #For testing purposes:
    local_spintest_object=spintestModule.SpinTest()
    
    incomingData=request.get_json(force=True)
    list_of_the_keys=list(incomingData.keys())
    _KQ=incomingData[list_of_the_keys[0]]
     

    theQ=local_spintest_object.calcQ(KQ=_KQ)
    
    print("Ran find Q function")
    print(local_spintest_object.residualSol)
    print(theQ)
    
    outdata={'The Flows':theQ}
    global theAnswer
    theAnswer=json.dumps(outdata)
    print("Sent back to frontend from /find_flowrate:")
    print(theAnswer)

    return 
    
def fulfill_criteria():
      
    #local_spintest_object=create_spintest_object()
    #For testing purposes:
    local_spintest_object=spintestModule.SpinTest()
    
    incomingData=request.get_json(force=True)
    #For testing purposes:
    #incomingData={'TheCriteria':0.23,'theVectorOfKQ':[150,250,350,450],'DesiredQ':60}
    
    
    
    
    list_of_the_keys=list(incomingData.keys())
    #can pass desiredQ,KQ or Ae and Criteria
    _criteria=incomingData[list_of_the_keys[0]]
    KQ=incomingData[list_of_the_keys[1]]
    
 
    if(KQ==None):
        vector_of_KQ=[100,200,300,400]
    else:
        vector_of_KQ=[KQ*0.1,KQ*0.5,KQ,KQ*1.5,KQ*2]
    

  



    LF,Qmax,KQ=local_spintest_object.resSolCrit(criteria=_criteria,KQ=vector_of_KQ)
    LF=LF*3600
    
    for i in range(0,len(Qmax)):
        Qmax[i]=Qmax[i]*3600
    
    outdata={'LF':LF,'Qmax':Qmax,'KQ':KQ}
    global theAnswer
    theAnswer=json.dumps(outdata)
    print("Sent back to frontend from /fulfill_criteria:")
    print(theAnswer)

    
    
    return

def find_capacity():
    #local_spintest_object=create_spintest_object()
    #For testing purposes:
    local_spintest_object=spintestModule.SpinTest()

    
    incomingData=request.get_json(force=True)
    #For testing purposes:
    #incomingData={'Approx. eff.':0.23,'DesiredQ':60}
    
    
    list_of_the_keys=list(incomingData.keys())
    #can pass desiredQ,KQ or Ae and Criteria
    desiredQ=incomingData[list_of_the_keys[0]]
    effluent_conc1=incomingData[list_of_the_keys[1]]
    effluent_conc2=incomingData[list_of_the_keys[2]]
    
    effluent_conc_mid=(effluent_conc1+effluent_conc2)/2
    

    
    LF_1,temp,KQ_1=local_spintest_object.resSolCrit(criteria=effluent_conc1,Qdesired=desiredQ)
    LF_1=LF_1*3600
    LF,temp,KQ=local_spintest_object.resSolCrit(criteria=effluent_conc_mid,Qdesired=desiredQ)
    LF=LF*3600
    LF_2,temp,KQ_2=local_spintest_object.resSolCrit(criteria=effluent_conc2,Qdesired=desiredQ)
    LF_2=LF_2*3600
    
    print(LF_1,LF,LF_2)
    print(KQ_1,KQ,KQ_2)
    
    outdata={'LF_1':LF_1,'LF':LF,'LF_2':LF_2,'KQ_1':KQ_1,'KQ':KQ,'KQ_2':KQ_2}
    global theAnswer
    theAnswer=json.dumps(outdata)
    print("Sent back to frontend from /find_capacity:")
    print(theAnswer)

    return


def calculate_spintimes():
    
    #local_spintest_object=create_spintest_object()
    #For testing purposes:
    local_spintest_object=spintestModule.SpinTest()
    
    incomingData=request.get_json(force=True)
    #For testing purposes:

    
    
    list_of_the_keys=list(incomingData.keys())
    #can pass desiredQ,KQ or Ae and Criteria
    KQ=incomingData[list_of_the_keys[0]]
    Flow1=incomingData[list_of_the_keys[1]]
    Flow4=incomingData[list_of_the_keys[2]]
    SpinningSpeed=incomingData[list_of_the_keys[3]]
    
    Flow2=Flow1+((Flow4-Flow1)/3)
    Flow3=Flow1+(2*(Flow4-Flow1)/3)
    
    Flows=[Flow1,Flow2,Flow3,Flow4]
    
    
    
    
    
    
    rec_spintimes=local_spintest_object.getSpinTimes(Q=Flows,w0=SpinningSpeed,Ae=KQ*38.2)
    
    
    outdata=[rec_spintimes]
    global theAnswer
    theAnswer=json.dumps(outdata)
    print("Sent back to frontend from /calculate_spintimes:")
    print(theAnswer)
    
    
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
        return _process_fluid_properties(jsonify(theAnswer))
    
@app.route('/send_equipment_properties', methods = ['POST'])
def respond_to_equipment_properties():
    if request.method == "OPTIONS":
        return _build_cors_preflight_response()
    if request.method == "POST":
        #It seems to only go post never options anymore. Shall try to do without the corsify
        #Nope doesn't work we need it.
        return _process_equipment_properties(jsonify(theAnswer))

   
@app.route('/send_spintest_data', methods = ['POST'])
def respond_to_spintest_data():
    if request.method == "OPTIONS":
        return _build_cors_preflight_response()
    if request.method == "POST":
        #It seems to only go post never options anymore. Shall try to do without the corsify
        #Nope doesn't work we need it, but it is now just added to my other processing.
        return _process_spintest_data(jsonify(theAnswer))
    
@app.route('/find_flowrate',methods=['POST'])
def respond_with_results():
    if request.method == "OPTIONS":
        return _build_cors_preflight_response()
    if request.method == "POST":
        #It seems to only go post never options anymore. Shall try to do without the corsify
        #Nope doesn't work we need it, but it is now just added to my other processing.
        find_flowrate()
        return addHeadersToResponse(jsonify(theAnswer))


@app.route('/fulfill_criteria',methods=['POST'])
def respond_with_results2():
    if request.method == "OPTIONS":
        return _build_cors_preflight_response()
    if request.method == "POST":
        #It seems to only go post never options anymore. Shall try to do without the corsify
        #Nope doesn't work we need it, but it is now just added to my other processing.
        fulfill_criteria()
        return addHeadersToResponse(jsonify(theAnswer))
    
@app.route('/find_capacity',methods=['POST'])
def respond_with_results3():
    if request.method == "OPTIONS":
        return _build_cors_preflight_response()
    if request.method == "POST":
        #It seems to only go post never options anymore. Shall try to do without the corsify
        #Nope doesn't work we need it, but it is now just added to my other processing.
        find_capacity()
        return addHeadersToResponse(jsonify(theAnswer))
    
@app.route('/calculate_spintimes',methods=['POST'])
def respond_with_results4():
    if request.method == "OPTIONS":
        return _build_cors_preflight_response()
    if request.method == "POST":
        #It seems to only go post never options anymore. Shall try to do without the corsify
        #Nope doesn't work we need it, but it is now just added to my other processing.
        calculate_spintimes()
        return addHeadersToResponse(jsonify(theAnswer))






app.run()

