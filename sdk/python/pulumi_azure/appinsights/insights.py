# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities

class Insights(pulumi.CustomResource):
    """
    Manage an Application Insights component.
    """
    def __init__(__self__, __name__, __opts__=None, application_type=None, location=None, name=None, resource_group_name=None, tags=None):
        """Create a Insights resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not application_type:
            raise TypeError('Missing required property application_type')
        elif not isinstance(application_type, basestring):
            raise TypeError('Expected property application_type to be a basestring')
        __self__.application_type = application_type
        """
        Specifies the type of Application Insights to create. Valid values are `Java`, `iOS`, `MobileCenter`, `Other`, `Phone`, `Store` and `Web`.
        """
        __props__['applicationType'] = application_type

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
        Specifies the name of the Application Insights component. Changing this forces a
        new resource to be created.
        """
        __props__['name'] = name

        if not resource_group_name:
            raise TypeError('Missing required property resource_group_name')
        elif not isinstance(resource_group_name, basestring):
            raise TypeError('Expected property resource_group_name to be a basestring')
        __self__.resource_group_name = resource_group_name
        """
        The name of the resource group in which to
        create the Application Insights component.
        """
        __props__['resourceGroupName'] = resource_group_name

        if tags and not isinstance(tags, dict):
            raise TypeError('Expected property tags to be a dict')
        __self__.tags = tags
        """
        A mapping of tags to assign to the resource.
        """
        __props__['tags'] = tags

        __self__.app_id = pulumi.runtime.UNKNOWN
        """
        The App ID associated with this Application Insights component.
        """
        __self__.instrumentation_key = pulumi.runtime.UNKNOWN
        """
        The Instrumentation Key for this Application Insights component.
        """

        super(Insights, __self__).__init__(
            'azure:appinsights/insights:Insights',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'appId' in outs:
            self.app_id = outs['appId']
        if 'applicationType' in outs:
            self.application_type = outs['applicationType']
        if 'instrumentationKey' in outs:
            self.instrumentation_key = outs['instrumentationKey']
        if 'location' in outs:
            self.location = outs['location']
        if 'name' in outs:
            self.name = outs['name']
        if 'resourceGroupName' in outs:
            self.resource_group_name = outs['resourceGroupName']
        if 'tags' in outs:
            self.tags = outs['tags']
