


class Service:
    def __init__(self, args):
        self.names = ["Назва", "Анотація", "Тип", "Версія", "Автор", "Умови", "Зареєстровані"]
        self.names_eng = ['title', 'annotation','type','version','author','terms','registered']
        try:
            self._properties = args
            self.title = args[0]
            self.annotation = args[1]
            self.type = args[2]
            self.version = args[3]
            self.authors = args[4]
            self.terms = args[5]
            self.registered = args[6]
        except Exception as exp:
            print(exp)
        
    def info(self) -> str:
        """Returns:
            str: [information about properties]
        """
        text = ''
        for i in range(len(self.names)):
            if self.names[i].lower() == "автор":
               for author in self.authors:
                  text += self.names[i] + ": " + author + '\n'  
            else:
                text += self.names[i] + ": " + self._properties[i] + '\n'
        text += '-'*10 + '\n'
        return text
    
    def properties(self) -> list:
        return self._properties
    
    def get_names_eng(self):
        return self.names_eng
        