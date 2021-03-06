# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities

class ActiveDirectoryAdministrator(pulumi.CustomResource):
    """
    Allows you to set a user or group as the AD administrator for an Azure SQL server
    """
    def __init__(__self__, __name__, __opts__=None, login=None, object_id=None, resource_group_name=None, server_name=None, tenant_id=None):
        """Create a ActiveDirectoryAdministrator resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not login:
            raise TypeError('Missing required property login')
        elif not isinstance(login, basestring):
            raise TypeError('Expected property login to be a basestring')
        __self__.login = login
        """
        The login name of the principal to set as the server administrator
        """
        __props__['login'] = login

        if not object_id:
            raise TypeError('Missing required property object_id')
        elif not isinstance(object_id, basestring):
            raise TypeError('Expected property object_id to be a basestring')
        __self__.object_id = object_id
        """
        The ID of the principal to set as the server administrator
        """
        __props__['objectId'] = object_id

        if not resource_group_name:
            raise TypeError('Missing required property resource_group_name')
        elif not isinstance(resource_group_name, basestring):
            raise TypeError('Expected property resource_group_name to be a basestring')
        __self__.resource_group_name = resource_group_name
        """
        The name of the resource group for the SQL server. Changing this forces a new resource to be created.
        """
        __props__['resourceGroupName'] = resource_group_name

        if not server_name:
            raise TypeError('Missing required property server_name')
        elif not isinstance(server_name, basestring):
            raise TypeError('Expected property server_name to be a basestring')
        __self__.server_name = server_name
        """
        The name of the SQL Server on which to set the administrator. Changing this forces a new resource to be created.
        """
        __props__['serverName'] = server_name

        if not tenant_id:
            raise TypeError('Missing required property tenant_id')
        elif not isinstance(tenant_id, basestring):
            raise TypeError('Expected property tenant_id to be a basestring')
        __self__.tenant_id = tenant_id
        """
        The Azure Tenant ID
        """
        __props__['tenantId'] = tenant_id

        super(ActiveDirectoryAdministrator, __self__).__init__(
            'azure:sql/activeDirectoryAdministrator:ActiveDirectoryAdministrator',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'login' in outs:
            self.login = outs['login']
        if 'objectId' in outs:
            self.object_id = outs['objectId']
        if 'resourceGroupName' in outs:
            self.resource_group_name = outs['resourceGroupName']
        if 'serverName' in outs:
            self.server_name = outs['serverName']
        if 'tenantId' in outs:
            self.tenant_id = outs['tenantId']
