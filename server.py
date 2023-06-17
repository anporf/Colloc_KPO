import json
from flask import Flask, request
import db_functions

app = Flask(__name__)


@app.route('/rates', methods=['GET'])
def get_value():
    """
    Это api возвращает список всех возможных курсов валют
    :return: Список всех курсов
    """
    select_query = f'''SELECT currency_origin, currency_target, exchange FROM rates ;'''
    data = db_functions.get_from_db(select_query)
    response_data = {
        'rates': []
    }
    for row in data:
        response_data['rates'].append({
            row[0]: 1,
            row[1]: float(row[2])
        })
        response_data['rates'].append({
            row[1]: 1,
            row[0]: 1 / float(row[2])
        })
    response = app.response_class(response=json.dumps(response_data),
                                  status=200,
                                  mimetype='application/json')
    return response


@app.route('/exchange', methods=["POST"])
def exchange():
    """
    Это api переводит одну валюту, в другую
    :return: Количество денег в новой валюте
    """
    currency_origin = str(request.json['currency_origin'])
    currency_target = str(request.json['currency_target'])
    amount = float(request.json['amount'])
    select_query = f'''SELECT currency_origin, currency_target, exchange FROM rates 
                        WHERE currency_origin = "{currency_origin}" and currency_target = "{currency_target}";'''
    data = db_functions.get_from_db(select_query)
    status = 200
    if len(data) == 0:
        select_query = f'''SELECT currency_origin, currency_target, exchange FROM rates 
                            WHERE currency_origin = "{currency_target}" and currency_target = "{currency_origin}";'''
        data = db_functions.get_from_db(select_query)
        if len(data) == 0:
            response_data = {
                'status': 'failed',
                'message': 'Такого курса не существует'
            }
            status = 204
        else:
            response_data = {
                'status': 'success',
                'message': 'Валюта успешно переведена',
                'target': amount / float(data[0][2])
            }
    else:
        response_data = {
            'status': 'success',
            'message': 'Валюта успешно переведена',
            'target': amount * float(data[0][2])
        }
    response = app.response_class(response=json.dumps(response_data),
                                  status=status,
                                  mimetype='application/json')
    return response


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=2023)
