import os
from flask import Flask, send_file, abort

app = Flask(__name__)

@app.route('/')
def index():
    # 获取文件列表
    files = os.listdir("files/")
    
    # 生成带样式的HTML页面
    html = '''
    <html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body {
                font-family: Arial, sans-serif;
                max-width: 800px;
                margin: 0 auto;
                padding: 15px;
                background-color: #f5f5f5;
            }
            h1 {
                color: #333;
                text-align: center;
                padding: 20px 0;
            }
            ul {
                list-style: none;
                padding: 0;
            }
            li {
                margin: 10px 0;
                background: white;
                border-radius: 8px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }
            a {
                display: block;
                padding: 15px 20px;
                color: #2196F3;
                text-decoration: none;
                font-size: 16px;
            }
            a:hover {
                background-color: #f0f0f0;
                border-radius: 8px;
            }
        </style>
    </head>
    <body>
        <h1>点击下载</h1>
        <ul>
    '''
    
    for filename in files:
        html += f'<li><a href="/download/{filename}">{filename}</a></li>'
    
    html += '</ul></body></html>'
    
    return html

@app.route('/download/<filename>')
def download_file(filename):
    FILE_DIRECTORY = "files/"
    file_path = os.path.join(FILE_DIRECTORY, filename)
    if not os.path.abspath(file_path).startswith(os.path.abspath(FILE_DIRECTORY)):
        abort(403)  # 返回 403 禁止访问
    elif not os.path.exists(file_path):
        abort(404)  # 返回 404 文件未找到
    else :
        try:
            return send_file(f"files/{filename}", as_attachment=True)
        except Exception as e:
            return str(e), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
