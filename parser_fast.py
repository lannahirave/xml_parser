import xml.etree.ElementTree as ET
from service import Service


class Parser:
    def __init__(self):
        self.services_list = [] 
       
    def parse(self, path='services.xml'):
        self.services_list.clear()
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
    
    def get_array(self):
        return self.services_list

if __name__ == "__main__":
    parser = Parser()
    parser.parse('services.xml')
    xml = parser.get_array()
    for item in xml:
        print(item.info())