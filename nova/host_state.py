# Copyright (c) 2014 Cisco Systems Inc.
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

"""
HostState class definition. 
"""

import collections
import UserDict
import json


class ReadOnlyDict(UserDict.IterableUserDict):
    """A read-only dict."""
    def __init__(self, source=None):
        self.data = {}
        self.update(source)

    def __setitem__(self, key, item):
        raise TypeError()

    def __delitem__(self, key):
        raise TypeError()

    def clear(self):
        raise TypeError()

    def pop(self, key, *args):
        raise TypeError()

    def popitem(self):
        raise TypeError()

    def update(self, source=None):
        if source is None:
            return
        elif isinstance(source, UserDict.UserDict):
            self.data = source.data
        elif isinstance(source, type({})):
            self.data = source
        else:
            raise TypeError()


# Representation of a single metric value from a compute node.
MetricItem = collections.namedtuple(
             'MetricItem', ['value', 'timestamp', 'source'])


class HostState(object):
    """Mutable and immutable information tracked for a host.
    This is an attempt to remove the ad-hoc data structures
    previously used and lock down access.
    """

    def __init__(self, host, node, capabilities=None, service=None):
        self.host = host
        self.nodename = node
        self.update_capabilities(capabilities, service)

        # Mutable available resources.
        # These will change as resources are virtually "consumed".
        self.total_usable_ram_mb = 0
        self.total_usable_disk_gb = 0
        self.disk_mb_used = 0
        self.free_ram_mb = 0
        self.free_disk_mb = 0
        self.vcpus_total = 0
        self.vcpus_used = 0

        # Additional host information from the compute node stats:
        self.vm_states = {}
        self.task_states = {}
        self.num_instances = 0
        self.num_instances_by_project = {}
        self.num_instances_by_os_type = {}
        self.num_io_ops = 0

        # Other information
        self.host_ip = None
        self.hypervisor_type = None
        self.hypervisor_version = None
        self.hypervisor_hostname = None
        self.cpu_info = None
        self.supported_instances = None

        # Resource oversubscription values for the compute host:
        self.limits = {}

        # Generic metrics from compute nodes
        self.metrics = {}

        self.updated = None

    def update_capabilities(self, capabilities=None, service=None):
        # Read-only capability dicts

        if capabilities is None:
            capabilities = {}
        self.capabilities = ReadOnlyDict(capabilities)
        if service is None:
            service = {}
        self.service = ReadOnlyDict(service)
