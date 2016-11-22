from collections import OrderedDict

ENCODERS = OrderedDict()

try:
    import msgpack

    ENCODERS['msgpack'] = msgpack

except ImportError:
    pass

try:
    import json

    ENCODERS['json'] = json

except ImportError:
    pass
