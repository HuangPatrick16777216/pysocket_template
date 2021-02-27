#
#  Pysocket Template
#  Template classes for Python socket applications.
#  Copyright Patrick Huang 2021
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

# Similar to pickle but doesn't execute any code.
# Safe to use.

import struct
from typing import Any, List, Tuple

ALLOWED_TYPES = (
    bool,
    int,
    float,
    str,
    bytes,
    Tuple,
    List,
)


def pack_int(i):
    packed = struct.pack("<I", i)
    if len(packed) != 4:
        raise ValueError(f"Integer {i} too large to pack as 32 bits.")
    return packed


def pack_float(i):
    packed = struct.pack("f", i)
    if len(packed) != 4:
        raise ValueError(f"Float {i} too large to pack as 32 bits.")
    return packed


def dumps(obj: Any):
    """
    Saves obj as a byte string.
    :param obj: Any object in ALLOWED_TYPES.
    """
    if isinstance(obj, bool):
        data = b"\x00"
        data += b"\x01" if obj else b"\x00"
        return data

    elif isinstance(obj, int):
        data = b"\x01" + pack_int(obj)
        return data

    elif isinstance(obj, float):
        data = b"\x02" + pack_float(obj)
        return data

    elif isinstance(obj, str):
        data = b"\x03" + pack_int(len(obj))
        data += obj.encode()
        return data

    elif isinstance(obj, bytes):
        data = b"\x04" + pack_int(len(obj))
        data += obj
        return data

    elif isinstance(obj, tuple):
        data = b"\x05"
        data += len(obj)
        for o in obj:
            data += dumps(o)

    elif isinstance(obj, list):
        data = b"\x06"
        data += len(obj)
        for o in obj:
            data += dumps(o)


def loads(data: bytes):
    """
    Loads byte string as an object.
    :param data: String of bytes to load.
    """
