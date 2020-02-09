__author__ = 'Hamilakis Nicolas'
__copyright__ = 'Hamilakis Nicolas 2020'
__license__ = 'MIT'
__url__ = 'https://github.com/nhamilakis/py-serializer'
__maintainer__ = 'Hamilakis Nicolas'
__email__ = 'nick.hamilakis562@gmail.com'
__status__ = "production"
__description__ = "Package for serializing python object & dataclasses"

#  The MIT License (MIT)
#
#  Copyright (c) 2020 Nicolas Hamilakis
#

from pathlib import Path

from ._core import _Serializable as SerializableMixin  # noqa: F401
from ._core import serializable  # noqa: F401
from ._serializer import serializer  # noqa: F401

__version__ = open(Path(__file__).parents[0] / 'VERSION').read()

__doc__ = f"""
+------======================================-------+
+ Serializer Module  v{__version__} by {__author__}
+ © {__copyright__} under {__license__} licence.
+ Module that allows to mark objects as serializable & 
+ export them into dictionaries. for more info see {__url__}
+------======================================-------+
+ Contact : {__maintainer__} <{__email__}>
+ Status : {__status__}
+------======================================-------+
"""  # noqa: W291
