import speech_recognition as sr
import pygame
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
pinc=17
pins=27
pinp=22
pygame.init()

def botao(vezes, pino):
    for x in range(vezes):
        GPIO.setup(pino, GPIO.OUT)
        time.sleep(0.2)
        GPIO.cleanup(pino)
        time.sleep(0.2)
        GPIO.setmode(GPIO.BCM)
        print("deu buia")

r = sr.Recognizer()
while True:
    with sr.Microphone() as source:
        print("comeco")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print(text)
            if "start" in text.lower():
                pygame.mixer.music.load('time.mp3')
                pygame.mixer.music.play()
                while True:
                    try:
                        with sr.Microphone() as source:
                            print("comeco2")
                            audio = r.listen(source)
                            text2 = r.recognize_google(audio)
                            print(text2)
                            if "30" in text2.lower():
                                botao(1, pinc)
                                break
                            if "1 minute" in text2.lower():
                                botao(2, pinc)
                                pygame.mixer.music.load('start.mp3')
                                pygame.mixer.music.play()
                                break
                            if "2 minutes" in text2.lower():
                                botao(4, pinc)
                                pygame.mixer.music.load('start.mp3')
                                pygame.mixer.music.play()
                                break
                            if "popcorn" in text2.lower():
                                botao(8, pinc)
                                pygame.mixer.music.load('start.mp3')
                                pygame.mixer.music.play()
                                break
                    except:
                        print("erro")
            elif "stop" in text.lower():
                botao(1, pins)
                pygame.mixer.music.load('stop.mp3')
                pygame.mixer.music.play()
                print("Comando 'stop' reconhecido!")
            elif "potency" in text.lower():
                botao(1, pinp)
                print("Potência alterada")
                pygame.mixer.music.load('potencia.mp3')
                pygame.mixer.music.play()
        except:
            print("pqp")
                           

