from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
import six

from elixir import Entity, ManyToMany, using_options

class B(Entity):
    using_options(resolve_root='tests.db1')

    cs = ManyToMany('.c.C')
    a1s = ManyToMany('a.A1')
