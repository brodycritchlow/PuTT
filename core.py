from typing import Dict, Sequence, Iterator, TypeVar, Any, Tuple

_T = TypeVar("_T", bound=Any)

def recursive_iterator(item: Dict[_T, _T] | Sequence[_T]) -> Iterator[_T | Tuple[_T, _T]]:
    """
    This iterates a sequence or a dictionary for each child and subchild, and yields (key, value) | (value).
    """
    valid_types = [list, tuple, dict]
    itype = type(item)

    if itype == dict:
        for key, value in item:
            if isinstance(value, tuple(valid_types)):
                yield from recursive_iterator(value)
            else:
                yield key, value
    else:
        for value in item:
            if isinstance(value, tuple(valid_types)):
                yield from recursive_iterator(value)
            else:
                yield value

