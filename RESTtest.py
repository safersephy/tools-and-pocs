from flask import Flask
from flask_restful import Resource, Api,reqparse

from flask import jsonify
import werkzeug

app = Flask(__name__)
api = Api(app)

class ProcessImageEndpoint(Resource):
    def __init__(self):
        # Create a request parser
        parser = reqparse.RequestParser()
        parser.add_argument("image", type=werkzeug.datastructures.FileStorage, location='files')
        self.req_parser = parser

    def post(self):
        # The image is retrieved as a file
        image_file = self.req_parser.parse_args(strict=True).get("image", None)
        if image_file:
            # Get the byte content using `.read()`
            image = image_file.read()
            # Now do something with the image...
            return "Yay, you sent an image!"

        else:
            return "No image sent :("

class Receipt(Resource):
    def get(self):
        result = {"type":"receipt","id":1}
        return jsonify(result)



api.add_resource(Receipt, '/receipt')
api.add_resource(ProcessImageEndpoint, '/upload')


if __name__ == '__main__':
     app.run(host= '0.0.0.0',port='5002')