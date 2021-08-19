class Human:
    def __init__(self, **kwargs):
        self.first_name = kwargs['first_name']
        self.last_name = kwargs['last_name']
    
    def show_full_name(self):
        self.show_first_name()
        self.show_last_name()
    
    def show_first_name(self):
        print(self.first_name)

    def show_last_name(self):
        print(self.last_name)

    def show_num(self):
        print(100)


if __name__ == '__main__':
    human01 = Human(first_name='Tanaka', last_name='Kei')
    human01.show_full_name()
    print(Human)