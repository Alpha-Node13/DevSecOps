from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    #return "Hello, Insecure World!"   # insecure variant
    return "Hello, Secure World!"

@app.route('/health')
def health():
    return {"status": "healthy"}

if __name__ == '__main__':
    #app.run(host='0.0.0.0', port=80)   # insecure variant: root on privileged port 80
    # Use non-privileged port and environment-based configuration
    port = int(os.getenv('PORT', 8080))
    app.run(host='0.0.0.0', port=port)