# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities

class Namespace(pulumi.CustomResource):
    """
    Manages an Azure Relay Namespace.
    """
    def __init__(__self__, __name__, __opts__=None, location=None, name=None, resource_group_name=None, sku=None, tags=None):
        """Create a Namespace resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not location:
            raise TypeError('Missing required property location')
        elif not isinstance(location, basestring):
            raise TypeError('Expected property location to be a basestring')
        __self__.location = location
        """
        Specifies the supported Azure location where the Azure Relay Namespace exists. Changing this forces a new resource to be created.
        """
        __props__['location'] = location

        if name and not isinstance(name, basestring):
            raise TypeError('Expected property name to be a basestring')
        __self__.name = name
        """
        Specifies the name of the Azure Relay Namespace. Changing this forces a new resource to be created.
        """
        __props__['name'] = name

        if not resource_group_name:
            raise TypeError('Missing required property resource_group_name')
        elif not isinstance(resource_group_name, basestring):
            raise TypeError('Expected property resource_group_name to be a basestring')
        __self__.resource_group_name = resource_group_name
        """
        The name of the resource group in which to create the Azure Relay Namespace.
        """
        __props__['resourceGroupName'] = resource_group_name

        if not sku:
            raise TypeError('Missing required property sku')
        elif not isinstance(sku, dict):
            raise TypeError('Expected property sku to be a dict')
        __self__.sku = sku
        """
        A `sku` block as defined below.
        """
        __props__['sku'] = sku

        if tags and not isinstance(tags, dict):
            raise TypeError('Expected property tags to be a dict')
        __self__.tags = tags
        """
        A mapping of tags to assign to the resource.
        """
        __props__['tags'] = tags

        __self__.metric_id = pulumi.runtime.UNKNOWN
        """
        The Identifier for Azure Insights metrics.
        """
        __self__.primary_connection_string = pulumi.runtime.UNKNOWN
        """
        The primary connection string for the authorization rule `RootManageSharedAccessKey`.
        """
        __self__.primary_key = pulumi.runtime.UNKNOWN
        """
        The primary access key for the authorization rule `RootManageSharedAccessKey`.
        """
        __self__.secondary_connection_string = pulumi.runtime.UNKNOWN
        """
        The secondary connection string for the authorization rule `RootManageSharedAccessKey`.
        """
        __self__.secondary_key = pulumi.runtime.UNKNOWN
        """
        The secondary access key for the authorization rule `RootManageSharedAccessKey`.
        """

        super(Namespace, __self__).__init__(
            'azure:relay/namespace:Namespace',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'location' in outs:
            self.location = outs['location']
        if 'metricId' in outs:
            self.metric_id = outs['metricId']
        if 'name' in outs:
            self.name = outs['name']
        if 'primaryConnectionString' in outs:
            self.primary_connection_string = outs['primaryConnectionString']
        if 'primaryKey' in outs:
            self.primary_key = outs['primaryKey']
        if 'resourceGroupName' in outs:
            self.resource_group_name = outs['resourceGroupName']
        if 'secondaryConnectionString' in outs:
            self.secondary_connection_string = outs['secondaryConnectionString']
        if 'secondaryKey' in outs:
            self.secondary_key = outs['secondaryKey']
        if 'sku' in outs:
            self.sku = outs['sku']
        if 'tags' in outs:
            self.tags = outs['tags']
