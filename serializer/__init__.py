
__author__ = 'Hamilakis Nicolas'
__copyright__ = 'Hamilakis Nicolas 2020'
__license__ = 'MIT'
__url__ = ''
__maintainer__ = 'Hamilakis Nicolas'
__email__ = 'nick.hamilakis562@gmail.com'
__status__ = "production"
__description__ = "Package for serializing python object & dataclasses"

from ._core import _Serializable as SerializableMixin
from ._core import serializable
from ._serializer import serializer
from pathlib import Path

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
"""
