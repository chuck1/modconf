modconf
=======
.. image:: https://travis-ci.org/chuck1/modconf.svg?branch=master
    :target: https://travis-ci.org/chuck1/modconf
.. image:: https://codecov.io/gh/chuck1/modconf/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/chuck1/modconf
.. image:: https://img.shields.io/pypi/v/modconf.svg
   :target: https://pypi.python.org/pypi/modconf
.. image:: https://readthedocs.org/projects/modconf/badge/?version=dev
   :target: http://modconf.readthedocs.io/en/dev/?badge=dev
   :alt: Documentation Status

Pattern for using python modules as configuration files.

Install
-------

::

    pip3 install modconf

Example
-------

::

    from modconf import import_conf

    conf = import_conf('module_name', 'optional module search path')

``conf`` is simply the module loaded using ``__import__``


