from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
        return render_template('project.html')

@app.route('/manager/' , methods=['GET']) #get을 통해 데이터 전달 받음
def manager():
	return render_template('manager.html')

@app.route('/user/' , methods=['GET'])
def user():
	return render_template('user.html')

if __name__ == "__main__":
        app.run(host='0.0.0.0', port=8080)

