'''

from flask import Flask,request
app = Flask(__name__)
@app.route('/sum')
def calculate_sum():
    args=request.args
    try:
        number1=float(args.get("number1",0))
        number2=float(args.get("number2",0))
        total=number1+number2
        return str(total)
    except (TypeError,ValueError):
        return "invalid input: please provide a valid number for number 1 and number 2",400

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=5000,debug=True,use_reloader=False)
'''
'''
from flask import Flask, request, jsonify
'''
app = Flask(__name__)
'''
@app.route('/sum')
def calculate_sum():
    args = request.args
    try:
        number1 = float(args.get("number1"))
        number2 = float(args.get("number2"))
        total_sum = number1 + number2
        response = {
            "number1": number1,
            "number2": number2,
            "total_sum": total_sum
        }
        return jsonify(response)
    except (TypeError, ValueError):
        return 'Invalid input: Please provide a valid number for number1 and number2', 400

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True, use_reloader=False)
'''
#ex1
from flask import Flask, Response
import json
import math
app = Flask(__name__)
@app.route('/prime_number/<number>')
def is_prime(number):
    try:
        int_number = int(number)
        check = True
        for i in range(2, int(math.sqrt(int_number) + 1)):
            if int_number % i == 0:
                check = False
                break
        if int_number < 2:
            check = False
        response = {"Number": number}
        if check:
            response["isPrime"] = True
        else:
            response["isPrime"] = False
        return response
    except ValueError:
        response = {
            "message": "Invalid number as input",
            "status": 400
        }
        json_response = json.dumps(response)
        http_response = Response(response = json_response, status = 400, mimetype = "application/json")
        return http_response

@app.errorhandler(404)
def page_not_found(error_code):
    response = {
        "message": "Invalid endpoint",
        "status": 404
    }
    json_response = json.dumps(response)
    http_response = Response(response = json_response, status = 404, mimetype = "application/json")
    return http_response

if __name__ == '__main__':
    app.run(use_reloader = True, host ="127.0.0.1", port = 5000)


#ex2
from flask import Flask, Response
import json
import mysql.connector

connection = mysql.connector.connect(
    host = '127.0.0.1',
    port = 3306,
    database = 'flight_game',
    user = 'root',
    password = '16102006',
    autocommit = True
)

app = Flask(__name__)
@app.route('/airport/<icao>')
def get_airport(icao):
    try:
        sql = """SELECT name, municipality FROM airport WHERE ident = %s;"""
        cursor = connection.cursor(dictionary = True)
        cursor.execute(sql, (icao,))
        result = cursor.fetchone()
        response = {
            "ICAO": icao,
            "Name": result["name"],
            "Location": result["municipality"]
        }
        return response
    except ValueError:
        response = {
            "message": "Invalid ICAO code.",
            "status": 400
        }
        json_response = json.dumps(response)
        http_response = Response(response = json_response, status = 400, mimetype = "application/json")
        return http_response

@app.errorhandler(404)
def page_not_found(error_code):
    response = {
        "message": "Invalid endpoint.",
        "status": 404
    }
    json_response = json.dumps(response)
    http_response = Response(response = json_response, status = 404, mimetype = "application/json")
    return http_response

if __name__ == '__main__':
    app.run(use_reloader = True, host = '127.0.0.1', port = 5000)



