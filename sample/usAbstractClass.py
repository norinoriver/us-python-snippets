from abc import ABCMeta, abstractclassmethod, abstractmethod

class Users(metaclass=ABCMeta):
    @abstractmethod
    def get_name(self, user_id: int)-> str:
        pass

    @abstractmethod
    def put_name(self, user_id: int, name: str):
        pass

    def get_family_name(self, user_id) -> str:
        return self.get_family_name(user_id.split())[0]

class DictUsers(Users):
    def __init__(self, d: dict):
        self._d = d

    def get_name(self, user_id: int) -> str:
        return self._d[user_id]

def add_honor(name:str, is_female:bool) -> str:
    if is_female:
        return 'Ms. ' + name

    else:
        return 'Mr. ' + name

def calc_add(num_a: int, num_b: int) -> int:
    return num_a + num_b;    

if __name__ == '__main__':
    name_title = add_honor("Yamaguchi", True)
    print(calc_add(1,3.1))
    print(name_title)