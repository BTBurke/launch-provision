.. Launch & Provision API documentation master file, created by
   sphinx-quickstart on Mon Oct 29 10:51:24 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Launch & Provision Internal API 
===============================

REST API to launch and provision instances on EC2.  This is an internal-only API designed to be used by other infrastructure components to manage the infrastructure.  There is a separate external API for user interaction.  This functionality is designed as an API for scalability and to enable components written in multiple languages to have a single interface for infrastructure commands.  


Instance Actions
==================

Launch Instance
----------------
**PUT /v1/launch**

Launches an instance of the specified AMI and instance type

:Params:
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

:Returns:
    ======  ================================
    Status  Body
    ======  ================================
    200     List of instance IDs
    400     Required arguments not provided
    408     Error while running via EC2 API
    ======  ================================

Start Instance
----------------
**PUT /v1/[instance-id]/start**

Starts an instance

:Returns:
    ======  ================================
    Status  Body
    ======  ================================
    200     Instance modification succeeded
    404     Instance ID not found
    408     Error while modifying via EC2 API
    ======  ================================

Stop Instance
----------------
**PUT /v1/[instance-id]/stop**

Stops an instance

:Params:
    ====================================    ===============     ===============
    Parameter                               Default             Type
    ====================================    ===============     ===============
    force                                   false               bool
    ====================================    ===============     ===============

:Returns:
    ======  ================================
    Status  Body
    ======  ================================
    200     Instance modification succeeded
    404     Instance ID not found
    408     Error while modifying via EC2 API
    ======  ================================

Terminate Instance
--------------------
**PUT /v1/[instance-id]/terminate**

Terminates an instance

:Params:
    ====================================    ===============     ===============
    Parameter                               Default             Type
    ====================================    ===============     ===============
    force                                   false               bool
    ====================================    ===============     ===============

:Returns:
    ======  ================================
    Status  Body
    ======  ================================
    200     Instance modification succeeded
    404     Instance ID not found
    408     Error while modifying via EC2 API
    ======  ================================

Reboot Instance
----------------
**PUT /v1/[instance-id]/reboot**

Reboots an instance

:Returns:
    ======  ================================
    Status  Body
    ======  ================================
    200     Instance modification succeeded
    404     Instance ID not found
    408     Error while modifying via EC2 API
    ======  ================================

Instance Attributes
--------------------
**GET /v1/[instance-id]/attributes**

Gets instance attributes

:Params:
    ====================================    ===============     ===============
    Parameter                               Default             Type
    ====================================    ===============     ===============
    filter                                                      Comma-separated list of fields
    ====================================    ===============     ===============


:Returns:
    =====================================   ================================
    Field                                   Body
    =====================================   ================================
    id                                      Instance ID
    public_dns_name                         Public FQDN
    private_dns_name                        Private FQDN
    state                                   pending, running, shutting-down, terminated, stopping, stopped
    state_code                              0, 16, 32, 48, 64, 80
    key_name                                SSH Keypair Name
    instance_type                           Instance Type (t1.micro, etc.)
    launch_time                             YYYY-MM-DDTHH-MM-SS.000Z
    image_id                                AMI Image ID
    placement                               AWS placement zone
    placement_group                         Placement group
    private_ip_address                      EC2 internal network IP
    ip_address                              Public IP address
    =====================================   ================================

Instance Attributes (single field)
------------------------------------
**GET /v1/[instance-id]/attributes/[field]**

Gets instance attribute (single field)

:Returns:
    Field: Field value


Modify Instance Attribute
--------------------------
**PUT /v1/[instance-id]/modify**

Modifies an instance's attributes

    
:Params:
    ====================================    ===============     ===============
    Parameter                               Default             Type
    ====================================    ===============     ===============
    attribute                               required            string
    value                                   required            string
    ====================================    ===============     ===============

:Returns:
    ======  ================================
    Status  Body
    ======  ================================
    200     Instance modification succeeded
    404     Instance ID not found
    408     Error while modifying via EC2 API
    ======  ================================