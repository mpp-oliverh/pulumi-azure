# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities

class GetServicePrincipalResult(object):
    """
    A collection of values returned by getServicePrincipal.
    """
    def __init__(__self__, application_id=None, display_name=None, object_id=None, id=None):
        if application_id and not isinstance(application_id, basestring):
            raise TypeError('Expected argument application_id to be a basestring')
        __self__.application_id = application_id
        if display_name and not isinstance(display_name, basestring):
            raise TypeError('Expected argument display_name to be a basestring')
        __self__.display_name = display_name
        if object_id and not isinstance(object_id, basestring):
            raise TypeError('Expected argument object_id to be a basestring')
        __self__.object_id = object_id
        if id and not isinstance(id, basestring):
            raise TypeError('Expected argument id to be a basestring')
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """

def get_service_principal(application_id=None, display_name=None, object_id=None):
    """
    Gets information about a Service Principal associated with an Application within Azure Active Directory.
    
    -> **NOTE:** If you're authenticating using a Service Principal then it must have permissions to both `Read and write all applications` and `Sign in and read user profile` within the `Windows Azure Active Directory` API.
    """
    __args__ = dict()

    __args__['applicationId'] = application_id
    __args__['displayName'] = display_name
    __args__['objectId'] = object_id
    __ret__ = pulumi.runtime.invoke('azure:ad/getServicePrincipal:getServicePrincipal', __args__)

    return GetServicePrincipalResult(
        application_id=__ret__.get('applicationId'),
        display_name=__ret__.get('displayName'),
        object_id=__ret__.get('objectId'),
        id=__ret__.get('id'))
