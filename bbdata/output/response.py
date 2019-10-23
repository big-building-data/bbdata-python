
class Response:
    '''
    A class, that handles the responses done  by the route. If nothing is specified the normal list of dict can be used.
    '''
    def __init__(self, return_value=None):
        self.raw_out = return_value

    def to_dataframe(self):
        pass

    def to_csv(self):
        pass

    def to_pickle(self):
        pass

    def __repr__(self):
        return "Response()"

    def __str__(self):
        return str(self.raw_out)

    def __iter__(self):
        return ResponseIterator(self.raw_out)

    def __getitem__(self, item):
        return self.raw_out[item]


class ResponseIterator():
    def __init__(self, raw_out):
        #data
        self._raw_out = raw_out
        #start index
        self._index = 0

        print(type(raw_out))

    def __next__(self):
        if self._index < len(self._raw_out):
            result =self._raw_out[self._index]
            self._index += 1
            return result

        raise StopIteration





