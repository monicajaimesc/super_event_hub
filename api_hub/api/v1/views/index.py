#!/usr/bin/python3
"""
this file has the end point route
"""
from api.v1.views import app_views
from flask import jsonify, request, abort, make_response
from models.db_mysql import db
import requests
import time

@app_views.route('/status', methods=["GET"])
def json_status():
    """
    return a json file
    """
    
    return jsonify({"status": "OK"})

@app_views.route('/companies', methods=["GET"], strict_slashes=False)
def companies():
    """
    It will list all the companies that we get from a microservice
    return: a JSON
    """
    res = requests.get('http://0.0.0.0:5002/companies')
  
    return jsonify(res.json())

@app_views.route('/company/<id>/products',methods=["GET"], strict_slashes=False)
def companies_by_id(id):
    """
    it will list companies by ide
    Return:
    """
    #print(id)
    #return 'hola'
    res = requests.get('http://0.0.0.0:5002/company/{}/products'.format(id))
    #return res
    return jsonify(res.json())
    
@app_views.route('/proveedores', methods=["GET"], strict_slashes=False)
def proveedores():
    """
    It will list all the companies that we get from a microservice
    return: a JSON
    """
    if request.method == "GET":
        cur = db.cursor()
        cur.execute("SELECT * FROM proveedor ORDER BY proveedor.id ASC")

        rows = cur.fetchall()
        console.log(rows)
    
