# ReadingRoomManagement
라즈베리파이를 이용한 독서실 이용관리 시스템

## 📚&nbsp; 작품 소개

독서실에 카메라, 초음파 센서, 온습도 센서, LED 등을 연결한 라즈베리파이를 이용해 독서실을 관리하는 시스템이다. <br>
이 시스템은 먼저 하나의 웹사이트로 관리를 할 수 있다. 이러한 관리 시스템은 웹사이트 접속자가 사용자인지 관리자인지에 따라 용도가 다르다. 사용자인지 관리자인지는 웹사이트에서 선택할 수 있다.<br>
<br>

### 🙍🏻‍♀️&nbsp; 사용자
먼저 사용자는 웹사이트를 통해 사용여부와 사용 시간을 선택할 수 있다. 그리고 자리에서 초음파 센서 10cm이내 거리에 손을 가져다 되면 조명이 켜진다. 조명의 기본 설정은 하얀색 LED이다. 사용자는 LED의 색상을 웹사이트를 이용해 변경할 수 있다. 사용자는 웹사이트 내 조명 선택 라디오 버튼을 통해 조명을 초록, 노랑, 하얀색 중 선택할 수 있다(다중 선택 가능). 또한 독서실 자리에 있는 온습도 센서를 이용해 적정 실내 온도(18 ~ 20°C)를 넘어 25°C가 되거나 혹은 적정 실내 습도(40 ~ 60%)를 넘어 65%가 되면 빨간색 조명을 3번 깜박거려 온습도가 적정 부분을 넘겼음을 알린다. 이러한 온습도 그래프는 웹사이트 내에서 확인 할 수 있다. 그리고 사용자 웹사이트에 warning 버튼이 하나 있다. 이 버튼은 관리자 호출 버튼으로 독서실 내에 문제가 생겼을 시 누르면 관리자에게 ‘호출’이라는 알림이 간다. 또한 사용자가 선택한 사용 시간이 다 되면 자리의 LED는 자동으로 꺼지고 웹사이트 내에 ‘사용 시간이 종료 되었습니다.’와 같은 메시지를 띄운다.<br>
독서실에 카메라, 초음파 센서, 온습도 센서, LED 등을 연결한 라즈베리파이를 이용해 독서실을 관리하는 시스템이다. 이 시스템은 먼저 하나의 웹사이트로 관리를 할 수 있다. 이러한 관리 시스템은 웹사이트 접속자가 사용자인지 관리자인지에 따라 용도가 다르다. 사용자인지 관리자인지는 웹사이트에서 선택할 수 있다.<br>

### 🤵🏻&nbsp; 관리자
독서실에 카메라, 초음파 센서, 온습도 센서, LED 등을 연결한 라즈베리파이를 이용해 독서실을 관리하는 시스템이다. 이 시스템은 먼저 하나의 웹사이트로 관리를 할 수 있다. 이러한 관리 시스템은 웹사이트 접속자가 사용자인지 관리자인지에 따라 용도가 다르다. 사용자인지 관리자인지는 웹사이트에서 선택할 수 있다.<br>
관리자는 사용자의 선택에 따라 독서실 내에 자리에 사람이 있는지 있다면 사용 시간은 얼마나 남았는지 확인할 수 있다. 또한 사용자의 사용여부를 초음파 센서와 카메라를 통해 알아낼 수 있다. 그리고 이를통해 사용자가 존재하지 않음이 판단될 경우 관리자 임의로 자리를 비울 수 있다.<br>
사용자 사용여부는 사용자 자리에 있는 초음파 센서 변화 그래프를 통해 확인하거나 독서실을 비추고 있는 카메라를 확인하여 사용자가 자리에 없음이 확인할 수 있다. <br><br>

## ✍🏻&nbsp; 시스템 구조

