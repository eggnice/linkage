# -*- coding: utf-8 -*-
"""
__mktime__ = '2018/6/6'
__author__ = 'Administrator'
__filename__ = 'baseGlanceApi'
"""
from linkage.openstack.baseOpenstackApi import openstackapi

class glanceapi(openstackapi):

    def __init__(self):
        pass

    def images_showImage(self, image_id, **kwargs):
        """ Shows details for an image """
        api = "/v2/images/%s" % image_id
        params = kwargs
        return self.connGlance('GET', api, params=params)

    def images_listImages(self, **kwargs):
        """ Lists public virtual machine (VM) images """
        api = "/v2/images"
        params = kwargs
        return self.connGlance('GET', api, params=params)

    def images_showImageMemberDetails(self, image_id, member_id, **kwargs):
        """ Shows image member details """
        api = "/v2/images/%s/members/%s" % (image_id, member_id)
        params = kwargs
        return self.connGlance('GET', api, params=params)

    def images_listImageMembers(self, image_id, **kwargs):
        """ Lists the tenants that share this image """
        api = "/v2/images/%s/members" % image_id
        params = kwargs
        return self.connGlance('GET', api, params=params)

    def schemas_showImagesSchema(self, **kwargs):
        api = "/v2/schemas/images"
        params = kwargs
        return self.connGlance('GET', api, params=params)

    def schemas_showImageSchema(self, **kwargs):
        api = "/v2/schemas/image"
        params = kwargs
        return self.connGlance('GET', api, params=params)

    def schemas_showImageMembersSchema(self, **kwargs):
        api = "/v2/schemas/members"
        params = kwargs
        return self.connGlance('GET', api, params=params)

    def schemas_showImageMemberSchema(self, **kwargs):
        api = "/v2/schemas/member"
        params = kwargs
        return self.connGlance('GET', api, params=params)

    def images_downloadBinaryImageData(self, image_id, **kwargs):
        api = "/v2/images/%s/file" % image_id
        params = kwargs
        return self.connGlance('GET', api, params=params)

    def images_importMethodsAndValuesDiscovery(self, **kwargs):
        api = "/v2/info/import"
        params = kwargs
        return self.connGlance('GET', api, params=params)

    def tasks_lisTasks(self, **kwargs):
        api = "/v2/tasks"
        params = kwargs
        return self.connGlance('GET', api, params=params)

    def tasks_showTaskDetails(self, task_id, **kwargs):
        api = "/v2/tasks/"
        params = kwargs
        return self.connGlance('GET', api, params=params)

    def schemas_showTasksSchema(self, **kwargs):
        api = "/v2/schemas/tasks"
        params = kwargs
        return self.connGlance('GET', api, params=params)

    def schemas_showTaskSchema(self, **kwargs):
        api = "/v2/schemas/task"
        params = kwargs
        return self.connGlance('GET', api, params=params)

    def namespaces_listNamespaces(self, **kwargs):
        """ Lists available namespaces """
        api = "/v2/metadefs/namespaces"
        params = kwargs
        return self.connGlance('GET', api, params=params)

    def namespaces_getNamespaceDetails(self, namespace_name, **kwargs):
        """ Gets details for a namespace """
        api = "/v2/metadefs/namespaces/%s" % namespace_name
        params = kwargs
        return self.connGlance('GET', api, params=params)

    def metadefs_listResourceTypes(self, **kwargs):
        """ Lists all available resource types """
        api = "/v2/metadefs/resource_types"
        params = kwargs
        return self.connGlance('GET', api, params=params)

    def metadefs_listResourceTypeAssociations(self, namespace_name, **kwargs):
        """ Lists resource type associations in a namespace """
        api = "/v2/metadefs/namespaces/%s/resource_types" % namespace_name
        params = kwargs
        return self.connGlance('GET', api, params=params)

    def metadefs_listObjects(self, namespace_name, **kwargs):
        """ Lists object definitions in a namespace """
        api = "/v2/metadefs/namespaces/%s/objects" % namespace_name
        params = kwargs
        return self.connGlance('GET', api, params=params)

    def metadefs_showObjects(self, namespace_name, object_name, **kwargs):
        """ Shows the definition for an object """
        api = "/v2/metadefs/namespaces/%s/objects/%s" % (namespace_name, object_name)
        params = kwargs
        return self.connGlance('GET', api, params=params)

    def metadefs_listProperties(self, namespace_name, **kwargs):
        """ Lists property definitions in a namespace """
        api = "/v2/metadefs/namespaces/%s/properties" % namespace_name
        params = kwargs
        return self.connGlance('GET', api, params=params)

    def metadefs_showPropertyDefinition(self, namespace_name, property_name, **kwargs):
        """ Shows the definition for a property """
        api = "/v2/metadefs/namespaces/%s/properties/%s" % (namespace_name, property_name)
        params = kwargs
        return self.connGlance('GET', api, params=params)

    def metadefs_getTagDefinition(self, namespace_name, tag_name, **kwargs):
        """ Gets a definition for a tag """
        api = "/v2/metadefs/namespaces/%s/tags/%s" % (namespace_name, tag_name)
        params = kwargs
        return self.connGlance('GET', api, params=params)

    def metadefs_listTags(self, namespace_name, **kwargs):
        """ Lists the tag definitions within a namespace """
        api = "/v2/metadefs/namespaces/%s/tags" % namespace_name
        params = kwargs
        return self.connGlance('GET', api, params=params)

    def schemas_showMetadataDefinitionNamespaceSchema(self, **kwargs):
        """ Shows a JSON schema document that represents a metadata definition namespace entity """
        api = "/v2/schemas/metadefs/namespace"
        params = kwargs
        return self.connGlance('GET', api, params=params)

    def schemas_showMetadataDefinitionNamespacesSchema(self, **kwargs):
        """ Shows a JSON schema document that represents a metadata definition namespace entity """
        api = "/v2/schemas/metadefs/namespaces"
        params = kwargs
        return self.connGlance('GET', api, params=params)

    def schemas_showmetadataDefinitionNamespaceResourceTypeAssociationSchema(self, **kwargs):
        """ 
        Shows a JSON schema document that represents a metadata definition namespace resource type association entity 
        """
        api = "/v2/schemas/metadefs/resource_type"
        params = kwargs
        return self.connGlance('GET', api, params=params)

    def schemas_showMetadataDefinitionNamespaceResourceTypeAssociationsSchema(self, **kwargs):
        api = "/v2/schemas/metadefs/resource_types"
        params = kwargs
        return self.connGlance('GET', api, params=params)

    def schemas_showMetadataDefinitionObjectSchema(self, **kwargs):
        api = "/v2/schemas/metadefs/object"
        params = kwargs
        return self.connGlance('GET', api, params=params)

    def schemas_showMetadataDefinitionObjectsSchema(self, **kwargs):
        api = "/v2/schemas/metadefs/objects"
        params = kwargs
        return self.connGlance('GET', api, params=params)

    def schemas_showMetadataDefinitionPropertySchema(self, **kwargs):
        api = "/v2/schemas/metadefs/property"
        params = kwargs
        return self.connGlance('GET', api, params=params)

    def schemas_showMetadataDefinitionPropertiesSchema(self, **kwargs):
        api = "/v2/schemas/metadefs/properties"
        params = kwargs
        return self.connGlance('GET', api, params=params)

    def schemas_showMetadataDefinitionTagSchema(self, **kwargs):
        api = "/v2/schemas/metadefs/tag"
        params = kwargs
        return self.connGlance('GET', api, params=params)

    def schemas_showMetadataDefinitionTagsSchema(self, **kwargs):
        api = "/v2/schemas/metadefs/tags"
        params = kwargs
        return self.connGlance('GET', api, params=params)









