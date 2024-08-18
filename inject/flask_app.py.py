from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

received_data = ""  # 用于存储输入的内容

@app.route('/')
def main_page():
    return render_template('main.html')

@app.route('/input')
def input_page():
    return render_template('input.html')

@app.route('/receive', methods=['GET', 'POST'])
def receive_page():
    global received_data
    if request.method == 'POST':
        received_data = request.form.get('q')  # 获取从 input.html 提交的数据
        return jsonify({'status': 'success'})  # 返回成功状态
    elif request.method == 'GET':
        # 处理 GET 请求，返回当前存储的数据
        return render_template('receive.html', received_data=received_data)
    else:
        return jsonify({'error': 'Method not allowed'}), 405

if __name__ == '__main__':
    app.run(debug=True)
