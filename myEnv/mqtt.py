# publisher/subscriber

import time
import paho.mqtt.client as mqtt
import myCamera # 카메라 사진 보내기
import circuit # 초음파 센서 입력 모듈 임포트
import environment # 온 습도 센서 입력 모듈 임포트

flag = False # True이면 "action" 메시지를 수신하였음을 나타냄

def on_connect(client, userdata, flag, rc):
	client.subscribe("facerecognition", qos = 0)


def on_connect(client, userdata, flag, rc):
	client.subscribe("led", qos = 0)


def on_message(client, userdata, msg) :
	#camera
	global flag
	command = msg.payload.decode("utf-8")
	if command == "action" :
		print("action msg received..")
		flag = True

	#led
	msg = int(msg.payload);
	print(msg)
	circuit.controlLED(msg) # msg는 0 또는 1의 정수
	

broker_ip = "localhost" # 현재 이 컴퓨터를 브로커로 설정

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker_ip, 1883)
client.loop_start()

while True :
	if flag==True : # "action" 메시지 수신. 사진 촬영
		imageFileName = myCamera.takePicture() # 카메라 사진 촬영
		print(imageFileName)
		client.publish("image", imageFileName, qos=0)
		flag = False
        
	distance = circuit.measureDistance()
	client.publish("ultrasonic", distance, qos=0)
	temperature = environment.getTemperature()
	client.publish("temperature", temperature, qos=0)
	humidity = environment.getHumidity()
	client.publish("humidity", humidity, qos=0)

	time.sleep(1)
	#print("time...", end=" ")
	#print(flag)

client.loop_end()
client.disconnect()

