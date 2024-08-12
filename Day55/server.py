from flask import Flask

app = Flask(__name__)


def make_h1(func):
    def wrapper():
        return f"<h1>{func()}</h1>"
    return wrapper


@app.route('/')
@make_h1
def guess_number():
    return ('<h1>Guess a number between 0 and 9</h1>'
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">')


@app.route('/<int:number>')
def right_or_wrong(number):
    if number < 7:
        return ('<h1 style="color: red">Too low, try again!</h1>'
                '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">')
    elif number == 7:
        return ('<h1 style="color: green">You Found me!</h1>'
                '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">')
    else:
        return ('<h1 style="color: purple">Too high, try again!</h1>'
                '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">')
# <path:name>   '/'문자를 가져오기
# <int:number>  숫자형으로 가져오기


if __name__ == "__main__":
    app.run(debug=True)
# ---------------------------------------------------------------------------------------
# class User:
#     def __init__(self, name):
#         self.name = name
#         self.is_logged_in = False
#
#
# def is_authenticated_decorator(function):
#     def wrapper(*args, **kwargs):
#         if args[0].is_logged_in:
#             function(args[0])
#     return wrapper
#
#
# @is_authenticated_decorator
# def create_blog_post(user):
#     print(f"This is {user.name}'s new blog post.")
#
#
# new_user = User('MinSoo')
# new_user.is_logged_in = True
# create_blog_post(new_user)
# ------------------------------------------------------------------------------------
# inputs = list(map(int, input().split()))
#
#
# def decorator_function(function):
#     def wrapper(*args):
#         print(f"You called {function.__name__}{args}")
#         print(f"It returned: {function(*args)}")
#     return wrapper
#
#
# @decorator_function
# def a_function(a, b, c):
#     return a * b * c
#
#
# a_function(inputs[0], inputs[1], inputs[2])
