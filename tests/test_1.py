import unittest
import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
import strategy

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

file = 'file.xml'
answers = ['Розклад занять для студентів ФКНК', 'Розклад', 'Електронний', 'Фінальна версія', ['Юрій Головач', 'Євген Пархоменко', 'Ярослав Великий'], 'Вільні умови', '1524'],\
['Розклад занять для викладачів ФКНК', 'Розклад', 'Електронний', 'Фінальна версія', ['Олена Висоцька'], 'Вільні умови', '123'],\
['Відомість студентів', 'Відомість з відмітками', 'Фізичний', 'Фінальна версія', ['Кіріл Шевчук', 'Антон Работніков', 'Максим Гнідченко'], 'Для викладачів', '110'],\
['Тритон', 'Помічник студента', 'Електронний', 'Редагуєма версія', ['Наполеон', 'Деканат №1', 'Деканат №3'], 'Для студентів', '31253']

class Tests(unittest.TestCase):
    def test_sax(self):
        """
        SAX parser testing
        """
        #print('----------------------------------------------------------------------')
        parser = strategy.SAX_parser()
        parser.parse(file)
        answer = parser.get_list()
        for i in range(len(answer)):
            self.assertEqual(answer[i].properties(), answers[i])
        print(bcolors.OKGREEN + "SAX SUCCESS." + bcolors.ENDC)
        
    def test_fast(self):
        """
        FAST parser testing
        """
        #print('----------------------------------------------------------------------')
        parser = strategy.FAST_parser()
        parser.parse(file)
        answer = parser.get_list()
        for i in range(len(answer)):
            self.assertEqual(answer[i].properties(), answers[i])
        print(bcolors.OKGREEN + "FAST SUCCESS." + bcolors.ENDC)
    
    def test_dom(self):
        """
        DOM parser testing
        """
        #print('----------------------------------------------------------------------')
        parser = strategy.DOM_parser()
        parser.parse(file)
        answer = parser.get_list()
        for i in range(len(answer)):
            self.assertEqual(answer[i].properties(), answers[i])
        print(bcolors.OKGREEN + "DOM SUCCESS." + bcolors.ENDC)
 

if __name__ == '__main__':
    unittest.main()