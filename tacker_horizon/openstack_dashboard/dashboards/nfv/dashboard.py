# Copyright 2015 Brocade Communications System, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.


from django.utils.translation import gettext_lazy as _

import horizon


class Vnfmgroup(horizon.PanelGroup):
    slug = "nfvgroup"
    name = _("VNF Management")
    panels = ('vnfcatalog', 'vnfmanager',)


class Nfvogroup(horizon.PanelGroup):
    slug = "nfvogroup"
    name = _("NFV Orchestration")
    panels = ('vim', 'vnffgcatalog', 'vnffgmanager',
              'nscatalog', 'nsmanager')


class Nfv(horizon.Dashboard):
    name = _("NFV")
    slug = "nfv"
    panels = (Vnfmgroup, Nfvogroup,)  # Add your panels here.
    default_panel = 'vnfcatalog'  # Specify the slug of the dashboard's
    # default panel.


horizon.register(Nfv)
