from abc import ABC, abstractmethod
from sax_parser import XMLHandler
import xml.sax
import xml.etree.ElementTree as ET
import xml.dom.minidom
from service import Service


class Parser(ABC):
    """
    The Strategy interface declares operations common to all supported versions
    of some algorithm.

    The Context uses this interface to call the algorithm defined by Concrete
    Strategies.
    """
    @abstractmethod
    def parse(self, path) -> None:
        pass
    
    @abstractmethod
    def get_list(self) -> list:
        pass
    

class SAX_parser(Parser):
    def parse(self, path):
        #print("SAX", path)
        parser = xml.sax.make_parser()
        parser.setFeature(xml.sax.handler.feature_namespaces, 0)

        self.Handler = XMLHandler()
        parser.setContentHandler(self.Handler)
        parser.parse(path)
    
    def get_list(self) -> list:
        return self.Handler.get_list()

 
class DOM_parser(Parser):
    def parse(self, path):
        #print("DOM", path)
        self.services_list = []
        dom = xml.dom.minidom.parse(path)
        dom.normalize()
        services = dom.getElementsByTagName('service')
        for service in services:
            d = {}
            authors = []
            for item in service.childNodes:
                if type(item) != xml.dom.minidom.Text:
                    #print(item)
                    if item.nodeName.lower() in ('author', 'автор'):
                        authors.append(item.firstChild.nodeValue)
                        d[item.nodeName] = authors
                    else:
                        d[item.nodeName] = item.firstChild.nodeValue
            items = []
            for i in d.values():
                items.append(i)
            #print(items)
            self.services_list.append(Service(items))
    
    def get_list(self) -> list:
        return self.services_list 


class FAST_parser(Parser):
    def parse(self, path):
        #print("FAST", path)
        self.services_list = []
        tree = ET.parse(path)
        root = tree.getroot()
        for child in root:
            d = {}
            authors = []
            for i in range(len(child)):
                #print(child[i].tag + ': ' + child[i].text)
                if child[i].tag == 'Автор' or child[i].tag.lower() == 'author':
                    authors.append(child[i].text)
                    d[child[i].tag] = authors
                else:
                    d[child[i].tag] = child[i].text
            items = []
            for i in d.values():
                items.append(i)
            #print(items)
            self.services_list.append(Service(items))
    
    def get_list(self) -> list:
        return self.services_list
    
class Context():
    def __init__(self, strategy: Parser):
        self._strategy = strategy
    
    @property
    def strategy(self) -> Parser:
        return self._strategy
    
    @strategy.setter
    def strategy(self, strategy: Parser) -> None:
        self._strategy = strategy
    
    def parse(self, path) -> list:
        self._strategy.parse(path)
        return self._strategy.get_list()