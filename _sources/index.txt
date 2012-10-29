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
**PUT /v1/launch**

Launches an instance of the specified AMI and instance type

====================================    ===============     ===============
Parameter                               Default             Type
====================================    ===============     ===============
ami                                     required          	string
instance_type                           required          	string
min_count                               1                   int
max_count                               1                   int
key_name                                scalacity_dev1      string
security_groups                         SSH                 list of strings
user_data                                                   string
placement                               us-east-1b          string
placement_group                                             string
instance_initiated_shutdown_behavior    terminate           string
ebs_optimized                           False               bool
====================================    ===============     ===============

Returns:

======  ================================
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

