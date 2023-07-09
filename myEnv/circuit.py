# 초음파 센서에 대한 전역 변수 선언 및 초기화 및 LED 조명 on/off
import time
import RPi.GPIO as GPIO

trig = 20
echo = 16

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)
GPIO.output(trig, False)

def measureDistance():
    global trig, echo
    GPIO.output(trig, True)  # 신호 1 발생
    time.sleep(0.00001)  # 짧은 시간 후 0으로 떨어뜨려 falling edge를 만들기 위함
    GPIO.output(trig, False)  # 신호 0 발생 (falling edge)

    while GPIO.input(echo) == 0:
        pass
    pulse_start = time.time()  # 신호 1. 초음파 발생이 시작되었음을 알림

    while GPIO.input(echo) == 1:
        pass
    pulse_end = time.time()  # 신호 0. 초음파 수신 완료를 알림

    pulse_duration = pulse_end - pulse_start
    return 340 * 100 / 2 * pulse_duration

def ledOnOff(led, onOff):  # led 번호의 핀에 onOff(0/1) 값 출력하는 함수
    GPIO.output(led, onOff)

# LED 점등을 위한 전역 변수 선언 및 초기화
led = [6, 13, 19]  # 핀 번호 GPIO5, GPIO6, GPIO13, GPIO19 의미

for i in range(0, 3, 1):
    GPIO.setup(led[i], GPIO.OUT)  # GPIO 5, 6, 13 핀을 출력 선으로 지정.

def controlLED(msg):  # led 번호의 핀에 onOff(0/1) 값 출력하는 함수
    # msg = {0, 1, 2, 3, 4, 5}. 짝수면 led off, 홀수면 led on
    i = int(msg / 2)  # led 정보 확인
    onOff = int(msg % 2)  # led on/off 확인
    ledOnOff(led[i], onOff)

onOff = 1
ledRed = 5
GPIO.setup(ledRed, GPIO.OUT)

def warningLED():  # 빨간색 LED 깜빡거리기
    global onOff
    for i in range(6):  # 3번 깜빡
        ledOnOff(ledRed, onOff)
        time.sleep(1)
        onOff = 0 if onOff == 1 else 1  # 0과 1의 토글링
