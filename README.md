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

**1) app.py** – 웹브라우저로부터 접속과 요청을 받아 처리하는 플라스크 앱<br>
&emsp;&emsp;&emsp;&emsp; : 모드 선택 모드 / 사용자 사용여부, 시간 설정 / 관리자 로그인 웹페이지 로딩 / 사용시간 설정(timer)<br><br>
**2) mqtt.py** – mqtt subscribe하고 publish하는 파이썬 코드<br>
&emsp;&emsp;&emsp;&emsp; : mqtt서버로부터 date 토픽을 subscribe하고 data 토픽을 publish하는 코드<br><br>
**3) circuit.py** – 초음파센서, LED 조정하는 파이썬 코드<br>
&emsp;&emsp;&emsp;&emsp; :  사용자 자리 초음파 센서를 값을 알아내고 LED 조명을 on/off하는 코드<br><br>
**4) environment.py** – 온습도센서 조정하는 파이썬 코드<br>
&emsp;&emsp;&emsp;&emsp; : 사용자 자리 온습도 센서 값을 알아내는 코드<br><br>
**5) myCamera.py** – 카메라 촬영하는 파이썬 코드<br>
&emsp;&emsp;&emsp;&emsp; : 카메라를 통해 사용자 자리를 촬영하고 openCV를 가지고 사람의 얼굴을 표시하는 코드<br><br>

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

1. 초기 화면 – 관리자 모드, 사용자 모드 중에 모드 선택할 수 있다

![image](https://user-images.githubusercontent.com/109158497/200008251-bf618b4c-630f-4b34-9f6a-4aa64900dcce.png)

<h2>사용자 모드</h2>

2 초기화면 페이지에서 user 선택 후 (사용자 권한 출입 관리 시스템 선택) 

1) 현재 독서실 사용중인 사용자가 없을 경우 – 사용여부 물어보는 웹페이지<br>
2) 현재 독서실 사용중인 사용자가 있을 경우 – 사용중임을 알리는 웹페이지<br>

![image](https://user-images.githubusercontent.com/109158497/200008530-3bc5424b-7150-4990-af82-6816aaf1f833.png)

3 2.1에서 사용자가 독서실 사용을 선택 할 경우 사용시간 설정하는 웹페이지 등장
- 버튼을 눌러 사용시간을 설정하거나 직접 입력을 통해 시간을 설정 할 수 있다.

![image](https://user-images.githubusercontent.com/109158497/200008724-813af02b-f015-43da-917b-bede516ce922.png)

4 사용시간 설정, timeset버튼 클릭 -> 사용자 모드 (초기 조명 상태)

![image](https://user-images.githubusercontent.com/109158497/200008786-7fc1c806-ec08-494c-8530-2a1be0c3168c.png)

![image](https://user-images.githubusercontent.com/109158497/200008812-33323b5d-5f37-446b-926d-9919dcbf02b4.png)

5 초음파센서 10cm 이내가 될 시 (조명 상태 – 흰색 조명 on)

![image](https://user-images.githubusercontent.com/109158497/200008897-60843edc-4452-42bc-952d-55eecb73a943.png)

6 사용자 웹사이트에 독서실 이용 누르고 흰, 초록, 노란 LED on 했을 시 (조명 상태)

![image](https://user-images.githubusercontent.com/109158497/200008950-a0373ac8-7460-41e1-8f26-96df9a63e499.png)

![image](https://user-images.githubusercontent.com/109158497/200008983-d1534c2b-76c4-46ac-be18-0a5fa5bf043c.png)

7 사용자 웹사이트에 독서실 온습도 그래프

![image](https://user-images.githubusercontent.com/109158497/200009024-3b96d49f-0ca4-4f1b-b87b-a78c3acfef08.png)

8 독서실 온도가 25도 이상이거나 습도가 65% 이상일 경우 (빨간색 LED 깜빡거림)

![image](https://user-images.githubusercontent.com/109158497/200009075-e60452ee-5d41-4f82-aa64-60d685910392.png)

![image](https://user-images.githubusercontent.com/109158497/200009136-41a6e61d-4a75-413b-87f4-ebd216cecf2d.png)

<h2>관리자 모드</h2>
1 초기화면 페이지에서 manager 선택 후 (관리자 권한 출입 관리 시스템 선택) - 관리자 로그인 페이지

![image](https://user-images.githubusercontent.com/109158497/200009486-d9120fdf-de27-4ba5-ac80-3812c1058632.png)

2 로그인 시도 

1) id와 password를 틀렸을 시<br>
2) id와 password를 제대로 입력했을 시 -> 관리자 모드<br>

![image](https://user-images.githubusercontent.com/109158497/200009661-b569a0e4-8c2b-4125-99fc-a6fb313b30c7.png)

3 관리자 모드에서 Connect 하고 초음파 센서 변화 밑에 측정시작 버튼 누른 뒤

![image](https://user-images.githubusercontent.com/109158497/200009777-b6bd1a21-67ab-44ec-bbee-746f57150e6f.png)

4 관리자 모드에서 독서실 내 카메라 확인 밑에 촬영 버튼 누른 뒤

![image](https://user-images.githubusercontent.com/109158497/200009831-35bc2448-afc8-4742-b4cd-550f4c10e7f0.png)

5 사용자모드에서 warning 버튼 누를 시 - 관리자 모드로 들어가서 보면 없던 호출이라는 글씨가 나타난다.

사용자 모드 || 관리자 모드

![image](https://user-images.githubusercontent.com/109158497/200010176-e663bfe7-1cee-4650-822c-801c0cde7970.png)

6 관리자 모드에서 독서실 자리 비우기 버튼 누를 시 (시간 종료 , LED 조명 모두 off)<br>
+ 이 외에도 사용시간이 종료되거나 사용자가 사용을 임의로 종료했을 시(독서실 자리 비우기)에도 자동으로 led가 모두 꺼진다.

![image](https://user-images.githubusercontent.com/109158497/200010308-f7c78e1c-d713-4768-bbaa-68c6fe8d28fc.png)
![image](https://user-images.githubusercontent.com/109158497/200010346-588b675d-5932-4707-90aa-656341e355ff.png)


