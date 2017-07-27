# python-to-json
Converts Python objects into JSON serializable dictionaries.

# Example
```python

from python_to_json.mixins import JSONMixin


# Your Python class
class TestClass(JSONMixin):
    
    def __init__(self, some_string, some_int, some_float, some_datetime,
                 some_dict, some_list):
        self.some_string = some_string
        self.some_int = some_int
        self.some_float = some_float
        self.some_datetime = some_datetime
        self.some_dict = some_dict
        self.some_list = some_list


# Works on nested classes
class TestChildClass(JSONMixin):

    def __init__(self, value):
        self.value = value


# Create some test data
test_datetime = datetime.datetime.now()
test_child_obj = TestChildClass('test')
test_second_child_obj = TestChildClass('test2')
test_dict = {'first': test_child_obj, 'second': test_second_child_obj}
test_list = [test_child_obj, test_second_child_obj]
test_object = TestClass('string', 1, 2.345, test_datetime, test_dict, test_list)

print(test_object.as_dict_for_json())
>> {'some_list': [{'value': 'test'}, {'value': 'test2'}], 'some_float': 2.345, 'some_datetime': '2017-07-27T09:33:30.933271', 'some_int': 1, 'some_string': 'string', 'some_dict': {'second': {'value': 'test2'}, 'first': {'value': 'test'}}}

print(type(test_object.as_dict_for_json()))
<type 'dict'>

print(test_object.as_json())
{"some_list": [{"value": "test"}, {"value": "test2"}], "some_float": 2.345, "some_datetime": "2017-07-27T09:33:30.933271", "some_int": 1, "some_string": "string", "some_dict": {"second": {"value": "test2"}, "first": {"value": "test"}}}

print(type(test_object.as_json()))
<type 'str'>

# Allows you to hide empty and None fields:
test_object.some_list = []
test_object.some_dict = {}
test_object.some_datetime = None
test_object.some_int = None
test_object.some_float = None
print(test_object.as_json(hide_empty=True, hide_none=True))
>> {"some_string": "string"}

```
