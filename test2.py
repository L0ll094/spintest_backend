
import datetime as DT
import SpinTest.SpinTestClass as spintestModule
#import SpinTest.test as importedModule #for testing purposes
from flask import Flask, make_response,jsonify,request,json
import pdb
#Added this comment from company laptop to test if shit works
local_spintest_object=None
local_spintest_object=spintestModule.SpinTest()
_KQ=200
local_spintest_object.calcQ(KQ=_KQ)