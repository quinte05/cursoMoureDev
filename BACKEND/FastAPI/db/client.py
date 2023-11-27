from pymongo import MongoClient

#Base de Datos Local
#db_client = MongoClient().local

#Base de Datos Remota
db_client = MongoClient("mongodb+srv://quinte05:ThmKNr5NBDMCOv3Z@cluster0.ov0rqh2.mongodb.net/?retryWrites=true&w=majority").test