import xml.sax
from service import Service

class XMLHandler(xml.sax.ContentHandler):
    """
    reimplemented xml sax parser class
    """
    def __init__(self):
        self.CurrentData = ''
        self.title = ''
        self.annotation = ''
        self.type = ''
        self.version = ''
        self.authors = []
        self.terms = ''
        self.registered = 0
        self.services_list = []
        
    def startElement(self, tag, attributes):
        self.CurrentData = tag
        
        if tag == 'service':
            self.title = ''
            self.annotation = ''
            self.type = ''
            self.version = ''
            self.authors = []
            self.terms = ''
            self.registered = 0

    
    def endElement(self, tag):
        """ 
        prints xml contents
        """
        """
        if self.CurrentData == "title":
            print("Назва:", self.title)
        elif self.CurrentData == "annotation":
            print("Анотація:", self.annotation)
        elif self.CurrentData == "type":
            print("Тип:", self.type)
        elif self.CurrentData == "version":
            print("Версія:", self.version)
        elif self.CurrentData == "author":
            for i in self.authors:
                print("Автор:", i)
        elif self.CurrentData == "terms":
            print("Умови:", self.terms)
        elif self.CurrentData == "registered":
            print("Кількість зареєстрованих:", self.registered)
        """        
        self.CurrentData = ''
    
    def characters(self, content):
        """
        Finds contents inside <> </>
        """
        if self.CurrentData == "title":
            self.title = content
        elif self.CurrentData == "annotation":
            self.annotation = content
        elif self.CurrentData == "type":
            self.type = content
        elif self.CurrentData == "version":
            self.version = content
        elif self.CurrentData == "author":
            self.authors.append(content)
        elif self.CurrentData == "terms":
            self.terms = content
        elif self.CurrentData == "registered":
            self.registered = content
            service = Service([self.title, self.annotation, self.type, self.version, \
                self.authors.copy(), self.terms, self.registered])
            self.services_list.append(service)
            self.authors.clear()
             
    def get_list(self):
        """
        Returns list of Services
        """
        return self.services_list   
