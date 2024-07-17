from source.main.models.idols import Idols
from flask import jsonify, request
from source import db
def getAllIdols():
    try:
        idols = Idols.query.all()
        data = []
        for idol in idols:
            data.append({"id":idol.id,"name":idol.name})
        return jsonify({'status':200,'data':data})
    except Exception as e:
        return jsonify({'status':404,'message':str(e)})
    
def addIdols():
    try:
        data = request.form
        idol = Idols(name=data['name'])
        db.session.add(idol)
        db.session.commit()
        return jsonify({'status':200,'message':'Add idol successful'})
    except Exception as e:
        return jsonify({'status':404,'message':str(e)})