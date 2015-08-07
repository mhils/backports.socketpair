backports.socketpair
====================

This package provides Windows support for ``socket.socketpair()``
for Python 2 (and 3) using the pure-python method implemented in Python 3.5+.

Usage:

.. code:: python

	import socket
	import backports.socketpair

	s1, s2 = socket.socketpair()