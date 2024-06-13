from flask import Flask
from flask import render_template
import RPi.GPIO as GPIO
import time

app= Flask(__name__)

pinc=17
pins=27
pinp=22

def botao(vezes, pino):
    for x in range(vezes):
        GPIO.setup(pino, GPIO.OUT)
        time.sleep(0.13)
        GPIO.cleanup(pino)
        time.sleep(0.13)
        GPIO.setmode(GPIO.BCM)
        print("deu buia")

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
print("Done")

@app.route('/')
def index():
    return render_template('webpage.html')

@app.route('/A')
def led1on():
    GPIO.setup(17, GPIO.OUT)
    time.sleep(0.2)
    GPIO.cleanup(17)
    time.sleep(0.2)
    GPIO.setmode(GPIO.BCM)
    print("deu buia")
    return render_template('webpage.html')

@app.route('/a')
def led1off():
    botao(2, pinc)
    return render_template('webpage.html')

@app.route('/B')
def led2on():
    botao(4, pinc)
    return render_template('webpage.html')

@app.route('/b')
def led2off():
    botao(8, pinc)
    return render_template('webpage.html')

@app.route('/C')
def led3on():
    botao(1, pins)
    return render_template('webpage.html')

@app.route('/c')
def led3off():
    botao(1, pinp)
    return render_template('webpage.html')

if __name__=="__main__":
    print("Start")
    app.run('0.0.0.0', debug=True)
        
