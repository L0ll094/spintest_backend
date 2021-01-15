
import numpy as np
import SpinTest.SpinTestClass as spintestModule
#import SpinTest.test as importedModule #for testing purposes
from flask import Flask, make_response,jsonify,request,json
import pdb
import datetime

#Added this comment from company laptop to test if shit works


local_spintest_object=spintestModule.SpinTest()

Flow4=4.5
Flow1=36
SpinningSpeed=1400
#incoming as m3/h
Flow3=Flow1+((Flow4-Flow1)/3)
Flow2=Flow1+(2*(Flow4-Flow1)/3)

TheFlows=[Flow1,Flow2,Flow3,Flow4]       
print("Flows now look like 1:")
print(TheFlows)

#Getting recommended spintimes in seconds
rec_spintimes=local_spintest_object.getSpinTimes(Qin=[Flow1,Flow2,Flow3,Flow4],w0=SpinningSpeed,Ae=2999.9999999999995)
print("Rec spintimes:")
print(rec_spintimes)
for sec in rec_spintimes:
    print(str(datetime.timedelta(seconds=sec)))





