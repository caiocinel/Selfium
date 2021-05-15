
"""
Selfium Auth Tools
~~~~~~~~~~~~~~~~~~~
All Auth functions used in Selfium project;
:copyright: (c) 2021 - Caillou and ZeusHay;
:license: MIT, see LICENSE for more details.
"""

import asyncio
loop = asyncio.get_event_loop()

from .token import *
from .client import *
from .run import *

