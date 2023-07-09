from flask import Flask, render_template, request
from datetime import datetime
from circuit import controlLED

app = Flask(__name__)

Uid = 1234
Upasswd = 1234

# 관리자 로그인 페이지에 알맞는 id, password 설정
Utime = 0
nowHour = 0  # 사용자가 시간을 설정했을 때 시
nowMinute = 0  # 사용자가 시간을 설정했을 때 분
nowSecond = 0  # 사용자가 시간을 설정했을 때 초

# 사용자가 시간을 설정했을 때 관리자 페이지에서도 동일한 시간을 나타내기 위해
# 사용자가 다시 웹사이트에 들어왔을 때 사용시간이 얼마나 남았는지 확인하기 위해
# 사용중임을 알리기 위해 설정
Uwarning = " "

# 사용자가 warning 버튼을 눌렀을 때 관리자에게 호출을 알리기 위해 설정
def getTime():  # 사용자의 남은 시간 알아내는 함수
    now = datetime.now()
    itHour = now.hour - nowHour
    itMinute = now.minute - nowMinute
    itSecond = now.second - nowSecond
    # 사용자가 설정한 시간으로부터 얼마나 지나갔는지 알아내기
    if itHour < 0:
        itHour = 0
    if itMinute < 0:
        itMinute = 0
    if itSecond < 0:
        itSecond = 0
    # -값이 나올 경우를 대비
    itTime = (itHour * 60 * 60) + itMinute * 60 + itSecond
    # 시각을 초로 변경하기
    itTime = Utime - itTime  # 사용자 설정 시각을 초로 변경한 것 - 현재 시각을 초로 변경한 것: 지난 시간을 뺀 남은 시간
    if itTime <= 0:
        itTime = 0
    return itTime

def setEnd():  # 임의로 사용을 종료할 경우 호출 (LED 모두 끄기 and 시간하고 호출 메시지 초기화)
    global Utime, Uwarning
    Utime = 0
    Uwarning = " "
    controlLED(0)
    controlLED(2)
    controlLED(4)

@app.route('/')
def index():  # 초기 화면
    return render_template('project.html')

@app.route('/manager/', methods=['GET'])
def login():  # 초기화면에서 관리자 모드 로그인 페이지
    return render_template('managerLogin.html')

@app.route('/user/', methods=['GET'])
def userChoose():  # 초기화면에서 사용자 모드
    global Utime, nowHour, nowMinute, nowSecond, Uwarning
    if getTime() == 0 or Utime == 0:  # 사용자가 현재 없을 경우 (설정시간으로부터 시간이 지났거나 관리자 or 사용자가 임의로 사용종료)
        Utime = 0
        nowHour = 0
        nowMinute = 0
        nowSecond = 0
        Uwarning = " "
        # 값들 초기화
        return render_template('useChoose.html')  # 사용 설정 웹
    else:  # 독서실 사용중일 경우
        return render_template('useStudyRoom.html')  # 사용중 표시 웹

@app.route('/use/yes', methods=['GET'])
def yes():  # 사용자가 사용을 한다 했을 경우
    return render_template('timeSetting.html')  # 시간 설정 웹

@app.route('/use/no', methods=['GET'])
def no():  # 사용자가 사용을 안할 경우
    return render_template('project.html')  # 초기화면

@app.route('/timeset/', methods=['POST'])  # post을 통해 데이터 전달 받음
def timeset():  # 시간 설정
    hour = request.form['hour']
    minute = request.form['minute']
    second = request.form['second']
    # 웹 페이지에 name이 hour, minute, second인 것들의 값을 가져옴 (웹 페이지에서 설정한 사용시간)
    global Utime, nowHour, nowMinute, nowSecond
    Utime = int(second) + (int(minute) * 60) + (int(hour) * 60 * 60)  # 가져온 값을 초로 만들어 저장
    now = datetime.now()
    nowHour = now.hour
    nowMinute = now.minute
    nowSecond = now.second
    # 현재 시간 알아내 저장
    itTime = getTime()
    # 0초 이상의 값을 설정했을 경우 user 페이지로
    return render_template('user.html', time=itTime)

@app.route('/login', methods=['POST'])  # post을 통해 데이터 전달 받음
def user():
    global Uid, Upasswd, nowHour, nowMinute, nowSecond, Utime, Uwarning
    id = request.form['id']
    pw = request.form['pw']  # 웹에서 id와 pw 입력한 값 가져오기
    if id == str(Uid) and pw == str(Upasswd):  # 일치하는 정보를 입력했을 경우
        itTime = getTime()  # 현재 사용자 남은 시간 가져오기
        return render_template('manager.html', time=itTime, warning=Uwarning)
    else:  # 일치하는 정보를 입력하지 않았을 시 넘어가지 못함
        return render_template('managerLogin.html', msg="id와 password를 정확하게 입력해주세요.")

@app.route('/userEnd', methods=['GET'])
def userEnd():  # 관리자가 사용자 자리 비우기 버튼을 눌렀을 때
    setEnd()  # 설정 초기화
    return render_template('manager.html', time=Utime, warning=Uwarning)

@app.route('/End', methods=['GET'])
def End():  # 사용자가 자리 비우기 버튼을 눌렀을 때
    setEnd()  # 설정 초기화
    return render_template('project.html')

@app.route('/warning', methods=['GET'])
def setWarning():  # 사용자가 warning 버튼을 눌렀을 때
    global Uwarning
    Uwarning = "!!!호출!!!"  # Uwarning 글씨 변경
    itTime = getTime()  # 남은 시간 가져오기
    return render_template('user.html', time=itTime)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
