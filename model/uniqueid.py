# Embedded file name: c:\Jenkins\live\output\win_64_static\Release\midi-remote-scripts\Push2\model\uniqueid.py
from itertools import count

class UniqueIdMixin(object):
    _idgen = count()

    def __init__(self, *a, **k):
        super(UniqueIdMixin, self).__init__(*a, **k)
        self.__id__ = self._idgen.next()