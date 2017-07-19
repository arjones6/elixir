from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
import six

from elixir import Entity, ManyToMany

class A(Entity):
    cs = ManyToMany('..db1.c.C')
