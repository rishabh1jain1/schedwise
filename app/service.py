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

from oslo.config import cfg

from nova.scheduler.solvers.pluggable_hosts_pulp_solver import HostsPulpSolver
from nova.host_state import HostState

CONF = cfg.CONF
CONF(default_config_files = ['conf/smart_scheduler.conf'])

#TODO implement Hosts caching talking to OpenStack HostManager
#Temporarily using a hosts list for demo purposes
hosts = [{'uuid': 'uuid1', 'free_disk_mb': 10240, 'total_usable_disk_gb': 10,
          'host': 'Host1', 'free_ram_mb': 512, 'nodename': 'Node1'},
         {'uuid': 'uuid2', 'free_disk_mb': 1280, 'total_usable_disk_gb': 2,
          'host': 'Host2', 'free_ram_mb': 256, 'nodename': 'Node2'},
         {'uuid': 'uuid3', 'free_disk_mb': 256, 'total_usable_disk_gb': 1,
          'host': 'Host3', 'free_ram_mb': 256, 'nodename': 'Node3'}]

#TODO - build this dictionary by calling Openstack apis
supported_flavors = {'m1.tiny': {'memory_mb': 512, 'root_gb': 1, 'vcpus': 1}, 
           'm1.small': {'memory_mb': 2048, 'root_gb': 10, 'vcpus': 1},
           'm1.medium': {'memory_mb': 4096, 'root_gb': 10, 'vcpus': 2}}


class SchedulerService(object):
    """Class with Scheduler Service Implementations."""
    
    def __init__(self):
        self.solver = HostsPulpSolver()

    def get_placement(self, instance_uuids, request_properties, request_spec=None):
        requested_flavor = request_properties.get('flavor', None)
        if requested_flavor:
            filter_properties = {'instance_type': supported_flavors.get(requested_flavor, None)}
        else:
            filter_properties = request_properties
        print hosts
        print instance_uuids
        print filter_properties
        host_states = []
        for host in hosts:
            hostname = host.get('host','')
            nodename = host.get('nodename', '')
            total_usable_disk_gb = host.get('total_usable_disk_gb', 0)
            free_disk_mb = host.get('free_disk_mb', 0)
            free_ram_mb = host.get('free_ram_mb', 0)
            host_state = HostState(hostname, nodename)
            host_state.total_usable_disk_gb = total_usable_disk_gb
            host_state.free_disk_mb = free_disk_mb
            host_state.free_ram_mb = free_ram_mb
            print hostname, nodename, total_usable_disk_gb, free_disk_mb, free_ram_mb
            host_states.append(host_state)
        placement_tuples = self.solver.host_solve(hosts=host_states,
                                         instance_uuids=instance_uuids,
                                         request_spec=request_spec,
                                         filter_properties=filter_properties)
        print 'placement_tuples'
        print placement_tuples
        results = []
        for (host, instance_uuid) in placement_tuples:
            result_dict = {'host': {'host': host.host, 'nodename': host.nodename}, 'instance_uuid': instance_uuid}
            results.append(result_dict)
        return results 

    def get_resources(self):
        resources = {'hosts': hosts}
        return resources 
