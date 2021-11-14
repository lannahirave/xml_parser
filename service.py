


class Service:
    def __init__(self, args):
        self.names = ["Назва", "Анотація", "Тип", "Версія", "Автор", "Умови", "Зареєстровані"]
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
        """[summary]

        Returns:
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
        