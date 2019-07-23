from flask import Flask,render_template
from concurrent.futures import ThreadPoolExecutor
import attendance.py

executor = ThreadPoolExecutor(1)

app = Flask(__name__)




@app.route('/')
def index():
    executor.submit(countdown)
    return render_template('index.html')




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
