#doamne ajuta sa nu mai codeze adi ca ma nenoroceste
import re
from elasticsearch import Elasticsearch
from datetime import datetime

from dataset import dataset

class Paragraph:
    def __init__(self, label:str, content:list) -> None:
        self.label = label
        self.content = content
        
def paragraphToJSON(paragraph):
    return {
        "label" : paragraph.label,
        "content" : paragraph.content
    }
        
class Document:
    def __init__(self):
        None
        
    def __init__(self, paragraphs: list, date):
        self.paragraphs = paragraphs
        self.date = date
        
    def toJSON(self):
        return {
            "paragraphs" : map(self.paragraphs, paragraphToJSON),
            "date": self.date
        }
        
class ElasticConnection(object):
    indexParagrafe = "datasets_docs"
    es = Elasticsearch(
        "https://localhost:9200",
        basic_auth=("elastic", "2y1FatvwqH=cb1DKzZU6"),
        ca_certs="/LegaROProject/http_ca.crt",
        verify_certs=False
    )
    
    @staticmethod
    def addDocument1(document: Document):
        ElasticConnection.es.index(index=ElasticConnection.indexParagrafe, document=document.toJSON())
        
    @staticmethod
    def addDocuments(documents: dict):
        ElasticConnection.es.index(index=ElasticConnection.indexParagrafe, document=documents)
        
    @staticmethod
    def getDocument():
        search_param = {
            'query': {
                'match': {
                    ''
                }
            }
}


# es.create(index="datasets_docs", id="2", document={})

dict = {}
with open("./dataset.py", "rt") as file:
    values = re.findall("\# File .+", file.read())
    
    arrayDocuments = []
    res = [value.split(" ") for value in values]
    
    for _res in res:
        try:
            dict[_res[2][2:]] = int(_res[4][1:])
            my_obj = dataset[int(_res[4][1:])]
            arrayDocuments.append(
                {
                    "docName": _res[2][2:],
                    "paragraphs": my_obj[1],
                    "date": ""
                }
            )
            ElasticConnection.addDocuments(arrayDocuments[-1])
        except Exception as e:
            print(e)
        
        
    print(len(arrayDocuments))
    
# Paragraph {
#     label string[]
#       content string
# }
#
#Document {
# paragraphs Paragraph[], date
#}

