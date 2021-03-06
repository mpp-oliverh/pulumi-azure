# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities

class GetNamespaceResult(object):
    """
    A collection of values returned by getNamespace.
    """
    def __init__(__self__, enabled=None, location=None, namespace_type=None, servicebus_endpoint=None, sku=None, id=None):
        if enabled and not isinstance(enabled, bool):
            raise TypeError('Expected argument enabled to be a bool')
        __self__.enabled = enabled
        """
        Is this Notification Hub Namespace enabled?
        """
        if location and not isinstance(location, basestring):
            raise TypeError('Expected argument location to be a basestring')
        __self__.location = location
        """
        The Azure Region in which this Notification Hub Namespace exists.
        """
        if namespace_type and not isinstance(namespace_type, basestring):
            raise TypeError('Expected argument namespace_type to be a basestring')
        __self__.namespace_type = namespace_type
        """
        The Type of Namespace, such as `Messaging` or `NotificationHub`.
        """
        if servicebus_endpoint and not isinstance(servicebus_endpoint, basestring):
            raise TypeError('Expected argument servicebus_endpoint to be a basestring')
        __self__.servicebus_endpoint = servicebus_endpoint
        if sku and not isinstance(sku, dict):
            raise TypeError('Expected argument sku to be a dict')
        __self__.sku = sku
        """
        A `sku` block as defined below.
        """
        if id and not isinstance(id, basestring):
            raise TypeError('Expected argument id to be a basestring')
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """

def get_namespace(name=None, resource_group_name=None):
    """
    Gets information about the specified Notification Hub Namespace.
    """
    __args__ = dict()

    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    __ret__ = pulumi.runtime.invoke('azure:notificationhub/getNamespace:getNamespace', __args__)

    return GetNamespaceResult(
        enabled=__ret__.get('enabled'),
        location=__ret__.get('location'),
        namespace_type=__ret__.get('namespaceType'),
        servicebus_endpoint=__ret__.get('servicebusEndpoint'),
        sku=__ret__.get('sku'),
        id=__ret__.get('id'))
