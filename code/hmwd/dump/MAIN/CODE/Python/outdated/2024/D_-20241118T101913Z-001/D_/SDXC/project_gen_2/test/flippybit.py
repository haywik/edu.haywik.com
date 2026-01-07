from flask import Flask,render_template,jsonify,request,abort
import subprocess
from datetime import *
from datetime import *
now = datetime.now()
import time
min = timedelta(seconds=1)
a = int(input("t:"))
x = timedelta(minutes=a)
print(x)



while True:
    time.sleep(1)

    x = x-min
    

   
    
    print(str(x))