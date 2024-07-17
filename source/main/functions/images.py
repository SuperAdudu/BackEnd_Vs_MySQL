from source.main.models.images import Images
from source import db
from flask import request, jsonify,send_from_directory
import os
from werkzeug.utils import secure_filename


UPLOAD_FOLDER = os.path.abspath('media')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
BASE_URL = 'http://127.0.0.1:5000'

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def addImage():
    try:
        data = request.form
        file = request.files['image'] if 'image' in request.files else None
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            image_url = f"{BASE_URL}/media/{filename}"
        else:
            image_url = None
        new_image = Images(
            idModel=data['idModel'],
            idAlbum=data['idAlbum'],
            link=image_url
        )
        db.session.add(new_image)
        db.session.commit()
        return jsonify({"status":200,"message":"Add image successfull"})
    except Exception as e:
        return jsonify({"status":404,"message":str(e)})
    
def viewImage(filename):
    try:
        return send_from_directory(UPLOAD_FOLDER, filename)
    except Exception as e:
        return jsonify({"status":404,"message":str(e)})
    
def getImageByAlbum():
    try:
        data = request.form
        images = Images.query.filter(Images.idAlbum==data['idAlbum']).all()
        if images:
            result = []
            for image in images:
                result.append({
                    "idImage":image.id,
                    "idModel":image.idModel,
                    "link":image.link
                })
            return jsonify({"status":200,"data":result})
        else:
            return jsonify({"status":200,"message":"idAlbum is not correct"})
    except Exception as e:
        return jsonify({"status":404,"message":str(e)})
