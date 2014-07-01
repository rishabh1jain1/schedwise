SchedWise
=========

A Wise Scheduler for Intelligent Resource Placements in Openstack Clouds. 
It provides an interactive scheduler UI dashboard and a backend Scheduler-as-a-Service implementation. 


SchedWise Service
-----------------

This provides a RESTful backend service with APIs to support the frontend Scheduler UI. 
This service wraps a stand-alone intelligent placement decision engine that is capable of deciding the optimal 
compute placements for a given request. 

To run this service:

$> python main.py

This will launch the service on localhost at port 5000 by default.  This implementation currently
includes a prototype hosts resource cache for demo purposes. But the host resources will be made
available to this service by connecting to an Openstack deployment through API calls.  

Requirements
------------

Please ensure you have the necessary third party library installed. Easiest way is to install the 
Openstack Nova projects [requirements](https://github.com/openstack/nova/blob/master/requirements.txt)
and a few additional libraries such as flask and coinor.pulp>=1.0.4.
This should satisfy all the requirements of this project. 


Supported APIs
--------------

1. POST schedwise/v1.0/placement  - return placement decision with VM to Host Mappings, 
   Accepts: JSON of VM request with the request properties that includes constraints. 

Example API call using curl that can be used with the current implementation, that includes a prototype demoable hosts resource cache:

curl -i -H "Content-Type: application/json" -X POST -d '{"instance_requests": [{"num_instances": 10, "request_properties": {"instance_type": {"root_gb": 1}}}, {"num_nstances": 2, "request_properties": {"flavor": "m1.tiny"}}]}' http://localhost:5000/schedwise/v1.0/placement

2. GET schedwise/v1.0/resource – return set of resources with capacities

Example API call using curl that can be used with the current implementation:

curl -i -H "Content-Type: application/json" -X GET http://localhost:5000/schedwise/v1.0/resource


Additional APIs are in the pipeline. 



