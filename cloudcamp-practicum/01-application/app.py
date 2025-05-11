from flask import Flask, render_template_string
import os
import socket

app = Flask(__name__)

@app.route('/')
def index():
    host_name = socket.gethostname()
    ip_address = socket.gethostbyname(host_name)

    author = os.getenv('AUTHOR', 'Unknown')

    html = '''
        <h1>Информация о сервере</h1>
        <p><strong>Имя хоста:</strong> {{ host_name }}</p>
        <p><strong>IP адрес хоста:</strong> {{ ip_address }}</p>
        <p><strong>Автор:</strong> {{ author }}</p>
    '''

    return render_template_string(html, host_name=host_name, ip_address=ip_address, author=author)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

