from typing import Any, Dict, List, Set


def check(lst: List[Dict[Any, Any]]) -> Set[Any]:
    set_value = set()
    for dicte in lst:
        for key, value in dicte.items():
            set_value.add(value)
    return set_value


print(check([{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]))