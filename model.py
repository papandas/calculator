'''
created on Apr 19, 2022

@author Papan Das
'''

class Model:
    '''
    classdocs
    '''

    def __init__(self):
        '''
        constructor
        '''

        self.previous_value = ''
        self.value = ''
        self.operator = ''


    def calculate(self, caption):
        print(f'Model <<calcualte : {caption}>>')
        if caption == 'C':
            self.previous_value = ''
            self.value = ''
            self.operator = ''

        elif caption == '+/-':
            self.value = self.value[1:] if self.value[0] == '-' else '-' + self.value

        elif caption == '%':
            value = float(self.value) if '.' in self.value else int(self.value)
            self.value = str(value / 100)

        elif caption == '/':
            pass

        elif caption == '=':
            value = self._evaluate()
            if str(value).endswith('.0'):
                value = int(value)

            self.value = str(value)

        elif caption == '.':
            # Check if decimal do not exist
            if not caption in self.value:
                self.value += caption

        elif isinstance(caption, int):
            self.value += str(caption)

        elif caption == 'back':
            #print(self.value, self.value[::-1])
            pass

        else:
            if self.value:
                self.operator = caption
                self.previous_value = self.value
                self.value = ''


        return self.value

    def _evaluate(self):
        try:
            return eval(self.previous_value + self.operator + self.value)
        except Exception as e:
            print(f"Model <<{e}>>")