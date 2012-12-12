.. image:: https://secure.travis-ci.org/yourlabs/django-cities-light.png?branch=master

django-cities-light-with-population -- *django-cities-light alternative to include population*
=========================================================

This add-on provides models and commands to import country, region/state, and
city data in your database.

The data is pulled from `GeoNames
<http://www.geonames.org/>`_ and contains population cities, regions/states and countries.
** Not all data will work **

Spatial query support is not required by this application.

This application is very simple and is useful if you want to make a simple
address book for example. If you intend to build a fully featured spatial
database, you should use
`django-cities
<https://github.com/coderholic/django-cities>`_.

Unless you absolutely must need population, use django-cities-light instead

Upgrade
-------

See CHANGELOG.

Installation
------------

see django-cities-light

Data update
-----------

Finally, populate your database with command::

    ./manage.py cities_light

This command is well documented, consult the help with::

    ./manage.py help cities_light

Resources
---------

You could subscribe to the mailing list ask questions or just be informed of
package updates.

- `Mailing list graciously hosted
  <http://groups.google.com/group/yourlabs>`_ by `Google
  <http://groups.google.com>`_
- `Git graciously hosted
  <https://github.com/yourlabs/django-cities-light/>`_ by `GitHub
  <http://github.com>`_,
- `Documentation graciously hosted
  <http://django-cities-light.rtfd.org>`_ by `RTFD
  <http://rtfd.org>`_,
- `Package graciously hosted
  <http://pypi.python.org/pypi/django-cities-light/>`_ by `PyPi
  <http://pypi.python.org/pypi>`_,
- `Continuous integration graciously hosted
  <http://travis-ci.org/yourlabs/django-cities-light>`_ by `Travis-ci
  <http://travis-ci.org>`_
