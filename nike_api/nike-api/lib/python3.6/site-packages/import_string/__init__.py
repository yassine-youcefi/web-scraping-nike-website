# -*- coding: utf-8 -*-
import sys
from .base import import_string

import_string.__author__ = 'Bruno Rocha'
import_string.__email__ = 'rochacbruno@gmail.com'
import_string.__version__ = '0.1.0'

sys.modules[__name__] = import_string
