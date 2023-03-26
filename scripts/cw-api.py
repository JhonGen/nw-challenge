from flask import Flask,request
from flask_restful import Resource, Api
import pickle
import pandas as pd
from flask_cors import CORS


app = Flask(__name__)
#
CORS(app)
# creating an API object
api = Api(app)

#prediction api call
class prediction(Resource):
    def get(self,budget):
        #budget = request.args.get('budget')
        print(budget)
        # Let's load the package
        budget = [int(budget)]
        df = pd.DataFrame(budget, columns=[])
        model = pickle.load(open('../model/XGB_model.pkl', 'rb'))
        prediction = model.predict(df)
        prediction = int(prediction[0])
        return str(prediction)

#data api
class getData(Resource):
    def get(self):
            df = pd.read_csv('data.xlsx')
            df =  df.rename({}, axis=1)  # rename columns
            #print(df.head())
            #out = {'key':str}
            res = df.to_json(orient='records')
            #print( res)
            return res

#
api.add_resource(getData, '/api')
api.add_resource(prediction, '/prediction/<int:budget>')

if __name__ == '__main__':
    app.run(debug=True)