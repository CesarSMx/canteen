from flask import Flask, request, make_response, redirect, render_template
#resquest is used to get information about the user throug the browser 


#we pass the name of the app, in this case will be main.py
app = Flask(__name__)

@app.route('/')
def index():
    user_ip = request.remote_addr
    response = make_response(redirect('/hello'))
    response.set_cookie('user_ip', user_ip)

    return response

    
@app.route('/hello')
def  hello():
    user_ip = request.cookies.get('user_ip')
    return f'Hello there, your IP is {user_ip}' #will print the message on screen


if __name__ == '__main__':
    app.run(debug=True) #This could replace the use of enviroment variables such as FLASK_APP=main.py and FLASK_DEBUG=1
