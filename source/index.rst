.. Launch & Provision API documentation master file, created by
   sphinx-quickstart on Mon Oct 29 10:51:24 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Launch & Provision Internal API 
===============================

REST API to launch and provision instances on EC2.  This is an internal-only API designed to be used by other infrastructure components to manage the infrastructure.  There is a separate external API for user interaction.  This functionality is designed as an API for scalability and to enable components written in multiple languages to have a single interface for infrastructure commands.  

Contents:

.. toctree::
   :maxdepth: 2


Instance Actions
==================

Launch Instance
----------------
.. py:function:: PUT /v1/launch

Launches an instance of the specified AMI and instance type

:param ami: (required) [string]
:param instance_type: (required) [string]
:param min_count: (default = 1) [int]
:param max_count: (default = 1) [int]
:param key_name: (default = scalacity_dev1) [string]
:param security_groups: (default=SSH) [list of strings]
:param user_data: (default = none) [string]
:param placement: (default = us-east-1b) [string]
:param placement_group: (default = none) [string]
:param instance_initiated_shutdown_behavior: (default = 'terminate') [string]
:param ebs_optimized: (default = False)
:rtype: ======  ================================
        Status  Body
        ======  ================================
        200     List of instance IDs
        400     Required arguments not provided
        408     Error while running via EC2 API
        ======  ================================


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

