# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities

class EventHub(pulumi.CustomResource):
    """
    Manages a Event Hubs as a nested resource within a Event Hubs namespace.
    """
    def __init__(__self__, __name__, __opts__=None, capture_description=None, location=None, message_retention=None, name=None, namespace_name=None, partition_count=None, resource_group_name=None):
        """Create a EventHub resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if capture_description and not isinstance(capture_description, dict):
            raise TypeError('Expected property capture_description to be a dict')
        __self__.capture_description = capture_description
        """
        A `capture_description` block as defined below.
        """
        __props__['captureDescription'] = capture_description

        if location and not isinstance(location, basestring):
            raise TypeError('Expected property location to be a basestring')
        __self__.location = location
        __props__['location'] = location

        if not message_retention:
            raise TypeError('Missing required property message_retention')
        elif not isinstance(message_retention, int):
            raise TypeError('Expected property message_retention to be a int')
        __self__.message_retention = message_retention
        """
        Specifies the number of days to retain the events for this Event Hub. Needs to be between 1 and 7 days; or 1 day when using a Basic SKU for the parent EventHub Namespace.
        """
        __props__['messageRetention'] = message_retention

        if name and not isinstance(name, basestring):
            raise TypeError('Expected property name to be a basestring')
        __self__.name = name
        """
        Specifies the name of the EventHub Namespace resource. Changing this forces a new resource to be created.
        """
        __props__['name'] = name

        if not namespace_name:
            raise TypeError('Missing required property namespace_name')
        elif not isinstance(namespace_name, basestring):
            raise TypeError('Expected property namespace_name to be a basestring')
        __self__.namespace_name = namespace_name
        """
        Specifies the name of the EventHub Namespace. Changing this forces a new resource to be created.
        """
        __props__['namespaceName'] = namespace_name

        if not partition_count:
            raise TypeError('Missing required property partition_count')
        elif not isinstance(partition_count, int):
            raise TypeError('Expected property partition_count to be a int')
        __self__.partition_count = partition_count
        """
        Specifies the current number of shards on the Event Hub.
        """
        __props__['partitionCount'] = partition_count

        if not resource_group_name:
            raise TypeError('Missing required property resource_group_name')
        elif not isinstance(resource_group_name, basestring):
            raise TypeError('Expected property resource_group_name to be a basestring')
        __self__.resource_group_name = resource_group_name
        """
        The name of the resource group in which the EventHub's parent Namespace exists. Changing this forces a new resource to be created.
        """
        __props__['resourceGroupName'] = resource_group_name

        __self__.partition_ids = pulumi.runtime.UNKNOWN
        """
        The identifiers for partitions created for Event Hubs.
        """

        super(EventHub, __self__).__init__(
            'azure:eventhub/eventHub:EventHub',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'captureDescription' in outs:
            self.capture_description = outs['captureDescription']
        if 'location' in outs:
            self.location = outs['location']
        if 'messageRetention' in outs:
            self.message_retention = outs['messageRetention']
        if 'name' in outs:
            self.name = outs['name']
        if 'namespaceName' in outs:
            self.namespace_name = outs['namespaceName']
        if 'partitionCount' in outs:
            self.partition_count = outs['partitionCount']
        if 'partitionIds' in outs:
            self.partition_ids = outs['partitionIds']
        if 'resourceGroupName' in outs:
            self.resource_group_name = outs['resourceGroupName']
