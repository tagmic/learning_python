#使用web框架flask搭建简易服务
from flask import Flask,request,render_template
app=Flask(__name__)

#首页
@app.route('/',methods=['GET','POST'])
def home():
    return render_template('home.html')

#登录页面
@app.route('/login',methods=['GET'])
def signin():
    return render_template('login.html')

#验证登录信息
@app.route('/login_ok',methods=['POST'])
def signin_ok():
    username=request.form['username']
    password=request.form['password']
    if username=='admin'and password=='password':
        return render_template('login_ok.html',username=username)
    return render_template('login.html',message='Bad username or password',username=username)

if __name__=='__main__':
    app.run()