from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os
load_dotenv()
user = os.getenv('MONGO_USER')
password = os.getenv('MONGO_PASSWORD')
hostname = os.getenv('MONGO_HOSTNAME')
uri = f"mongodb+srv://{user}:{password}@{hostname}/?retryWrites=true&w=majority"

def conexion():
    try:
        # create a new client and connect to the server
        client = MongoClient(uri, server_api=ServerApi('1'))
        db=client['Laganga']
        client.admin.command('ping')
        print("Conexión Exitosa!")
        return db
    except exception as e:
        print("No se pudo Conectar",e)