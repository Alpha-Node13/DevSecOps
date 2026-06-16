from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, Insecure World!"
    #return "Hello, Secure World!" #Uncomment this line when using Dockerfile.secure.

@app.route('/health')
def health():
    return {"status": "healthy"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
    # Use non-privileged port and environment-based configuration
   # port = int(os.getenv('PORT', 8080)) #Uncomment this line when using Dockerfile.secure.
   # app.run(host='0.0.0.0', port=port)  #Uncomment this line when using Dockerfile.secure.