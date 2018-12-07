# *_* coding: utf-8 *_*
# __author__: eggnice

"""cinder apis to request cinder server if http code 200 (return: if json else text) else raise"""

from linkage.openstack.baseOpenstackApi import openstackapi

class cinderapi(openstackapi):
    # cinder api
    def __init__(self, tenant_id):
        self.tenant_id = tenant_id

    def api_listVersion(self, **kwargs):
        """ Lists information for all Block Storage API versions """
        api = '/v2/'
        params = kwargs
        return self.connCinder('GET', api, params=params)

    def backup_listDetails(self, **kwargs):
        """ Lists Block Storage backups, with details, to which the project has access """
        api = "/v2/%s/backups/detail" % self.tenant_id
        params = kwargs
        return self.connCinder('GET', api, params=params)

    def backup_showDetails(self, backup_id, **kwargs):
        """ Shows details for a backup """
        api = '/v2/%s/backups/%s' % (self.tenant_id, backup_id)
        params = kwargs
        return self.connCinder('GET', api, params=params)

    def backup_listBackups(self, **kwargs):
        """ Lists Block Storage backups to which the project has access """
        api = '/v2/%s/backups' % self.tenant_id
        params = kwargs
        return self.connCinder('GET', api, params=params)

    def backup_exportBackup(self, backup_id, **kwargs):
        """ Export information about a backup """
        api = "/v2/%s/backups/%s/export_record" % (self.tenant_id, backup_id)
        params = kwargs
        return self.connCinder('GET', api, params=params)

    def capabilities_showCapabilities(self, hostname, **kwargs):
        """
        Shows capabilities for a storage back end on the host
        The hostname takes the form of hostname@volume_backend_name
        """
        api = "/v2/%s/capabilities/%s" % (self.tenant_id, hostname)
        params = kwargs
        return self.connCinder('GET', api, params=params)

    def cgsnapshots_showCGSnapshotsDetails(self, cgsnapshot_id, **kwargs):
        """ Shows details for a consistency group snapshot """
        api = "/v2/%s/cgsnapshots/%s" % (self.tenant_id, cgsnapshot_id)
        params = kwargs
        return self.connCinder('GET', api, params=params)

    def cgsnapshots_listCGSnapshotsDetails(self, **kwargs):
        """ Lists all consistency group snapshots with details """
        api = "/v2/%s/cgsnapshots/detail" % self.tenant_id
        params = kwargs
        return self.connCinder('GET', api, params=params)

    def cgsnapshots_listCGSnapshots(self, **kwargs):
        """ Lists all consistency group snapshots """
        api = "/v2/%s/cgsnapshots" % self.tenant_id
        params = kwargs
        return self.connCinder('GET', api, params=params)

    def cg_listConsistencyGroups(self, **kwargs):
        """ Lists consistency groups """
        api = "/v2/%s/consistencygroups" % self.tenant_id
        params = kwargs
        return self.connCinder('GET', api, params=params)

    def cg_showConsistencyGroupsDetails(self, consistencygroup_id, **kwargs):
        """ Shows details for a consistency group """
        api = "/v2/%s/consistencygroups/%s" % (self.tenant_id, consistencygroup_id)
        params = kwargs
        return self.connCinder('GET', api, params=params)

    def cg_listConsistencyGroupsDetails(self, **kwargs):
        """ Lists consistency groups with details """
        api = "/v2/%s/consistencygroups/detail" % self.tenant_id
        params = kwargs
        return self.connCinder('GET', api, params=params)

    def host_listAllHosts(self, **kwargs):
        """ Lists all hosts summary info that is not disabled """
        api = "/v2/%s/os-hosts" % self.tenant_id
        params = kwargs
        return self.connCinder('GET', api, params=params)

    def host_showHostDetails(self, host_name, **kwargs):
        """ Shows volume and snapshot details for a cinder-volume host """
        api = "/v2/%s/os-hosts/%s" % (self.tenant_id, host_name)
        params = kwargs
        return self.connCinder('GET', api, params=params)

    def limits_showAbsoluteLimits(self, **kwargs):
        """ Shows absolute limits for a project """
        api = "/v2/%s/limits" % self.tenant_id
        params = kwargs
        return self.connCinder('GET', api, params=params)

    def pool_listStoragePools(self, **kwargs):
        """ Lists all back-end storage pools """
        api = "/v2/%s/scheduler-stats/get_pools" % self.tenant_id
        params = kwargs
        return self.connCinder('GET', api, params=params)

    def transfer_listVolumeTransfers(self, **kwargs):
        """ Lists volume transfers """
        api = "/v2/%s/os-volume-transfer" % self.tenant_id
        params = kwargs
        return self.connCinder('GET', api, params=params)

    def transfer_showVolumeTransferDetails(self, transfer_id, **kwargs):
        """ Shows details for a volume transfer """
        api = "/v2/%s/os-volume-transfer/%s" % (self.tenant_id, transfer_id)
        params = kwargs
        return self.connCinder('GET', api, params=params)

    def transfer_listVolumeTransferDetails(self, **kwargs):
        """ Lists volume transfers, with details """
        api = "/v2/%s/os-volume-transfer/detail" % self.tenant_id
        params = kwargs
        return self.connCinder('GET', api, params=params)

    def qos_DisassociateQoSSpecification(self, qos_id, **kwargs):
        """ Disassociates a QoS specification from all associations """
        api = "/v2/%s/qos-specs/%s/disassociate_all" % (self.tenant_id, qos_id)
        params = kwargs
        return self.connCinder('GET', api, params=params)

    def qos_getAllAssociations(self, qos_id, **kwargs):
        """ Lists all associations for a QoS specification """
        api = "/v2/%s/qos-specs/%s/associations" % (self.tenant_id, qos_id)
        params = kwargs
        return self.connCinder('GET', api, params=params)

    def qos_associateSpecification(self, qos_id, **kwargs):
        """ Associates a QoS specification with a volume type """
        api = "/v2/%s/qos-specs/%s/associate" % (self.tenant_id, qos_id)
        params = kwargs
        return self.connCinder('GET', api, params=params)

    def qos_disassociateSpecification(self, qos_id, **kwargs):
        """ Disassociates a QoS specification from a volume type """
        api = "/v2/%s/qos-specs/%s/disassociate" % (self.tenant_id, qos_id)
        params = kwargs
        return self.connCinder('GET', api, params=params)

    def qos_showSpecificationDetails(self, qos_id, **kwargs):
        """ Shows details for a QoS specification """
        api = "/v2/%s/qos-specs/%s" % (self.tenant_id, qos_id)
        params = kwargs
        return self.connCinder('GET', api, params=params)

    def quota_showQuotaClasses(self, quota_class_name, **kwargs):
        """
        Shows quota class set for a project
        If no specific value for the quota class resource exists, then the default value will be reported
        """
        api = "/v2/%s/os-quota-class-sets/%s" % (self.tenant_id, quota_class_name)
        params = kwargs
        return self.connCinder('GET', api, params=params)

    def quota_showQuotas(self, admin_project_id, **kwargs):
        """ Shows quotas for a project """
        api = "/v2/%s/os-quota-sets/%s" % (admin_project_id, self.tenant_id)
        params = kwargs
        return self.connCinder('GET', api, params=params)

    def quota_getDefaultQuotas(self, admin_project_id, **kwargs):
        """ Gets default quotas for a project """
        api = "/v2/%s/os-quota-sets/%s/defaults" % (admin_project_id, self.tenant_id)
        params = kwargs
        return self.connCinder('GET', api, params=params)

    def volumes_listPrivateVolumeType(self, volume_type, **kwargs):
        """ Lists project IDs that have access to private volume type """
        api = "/v2/%s/types/%s/os-volume-type-access" % (self.tenant_id, volume_type)
        params = kwargs
        return self.connCinder('GET', api, params=params)

    def extensions_listApiExtensions(self, **kwargs):
        """ Lists Block Storage API extensions """
        api = "/v2/%s/extensions" % self.tenant_id
        params = kwargs
        return self.connCinder('GET', api, params=params)

    def snapshots_listSnapshotDetails(self, **kwargs):
        """ Lists all Block Storage snapshots, with details, that the project can access """
        api = "/v2/%s/snapshots/detail" % self.tenant_id
        params = kwargs
        return self.connCinder('GET', api, params=params)

    def snapshots_showSnapshotMetadata(self, snapshot_id, **kwargs):
        """ Shows metadata for a snapshot """
        api = "/v2/%s/snapshots/%s/metadata" % (self.tenant_id, snapshot_id)
        params = kwargs
        return self.connCinder('GET', api, params=params)

    def snapshots_showSnapshotDetails(self, snapshot_id, **kwargs):
        """ Shows details for a snapshot """
        api = "/v2/%s/snapshots/%s" % (self.tenant_id, snapshot_id)
        params = kwargs
        return self.connCinder('GET', api, params=params)

    def types_showVolumeTypeDetails(self, volume_type_id, **kwargs):
        """ Shows details for a volume type """
        api = "/v2/%s/types/%s" % (self.tenant_id, volume_type_id)
        params = kwargs
        return self.connCinder('GET', api, params=params)

    def types_listVolumeType(self, **kwargs):
        """ Lists volume types """
        api = "/v2/%s/types" % self.tenant_id
        params = kwargs
        return self.connCinder('GET', api, params=params)

    def types_showEncryptionType(self, volume_type_id, **kwargs):
        """ Show an encryption type """
        api = "/v2/%s/types/%s/encryption" % (self.tenant_id, volume_type_id)
        params = kwargs
        return self.connCinder('GET', api, params=params)

    def types_deleteEncryptionType(self, volume_type_id, encryption_id, **kwargs):
        """ Delete an encryption type """
        api = "/v2/%s/types/%s/encryption/%s" % (self.tenant_id, volume_type_id, encryption_id)
        params = kwargs
        return self.connCinder('GET', api, params=params)

    def volumes_listVolumeDetails(self, **kwargs):
        """ Lists all Block Storage volumes, with details, that the project can access """
        api = "/v2/%s/volumes/detail" % self.tenant_id
        params = kwargs
        return self.connCinder('GET', api, params=params)

    def volumes_listVolumes(self, **kwargs):
        """ Lists summary information for all Block Storage volumes that the project can access """
        api = "/v2/%s/volumes" % self.tenant_id
        params = kwargs
        return self.connCinder('GET', api, params=params)

    def volumes_showVolumeDetails(self, volume_id, **kwargs):
        """ Shows details for a volume """
        api = "/v2/%s/volumes/%s" % (self.tenant_id, volume_id)
        params = kwargs
        return self.connCinder('GET', api, params=params)

    def volumes_showVolumeMetadata(self, volume_id, **kwargs):
        """ Shows metadata for a volume """
        api = "/v2/%s/volumes/%s/metadata" % (self.tenant_id, volume_id)
        params = kwargs
        return self.connCinder('GET', api, params=params)

    def volumes_showVMForKey(self, volume_id, key, **kwargs):
        """ Shows metadata for a volume for a specific key """
        api = "/v2/%s/volumes/%s/metadata/%s" % (self.tenant_id, volume_id, key)
        params = kwargs
        return self.connCinder('GET', api, params=params)

