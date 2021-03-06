# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities

class EventHubConsumerGroup(pulumi.CustomResource):
    """
    Manages a Event Hubs Consumer Group as a nested resource within an Event Hub.
    """
    def __init__(__self__, __name__, __opts__=None, eventhub_name=None, location=None, name=None, namespace_name=None, resource_group_name=None, user_metadata=None):
        """Create a EventHubConsumerGroup resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not eventhub_name:
            raise TypeError('Missing required property eventhub_name')
        elif not isinstance(eventhub_name, basestring):
            raise TypeError('Expected property eventhub_name to be a basestring')
        __self__.eventhub_name = eventhub_name
        """
        Specifies the name of the EventHub. Changing this forces a new resource to be created.
        """
        __props__['eventhubName'] = eventhub_name

        if location and not isinstance(location, basestring):
            raise TypeError('Expected property location to be a basestring')
        __self__.location = location
        __props__['location'] = location

        if name and not isinstance(name, basestring):
            raise TypeError('Expected property name to be a basestring')
        __self__.name = name
        """
        Specifies the name of the EventHub Consumer Group resource. Changing this forces a new resource to be created.
        """
        __props__['name'] = name

        if not namespace_name:
            raise TypeError('Missing required property namespace_name')
        elif not isinstance(namespace_name, basestring):
            raise TypeError('Expected property namespace_name to be a basestring')
        __self__.namespace_name = namespace_name
        """
        Specifies the name of the grandparent EventHub Namespace. Changing this forces a new resource to be created.
        """
        __props__['namespaceName'] = namespace_name

        if not resource_group_name:
            raise TypeError('Missing required property resource_group_name')
        elif not isinstance(resource_group_name, basestring):
            raise TypeError('Expected property resource_group_name to be a basestring')
        __self__.resource_group_name = resource_group_name
        """
        The name of the resource group in which the EventHub Consumer Group's grandparent Namespace exists. Changing this forces a new resource to be created.
        """
        __props__['resourceGroupName'] = resource_group_name

        if user_metadata and not isinstance(user_metadata, basestring):
            raise TypeError('Expected property user_metadata to be a basestring')
        __self__.user_metadata = user_metadata
        """
        Specifies the user metadata.
        """
        __props__['userMetadata'] = user_metadata

        super(EventHubConsumerGroup, __self__).__init__(
            'azure:eventhub/eventHubConsumerGroup:EventHubConsumerGroup',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'eventhubName' in outs:
            self.eventhub_name = outs['eventhubName']
        if 'location' in outs:
            self.location = outs['location']
        if 'name' in outs:
            self.name = outs['name']
        if 'namespaceName' in outs:
            self.namespace_name = outs['namespaceName']
        if 'resourceGroupName' in outs:
            self.resource_group_name = outs['resourceGroupName']
        if 'userMetadata' in outs:
            self.user_metadata = outs['userMetadata']
