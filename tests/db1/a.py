from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
import six

from elixir import Entity, ManyToOne, OneToMany, ManyToMany, using_options

class A1(Entity):
    using_options(resolve_root='tests.db1')

    a2s = OneToMany('A2')
    bs = ManyToMany('b.B')

class A2(Entity):
    a1 = ManyToOne('A1')

