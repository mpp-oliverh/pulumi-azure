# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities

class ActionHttp(pulumi.CustomResource):
    """
    Manages an HTTP Action within a Logic App Workflow
    """
    def __init__(__self__, __name__, __opts__=None, body=None, headers=None, logic_app_id=None, method=None, name=None, uri=None):
        """Create a ActionHttp resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if body and not isinstance(body, basestring):
            raise TypeError('Expected property body to be a basestring')
        __self__.body = body
        """
        Specifies the HTTP Body that should be sent to the `uri` when this HTTP Action is triggered.
        """
        __props__['body'] = body

        if headers and not isinstance(headers, dict):
            raise TypeError('Expected property headers to be a dict')
        __self__.headers = headers
        """
        Specifies a Map of Key-Value Pairs that should be sent to the `uri` when this HTTP Action is triggered.
        """
        __props__['headers'] = headers

        if not logic_app_id:
            raise TypeError('Missing required property logic_app_id')
        elif not isinstance(logic_app_id, basestring):
            raise TypeError('Expected property logic_app_id to be a basestring')
        __self__.logic_app_id = logic_app_id
        """
        Specifies the ID of the Logic App Workflow. Changing this forces a new resource to be created.
        """
        __props__['logicAppId'] = logic_app_id

        if not method:
            raise TypeError('Missing required property method')
        elif not isinstance(method, basestring):
            raise TypeError('Expected property method to be a basestring')
        __self__.method = method
        """
        Specifies the HTTP Method which should be used for this HTTP Action. Possible values include `DELETE`, `GET`, `PATCH`, `POST` and `PUT`.
        """
        __props__['method'] = method

        if name and not isinstance(name, basestring):
            raise TypeError('Expected property name to be a basestring')
        __self__.name = name
        """
        Specifies the name of the HTTP Action to be created within the Logic App Workflow. Changing this forces a new resource to be created.
        """
        __props__['name'] = name

        if not uri:
            raise TypeError('Missing required property uri')
        elif not isinstance(uri, basestring):
            raise TypeError('Expected property uri to be a basestring')
        __self__.uri = uri
        """
        Specifies the URI which will be called when this HTTP Action is triggered.
        """
        __props__['uri'] = uri

        super(ActionHttp, __self__).__init__(
            'azure:logicapps/actionHttp:ActionHttp',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'body' in outs:
            self.body = outs['body']
        if 'headers' in outs:
            self.headers = outs['headers']
        if 'logicAppId' in outs:
            self.logic_app_id = outs['logicAppId']
        if 'method' in outs:
            self.method = outs['method']
        if 'name' in outs:
            self.name = outs['name']
        if 'uri' in outs:
            self.uri = outs['uri']