### 1) 독서실 자리 - 사용자 및 관리자의 데이터 전송 구조
![Group 9](https://github.com/kyum-q/ReadingRoomManagement/assets/109158497/d67453c4-c163-48e7-9785-673d82b34914)
<br>

### 2) 사용자의 웹브라우저 사용 흐름
![image 15](https://github.com/kyum-q/ReadingRoomManagement/assets/109158497/22379be9-34b2-418a-b1df-6b9e15cc05ac)
<br>

## 💻&nbsp; 하드웨어 구조

라즈베리파이에 카메라 1개, 온습도 센서 1개, 초음파 센서 1개, LED 4개, 버튼 1개를 사용한다.<br><br>

이들은 각 GPIO 핀은 다음과 같다.<br>
LED – GPIO 5, GPIO 6, GPIO 13, GPIO 19<br>
초음파 센서 – GPIO 16, GPIO 20<br>
온습도 센서 – GPIO 2, GPIO 3<br><br>

![image](https://user-images.githubusercontent.com/109158497/200011368-e59c74c5-2bdc-4d79-89c3-569881ef464e.png)
**<p align="center">[라즈베리파이 구성]</p>**
<br>

## 💡&nbsp; 소프트웨어 구조

<img width="1439" alt="image" src="https://github.com/kyum-q/ReadingRoomManagement/assets/109158497/5ba77b43-ab0b-4b42-bffa-297241cdc22d">

**<p align="center">[소프트웨어 구성]</p>**
<br>

### 1) 파이썬 코드

**1) app.py** – [웹브라우저로부터 접속과 요청을 받아 처리하는 플라스크 앱] 모드 선택 모드 / 사용자 사용여부, 시간 설정 / 관리자 로그인 웹페이지 로딩 / 사용시간 설정(timer)<br><br>
**2) mqtt.py** – [mqtt subscribe하고 publish하는 파이썬 코드] mqtt서버로부터 date 토픽을 subscribe하고 data 토픽을 publish하는 코드<br><br>
**3) circuit.py** - [초음파센서, LED 조정하는 파이썬 코드] 사용자 자리 초음파 센서를 값을 알아내고 LED 조명을 on/off하는 코드<br><br>
**4) environment.py** – [온습도센서 조정하는 파이썬 코드] 사용자 자리 온습도 센서 값을 알아내는 코드<br><br>
**5) myCamera.py** – [카메라 촬영하는 파이썬 코드] 카메라를 통해 사용자 자리를 촬영하고 openCV를 가지고 사람의 얼굴을 표시하는 코드<br><br>

### 2) js 혹은 css 코드 (static)

**1) mqttio.js** - mqtt를 이용하여 라즈베리파이와 값을 주고받는 자바스크립트 코드<br>
**2) face.js** – 웹페이지 내에 캔버스에 image을 그리는 자바스크립트<br>
**3) timer.js** – 웹페이지에서 초와 함께 호출하면 timer가 진행되는 자바스크립트<br>
**4) myChart.js** – 초음파센서로부터 얻은 값을 통해 그래프를 만드는 자바스크립트<br>
**5) userChart.js** – 온습도센서부터 얻은 값을 통해 그래프를 만드는 자바스크립트<br>

**6) main.css** – user.html/manager.html의 css 코드<br>
**7) login.css** – user.html/manager.html을 제외한 css 코드<br><br>

### 3) html 코드 (templates)

**1) project.html** – 초기화면 html (모드선택 가능 – 사용자, 관리자)<br>
**2) useChoose.html** – 사용자 사용여부 선택 html<br>
**3) useStudyRoom.html** – 누군가가 독서실을 사용할 경우 나타나는 사용중 표시 html<br>
**4) timeSetting.html** – 사용자의 독서실 사용 시간을 설정하는 html<br>
**5) user,html** – 사용자 모드 html (LED조정, 온습도센서 차트, 관리자호출)<br>
**6) managerLogin.html** – 관리자 모드 선택시 로그인 html<br>
**7) manager.html** – 관리자 모드 html (초음파센서 차트, 카메라 촬영, 사용자 사용 종료)<br><br>

## 📋&nbsp; 실행 화면
<br>

### 초기 화면 
![image-006](https://github.com/kyum-q/ReadingRoomManagement/assets/109158497/66b6972c-8631-4024-8a63-17c39528079a)
**<p align="center"> [관리자 모드, 사용자 모드 중에 모드 선택할 수 있다] </p>**
<br>

### 🙍🏻‍♀️&nbsp; 사용자 모드 실행 화면

#### 1. 사용자 모드 선택 시 웹 사이트

1) 현재 독서실 사용중인 사용자가 있을 경우<br>

