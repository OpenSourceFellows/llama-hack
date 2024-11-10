# api_clients/mindsdb_client.py
from mindsdb_sdk import Client
from config import MINDSDB_API_KEY

def connect_mindsdb():
    client = Client("https://cloud.mindsdb.com", api_key=MINDSDB_API_KEY)
    return client

def query_mindsdb(client, query):
    result = client.sql.query(query)
    return result.fetchall()
