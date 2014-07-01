# Copyright (c) 2014 Cisco Systems, Inc.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from flask import Flask, request, abort, make_response
from flask import jsonify, session, render_template
from app.service import SchedulerService
import json

app = Flask(__name__)
service = SchedulerService()

@app.route('/schedwise/v1.0/placement', methods = ['POST'])
def get_placement():
    instance_requests = request.json['instance_requests']
    results = []
    for rnum, instance_request in enumerate(instance_requests):
        instance_uuids = instance_request.get('instance_uuids', None)
        if not instance_uuids: 
            num_instances = instance_request['num_instances']
            instance_uuids = ['VM_ID_' + str(rnum) + '_' + str(i)
                              for i in xrange(num_instances)]
        request_properties = instance_request['request_properties']
        results.append(service.get_placement(instance_uuids, request_properties))    
    return jsonify( { 'result': results } ), 200

@app.route('/schedwise/v1.0/resource', methods = ['GET'])
def get_resources():
    resources = service.get_resources()
    return jsonify({'resources': resources}), 200



