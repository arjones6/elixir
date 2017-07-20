from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
import six

from elixir import *

class B(Entity):
    name = Field(String(30))
    many_a = OneToMany('tests.a.A')

