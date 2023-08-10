from ..core import recursive_iterator

assert [*recursive_iterator([1,[2,(3,)]])] == [1,2,3]
