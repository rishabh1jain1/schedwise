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

"""Ram cost."""

from nova.openstack.common import log as logging
from nova.scheduler.solvers import costs as solvercosts

from oslo.config import cfg

LOG = logging.getLogger(__name__)

ram_weight_multiplier_opt = cfg.FloatOpt(
        'ram_weight_multiplier', 
        default=1.0,
        help='+ve values result in stacking, while -ve spreading')

CONF = cfg.CONF
CONF.register_opt(ram_weight_multiplier_opt, group='solver_scheduler')
SOLVER_CONF = CONF.solver_scheduler

class RamCost(solvercosts.BaseCost):
    """The cost is evaluated by the production of hosts' free memory
    and a pre-defined multiplier.
    """

    def get_cost_matrix(self, hosts, instance_uuids, request_spec,
                        filter_properties):
        """Calculate the cost matrix."""
        num_hosts = len(hosts)
        if instance_uuids:
            num_instances = len(instance_uuids)
        else:
            num_instances = request_spec.get('num_instances', 1)

        costs = [[hosts[i].free_ram_mb * SOLVER_CONF.ram_weight_multiplier
                for j in range(num_instances)] for i in range(num_hosts)]
        #print 'costs', costs
        return costs
