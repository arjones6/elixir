from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
import six

from elixir import *

class A(Entity):
    name = Field(String(30))
    b = ManyToOne('tests.b.B')
