# from source import app
from source.main.functions.idols import *

def register_routes_idols(app):

    app.add_url_rule('/api/idols/get_all_idol',methods=["GET"],view_func=getAllIdols)

    app.add_url_rule('/api/idols/add_idol',methods=["POST"],view_func=addIdols)