import pytest
import datetime

from dateutil.tz import tzoffset
from python_to_json.mixins import JSONMixin

class TestJSONMixin:

    ZULU = tzoffset('ZULU', 0)

    class Foo(JSONMixin, object):

        def __init__(self, bar):
            self.bar = bar

    def test_with_none(self):
        obj = self.Foo(None)
        result = obj.__jsondict__()
        assert result == {}

    def test_with_empty(self):
        obj = self.Foo([])
        result = obj.__jsondict__()
        assert result == {}

    def test_with_none_with_hide_none_false(self):
        obj = self.Foo(None)
        result = obj.__jsondict__(hide_none=False)
        assert result == {'bar': None}

    def test_with_empty_with_hide_none_false(self):
        obj = self.Foo([])
        result = obj.__jsondict__(hide_none=False)
        assert result == {}

    def test_with_none_with_hide_empty_false(self):
        obj = self.Foo(None)
        result = obj.__jsondict__(hide_empty=False)
        assert result == {}

    def test_with_empty_with_hide_empty_false(self):
        obj = self.Foo([])
        result = obj.__jsondict__(hide_empty=False)
        assert result == {'bar': []}

    def test_normal_object(self):
        obj = self.Foo('hello world!')
        result = obj.__jsondict__()
        assert result == {'bar': 'hello world!'}

    def test_datetime(self):
        date = datetime.datetime(2017, 1, 25, 12, 39, 40, tzinfo=self.ZULU)
        obj = self.Foo(date)
        result = obj.__jsondict__()
        assert result == {'bar': '2017-01-25T12:39:40+00:00'}

    def test_date(self):
        obj = self.Foo(datetime.date(2017, 1, 25))
        result = obj.__jsondict__()
        assert result == {'bar': '2017-01-25'}

    def test_sub_json(self):
        subobj = self.Foo('hello world!')
        obj = self.Foo(subobj)
        result = obj.__jsondict__()
        assert result == {'bar': {'bar': 'hello world!'}}

    def test_list_of_normals(self):
        obj = self.Foo(['hello', 'world!'])
        result = obj.__jsondict__()
        assert result == {'bar': ['hello', 'world!']}

    def test_dict_of_normals(self):
        obj = self.Foo({'first': 'hello', 'second': 'world!'})
        result = obj.__jsondict__()
        assert result == {'bar': {'first': 'hello', 'second': 'world!'}}

    def test_list_of_subobjs(self):
        obj = self.Foo([self.Foo('hello'), self.Foo('world!')])
        result = obj.__jsondict__()
        assert result == {'bar': [{'bar': 'hello'}, {'bar': 'world!'}]}

    def test_dict_of_subobjs(self):
        obj = self.Foo({
            'first': self.Foo('hello'),
            'second': self.Foo('world!')
        })
        result = obj.__jsondict__()
        assert result == {
            'bar': {
                'first': {'bar': 'hello'},
                'second': {'bar': 'world!'}
            }
        }

    def test_as_json(self):
        obj = self.Foo('hello world!')
        result = obj.as_json()
        assert result == '{"bar": "hello world!"}'

    def test_as_dict_for_json(self):
        obj = self.Foo('hello world!')
        result = obj.as_dict_for_json()
        assert result == {'bar': 'hello world!'}
