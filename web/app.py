from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import joblib
import numpy as np

app = Flask(__name__)
api = Api(app)


with open('NB_gazete_model.pkl', 'rb') as f:
    text_classifier = joblib.load(f)
    
parser = reqparse.RequestParser()
parser.add_argument('query')


class TextClassification(Resource):
	def get(self):
		args = parser.parse_args()
		user_query = args['query']

		class_name = np.array(["Magazin","Dünya","Spor","Siyaset","Kültür-Sanat","Teknoloji"])
		prediction = text_classifier.predict([user_query])[0]
		
		output = {'Prediction': class_name[prediction]}

		return output

api.add_resource(TextClassification, '/')



if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)


