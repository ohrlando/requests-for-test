from functools import partial
import types


class UnexpectedReturn(Exception):
    pass


class RequestTest:
    def __init__(self):
        self.dict_returns = {
            "file": "f708a97sd9"
        }

    @staticmethod
    def set_post(expected_value=None, return_func=types.FunctionType):
        expected = expected_value or return_func or None

        return partial(RequestTest().post, expected)

    def post(self, expected, *args, **kwargs):
        try:
            return expected if isinstance(expected, types.FunctionType) \
                else (self.dict_returns[expected] if expected in self.dict_returns else expected)
        except:
            raise UnexpectedReturn()
