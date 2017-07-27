from python_to_json import JSONMixin
import datetime

class TestClass(JSONMixin):
    
    def __init__(self, some_string, some_int, some_float, some_datetime,
                 some_dict, some_list):
        self.some_string = some_string
        self.some_int = some_int
        self.some_float = some_float
        self.some_datetime = some_datetime
        self.some_dict = some_dict
        self.some_list = some_list


class TestChildClass(JSONMixin):

    def __init__(self, value):
        self.value = value


test_datetime = datetime.datetime.now()
test_child_obj = TestChildClass('test')
test_second_child_obj = TestChildClass('test2')
test_dict = {'first': test_child_obj, 'second': test_second_child_obj}
test_list = [test_child_obj, test_second_child_obj]

test_object = TestClass('string', 1, 2.345, test_datetime, test_dict, test_list)
print(test_object.as_dict_for_json())
print(type(test_object.as_dict_for_json()))
print(test_object.as_json())
print(type(test_object.as_json()))



