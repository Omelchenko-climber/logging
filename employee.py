import logging


logging.basicConfig(filename='employee.log', level=logging.INFO, format='%(levelname)s:%(message)s')


class Employee:
    
    def __init__(self, first, last) -> None:
        self.first = first
        self.last = last
        
        logging.info(f'Created Employee: {self.fullname} - {self.email}')
        
    @property
    def email(self):
        return f'{self.first}.{self.last}@email.com'
    
    @property
    def fullname(self):
        return f'{self.first} {self.last}'
    
    
emp_1 = Employee('John', 'Smith')
emp_2 = Employee('Anton', 'Omelchenko')
emp_3 = Employee('Tom', 'Thecat')