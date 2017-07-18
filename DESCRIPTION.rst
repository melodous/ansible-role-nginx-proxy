Role Name
=========

Install nginx as container and configure as reverse proxy

Requirements
------------

Docker engine up and running

Dependencies
------------



Example Playbook
----------------

.. code::

  - hosts: servers
    roles:
      - { role: nginx-proxy }
