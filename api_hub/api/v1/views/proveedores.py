#!/usr/bin/python3
"""
this file has the end point route
"""
from api.v1.views import app_views
from flask import jsonify, request, abort, make_response
from models.db_mysql import db
import requests
import time


@app_views.route('/proveedores', methods=["GET", "POST"], strict_slashes=False)
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
    
    if request.method == "POST":

