from functools import partial


class Filter:
    """
        Helper filter class. Accepts a list of single-argument
        functions that return True if object in list conforms to some criteria
    """
    def __init__(self, *functions):
        self.functions = functions

    def apply(self, data):
        """ Func applies the filters to the data """
        return [item for item in data if all(i(item) for i in self.functions)]


def make_filter(**keywords):
    """
        Generate filter object for specified keywords
    """
    filter_funcs = []

    def keyword_filter_func(data, key, value):
        return data.get(key) == value

    for key, value in keywords.items():
        func_for_key_value = partial(keyword_filter_func, key=key, value=value)
        filter_funcs.append(func_for_key_value)

    return Filter(*filter_funcs)