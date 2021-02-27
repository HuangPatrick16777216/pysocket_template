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
import ctypes
from typing import Callable, List, Tuple
from .pack import loads, dumps


class Client:
    """
    An instance of this is created every time a client connects.
    Meant for communication with that client only.
    Also meant to be used by the Server class only.
    """

    conn: socket.socket
    addr: Tuple
    start_func: Callable

    verbose: bool
    active: bool

    def __init__(self, conn: socket.socket, addr: Tuple, start_func: Callable, verbose: bool):
        """
        Initializes client.
        :param conn: Connection to the client.
        :param addr: Client address.
        :param verbose: Whether to print info to the console.
        """
        self.conn = conn
        self.addr = addr
        self.start_func = start_func

        self.verbose = verbose
        self.active = True

    def start(self):
        """
        Runs start_func and starts.
        """
        self.start_func()

    def quit(self):
        """
        Sets self.active to False
        This can be checked in the start_func.
        """
        self.active = False


class Server:
    """
    Server class.
    Handles client accepting.
    """

    ip: str
    port: int
    client_start: Callable

    verbose: bool
    active: bool
    clients: List[Client]

    server: socket.socket

    def __init__(self, ip: str, port: int, client_start: Callable, verbose: bool = True):
        """
        Initializes server.
        :param ip: IP address to bind to.
        :param port: Port to bind to.
        :param verbose: Whether to print information to the console.
        """
        self.ip = ip
        self.port = port
        self.client_start = client_start

        self.verbose = verbose
        self.active = True
        self.clients = []

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((ip, port))

    def start(self):
        self.server.listen()
        if self.verbose:
            print(f"[SERVER] Started. IP={self.ip}, PORT={self.port}")

        while self.active:
            conn, addr = self.server.accept()
            client = Client(conn, addr, self.client_start, self.verbose)
            self.clients.append(client)
            threading.Thread(target=client.start).start()

    def quit(self, force: bool = False):
        """
        Quits the server and all connected clients.
        :param force: Whether to force quit Python.
        """
        self.active = False
        self.server.close()
        for c in self.clients:
            c.quit()

        if force:
            ctypes.pointer(ctypes.c_char.from_address(5))[0]
