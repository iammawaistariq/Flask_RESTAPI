from flask import Flask,render_template, request, jsonify

app = Flask(__name__)


data = []
@app.route("/", methods = ['GET','POST'])
def home2():
    if request.method=="POST":
        name = request.json['name']
        email = request.json['email']
        address = request.json['address']
        roll = request.json['roll']
        course = request.json['course']
        
        record = {'name':name,
                  'email':email,
                  'address':address,
                  'roll':roll,
                  'course':course
                }
        data.append(record)
    
        return jsonify(data)
    
    else:
        return render_template("home2.html",data=data)

@app.route("/about2", methods = ['GET','POST'])
def About2():
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)