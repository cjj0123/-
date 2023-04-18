# 调用另一个python程序“雅砻江水位查询headless.py"
import subprocess

import pandas as pd
from flask import Flask, render_template

# 执行命令
cmd = ['c:/python3.8/python.exe', '雅砻江水位按站名查询headerless.py']
process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# 等待命令完成
stdout, stderr = process.communicate()
exit_code = process.wait()

# 输出命令的输出和错误信息
if exit_code == 0:
    print("命令成功执行")
else:
    print("命令执行失败")

app = Flask(__name__) # type: ignore
@app.route('/')
def index():
    # 从Excel文件中读取数据
    data = pd.read_excel('雅砻江站名水位-PC.xlsx')
    # 图片文件名列表
    images = ['锦屏一级.png', '官地.png', '二滩.png']
    # 渲染模板并展示数据和图片
    return render_template('index.html', data=data, image= images) # type: ignore
if __name__ == '__main__':
    app.run(use_reloader=False, use_debugger=False)