from unittest.mock import patch

from foo.a import A
from foo.b import B

@patch.object(B, '__init__', lambda a, x, y: None)
def test_a_init():
    a = A()
    import pdb
    pdb.set_trace()
    assert type(a.b) is B
