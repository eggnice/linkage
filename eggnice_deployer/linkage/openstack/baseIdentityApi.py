# *_* coding: utf-8 *_*
# __author__

"""inentity apis to request kenstone server if http code:200 (return: if json else text) else raise"""

from linkage.openstack.baseOpenstackApi import openstackapi


class identityapi(openstackapi):

    def token_showAndValidate(self, **kwargs):
        """ Validates and shows information for a token, including its expiration date and authorization scope """
        api = "/v3/auth/tokens"
        params = kwargs
        return self.connIdentity('GET', api, params=params)

    def token_getServiceCatalog(self, **kwargs):
        """ New in version 3.3 """
        api = "/v3/auth/catalog"
        params = kwargs
        return self.connIdentity('GET', api, params=params)

    def token_getAvailableProjectScopes(self, **kwargs):
        """ New in version 3.3 """
        api = "/v3/auth/projects"
        params = kwargs
        return self.connIdentity('GET', api, params=params)

    def token_getAvailableDomainScopes(self, **kwargs):
        """ New in version 3.3 """
        api = "/v3/auth/domains"
        params = kwargs
        return self.connIdentity('GET', api, params=params)

    def token_getAvailableSystemScopes(self, **kwargs):
        """ New in version 3.3 """
        api = "/v3/auth/system"
        params = kwargs
        return self.connIdentity('GET', api, params=params)

    def credentials_listApplication(self, user_id, **kwargs):
        """ List all application credentials for a user """
        api = "/v3/users/%s/application_credentials" % user_id
        params = kwargs
        return self.connIdentity('GET', api, params=params)

    def credentials_showApplicationDetails(self, user_id, application_credential_id, **kwargs):
        """ Show details of an application credential """
        api = "/v3/users/%s/application_credentials/%s" % (user_id, application_credential_id)
        params = kwargs
        return self.connIdentity('GET', api, params=params)

    def credentials_listCredentials(self, **kwargs):
        """ Lists all credentials """
        api = "/v3/credentials"
        params = kwargs
        return self.connIdentity('GET', api, params=params)

    def credentials_showCredentialsDetails(self, credential_id, **kwargs):
        """ Shows details for a credential """
        api = "/v3/credentials/%s" % credential_id
        params = kwargs
        return self.connIdentity('GET', api, params=params)

    def domains_listDomains(self, **kwargs):
        """ Lists all domains """
        api = "/v3/domains"
        params = kwargs
        return self.connIdentity('GET', api, params=params)

    def domains_showDomainDetails(self, domain_id, **kwargs):
        """ Shows details for a domain """
        api = "/v3/domains/%s" % domain_id
        params = kwargs
        return self.connIdentity('GET', api, params=params)

    def domains_showDefaultConfigurationSettings(self, **kwargs):
        """ The default configuration settings for the options that can be overridden can be retrieved """
        api = "/v3/domains/config/default"
        params = kwargs
        return self.connIdentity('GET', api, params=params)

    def domains_showDefaultConfiguration(self, group, **kwargs):
        """ Reads the default configuration settings for a specific group """
        api = "/v3/domains/config/%s/default" % group
        params = kwargs
        return self.connIdentity('GET', api, params=params)

    def domains_showDefaultOption(self, group, option, **kwargs):
        """ Reads the default configuration setting for an option within a group """
        api = "/v3/domains/config/%s/%s/default" % (group, option)
        params = kwargs
        return self.connIdentity('GET', api, params=params)

    def domains_showGroupOptionConfiguration(self, domain_id, group, option, **kwargs):
        """ Shows details for a domain group option configuration """
        api = "/v3/domains/%s/config/%s/%s" % (domain_id, group, option)
        params = kwargs
        return self.connIdentity('GET', api, params=params)

    def domains_showDomainGroupConfiguration(self, domain_id, group, **kwargs):
        """ Shows details for a domain group configuration """
        api = "/v3/domains/%s/config/%s" % (domain_id, group)
        params = kwargs
        return self.connIdentity('GET', api, params=params)

    def domains_showDomainConfiguration(self, domain_id, **kwargs):
        """ Shows details for a domain configuration """
        api = "/v3/domains/%s/config" % domain_id
        params = kwargs
        return self.connIdentity('GET', api, params=params)

    def groups_listGroups(self, **kwargs):
        """ Lists groups """
        api = "/v3/groups"
        params = kwargs
        return self.connIdentity('GET', api, params=params)

    def groups_showGroupDetails(self, group_id, **kwargs):
        """ Shows details for a group """
        api = "/v3/groups/%s" % group_id
        params = kwargs
        return self.connIdentity('GET', api, params=params)

    def groups_listUsers(self, group_id, **kwargs):
        """ Lists the users that belong to a group """
        api = "/v3/groups/%s/users" % group_id
        params = kwargs
        return self.connIdentity('GET', api, params=params)

    def domains_listUserInheritedProjectRoles(self, domain_id, user_id, **kwargs):
        """
        The list only contains those role assignments to the domain
        that were specified as being inherited to projects within that domain
        """
        api = "/v3/OS-INHERIT/domains/%s/users/%s/roles/inherited_to_projects" % (domain_id, user_id)
        params = kwargs
        return self.connIdentity('GET', api, params=params)

    def domains_listGroupInheritedProjectRoles(self, domain_id, group_id, **kwargs):
        """
        The list only contains those role assignments to the domain
        that were specified as being inherited to projects within that domain
        """
        api = "/v3/OS-INHERIT/domains/%s/groups/%s/roles/inherited_to_projects"
        params = kwargs
        return self.connIdentity('GET', api, params=params)

    def domains_listRoleAssignments(self, **kwargs):
        """ Get a list of role assignments """
        api = "/v3/role_assignments"
        params = kwargs
        return self.connIdentity('GET', api, params=params)

    def tokens_listRevokedTokens(self, **kwargs):
        """ Lists revoked PKI tokens """
        api = "/v3/auth/tokens/OS-PKI/revoked"
        params = kwargs
        return self.connIdentity('GET', api, params=params)

    def policies_listPolicies(self, **kwargs):
        """ Lists policies """
        api = "/v3/policies"
        params = kwargs
        return self.connIdentity('GET', api, params=params)

    def policies_showPolicyDetails(self, policy_id, **kwargs):
        """ Shows details for a policy """
        api = "/v3/policies/%s" % policy_id
        params = kwargs
        return self.connIdentity('GET', api, params=params)

    def projects_listProjects(self, **kwargs):
        """ Lists projects """
        api = "/v3/projects"
        params = kwargs
        return self.connIdentity('GET', api, params=params)

    def projects_showProjectDetails(self, project_id, **kwargs):
        """ Shows details for a project """
        api = "/v3/projects/%s" % project_id
        params = kwargs
        return self.connIdentity('GET', api, params=params)

    def projects_listTags(self, project_id, **kwargs):
        """ Lists all tags within a project """
        api = "/v3/projects/%s/tags" % project_id
        params = kwargs
        return self.connIdentity('GET', api, params=params)

    def projects_checkIfProjectContainsTag(self, project_id, tag, **kwargs):
        """ Checks if a project contains the specified tag """
        api = "/v3/projects/%s/tags/%s" % (project_id, tag)
        params = kwargs
        return self.connIdentity('GET', api, params=params)

    def regions_showRegionDetails(self, region_id, **kwargs):
        """ Shows details for a region, by ID """
        api = "/v3/regions/%s" % region_id
        params = kwargs
        return self.connIdentity('GET', api, params=params)

    def regions_listRegions(self, **kwargs):
        """ Lists regions """
        api = "/v3/regions"
        params = kwargs
        return self.connIdentity('GET', api, params=params)

    def roles_listRoles(self, **kwargs):
        """ Lists roles """
        api = "/v3/roles"
        params = kwargs
        return self.connIdentity('GET', api, params=params)

    def roles_showRoleDetails(self, role_id, **kwargs):
        """ Shows details for a role """
        api = "/v3/roles/%s"
        params = kwargs
        return self.connIdentity('GET', api, params=params)

    def domains_listRoleAssignmentsForGroup(self, domain_id, group_id, **kwargs):
        """ Lists role assignments for a group on a domain """
        api = "/v3/domains/%s/groups/%s/roles" % (domain_id, group_id)
        params = kwargs
        return self.connIdentity('GET', api, params=params)

    def domains_listRoleAssignmentsForUser(self, domain_id, user_id, **kwargs):
        """ Lists role assignments for a user on a domain """
        api = "/v3/domains/%s/users/%s/roles" % (domain_id, user_id)
        params = kwargs
        return self.connIdentity('GET', api, params=params)

    def porjects_listRoleAssignmentsForGroup(self, project_id, group_id, **kwargs):
        """ Lists role assignments for a group on a project """
        api = "/v3/projects/%s/groups/%s/roles" % (project_id, group_id)
        params = kwargs
        return self.connIdentity('GET', api, params=params)

    def projects_listRoleAssignmentsForUser(self, project_id, user_id, **kwargs):
        """ Lists role assignments for a user on a project """
        api = "/v3/projects/%s/users/%s/roles" % (project_id, user_id)
        params = kwargs
        return self.connIdentity('GET', api, params=params)

    def roles_listImpliedRoles(self, prior_role_id, **kwargs):
        """ Lists implied (inference) roles for a role """
        api = "/v3/roles/%s/implies" % (prior_role_id)
        params = kwargs
        return self.connIdentity('GET', api, params=params)

    def roles_getRoleInferenceRule(self, prior_role_id, implies_role_id, **kwargs):
        """ Gets a role inference rule """
        api = "/v3/roles/%s/implies/%s" % (prior_role_id, identityapi)
        params = kwargs
        return self.connIdentity('GET', api, params=params)

    def roles_listRoleAssignments(self, **kwargs):
        """ Lists role assignments """
        api = "/v3/role_assignments"
        params = kwargs
        return self.connIdentity('GET', api, params=params)

    def roles_listRoleInferenceRules(self, **kwargs):
        """ Lists all role inference rules """
        api = "/v3/role_inferences"
        params = kwargs
        return self.connIdentity('GET', api, params=params)

    def roles_listUserSystemRoleAssignments(self, user_id, **kwargs):
        """ Lists all system role assignment a user has """
        api = "/v3/system/users/%s/roles" % user_id
        params = kwargs
        return self.connIdentity('GET', api, params=params)

    def roles_getUserSystemRoleAssignment(self, user_id, role_id, **kwargs):
        """ Get a specific system role assignment for a user """
        api = "/v3/system/users/%s/roles/%s" % (user_id, role_id)
        params = kwargs
        return self.connIdentity('GET', api, params=params)

    def roles_listGroupSystemRoleAssignments(self, user_id, **kwargs):
        """ Lists all system role assignment a group has """
        api = "/v3/system/groups/%s/roles" % user_id
        params = kwargs
        return self.connIdentity('GET', api, params=params)

    def roles_getGroupSystemRoleAssignment(self, user_id, role_id, **kwargs):
        """ Get a specific system role assignment for a group """
        api = "/v3/system/groups/%s/roles/%s" % (user_id, role_id)
        params = kwargs
        return self.connIdentity('GET', api, params=params)

    def services_listservices(self, **kwargs):
        """ Lists all services """
        api = "/v3/services"
        params = kwargs
        return self.connIdentity('GET', api, params=params)

    def services_showServiceDetails(self, service_id, **kwargs):
        """ Shows details for a service """
        api = "/v3/services/%s" % service_id
        params = kwargs
        return self.connIdentity('GET', api, params=params)

    def endpoints_listEndpoints(self, **kwargs):
        """ Lists all available endpoints """
        api = "/v3/endpoints"
        params = kwargs
        return self.connIdentity('GET', api, params=params)

    def endpoints_showEndpointDetails(self, endpoint_id, **kwargs):
        """ Shows details for an endpoint """
        api = "/v3/endpoints/%s" % endpoint_id
        params = kwargs
        return self.connIdentity('GET', api, params=params)

    def limits_listRegisteredLimits(self, **kwargs):
        """ Lists Registered Limits """
        api = "/v3/registered_limits"
        params = kwargs
        return self.connIdentity('GET', api, params=params)

    def limits_showRegisteredLimitDetails(self, registered_limit_id, **kwargs):
        """ Shows details for a registered limit """
        api = "/v3/registered_limits/%s" % registered_limit_id
        params = kwargs
        return self.connIdentity('GET', api, params=params)

    def limits_listLimits(self, **kwargs):
        """ limits """
        api = "/v3/limits"
        params = kwargs
        return self.connIdentity('GET', api, params=params)

    def limits_showLimitDetails(self, limit_id, **kwargs):
        """ Shows details for a limit """
        api = "/v3/limits/%s" % limit_id
        params = kwargs
        return self.connIdentity('GET', api, params=params)

    def users_listUsers(self, **kwargs):
        """ Lists users """
        api = "/v3/users"
        params = kwargs
        return self.connIdentity('GET', api, params=params)

    def users_showUserDetails(self, user_id, **kwargs):
        """ Shows details for a user """
        api = "/v3/users/%s" % user_id
        params = kwargs
        return self.connIdentity('GET', api, params=params)

    def users_listGroups(self, user_id, **kwargs):
        """ Lists groups to which a user belongs """
        api = "/v3/users/%s/groups" % user_id
        params = kwargs
        return self.connIdentity('GET', api, params=params)

    def users_listProjects(self, user_id, **kwargs):
        """ List projects to which the user has authorization to access """
        api = "/v3/users/%s/projects" % user_id
        params = kwargs
        return self.connIdentity('GET', api, params=params)

