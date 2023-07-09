# publisher/subscriber
import app
import time
import paho.mqtt.client as mqtt
import myCamera  # 카메라 사진 보내기
import circuit  # 초음파 센서 입력 모듈 임포트
import environment  # 온습도 센서 입력 모듈 임포트

flag = False  # True이면 "action" 메시지를 수신하였음을 나타냄

def on_connect(client, userdata, flag, rc):  # 연결
    client.subscribe("facerecognition", qos=0)
    client.subscribe("led1", qos=0)
    client.subscribe("led2", qos=0)
    client.subscribe("led3", qos=0)
    client.subscribe("warning", qos=0)

def on_message(client, userdata, msg):
    global flag
    command = msg.payload.decode("utf-8")
    print(command)
    if command != "action":  # led 조정
        msg = int(msg.payload)
        circuit.controlLED(msg)  # msg는 0~5까지의 수
    else:  # command가 action인 경우 (사진 촬영)
        print("action msg received..")
        flag = True

broker_ip = "localhost"  # 현재 이 컴퓨터를 브로커로 설정
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker_ip, 1883)
client.loop_start()

while True:
    if flag == True:  # "action" 메시지 수신. 사진 촬영
        imageFileName = myCamera.takePicture()  # 카메라 사진 촬영
        print(imageFileName)
        client.publish("image", imageFileName, qos=0)
        flag = False

    distance = circuit.measureDistance()  # 초음파 센서 거리 측정
    client.publish("ultrasonic", distance, qos=0)
    temperature = environment.getTemperature()  # 온도 측정
    client.publish("temperature", temperature, qos=0)
    humidity = environment.getHumidity()  # 습도 측정
    client.publish("humidity", humidity, qos=0)

    if humidity >= 65 or temperature >= 25:  # (온도 > 25도) 혹은 (습도 > 65%) 일 경우
        circuit.warningLED()  # -> 빨간색 LED 깜빡거리게 설정

    if distance <= 10:  # 초음파센서에 거리가 10cm 이내일 경우
        circuit.controlLED(5)  # 하얀색 LED on

    time.sleep(1)

client.loop_end()
client.disconnect()
