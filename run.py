from flask import Flask, g
from flask_restful import Resource, Api, reqparse
import shelve

app = Flask(__name__)
api = Api(app)

def get_db():
	db = getattr(g, '_database', None)
	if db is None:
		db = g._database = shelve.open("devices.db")
	return db

class Index(Resource):
	def get(self):
		db = get_db()

		categories = list(db.keys())
		
		json = {}
		for category in categories:
			json[category] = db[category]

		return {"Page": "Index", "Data": json}

class Categories(Resource):
	def __init__(self):
		self.db = get_db()

	def get(self):
		categories = list(self.db.keys())
		
		return {"Categories": categories}

	def post(self):
		try:
			parser = reqparse.RequestParser()
			parser.add_argument('identifier')
			args = parser.parse_args()
			
			if args['identifier'] == "":
				return {"Error": "Category value cannot be empty"}

			categories = list(self.db.keys())

			if not categories.count(args['identifier']):
				self.db[args['identifier']] = []
				return {"Inserted": args['identifier']} 
			else:
				return {"Error": "Category already exists"}, 409 # Conflict
		except:
			return {"Error": "400 - Bad Request"}, 400 # Bad Request

	def put(self):
		try:
			parser = reqparse.RequestParser()
			parser.add_argument('identifier')
			parser.add_argument('replacement')
			args = parser.parse_args()
			
			if args['replacement'] == "":
				return {"Error": "Replacement value cannot be empty"}

			categories = list(self.db.keys())

			if categories.count(args['identifier']):
				del self.db[args['identifier']]
				self.db[args['replacement']] = []

				return {"Updated": args['identifier'], "Replacement": args['replacement']}
			else:
				return {"Error": "Category doesn't exist"}, 404
		except:
			return {"Error": "400 - Bad Request"}, 400

	def delete(self):
		try:
			parser = reqparse.RequestParser()
			parser.add_argument('identifier')
			args = parser.parse_args()

			del self.db[args['identifier']]

			return {"Deleted": args['identifier']} 	
		except:
			return {"Error": "400 - Bad Request"}, 400

class Products(Resource):
	def __init__(self):
		self.db = get_db()

	def get(self, category):
		try:
			return {category: self.db[category]}
		except:
			return {"Error": "Category not found"}, 404

	def post(self, category):
		try:
			parser = reqparse.RequestParser()
			parser.add_argument('identifier')
			args = parser.parse_args()

			if args['identifier'] == "":
				return {"Error": "Category value cannot be empty"}

			arr = self.db[category]

			if not arr.count(args['identifier']):
				arr.append(args['identifier'])
				arr.sort()

				self.db[category] = arr

				return {"Inserted": args['identifier']} 	
			else:
				return {"Error": "Product already inseted"}, 409
		except:
			return {"Error": "400 - Bad Request"}, 400

	def put(self, category):
		try:
			parser = reqparse.RequestParser()
			parser.add_argument('identifier')
			parser.add_argument('replacement')
			args = parser.parse_args()

			if args['replacement'] == "":
				return {"Error": "Replacement value cannot be empty"}

			arr = self.db[category]

			if arr.count(args['identifier']):
				arr.remove(args['identifier'])
				arr.append(args['replacement'])
				arr.sort()
				
				self.db[category] = arr

				return {"Updated": args['identifier'], "Replacement": args['replacement']} 	
			else:
				return {"Error": "Product doesn't exist"}, 404
		except:
			return {"Error": "400 - Bad Request"}, 400

	def delete(self, category):
		try:
			parser = reqparse.RequestParser()
			parser.add_argument('identifier')
			args = parser.parse_args()

			arr = self.db[category]

			if arr.count(args['identifier']):
				arr.remove(args['identifier'])

				self.db[category] = arr

				return {"Deleted": args['identifier']} 	
			else:
				return {"Error": "Product not found"}, 404
		except:
			return {"Error": "400 - Bad Request"}, 400


api.add_resource(Index, "/")
api.add_resource(Categories, "/categories")
api.add_resource(Products, "/categories/<string:category>")



if __name__ == "__main__":
	app.run(debug=True)










