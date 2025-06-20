from flask import Flask

app = Flask(__name__)

# 创建一个路由(route)，告诉程序当有人访问根目录("/")时该做什么
@app.route("/")
def hello_world():
    # 返回一个简单的字符串
    return "Hello, World!"