# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities

class GetResourceGroupResult(object):
    """
    A collection of values returned by getResourceGroup.
    """
    def __init__(__self__, location=None, tags=None, id=None):
        if location and not isinstance(location, basestring):
            raise TypeError('Expected argument location to be a basestring')
        __self__.location = location
        """
        The location of the resource group.
        """
        if tags and not isinstance(tags, dict):
            raise TypeError('Expected argument tags to be a dict')
        __self__.tags = tags
        """
        A mapping of tags assigned to the resource group.
        """
        if id and not isinstance(id, basestring):
            raise TypeError('Expected argument id to be a basestring')
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """

def get_resource_group(name=None):
    """
    Use this data source to access the properties of an Azure resource group.
    """
    __args__ = dict()

    __args__['name'] = name
    __ret__ = pulumi.runtime.invoke('azure:core/getResourceGroup:getResourceGroup', __args__)

    return GetResourceGroupResult(
        location=__ret__.get('location'),
        tags=__ret__.get('tags'),
        id=__ret__.get('id'))
