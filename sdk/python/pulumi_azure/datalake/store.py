# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities

class Store(pulumi.CustomResource):
    """
    Manage an Azure Data Lake Store.
    """
    def __init__(__self__, __name__, __opts__=None, encryption_state=None, encryption_type=None, firewall_allow_azure_ips=None, firewall_state=None, location=None, name=None, resource_group_name=None, tags=None, tier=None):
        """Create a Store resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if encryption_state and not isinstance(encryption_state, basestring):
            raise TypeError('Expected property encryption_state to be a basestring')
        __self__.encryption_state = encryption_state
        """
        Is Encryption enabled on this Data Lake Store Account? Possible values are `Enabled` or `Disabled`. Defaults to `Enabled`.
        """
        __props__['encryptionState'] = encryption_state

        if encryption_type and not isinstance(encryption_type, basestring):
            raise TypeError('Expected property encryption_type to be a basestring')
        __self__.encryption_type = encryption_type
        """
        The Encryption Type used for this Data Lake Store Account. Currently can be set to `SystemManaged` when `encryption_state` is `Enabled` - and must be a blank string when it's Disabled.
        """
        __props__['encryptionType'] = encryption_type

        if firewall_allow_azure_ips and not isinstance(firewall_allow_azure_ips, basestring):
            raise TypeError('Expected property firewall_allow_azure_ips to be a basestring')
        __self__.firewall_allow_azure_ips = firewall_allow_azure_ips
        """
        are Azure Service IP's allowed through the firewall? Possible values are `Enabled` and `Disabled`. Defaults to `Enabled.`
        """
        __props__['firewallAllowAzureIps'] = firewall_allow_azure_ips

        if firewall_state and not isinstance(firewall_state, basestring):
            raise TypeError('Expected property firewall_state to be a basestring')
        __self__.firewall_state = firewall_state
        """
        the state of the Firewall. Possible values are `Enabled` and `Disabled`. Defaults to `Enabled.`
        """
        __props__['firewallState'] = firewall_state

        if not location:
            raise TypeError('Missing required property location')
        elif not isinstance(location, basestring):
            raise TypeError('Expected property location to be a basestring')
        __self__.location = location
        """
        Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        """
        __props__['location'] = location

        if name and not isinstance(name, basestring):
            raise TypeError('Expected property name to be a basestring')
        __self__.name = name
        """
        Specifies the name of the Data Lake Store. Changing this forces a new resource to be created. Has to be between 3 to 24 characters.
        """
        __props__['name'] = name

        if not resource_group_name:
            raise TypeError('Missing required property resource_group_name')
        elif not isinstance(resource_group_name, basestring):
            raise TypeError('Expected property resource_group_name to be a basestring')
        __self__.resource_group_name = resource_group_name
        """
        The name of the resource group in which to create the Data Lake Store.
        """
        __props__['resourceGroupName'] = resource_group_name

        if tags and not isinstance(tags, dict):
            raise TypeError('Expected property tags to be a dict')
        __self__.tags = tags
        """
        A mapping of tags to assign to the resource.
        """
        __props__['tags'] = tags

        if tier and not isinstance(tier, basestring):
            raise TypeError('Expected property tier to be a basestring')
        __self__.tier = tier
        """
        The monthly commitment tier for Data Lake Store. Accepted values are `Consumption`, `Commitment_1TB`, `Commitment_10TB`, `Commitment_100TB`, `Commitment_500TB`, `Commitment_1PB` or `Commitment_5PB`.
        """
        __props__['tier'] = tier

        __self__.endpoint = pulumi.runtime.UNKNOWN
        """
        The Endpoint for the Data Lake Store.
        """

        super(Store, __self__).__init__(
            'azure:datalake/store:Store',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'encryptionState' in outs:
            self.encryption_state = outs['encryptionState']
        if 'encryptionType' in outs:
            self.encryption_type = outs['encryptionType']
        if 'endpoint' in outs:
            self.endpoint = outs['endpoint']
        if 'firewallAllowAzureIps' in outs:
            self.firewall_allow_azure_ips = outs['firewallAllowAzureIps']
        if 'firewallState' in outs:
            self.firewall_state = outs['firewallState']
        if 'location' in outs:
            self.location = outs['location']
        if 'name' in outs:
            self.name = outs['name']
        if 'resourceGroupName' in outs:
            self.resource_group_name = outs['resourceGroupName']
        if 'tags' in outs:
            self.tags = outs['tags']
        if 'tier' in outs:
            self.tier = outs['tier']