![image-008](https://github.com/kyum-q/ReadingRoomManagement/assets/109158497/e0f4f76c-cdaa-4f9f-9ed3-9da355c84987)
**<p align="center">[사용 중임을 알리는 웹 페이지]</p>**
<br>

2) 현재 독서실 사용중인 사용자가 없을 경우<br>

![image-007](https://github.com/kyum-q/ReadingRoomManagement/assets/109158497/da81536b-2655-4222-b7c7-0ff090519cdc)
**<p align="center">[사용여부 물어보는 웹 페이지]</p>**
<br>

#### 2. 사용시간 설정 웹사이트
사용자가 독서실 사용 버튼을 눌러 사용시간을 설정하거나 직접 입력을 통해 시간을 설정 할 수 있다.

![image-009](https://github.com/kyum-q/ReadingRoomManagement/assets/109158497/2f5e3a16-f767-4e01-86b1-f9ba779c15af)
**<p align="center">[사용시간 설정 웹 페이지]</p>**
<br><br>

#### 3. 사용자 모드 웹 사이트
사용시간 설정 후 timeset 버튼을 눌렀을 경우

![image-010](https://github.com/kyum-q/ReadingRoomManagement/assets/109158497/d70cb25b-25fd-4a0a-bd72-1184d201b8fb)
**<p align="center">[사용자모드 웹 페이지]</p>**
<br>

![image-011](https://github.com/kyum-q/ReadingRoomManagement/assets/109158497/e4eab0d5-3839-44b2-840d-d32e03064f6f)
**<p align="center">[기본 독서실 조명 상태]</p>**
<br><br>

#### - Warning
독서실에서 문제가 생겼을 때, Warning 버튼을 통해 관리자에게 도움을 요청할 수 있다.

#### - 조명 설정
> 독서실 이용 버튼을 눌러야지 다양한 독서실 이용 시스템을 사용할 수 있다.

사용자 웹사이트에 독서실 이용 누르고 조명설정에서 손 쉽게 조명을 크고 끌 수 있다.
가능한 조명 색상은 흰색, 초록색, 노란색이 존재한다.

![image-013](https://github.com/kyum-q/ReadingRoomManagement/assets/109158497/83ca77b2-b1d8-40d2-8100-1df0c001198e)
**<p align="center">[조명 설정 ]</p>**
<br>

![image-014](https://github.com/kyum-q/ReadingRoomManagement/assets/109158497/22889f0a-22cd-441c-b86c-f49ad856ed73)
**<p align="center">[흰색, 초록색, 노란색 조명을 모두 켠 상태]</p>**
<br><br>

#### - 독서실 온습도 그래프
현재 독서실의 온도와 습도를 손 쉽게 확인할 수 있다.

![image-015](https://github.com/kyum-q/ReadingRoomManagement/assets/109158497/34cac609-13d3-4468-9e92-e2f4770e0b90)
**<p align="center">[독서실 온습도 그래프 화면]</p>**
<br><br>

#### 독서실 자동 관리 기능

**1) 사용자 자동 인식 기능** <br>
초음파센서 10cm 이내가 물체가 인식 될 시, 흰색 조명이 켜진다.

![image-012](https://github.com/kyum-q/ReadingRoomManagement/assets/109158497/8b8b143a-80e0-4f47-aa05-9e6b7f3720dd)
**<p align="center">[10cm 이내, 조명 상태]</p>**
<br><br>

**2) 독서실 온습도 경고 기능** <br>
독서실 온도가 25도 이상이거나 습도가 65% 이상일 경우, 빨간색 LED를 깜빡거려 온습도가 적정오도가 아님을 알려준다.

![image-016](https://github.com/kyum-q/ReadingRoomManagement/assets/109158497/1403f5ea-48f6-4a8c-9815-05b9ed30bf14)
**<p align="center">[적정온도가 아닐 때 온습도 그래프 화면]</p>**
<br>

![image-017](https://github.com/kyum-q/ReadingRoomManagement/assets/109158497/25783e18-e4ff-4adf-a938-664f678adf44)
**<p align="center">[빨간색 LED가 켜진 상태]</p>**
<br><br>

### 🤵🏻&nbsp; 관리자 모드 실행 

#### 1. 관리자 로그인 웹 페이지
초기화면 페이지에서 manager 선택 후 나오는 로그인 웹페이지로, 기존에 관리자 ID와 password를 올바르게 입력해야지만 다음 페이지로 넘어갈 수 있다.

![image-018](https://github.com/kyum-q/ReadingRoomManagement/assets/109158497/bd64a59d-731e-4f8f-a90a-2af533c12f14)
**<p align="center">[관리자 로그인 웹 페이지]</p>**
<br><br>

#### - 로그인 시도 

1) id와 password를 틀렸을 시<br>
로그인 페이지에서 에러메시지를 띄워준다.

![image-019](https://github.com/kyum-q/ReadingRoomManagement/assets/109158497/63ce0b5d-96e4-4194-9c18-ed957b543221)
**<p align="center">[에러메시지 출력]</p>**
<br>

2) id와 password를 제대로 입력했을 시<br>
관리자 페이지로 전환된다.

#### 2. 관리자 모드 웹 사이트

![image-020](https://github.com/kyum-q/ReadingRoomManagement/assets/109158497/a700ee54-8e4b-4ead-a28d-9e0eed801da2)
**<p align="center">[관리자모드 웹 페이지]</p>**
<br><br>

#### - 독서실 자리 초음파 센서 변화 그래프
> Connect 버튼을 눌러야지 다양한 독서실 이용 시스템을 사용할 수 있다.

관리자 모드에서 Connect 하고 초음파 센서 변화 밑에 측정시작 버튼 누르면 현재 독서실에서 측정되는 초음파 센서 변화 값을 알아낼 수 있다. 이를 통해 현재 사용자가 존재하는지 어렴풋이 알 수 있다.

![image-021](https://github.com/kyum-q/ReadingRoomManagement/assets/109158497/d28fb8df-8d82-49da-b2df-3640b35a8e3b)
**<p align="center">[초음파 센서 변화 그래프 화면]</p>**
<br><br>

#### - 독서실 자리 카메라 기능
관리자 모드에서 독서실 내 카메라 확인 밑에 촬영 버튼 누르면 카메라를 작동시켜 사용자 존재 여부를 확실하게 알아낼 수 있다.

![image-022](https://github.com/kyum-q/ReadingRoomManagement/assets/109158497/6f62c2af-7ed2-4d55-b875-2976f9d56e13)
**<p align="center">[카메라 스트리밍 화면]</p>**
<br><br>

#### - 사용자 warning 기능 사용 유무 확인 기능
사용자가 warning 버튼 클릭 시, 호출이라는 글씨가 관리자 웹 사이트 나타난다.

![image-023](https://github.com/kyum-q/ReadingRoomManagement/assets/109158497/8f0ad972-3f7b-4595-b2fe-5502f0fda5ce)
**<p align="center">[호출 텍스트 확인되는 화면]</p>**
<br><br>

#### - 독서실 사용 종료
관리자 모드에서 독서실 자리 비우기 버튼 누를 시 [시간 종료 , LED 조명 모두 끄기 등] 독서실 이용을 종료 시킬 수 있다. 외에도 사용시간이 종료되거나 사용자가 사용을 임의로 종료했을 시(독서실 자리 비우기)에도 자동으로 LED가 모두 꺼진다.

![image-025](https://github.com/kyum-q/ReadingRoomManagement/assets/109158497/bd9c7e86-be84-48a0-a821-3740de46fee0)
**<p align="center">[사용자 자리비우기 화면]</p>**
<br>

![image-026](https://github.com/kyum-q/ReadingRoomManagement/assets/109158497/9929a579-95d7-4c87-9fc0-9e8744751431)
**<p align="center">[모든 LED가 꺼진 상태]</p>**
<br><br>
