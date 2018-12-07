# *_* coding: utf-8 *_*
# __author__: eggnice

"""nova apis to request nova server if http's code 200 (return: if json else text) else raise"""

from linkage.openstack.baseOpenstackApi import openstackapi

class novaapi(openstackapi):
    """nova api"""
    def __init__(self, tenant_id):
        self.tenant_id = tenant_id

    def api_showVersionDetails(self, api_version, **kwargs):
        """ This gets the details of a specific API at its root """
        api = "/%s/" % api_version
        params = kwargs
        return self.connNova('GET', api, params=params)

    def servers_listServers(self, **kwargs):
        """  Lists IDs, names, and links for all servers """
        api = "/v2/%s/servers" % self.tenant_id
        params = kwargs
        return self.connNova('GET', api, params=params)

    def servers_listServersDetailed(self, **kwargs):
        """
        For each server, shows server details including configuration drive
        extended status, and server usage information
        """
        api = "/v2/%s/servers/detail" % self.tenant_id
        params = kwargs
        return self.connNova('GET', api, params=params)

    def servers_showServerDetails(self, server_id, **kwargs):
        """
        Shows details for a server
        Includes server details including configuration drive, extended status, and server usage information
        """
        api = "/v2/%s/servers/%s" % (self.tenant_id, server_id)
        params = kwargs
        return self.connNova('GET', api, params=params)

    def servers_listSecurityGroups(self, server_id, **kwargs):
        """ Lists security groups for a server """
        api = "/v2/%s/servers/%s/os-security-groups" % (self.tenant_id, server_id)
        params = kwargs
        return self.connNova('GET', api, params=params)

    def servers_showDiagnostics(self, server_id, **kwargs):
        """ Shows basic usage data for a server """
        api = "/v2/%s/servers/%s/diagnostics" % (self.tenant_id, server_id)
        params = kwargs
        return self.connNova('GET', api, params=params)

    def servers_listIps(self, server_id, **kwargs):
        """ Lists IP addresses that are assigned to an instance """
        api = "/v2/%s/servers/%s/ips" % (self.tenant_id, server_id)
        params = kwargs
        return self.connNova('GET', api, params=params)

    def servers_showIpDetails(self, server_id, network_label, **kwargs):
        """ Shows IP addresses details for a network label of a server instance """
        api = "/v2/%s/servers/%s/ips/%s" % (self.tenant_id, server_id, network_label)
        params = kwargs
        return self.connNova('GET', api, params=params)

    def servers_listMetadata(self, server_id, **kwargs):
        """ Lists all metadata for a server """
        api = "/v2/%s/servers/%s/metadata" % (self.tenant_id, server_id)
        params = kwargs
        return self.connNova('GET', api, params=params)

    def servers_showMetadataItemDetails(self, server_id, key, **kwargs):
        """  """
        api = "/v2/%s/servers/%s/metadate/%s" % (self.tenant_id, server_id, key)
        params = kwargs
        return self.connNova('GET',api, params=params)

    def servers_vncAction(self, server_id, **kwargs):
        """post to get a vnc url"""
        api = '/v2/%s/servers/%s/action' %(self.tenant_id, server_id)
        params = kwargs
        json = {"os-getVNCConsole": {"type": "novnc"}}
        return self.connNova('POST', api, params=params, json=json)

    def servers_listActions(self, server_id, **kwargs):
        """ Lists actions for a server """
        api = "/v2/%s/servers/%s/os-instance-actions" % (self.tenant_id, server_id)
        params = kwargs
        return self.connNova('GET', api, params=params)

    def servers_showActionDetails(self, server_id, request_id, **kwargs):
        """ Shows details for a server action """
        api = "/v2/%s/servers/%s/os-instance-actions/%s" % (self.tenant_id, server_id, request_id)
        params = kwargs
        return self.connNova('GET', api, params=params)

    def port_listInterfaces(self, server_id, **kwargs):
        """ Lists port interfaces that are attached to a server """
        api = "/v2/%s/servers/%s/os-interface" % (self.tenant_id, server_id)
        params = kwargs
        return self.connNova('GET', api, params=params)

    def port_showInterfaceDetails(self, server_id, port_id, **kwargs):
        """ Shows details for a port interface that is attached to a server """
        api = "/v2/%s/servers/%s/os-interface/%s" % (self.tenant_id, server_id, port_id)
        params = kwargs
        return self.connNova('GET', api, params=params)

    def servers_showPassword(self, server_id, **kwargs):
        """ Shows the administrative password for a server """
        api = "/v2/%s/servers/%s/os-server-password" % (self.tenant_id, server_id)
        params = kwargs
        return self.connNova('GET', api, params=params)

    def servers_listVolumeAttachments(self, server_id, **kwargs):
        """ List volume attachments for an instance """
        api = "/v2/%s/servers/%s/os-volume_attachments" % (self.tenant_id, server_id)
        params = kwargs
        return self.connNova('GET', api, params=params)

    def servers_showVolumeAttachmentsDetial(self, server_id, volume_id, **kwargs):
        """ Show a detail of a volume attachment """
        api = "/v2/%s/servers/%s/os-volume_attachments/%s" % (self.tenant_id, server_id, volume_id)
        params = kwargs
        return self.connNova('GET', api, params=params)

    def flavors_listFlavors(self, **kwargs):
        """ Lists all flavors accessible to your project """
        api = "/v2/%s/flavors" % self.tenant_id
        params = kwargs
        return self.connNova('GET', api, params=params)

    def flavors_listDetails(self, **kwargs):
        """ Lists flavors with details """
        api = "/v2/%s/flavors/detail" % self.tenant_id
        params = kwargs
        return self.connNova('GET', api, params=params)

    def flavors_showDetails(self, flavor_id, **kwargs):
        """ Shows details for a flavor """
        api = "/v2/%s/flavors/%s" % (self.tenant_id, flavor_id)
        params = kwargs
        return self.connNova('GET', api, params=params)

    def flavors_listAccess(self, flavor_id, **kwargs):
        """ Lists flavor access information """
        api = "/v2/%s/flavors/%s/os-flavor-access" % (self.tenant_id, flavor_id)
        params = kwargs
        return self.connNova('GET', api, params=params)

    def flavors_listExtraSpecs(self, flavor_id, **kwargs):
        """ Lists all extra specs for a flavor, by ID """
        api = "/v2/%s/flavors/%s/os-extra_specs" % (self.tenant_id, flavor_id)
        params = kwargs
        return self.connNova('GET', api, params=params)

    def flavors_showExtraSpec(self, flavor_id, flavor_extra_spec_key, **kwargs):
        """ Shows an extra spec, by key, for a flavor, by ID """
        api = "/v2/%s/flavors/%s/os-extra_specs/%s" % (self.tenant_id, flavor_id, flavor_extra_spec_key)
        params = kwargs
        return self.connNova('GET', api, params=params)

    def keypairs_listKeypairs(self, **kwargs):
        """ Lists keypairs that are associated with the account """
        api = "/v2/%s/os-keypairs" % self.tenant_id
        params = kwargs
        return self.connNova('GET', api, params=params)

    def keypairs_showDetails(self, keypair_name, **kwargs):
        """ Shows details for a keypair that is associated with the account """
        api = "/v2/%s/os-keypairs/%s" % (self.tenant_id, keypair_name)
        params = kwargs
        return self.connNova('GET', api, params=params)

    def limits_showLimits(self, **kwargs):
        """ Shows rate and absolute limits for the project """
        api = "/v2/%s/limits" % self.tenant_id
        params = kwargs
        return self.connNova('GET', api, params=params)

    def angents_listAgentBuilds(self, **kwargs):
        """ Lists agent builds """
        api = "/v2/%s/os-agents" % self.tenant_id
        params = kwargs
        return self.connNova('GET', api, params=params)

    def aggregates_listAggregates(self, **kwargs):
        """ Lists all aggregates. Includes the ID, name, and availability zone for each aggregate """
        api = "/v2/%s/os-aggregates" % self.tenant_id
        params = kwargs
        return self.connNova('GET', api, params=params)

    def aggregates_showDetails(self, aggregate_id, **kwargs):
        """ Shows details for an aggregate. Details include hosts and metadata """
        api = "/v2/%s/os-aggregates/%s" % (self.tenant_id, aggregate_id)
        params = kwargs
        return self.connNova('GET', api, params=params)

    def zones_getAvailabilityZone(self, **kwargs):
        """ Lists and gets detailed availability zone information """
        api = "/v2/%s/os-availability-zone" % self.tenant_id
        params = kwargs
        return self.connNova('GET', api, params=params)

    def zones_getAvailabilityZoneDetail(self, **kwargs):
        """ Gets detailed availability zone information """
        api = "/v2/%s/os-availability-zone/detail" % self.tenant_id
        params = kwargs
        return self.connNova('GET', api, params=params)

    def cells_sistCells(self, **kwargs):
        """ Lists cells """
        api = "/v2/%s/os-cells" % self.tenant_id
        params = kwargs
        return self.connNova('GET', api, params=params)

    def cells_Capacities(self, **kwargs):
        """ Retrieve capacities """
        api = "/v2/%s/os-cells/capacities" % self.tenant_id
        params = kwargs
        return self.connNova('GET', api, params=params)

    def cells_listDetails(self, **kwargs):
        """ Lists cells with details of capabilities """
        api = "/v2/%s/os-cells/detail" % self.tenant_id
        params = kwargs
        return self.connNova('GET', api, params=params)

    def cells_Info(self, **kwargs):
        """ Retrieve info about the current cell """
        api = "/v2/%s/os-cells/info" % self.tenant_id
        params = kwargs
        return self.connNova('GET', api, params=params)

    def cells_showData(self, cell_id, **kwargs):
        """ Shows data for a cell """
        api = "/v2/%s/os-cells/%s" % (self.tenant_id, cell_id)
        params = kwargs
        return self.connNova('GET', api, params=params)

    def cells_showCapacities(self, cell_id, **kwargs):
        """ Shows capacities for a cell """
        api = "/v2/%s/os-cells/%s/capacities" % (self.tenant_id, cell_id)
        params = kwargs
        return self.connNova('GET', api, params=params)

    def consoles_ListsConsoles(self, server_id, **kwargs):
        """ Lists all consoles for a server """
        api = "/v2/%s/servers/%s/consoles" % (self.tenant_id, server_id)
        params = kwargs
        return self.connNova('GET', api, params=params)

    def consoles_showDetails(self, server_id, console_id, **kwargs):
        """ Shows console details for a server """
        api = "/v2/%s/servers/%s/consoles/%s" % (self.tenant_id, server_id, console_id)
        params = kwargs
        return self.connNova('GET', api, params=params)

    def consoles_showConnectionInformation(self, console_token, **kwargs):
        """ Given the console authentication token for a server, shows the related connection information """
        api = "/v2/%s/os-console-auth-tokens/%s" % (self.tenant_id, console_token)
        params = kwargs
        return self.connNova('GET', api, params=params)

    def hypervisors_listHypervisors(self, **kwargs):
        """ Lists hypervisors """
        api = "/v2/%s/os-hypervisors" % self.tenant_id
        params = kwargs
        return self.connNova('GET', api, params=params)

    def hypervisors_listDetails(self, **kwargs):
        """ Lists hypervisors details """
        api = "/v2/%s/os-hypervisors/detail" % self.tenant_id
        params = kwargs
        return self.connNova('GET', api, params=params)

    def hypervisors_showStatistics(self, **kwargs):
        """ Shows summary statistics for all enabled hypervisors over all compute nodes """
        api = "/v2/%s/os-hypervisors/statistics" % self.tenant_id
        params = kwargs
        return self.connNova('GET', api, params=params)

    def hypervisors_showDetails(self, hypervisor_id, **kwargs):
        """ Shows details for a given hypervisor """
        api = "/v2/%s/os-hypervisors/%s" % (self.tenant_id, hypervisor_id)
        params = kwargs
        return self.connNova('GET', api, params=params)

    def hypervisors_showUptime(self, hypervisor_id, **kwargs):
        """ Shows the uptime for a given hypervisor """
        api = "/v2/%s/os-hypervisors/%s/uptime" % (self.tenant_id, hypervisor_id)
        params = kwargs
        return self.connNova('GET', api, params=params)

    def hypervisors_searchHypervisor(self, hypervisor_hostname_pattern, **kwargs):
        """ Search hypervisor by a given hypervisor host name or portion of it """
        api = "/v2/%s/os-hypervisors/%s/search" % (self.tenant_id, hypervisor_hostname_pattern)
        params = kwargs
        return self.connNova('GET', api, params=params)

    def hypervisors_listHypervisorServers(self, hypervisor_hostname_pattern, **kwargs):
        """
        List all servers belong to each hypervisor whose host name is matching a given hypervisor host name or portion of it
        """
        api = "/v2/%s/os-hypervisors/%s/servers" % (self.tenant_id, hypervisor_hostname_pattern)
        params = kwargs
        return self.connNova('GET', api, params=params)

    def servers_listServerUsageAudits(self, **kwargs):
        """
        Lists usage audits for all servers on all compute hosts where usage auditing is configured
        """
        api = "/v2/%s/os-instance_usage_audit_log" % self.tenant_id
        params = kwargs
        return self.connNova('GET', api, params=params)

    def servers_listUsageAudits(self, before_timestamp, **kwargs):
        """ Lists usage audits that occurred before a specified time """
        api = "/v2/%s/os-instance_usage_audit_log/%s" % (self.tenant_id, before_timestamp)
        params = kwargs
        return self.connNova('GET', api, params=params)

    def migrations_listMigrations(self, **kwargs):
        """ Lists migrations """
        api = "/v2/%s/os-migrations" % self.tenant_id
        params = kwargs
        return self.connNova('GET', api, params=params)

    def migrations_listServerMigrations(self, server_id, **kwargs):
        """ Lists in-progress live migrations for a given serve """
        api = "/v2/%s/servers/%s/migrations" % (self.tenant_id, server_id)
        params = kwargs
        return self.connNova('GET', api, params=params)

    def migattions_showDetails(self, server_id, migration_id, **kwargs):
        """ Show details for an in-progress live migration for a given server """
        api = "/v2/%s/servers/%s/migrations/%s" % (self.tenant_id, server_id, migration_id)
        params = kwargs
        return self.connNova('GET', api, params=params)

    def quotas_showQuota(self, tenant_id, **kwargs):
        """ Show the quota for a project or a project and a user """
        api = "/v2/%s/os-quota-sets/%s" % (self.tenant_id, tenant_id)
        params = kwargs
        return self.connNova('GET', api, params=params)

    def quotas_listDefaultQuotas(self, tenant_id, **kwargs):
        """ Lists the default quotas for a project """
        api = "/v2/%s/os-quota-sets/%s/defaults" % (self.tenant_id, tenant_id)
        params = kwargs
        return self.connNova('GET', api, params=params)

    def quotas_showDetail(self, tenant_id, **kwargs):
        """ Show the detail of quota for a project or a project and a user """
        api = "/v2/%s/os-quota-sets/%s/detail" % (self.tenant_id, tenant_id)
        params = kwargs
        return self.connNova('GET', api, params=params)

    def quotas_showClassQuota(self, id, **kwargs):
        """ Show the quota for the Quota Class """
        api = "/v2/%s/os-quota-class-sets/%s" % (self.tenant_id, id)
        params = kwargs
        return self.connNova('GET', api, params=params)

    def groups_listServerGroups(self, **kwargs):
        """ Lists all server groups for the tenant """
        api = "/v2/%s/os-server-groups" % self.tenant_id
        params = kwargs
        return self.connNova('GET', api, params=params)

    def group_showDetails(self, server_group_id, **kwargs):
        """ Shows details for a server group """
        api = "/v2/%s/os-server-groups/%s" % (self.tenant_id, server_group_id)
        params = kwargs
        return self.connNova('GET', api, params=params)

    def tags_listTags(self, server_id, **kwargs):
        """ Lists all tags for a server """
        api = "/v2/%s/server/%s/tags" % (self.tenant_id, server_id)
        params = kwargs
        return self.connNova('GET', api, params=params)

    def tags_CheckExistence(self, server_id, tags, **kwargs):
        """
        Checks tag existence on the server
        If tag exists response with 204 status code will be returned. Otherwise returns 404.
        """
        api = "/v2/%s/server/%s/tags/%s" % (self.tenant_id, server_id, tags)
        params = kwargs
        return self.connNova('GET', api, params=params)

    def services_listServices(self, **kwargs):
        """ Lists all running Compute services """
        api = "/v2/%s/os-services" % self.tenant_id
        params = kwargs
        return self.connNova('GET', api, params=params)

    def usage_ListTenantUsageStatistics(self, **kwargs):
        """ Lists usage statistics for all tenants """
        api = "/v2/%s/os-simple-tenant-usage" % self.tenant_id
        params = kwargs
        return self.connNova('GET', api, params=params)

    def usage_ShowUsageStatistics(self, tenant_id, **kwargs):
        """ Shows usage statistics for a tenant """
        api = "/v2/%s/os-simple-tenant-usage/%s" % (self.tenant_id, tenant_id)
        params = kwargs
        return self.connNova('GET', api, params=params)

    def novaVncShow(self, vm_id, **kwargs):
        """ nova_vnc_show """
        api = '/v2/%s/servers/%s/action' % (self.tenant_id, vm_id)
        params = kwargs
        return self.connNova('POST', api, headers={'Content-Type': 'application/json',
                                                   'X-Auth-Token': self.token_id},
                             json={'os-getVNCConsole': {'type': 'novnc'}}, **kwargs)

    def novaImage(self, image_id=None, vm_id=None, **kwargs):
        """nova_image,nova_image_list_grep_server"""
        if image_id:
            api = "/v2/%s/images/%s" % (self.tenant_id, image_id)
        elif vm_id:
            api = '/v2/%s/images/detail?server=%s' % (self.tenant_id, vm_id)
        params = kwargs
        return self.connNova('GET', api, params=params)

    def novaList(self, private_ip=None, user_id=None, vm_name=None, mgmt_id=None, vm_id=None, **kwargs):
        """ novaListDetailGrepPrivateIpGrepUserId,nova_list_detail_grep_name,nova_show,nova_interface_list """
        params = kwargs
        if private_ip and user_id:
            api = "/v2/%s/servers/detail?all_tenants=1&user_id=%s&ip=%s" % (self.tenant_id, user_id, private_ip)
        elif vm_name:
            api = "/v2/%s/servers/detail?all_tenants=1&name=%s" % (self.tenant_id, vm_name)
        elif mgmt_id:
            api = "/v2/%s/servers/%s" % (self.tenant_id, mgmt_id)
        elif vm_id:
            api = '/v2/%s/servers/%s/os-interface' % (self.tenant_id, vm_id)
        return self.connNova('GET', api, params=params)
