from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

#this data comes from database
listOfDictionary = [{'name':'akash', 'age':24, 'deptName':'cs'}, 
                    {'name':'mayank', 'age':31, 'deptName':'mech'}, 
                    {'name':'alisha', 'age':22, 'deptName':'arts'}]

# return html page
@app.route('/')
def home():
    # connect db
    # fetch from database using select query
    # return response
    return render_template('home.html', data= listOfDictionary)

# return 
@app.route('/hello', methods=['POST','GET'])
def hello():
    # distric_id = request.get("distric_id")
    # date = request.get("date")
    # connect to nic database server(using password and username)
    # write sql to fetch vaccine availability
    # retrun json response
    if request.method == "POST":
        return "POST Request"
    
    elif request.method=='GET':
        return"Get Request"
    

@app.route('/db')
def anyFuncName():

    # connect db
    # fetch from database using select query
    # return response
    return jsonify({'sessions':listOfDictionary})


if __name__ == '__main__':
    # app.run(host="0.0.0.0", port=int(appConfig['flaskPort']), debug=True)
    app.run(debug=True)