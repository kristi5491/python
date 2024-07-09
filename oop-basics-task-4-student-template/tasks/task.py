class HistoryDict:
    def __init__(self, dictionary):
        self._history = []
        self._dictionary = dictionary

    def set_value(self, key, value):
        self._dictionary[key] = value
        if key in self._history:
            self._history.remove(key)
        self._history.append(key)
        if len(self._history) > 5:
            self._history.pop(0)

    def get_history(self):
        return self._history


d = HistoryDict({"foo": 42})
d.set_value("bar", 43)
print(d.get_history())