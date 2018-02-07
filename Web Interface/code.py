from flask import Flask,request,redirect,render_template
import RPi.GPIO as IO

#Create object of Flask (__name__ is the name of the main file, if single file then leave it as it is)
app = Flask(__name__)

#using route decorater to route the request made on the webpage
@app.route('/')
def hello_world():
    return render_template('index.html')

#using route decorater to route the request made on the webpage	
@app.route('/led1on',methods=['POST'])
def led1on():
    IO.output(20,1)			#Turn on the LED
    return redirect('/')

#using route decorater to route the request made on the webpage
@app.route('/led1off',methods=['POST'])
def led1off():
    IO.output(20,0)			#Turn off the LED
    return redirect('/')


if __name__=='__main__':
    IO.setmode (IO.BCM)		#Set up Raspberry Pi mode (Board/BCM)
    IO.setup(20,IO.OUT)		#Set the pin '20' or any other GPIO pin to Output
    app.run(host='10.11.6.40')	#run the server on the given host
    IO.cleanup()			#clean up the IO pins setup
