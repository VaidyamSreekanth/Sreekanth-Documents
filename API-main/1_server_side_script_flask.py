from flask import Flask, jsonify, request
import time

app = Flask(__name__)
cust_det = {'cust1':'KUMAR', 'cust2':'Balu'}

@app.route('/get', methods=['GET'])
def get_cust_details():
    '''
    To get all customer details
    '''
    time.sleep(2)
    return jsonify(cust_det)

@app.route('/create', methods=['POST'])
def create_customer():
    '''
    To create new record
    '''
    d = request.json
    cust_det.update(d)
    return jsonify(cust_det)

@app.route('/update', methods=['PUT'])
def update_emp():
    '''
    To update emp details
    '''
    d = request.json
    cust_det.update(d)
    keys = list(d.keys())
    k = keys[0]
    return ' {0} RECORD UPDATED SUCCESSFULLY'.format(k)

@app.route('/delete', methods=['DELETE'])
def delete_emp():
    '''
    To delete emp record
    '''
    d = request.json
    keys = list(d.keys())
    k = keys[0]
    del cust_det[k]
    return ' {0} record Deleted SUCCESSFULLY'.format(k)


l = []
@app.route('/list', methods=['POST'])
def add_list():
    '''
    Add values to the list
    http://127.0.0.1:5000/list
    {"list":[1,2,3,4]}
    '''
    d = request.json
    keys = list(d.keys())
    v = d[keys[0]]
    l.extend(v)
    print('\n\n\n\n ', type(v))
    return '{0}'.format(l)

# To run app
app.run(debug=True)

