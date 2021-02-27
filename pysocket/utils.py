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
from typing import Any


def dumps(obj: Any):
    """
    Saves obj as a byte string.
    :param obj: Any object in ALLOWED_TYPES.
    """


def loads(data: bytes):
    """
    Loads byte string as an object.
    :param data: String of bytes to load.
    """
