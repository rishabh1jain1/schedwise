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

from oslo.config import cfg

from nova.openstack.common import log as logging
from nova.scheduler.solvers import linearconstraints

CONF = cfg.CONF
max_instances_per_host_opt = cfg.IntOpt(
                                         'max_instances_per_host',
                                          default=1.0,
                                          help='Maximum instances per host')
CONF.register_opt(max_instances_per_host_opt, group='solver_scheduler')
#CONF.import_opt("max_instances_per_host", "nova.scheduler.filters.num_instances_filter")

LOG = logging.getLogger(__name__)


class NumInstancesPerHostConstraint(linearconstraints.BaseLinearConstraint):
    """Constraint that specifies the maximum number of instances that
    each host can launch.
    """

    # The linear constraint should be formed as:
    # coeff_matrix * var_matrix' (operator) (constants)
    # where (operator) is ==, >, >=, <, <=, !=, etc.
    # For convenience, the (constants) is merged into left-hand-side,
    # thus the right-hand-side is 0.

    def __init__(self, variables, hosts, instance_uuids, request_spec,
                filter_properties):
        [self.num_hosts, self.num_instances] = self._get_host_instance_nums(
                                        hosts, instance_uuids, request_spec)

    def _get_host_instance_nums(self, hosts, instance_uuids, request_spec):
        """This method calculates number of hosts and instances."""
        num_hosts = len(hosts)
        if instance_uuids:
            num_instances = len(instance_uuids)
        else:
            num_instances = request_spec.get('num_instances', 1)
        return [num_hosts, num_instances]

    def get_coefficient_vectors(self, variables, hosts, instance_uuids,
                                request_spec, filter_properties):
        """Calculate the coeffivient vectors."""
        # The coefficient for each variable is 1 and constant in
        # each constraint is -(max_instances_per_host)
        supply = [self._get_usable_instance_num(hosts[i])
                  for i in range(self.num_hosts)]
        coefficient_matrix = [[1 for j in range(self.num_instances)] +
                    [-supply[i]] for i in range(self.num_hosts)]
        return coefficient_matrix

    def get_variable_vectors(self, variables, hosts, instance_uuids,
                            request_spec, filter_properties):
        """Reorganize the variables."""
        # The variable_matrix[i,j] denotes the relationship between
        # host[i] and instance[j].
        variable_matrix = []
        variable_matrix = [[variables[i][j] for j in range(
                    self.num_instances)] + [1] for i in range(self.num_hosts)]
        return variable_matrix

    def get_operations(self, variables, hosts, instance_uuids, request_spec,
                        filter_properties):
        """Set operations for each constraint function."""
        # Operations are '<='.
        operations = [(lambda x: x <= 0) for i in range(self.num_hosts)]
        return operations

    def _get_usable_instance_num(self, host_state):
        """This method returns the usable number of instance
           for the given host.
        """
        num_instances = host_state.num_instances
        max_instances_allowed = CONF.max_instances_per_host
        usable_instance_num = max_instances_allowed - num_instance
        return usable_instance_num
