from copy import deepcopy
from typing import Any, Callable, Set, Dict
import numpy as np


def _fix_to_json(obj: Any):
    if type(obj) in (np.int64, np.longlong):
        return int(obj)
    if type(obj) is np.float64:
        return float(obj)
    if type(obj) is np.bool_:
        return bool(obj)
    return obj


def _traverse_object(obj: Any, func: Callable, ignore: Set[str] = None, is_first: bool = True) -> Any:
    if is_first:
        obj = deepcopy(obj)
    if ignore is None:
        ignore = set()
    if hasattr(obj, '_asdict'):
        obj = obj._asdict()
    if hasattr(obj, 'to_dict'):
        obj = obj.to_dict()
    if hasattr(obj, 'items'):
        for key, val in obj.items():
            if key in ignore:
                obj[key] = None
            else:
                obj[key] = _traverse_object(val, func, ignore, False)
    elif type(obj) in {list, tuple, set, frozenset, np.ndarray}:
        obj = [_traverse_object(val, func, ignore, False) for val in obj]
    else:
        obj = func(obj)
    return obj


def to_jsonable_dict(obj: Any, ignore: Set[str] = None) -> Dict:
    return _traverse_object(obj, _fix_to_json, ignore)
