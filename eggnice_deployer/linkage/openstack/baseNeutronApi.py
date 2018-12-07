# *_* coding: utf-8 *_*
# __author__ : eggnice

"""neutron apis to request neutron server if http code 200 (return: if json else text) else raise"""

from linkage.openstack.baseOpenstackApi import openstackapi

class neutronapi(openstackapi):
    "neutronapis"

    def api_listVersion(self, **kwargs):
        """ Lists information for all Networking API versions """
        api = "/v2.0/"
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def extensions_listExtensions(self, **kwargs):
        """ Lists available extensions """
        api = "/v2.0/extensions"
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def extensions_showDetails(self, alias, **kwargs):
        """
        Shows details for an extension, by alias. The response shows the extension name and its alias
        To show details for an extension, you specify the alias
        """
        api = "/v2.0/extensions/%s" % alias
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def netwrok_showDetails(self, network_id, **kwargs):
        """ Shows details for a network """
        api = "/v2.0/networks/%s" % network_id
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def network_listNetwork(self, **kwargs):
        """ Lists networks to which the project has access """
        api = "/v2.0/networks"
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def port_showDetails(self, port_id,**kwargs):
        """ Shows details for a port """
        api = "/v2.0/ports/%s" % port_id
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def port_listPort(self, **kwargs):
        api = "/v2.0/ports"
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def segments_showDetails(self, segment_id, **kwargs):
        """ Shows details for a segment """
        api = "/v2.0/segments/%s" % segment_id
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def segments_listSegments(self, **kwargs):
        """ Lists segments to which the project has access """
        api = "/v2.0/segments"
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def trunks_listTrunks(self, **kwargs):
        """ Lists trunks that are accessible to the user who submits the request """
        api = "/v2.0/trunks"
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def trunks_listSubports(self, trunk_id, **kwargs):
        """ List subports for trunk """
        api = "/v2.0/trunks/%s/get_subports" % trunk_id
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def trunks_showTrunk(self, trunk_id, **kwargs):
        """ Shows details for a trunk """
        api = "/v2.0/trunks/%s" % trunk_id
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def trunks_showTrunkDetails(self, port_id, **kwargs):
        """
        Shows details for a port
        The details available in the trunk_details attribute contain the trunk ID
        and the array showing information about the subports that belong to the trunk:
        the port UUID, the segmentation type, the segmentation ID, and the MAC address
        """
        api = "/v2.0/ports/%s" % port_id
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def address_showScope(self, address_scope_id, **kwargs):
        """ Shows information for an address scope """
        api = "/v2.0/address-scopes/%s" % address_scope_id
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def address_listScope(self, **kwargs):
        """ Shows information for an address scope """
        api = "/v2.0/address-scopes"
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def floatingips_listIps(self, **kwargs):
        """ Lists floating IPs visible to the user """
        api = "/v2.0/floatingips"
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def floatingips_showDetails(self, floatingip_id, **kwargs):
        """ Shows details for a floating IP """
        api = "/v2.0/floatingips/%s" % floatingip_id
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def routers_listRouters(self, **kwargs):
        """ Lists logical routers that the project who submits the request can access """
        api = "/v2.0/routers"
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def routers_showDetails(self, router_id, **kwargs):
        """ Shows details for a router """
        api = "/v2.0/routers/%s" % router_id
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def subnet_showSubnetPool(self, subnetpool_id, **kwargs):
        """ Shows information for a subnet pool """
        api = "/v2.0/subnetpools/%s" % subnetpool_id
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def subnet_lsitSubnetPool(self, **kwargs):
        """ Lists subnet pools that the project has access to """
        api = "/v2.0/subnetpools"
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def subnets_listSubnet(self, **kwargs):
        """ Lists subnets that the project has access to """
        api = "/v2.0/subnets"
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def subnets_showDetails(self, subnet_id, **kwargs):
        """ Shows details for a subnet """
        api = "/v2.0/subnets/%s" % subnet_id
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def fwaas1_listPolicies(self, **kwargs):
        """ Lists all firewall policies """
        api = "/v2.0/fw/firewall_policies"
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def fwaas1_showPoliciesDetails(self, firewall_policy_id, **kwargs):
        """ Shows details for a firewall policy """
        api = "/v2.0/fw/firewall_policies/%s" % firewall_policy_id
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def fwaas1_listRules(self, **kwargs):
        """ Lists all firewall rules """
        api = "/v2.0/fw/firewall_rules"
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def fwaas1_showRuleDtails(self, firewall_rule_id, **kwargs):
        """ Shows details for a firewall rule """
        api = "/v2.0/fw/firewall_rules/%s" % firewall_rule_id
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def fwaas1_listFirewall(self, **kwargs):
        """ Lists all firewalls """
        api = "/v2.0/fw/firewalls"
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def fwaas1_showDetails(self, firewall_id, **kwargs):
        """ Shows details for a firewall """
        api = "/v2.0/fw/firewalls/%s" % firewall_id
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def fwaas2_listGroups(self, **kwargs):
        """ Lists all firewall groups """
        api = "/v2.0/fwaas/firewall_groups"
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def fwaas2_showGroupDetails(self, firewall_group_id, **kwargs):
        """ Shows details for a firewall group """
        api = "/v2.0/fwaas/firewall_groups/%s" % firewall_group_id
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def fwaas2_listPolicies(self, **kwargs):
        """ Lists all firewall policies """
        api = "/v2.0/fwaas/firewall_policies"
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def fwaas2_showPolicieDetails(self, firewall_policy_id, **kwargs):
        """ Shows details of a firewall policy """
        api = "/v2.0/fwaas/firewall_policies/%s" % firewall_policy_id
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def fwaas2_listRules(self, **kwargs):
        """ Lists all firewall rules """
        api = "/v2.0/fwaas/firewall_rules"
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def fwaas2_showRuleDetails(self, firewall_rule_id, **kwargs):
        """ Shows details for a firewall rule """
        api = "/v2.0/fwaas/firewall_rules/%s" % firewall_rule_id
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def rbac_showPolicieDetails(self, rbac_policy_id, **kwargs):
        """ Show details for a given RBAC policy """
        api = "/v2.0/rbac-policies/%s" % rbac_policy_id
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def rbac_listPolicies(self, **kwargs):
        """ List RBAC policies that belong to a given tenant """
        api = "/v2.0/rbac-policies"
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def security_listGroupRules(self, **kwargs):
        """ Lists a summary of all OpenStack Networking security group rules that the project can access """
        api = "/v2.0/security-group-rules"
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def security_showGroupRule(self, security_group_rule_id, **kwargs):
        """ Shows detailed information for a security group rule """
        api = "/v2.0/security-group-rules/%s" % security_group_rule_id
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def security_listGroups(self, **kwargs):
        """ Lists OpenStack Networking security groups to which the project has access """
        api = "/v2.0/security-groups"
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def security_showGroups(self, security_group_id, **kwargs):
        """ Shows details for a security group """
        api = "/v2.0/security-groups/%s" % security_group_id
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def vpn_listIKEPolicies(self, **kwargs):
        """ Lists IKE policies """
        api = "/v2.0/vpn/ikepolicies"
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def vpn_showIKEPoliceyDetails(self, ikepolicy_id, **kwargs):
        """ Shows details for an IKE policy """
        api = "/v2.0/vpn/ikepolicies/%s" % ikepolicy_id
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def vpn_listIPsecPolicies(self, **kwargs):
        """ Lists all IPsec policies """
        api = "/v2.0/vpn/ipsecpolicies"
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def vpn_showIPsecPolicies(self, ipsecpolicy_id, **kwargs):
        """ Shows details for an IPsec policy """
        api = "/v2.0/vpn/ipsecpolicies/%s" % ipsecpolicy_id
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def vpn_listIPsecConnections(self, **kwargs):
        """ Lists all IPsec connections """
        api = "/v2.0/vpn/ipsec-site-connections"
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def vpn_showIPsecConnection(self, connection_id, **kwargs):
        """ Shows details for an IPsec connection """
        api = "/v2.0/vpn/ipsec-site-connections/%s" % connection_id
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def vpn_listEndpointGroups(self, **kwargs):
        """ Lists VPN endpoint groups """
        api = "/v2.0/vpn/endpoint-groups"
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def vpn_showEndpointGroups(self, endpoint_group_id, **kwargs):
        """ Shows details for a VPN endpoint group """
        api = "/v2.0/vpn/endpoint-groups/%s" % endpoint_group_id
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def vpn_listServices(self, **kwargs):
        """ Lists all VPN services """
        api = "/v2.0/vpn/vpnservices"
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def vpn_showServiceDetails(self, service_id, **kwargs):
        """ Shows details for a VPN service """
        api = "/v2.0/vpn/vpnservices/%s" % service_id
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def flavors_listFlavors(self, **kwargs):
        """ Lists all flavors visible to the project """
        api = "/v2.0/flavors"
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def flavors_showFlavorDetails(self, flavors_id, **kwargs):
        """ Shows details for a flavor """
        api = "/v2.0/flavors/%s" % flavors_id
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def flavors_listServiceProfiles(self, **kwargs):
        """ Lists all service profiles visible for the tenant account """
        api = "/v2.0/service_profiles"
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def flavors_showServieProfileDetails(self, profile_id, **kwargs):
        """ Shows details for a service profile """
        api = "/v2.0/service_profiles/%s" % profile_id
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def metering_listLabels(self, **kwargs):
        """ Lists all L3 metering labels that belong to the project """
        api = "/v2.0/metering/metering-labels"
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def metering_showLabelDetails(self, metering_label_id, **kwargs):
        """ Shows details for a metering label """
        api = "/v2.0/metering/metering-labels/%s" % metering_label_id
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def metering_listLabelRules(self, **kwargs):
        """ Lists a summary of all L3 metering label rules that belong to the project """
        api = "/v2.0/metering/metering-label-rules"
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def metering_showLabelRlueDetails(self, metering_label_rule_id, **kwargs):
        """ Shows details for a metering label rule """
        api = "/v2.0/metering/metering-label-rules/%s" % metering_label_rule_id
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def network_showIPAvailability(self, network_id, **kwargs):
        """ Shows network IP availability details for a network """
        api = "/v2.0/network-ip-availabilities/%s" % network_id
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def network_listIPAvailability(self, **kwargs):
        """ Lists network IP availability of all networks """
        api = "/v2.0/network-ip-availabilities"
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def quotas_liatProjectsQuotas(self, **kwargs):
        """ Lists quotas for projects with non-default quota values """
        api = "/v2.0/quotas"
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def quotas_listProjectQuotas(self, project_id, **kwargs):
        """ Lists quotas for a project """
        api = "/v2.0/quotas/%s" % project_id
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def quotas_listDefaultProjectQuotas(self, project_id, **kwargs):
        """ Lists default quotas for a project """
        api = "/v2.0/quotas/%s/default" % project_id
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def quotas_showQuotasDetails(self, project_id, **kwargs):
        """  Shows quota details for a project """
        api = "/v2.0/quotas/%s/details.json" % project_id
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def services_listServiceProviders(self, **kwargs):
        """ Lists service providers and their associated service types """
        api = "/v2.0/service-providers"
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def tags_ConfirmTag(self, resource_type, tag, resource_id, **kwargs):
        """ Confirms a given tag is set on the resource """
        api = "/v2.0/%s/%s/tags/%s" % (resource_type, resource_id, tag)
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def tags_listObtainTag(self, resource_type, resource_id, **kwargs):
        """ Obtains the tags for a resource """
        api = "/v2.0/%s/%s/tags" % (resource_type, resource_id)
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def qos_listRuletypes(self, **kwargs):
        """ Lists available qos rule types """
        api = "/v2.0/qos/rule-types"
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def qos_showRuleTypeDetails(self, rule_type, **kwargs):
        """ Shows details for an available QoS rule type """
        api = "/v2.0/qos/rule-types/%s" % rule_type
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def qos_listQosPolicies(self, **kwargs):
        """
        Lists all QoS policies associated with your project
        One policy can contain more than one rule type
        """
        api = "/v2.0/qos/policies"
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def qoses_showDosPoliciesDetails(self, policy_id, **kwargs):
        """ Shows details for a QoS policy. One policy can contain more than one rule type """
        api = "/v2.0/qoses/%s" % policy_id
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def bandwidth_listLimitRules(self, policy_id, **kwargs):
        """ Lists all bandwidth limit rules for a QoS policy """
        api = "/v2.0/qos/policies/%s/bandwidth_limit_rules" % policy_id
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def bandwidth_showLimitRuleDetails(self, policy_id, rule_id, **kwargs):
        """ Shows details for a bandwidth limit rule for a QoS policy """
        api = "/v2.0/qos/policies/%s/bandwidth_limit_rules/%s" % (policy_id, rule_id)
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def dscp_listMarkingRules(self, policy_id, **kwargs):
        """ Lists all DSCP marking rules for a QoS policy """
        api = "/v2.0/qos/policies/%s/dscp_marking_rules" % policy_id
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def dscp_showMarkingRuleDetails(self, policy_id, dscp_rule_id, **kwargs):
        """ Shows details for a DSCP marking rule for a QoS policy """
        api = "/v2.0/qos/policies/%s/dscp_marking_rules/%s" % (policy_id, dscp_rule_id)
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def bandwidth_listMinimumRules(self, policy_id, **kwargs):
        """ Lists all minimum bandwidth rules for a QoS policy """
        api = "/v2.0/qos/policies/%s/minimum_bandwidth_rules" % policy_id
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def bandwidth_showMinimumRuleDetails(self, policy_id, rule_id, **kwargs):
        """ Shows details for a minimum bandwidth rule for a QoS policy """
        api = "/v2.0/qos/policies/%s/minimum_bandwidth_rules/%s" % (policy_id, rule_id)
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def balancers_listBalancers(self, **kwargs):
        """ Lists all load balancers for the project """
        api = "/v2.0/lbaas/loadbalancers"
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def balancers_showBalancerDetails(self, loadbalancer_id, **kwargs):
        """ Shows details for a load balancer """
        api = "/v2.0/lbaas/loadbalancers/%s" % loadbalancer_id
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def balancers_showBalancerTree(self, loadbalancer_id, **kwargs):
        """ Shows the status tree for a load balancer """
        api = "/v2.0/lbaas/loadbalancers/%s/statuses" % loadbalancer_id
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def listeners_listListeners(self, **kwargs):
        """Lists all listeners """
        api = "/v2.0/lbaas/listeners"
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def listeners_showListenerDetails(self, listener_id, **kwargs):
        """ Shows details for a listener """
        api = "/v2.0/lbaas/listeners/%s" % listener_id
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def pools_listPools(self, **kwargs):
        """ Lists all pools that are associated with your project """
        api = "/v2.0/lbaas/pools"
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def pools_showPoolDetails(self, pool_id, **kwargs):
        """ Shows details for a pool """
        api = "/v2.0/lbaas/pools/%s" % pool_id
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def pools_listPoolMembers(self, pool_id, **kwargs):
        """ Lists members of a pool """
        api = "/v2.0/lbaas/pools/%s/members" % pool_id
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def pools_showPoolMemberDetails(self, pool_id, member_id, **kwargs):
        """ Shows details for a pool member """
        api = "/v2.0/lbaas/pools/%s/members/%s" % (pool_id,member_id)
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def monitors_listHealthMonitors(self, **kwargs):
        """ Lists health monitors """
        api = "/v2.0/lbaas/healthmonitors"
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def monitors_showHealthMonitorsDetails(self, healthmonitor_id, **kwargs):
        """ Shows details for a health monitor """
        api = "/v2.0/lbaas/healthmonitors/%s" % healthmonitor_id
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def resources_listLogging(self, **kwargs):
        """ Lists logging resources """
        api = "/v2.0/logging/logging_resources"
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def resources_showLoggingDetails(self, logging_resource_id, **kwargs):
        """ Shows details for a logging resource """
        api = "/v2.0/logging/logging_resources/%s" % logging_resource_id
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def firewall_listFirewallLogs(self, logging_resource_id, **kwargs):
        """ Lists firewall logs """
        api = "/v2.0/logging/logging_resources/%s/firewall_logs" % logging_resource_id
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def firewall_showFirewallLogsDetails(self, logging_resource_id, firewall_log_id, **kwargs):
        """ Shows details for a firewall log """
        api = "/v2.0/logging/logging_resources/%s/firewall_logs/%s" % (logging_resource_id, firewall_log_id)
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def vpns_listBGPVPNs(self, **kwargs):
        api = "/v2.0/bgpvpn/bgpvpns"
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def vpns_showBGPVPNDetails(self, bgpvpn_id, **kwargs):
        api = "/v2.0/bgpvpn/bgpvpns/%s" % bgpvpn_id
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def network_listNetworkAssociations(self, bgpvpn_id, **kwargs):
        api = "/v2.0/bgpvpn/bgpvpns/%s/network_associations" % bgpvpn_id
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def network_showNetworkAssociationDetails(self, bgpvpn_id, network_association_id, **kwargs):
        api = "/v2.0/bgpvpn/bgpvpns/%s/network_associations/%s" % (bgpvpn_id, network_association_id)
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def router_listRouterAssociations(self, bgpvpn_id, **kwargs):
        api = "/v2.0/bgpvpn/bgpvpns/%s/router_associations" % bgpvpn_id
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def router_showRouterAssociationDetails(self, bgpvpn_id, router_association_id, **kwargs):
        api = "/v2.0/bgpvpn/bgpvpns/%s/router_associations/%s" % (bgpvpn_id, router_association_id)
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def port_listPortAssociations(self, bgpvpn_id, **kwargs):
        api = "/v2.0/bgpvpn/bgpvpns/%s/port_associations" % bgpvpn_id
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def port_showPortAssociationDetails(self, bgpvpn_id, port_association_id, **kwargs):
        api = "/v2.0/bgpvpn/bgpvpns/%s/port_associations/%s" % (bgpvpn_id, port_association_id)
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def logs_listLogs(self, **kwargs):
        api = "/v2.0/log/logs"
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def logs_showLog(self, log_id, **kwargs):
        api = "/v2.0/log/logs/%s" % log_id
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def resources_listLoggableResources(self, **kwargs):
        api = "/v2.0/log/loggable-resources"
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def agents_listALLAgents(self, **kwargs):
        api = "/v2.0/agents"
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def agents_showAgetnDetails(self, agent_id, **kwargs):
        api = "/v2.0/agents/%s" % agent_id
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def agent_listRoutersHosted(self, agent_id, **kwargs):
        api = "/v2.0/agents/%s/l3-routers" % agent_id
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def agents_listARouterHosting(self, router_id, **kwargs):
        api = "/v2.0/routers/%s/l3-agents" % router_id
        params = kwargs
        return self.connNeutron('GET', api, params=params)

    def topologies_ShowAutoAllocatedTopologyDetails(self, project_id, **kwargs):
        api = "/v2.0/auto-allocated-topology/%s" % project_id
        params = kwargs
        return self.connNeutron('GET', api, params=params)





