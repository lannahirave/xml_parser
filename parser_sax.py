import xml.etree.ElementTree as ET

class Parser:
    def __init__(self):
        self.array_with_dicts = [] 
       
    def parse(self):
        
        tree = ET.parse('services.xml')
        root = tree.getroot()
        for child in root:
            d = {}
            authors = []
            for i in range(len(child)):
                #print(child[i].tag + ': ' + child[i].text)
                if child[i].tag == 'Автор':
                    authors.append(child[i].text)
                    d[child[i].tag] = authors
                else:
                    d[child[i].tag] = child[i].text
            self.array_with_dicts.append(d)
    
    def get_array(self):
        return self.array_with_dicts

if __name__ == "__main__":
    parser = Parser()
    parser.parse()
    xml = parser.get_array()
    for item in xml:
        print(item)