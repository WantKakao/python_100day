from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/bye')
def say_bye():
    return 'bye'

if __name__ == "__main__":
    app.run()


# import time
#
# def delay_func(fnc):
#     def real_func():
#         time.sleep(2)
#         fnc()
#         fnc()
#     return real_func
#
# @delay_func
# def say_hello():
#     print('hello')
#
# def say_bye():
#     print('bye')
#
# say_hello()
# say_bye()
# say_hell = delay_func(say_bye)
# say_hell()
