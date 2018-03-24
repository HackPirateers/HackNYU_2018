from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
import os
import io
import numpy

#     train_x[i] = list(map(degreeRankings.get,train_x[i]))
#     train_x[i] = list(map(educationRankings.get,train_x[i]))
#     train_x[i] = list(map(companyRankings.get,train_x[i]))
#
# print(train_x[44])

# API stuff

app = Flask(__name__)
CORS(app)  # <-- CORS is necessary for React.js's Axion to be able to use the methods in the api!
api = Api(app)

notes = {}


class Test(Resource):
    def put(self):
        # Parsing. View docs(https://flask-restful.readthedocs.io/en/latest/) if this isn't what you need.
        # parser.add_argument('list', action='append') lets flask know that list an argument that can hold 2+ pieces of data in this data :
        # put('http://localhost:5000/', data={"list" : ["When was Barack Obama's birthday?", "What is 10 plus 5 equal to?"]}).json()
        # With that, you have one piece of metadata associated with 2 or more peice of data(aka a list) that can be indexed
        # args is the main class here, and since list is the subclass(an arg of class args) of args, we can mention it freely
        # and access it like this : args.list. We can index by doing args.list[index]

        # parser = reqparse.RequestParser()
        # parser.add_argument('input')
        # args = parser.parse_args()
        # print(request.form)
        # print(args.list[0], " ", args.list[1])
        # notes[0] = args.list
        # print("Notes ")


        #http = urllib3.PoolManager()
        # url = 'http://api.glassdoor.com/api/api.htm?t.p=233537&t.k=b3Bt5z7OKJs&userip=0.0.0.0&useragent=&format=json&v=1&action=employers&jobTitle="Data Scientist"&q="IBM"'
        #
        # hdr = {'User-Agent': 'Mozilla/5.0'}
        # req = urllib3.Request(url, headers=hdr)
        # response = urllib2.urlopen(req)
        # # soup = BeautifulSoup(response)
        # hdr = {'User-Agent': 'Mozilla/5.0'}

        #CAMERA STUFF HERE.......

         # Formatting this is important. If you don't format it right,
        return z  # React won't get anything/ won't be able to index it.


api.add_resource(Test, '/')

if __name__ == '__main__':
    app.run(debug=True)
