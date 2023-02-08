import json
import time
import sys
import tensorflow as tf
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
sys.path.append("../../")

from configs.main_config import ELASTIC_SEARCH_BODY_FOR_DOCUMENTS

class ElasticSearchConnect:
    def __init__(self, host_port_dict) -> None:
        self.host_port_dict=host_port_dict
        self.es= Elasticsearch([self.host_port_dict])
    def check_connection(self):
        if self.es.ping():
            print("Elastic search connected.....")
            return self.es
        else:
            print(f"Elastic search not connected with {self.host_port_dict}")
            return False
    def get_elastic_cursor(self):
        if self.check_connection():
            return self.es
        else:
            return None
    def create_index(self, index_name, index_body):
        ret = self.get_elastic_cursor().indices.create(index=index_name, ignore=400, body=index_body) #400  caused by IndexAlreadyExistsException, 
        print(json.dumps(ret,indent=4))

if __name__=="__main__":
    host_port_dict={
        'host': 'localhost', 
        'port': 9300,
        'scheme': "http"
        }
    ElasticSearchConnect(host_port_dict).create_index(index_name="questions_index", index_body=ELASTIC_SEARCH_BODY_FOR_DOCUMENTS )
    cursor=db.get_elastic_cursor()
    if cursor.ping():
        print("connected")
    else:
        print("not connected")
    



