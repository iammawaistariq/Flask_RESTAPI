from flask import Flask,render_template, request, jsonify

app = Flask(__name__)

stores = [
    {
        'name': 'Store 1',
        'items': [
            {
                'name':'flowers 1',
                'price':100
            }
        ]
    }
    ,
    {
        'name': 'Store 2',
        'items': [
            {
                'name':'flowers 2',
                'price':100
            }
        ]
    }
]

@app.route("/")
def home():
    return "Hello API"


@app.route("/store", methods = ['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)   

@app.route('/store/<string:name>')
def get_store_name(name):
    for store in stores:
        if(store['name']==name):
            return jsonify(store)
    return jsonify({'message':'store not found'})


@app.route('/store')
def get_all_store_name():
    return jsonify({'stores':stores})


@app.route("/store/<string:name>/item", methods = ['POST'])
def create_store_item(name):
    request_data = request.get_json()
    for store in stores:
        if(store['name']==name):
            new_item = {
                'name': request_data['name'],
                'price':request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'mesage':'store not found'})
        
    return jsonify({'message':'store not found'})

@app.route("/store/<string:name>/item", methods = ['POST'])
def get_store_item(name):
    for store in stores:
        if(store['name']==name):
            return jsonify(store['items'])
        
    return jsonify({'message':'store not found'})

app.run(port=5000)

if __name__ == "__main__":
    app.run(debug=True)