
import numpy as np
import SpinTest.SpinTestClass as spintestModule
#import SpinTest.test as importedModule #for testing purposes
from flask import Flask, make_response,jsonify,request,json
import pdb
#Added this comment from company laptop to test if shit works
local_spintest_object=spintestModule.SpinTest(V1=100,V2=20,L1=76.2, L2=24.8)
print(local_spintest_object)
print(np.abs(-3))
