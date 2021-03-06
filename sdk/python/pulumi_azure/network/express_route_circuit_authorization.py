# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities

class ExpressRouteCircuitAuthorization(pulumi.CustomResource):
    """
    Manages an ExpressRoute Circuit Authorization.
    """
    def __init__(__self__, __name__, __opts__=None, express_route_circuit_name=None, name=None, resource_group_name=None):
        """Create a ExpressRouteCircuitAuthorization resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not express_route_circuit_name:
            raise TypeError('Missing required property express_route_circuit_name')
        elif not isinstance(express_route_circuit_name, basestring):
            raise TypeError('Expected property express_route_circuit_name to be a basestring')
        __self__.express_route_circuit_name = express_route_circuit_name
        """
        The name of the Express Route Circuit in which to create the Authorization.
        """
        __props__['expressRouteCircuitName'] = express_route_circuit_name

        if name and not isinstance(name, basestring):
            raise TypeError('Expected property name to be a basestring')
        __self__.name = name
        """
        The name of the ExpressRoute circuit. Changing this forces a
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
        create the ExpressRoute circuit. Changing this forces a new resource to be created.
        """
        __props__['resourceGroupName'] = resource_group_name

        __self__.authorization_key = pulumi.runtime.UNKNOWN
        """
        The Authorization Key.
        """
        __self__.authorization_use_status = pulumi.runtime.UNKNOWN
        """
        The authorization use status.
        """

        super(ExpressRouteCircuitAuthorization, __self__).__init__(
            'azure:network/expressRouteCircuitAuthorization:ExpressRouteCircuitAuthorization',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'authorizationKey' in outs:
            self.authorization_key = outs['authorizationKey']
        if 'authorizationUseStatus' in outs:
            self.authorization_use_status = outs['authorizationUseStatus']
        if 'expressRouteCircuitName' in outs:
            self.express_route_circuit_name = outs['expressRouteCircuitName']
        if 'name' in outs:
            self.name = outs['name']
        if 'resourceGroupName' in outs:
            self.resource_group_name = outs['resourceGroupName']
