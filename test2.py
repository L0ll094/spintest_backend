
import numpy as np
import SpinTest.SpinTestClass as spintestModule

#import SpinTest.test as importedModule #for testing purposes
from flask import Flask, make_response,jsonify,request,json
import pdb
import datetime

#Added this comment from company laptop to test if shit works




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



spintimes=[spintime1, spintime2, spintime3,spintime4]
Nstarts=[Nstart1,Nstart2,Nstart3,Nstart4]
Speeds=[speed1,speed2,speed3,speed4]
ResidualSolids=[residualSolids1,residualSolids2,residualSolids3,residualSolids4]
AccTable=[[Acc_rpm_1, Acc_rpm_2, Acc_rpm_3, Acc_rpm_4, Acc_rpm_5, Acc_rpm_6],[Acc_t_1, Acc_t_2, Acc_t_3, Acc_t_4, Acc_t_5, Acc_t_6]]
RetTable=[[Ret_rpm_1, Ret_rpm_2, Ret_rpm_3, Ret_rpm_4, Ret_rpm_5, Ret_rpm_6],[Ret_t_1, Ret_t_2, Ret_t_3, Ret_t_4, Ret_t_5, Ret_t_6]]

#ensure spintimes are provided as number of minutes
#Can be changed in frontend, but due to difficulties finding a good way to enter a time that is not a time of day
#THe decision was made to enter it as a number of minutes. 
spintimes_min=spintimes
    
    
local_spintest_object=spintestModule.SpinTest(spinTimes=spintimes_min,Nstart=Nstarts,speeds=Speeds,residualSol=ResidualSolids,\
                                        L1=L1,L2=L2,V1=V1,V2=V2,Va=Va, Vb=Vb, rCentrifuge=Rcentrifuge,\
                                        accelTab=AccTable, retardTab=RetTable)