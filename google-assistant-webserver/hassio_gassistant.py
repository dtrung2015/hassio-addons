from actions import say
from flask import Flask, request
from flask_restful import Resource, Api
import threading
app = Flask(__name__)
api = Api(app)

def start_server():
    app.run(host='0.0.0.0',port=5001)

def main():
        class tts(Resource):
            def get(self):
                message = request.args.get('message', default = 'This is a test!')
                say(message)
                return {'status': 'OK'}
        api.add_resource(tts, '/tts')
        server = threading.Thread(target=start_server,args=())
        server.setDaemon(True)
        server.start()

if __name__ == '__main__':
    main()
