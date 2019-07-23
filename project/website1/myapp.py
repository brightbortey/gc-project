
from flask import Flask, render_template
import attendance.py
#_____________1. init app_______________
app = Flask(__name__)

#___________2.   Routers________________

#@app.rout('/help')
#def help():
#    return render_template('help.html') 

@app.route('/')
def index():
   countdown(1) 
   return render_template('index.html')



#__________3.start server_____________________
if __name__== '__main__':
   app.run(debug=True, host='0.0.0.0')
