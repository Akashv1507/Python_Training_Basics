from flask import Flask, jsonify, render_template

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
@app.route('/hello')
def hello2():
    return "hello hello"

@app.route('/db')
def anyFuncName():
    # connect db
    # fetch from database using select query
    # return response
    return jsonify(listOfDictionary)


if __name__ == '__main__':
    # app.run(host="0.0.0.0", port=int(appConfig['flaskPort']), debug=True)
    app.run(debug=True)