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

import threading
import socket


class Server:
    """
    Server class.
    Handles client accepting.
    """

    ip: str
    port: int
    verbose: bool
    active: bool
    server: socket.socket

    def __init__(self, ip: str, port: int, verbose: bool = True):
        """
        Initializes server.
        :param ip: IP address to bind to.
        :param port: Port to bind to.
        :param verbose: Whether to print information to the console.
        """
        self.ip = ip
        self.port = port
        self.verbose = verbose
        self.active = True

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((ip, port))

    def start(self):
        self.server.listen()
        if self.verbose:
            print(f"[SERVER] Started. IP={self.ip}, PORT={self.port}")

        while True:
            conn, addr = self.server.accept()
