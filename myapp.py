import pandas as pd
from flask import Flask, render_template

app = Flask(__name__) # type: ignore
@app.route('/')
def index():
    # 从Excel文件中读取数据
    data = pd.read_excel('雅砻江水位-PC.xlsx')
    print(data.head())
    # 渲染模板并展示数据
    return render_template('index.html', data=data) # type: ignore
if __name__ == '__main__':
    app.run()