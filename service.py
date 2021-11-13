class Service:
    def __init__(self, args):
        self.names = ["Назва", "Анотація", "Тип", "Версія", "Автор", "Умови", "Зареєстровані"]
        
        try:
            self.properties = args
            self.title = args[0]
            self.annotation = args[1]
            self.type = args[2]
            self.version = args[3]
            self.authors = args[4]
            self.terms = args[5]
            self.registered = args[6]
        except Exception as exp:
            print(exp)
        
    def info(self):
        return [self.title, self.annotation, self.type, self.version, self.authors,\
            self.terms, self.registered]
        
    def set_from_dict(self):
        pass