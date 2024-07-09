from typing import Dict, Any, Callable, Iterable

DataType = Iterable[Dict[str, Any]]
ModifierFunc = Callable[[DataType], DataType]


def query(data: DataType, selector: ModifierFunc,
          *filters: ModifierFunc) -> DataType:
    """
    Query data with column selection and filters

    :param data: List of dictionaries with columns and values
    :param selector: result of `select` function call
    :param filters: Any number of results of `field_filter` function calls
    :return: Filtered data
    """
    data = selector(data)
    for filter_func in filters:
        data = filter_func(data)
    return data


def select(*columns: str) -> ModifierFunc:
    """Return function that selects only specific columns from dataset"""

    def selector(data: DataType) -> DataType:
        result = []
        for item in data:
            new_dict = {}
            for col in columns:
                if col in item:
                    new_dict[col] = item[col]
            result.append(new_dict)
        return result

    return selector


def field_filter(column: str, *values: Any) -> ModifierFunc:
    """Return function that filters specific column to be one of `values`"""

    def filters(data: DataType) -> DataType:
        result = []
        for dicte in data:
            if column in dicte and dicte[column] in values:
                result.append(dicte)
        return  result
    return filters


def test_query():
    friends = [
        {'name': 'Sam',
         'gender': 'male',
         'sport': 'Basketball'},
    ]
    value = query(
        friends,
        select(*('name', 'gender', 'sport')),
        field_filter(*('sport', *('Basketball', 'volleyball'))),
        field_filter(*('gender', *('male',))),
    )
    print(value)
    assert [{'gender': 'male',
             'name': 'Sam',
             'sport': 'Basketball'}] == value


if __name__ == "__main__":
    test_query()
