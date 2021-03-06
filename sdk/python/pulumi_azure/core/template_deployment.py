# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities

class TemplateDeployment(pulumi.CustomResource):
    """
    Manage a template deployment of resources
    
    ~> **Note on ARM Template Deployments:** Due to the way the underlying Azure API is designed, Terraform can only manage the deployment of the ARM Template - and not any resources which are created by it.
    This means that when deleting the `azurerm_template_deployment` resource, Terraform will only remove the reference to the deployment, whilst leaving any resources created by that ARM Template Deployment.
    One workaround for this is to use a unique Resource Group for each ARM Template Deployment, which means deleting the Resource Group would contain any resources created within it - however this isn't ideal. [More information](https://docs.microsoft.com/en-us/rest/api/resources/deployments#Deployments_Delete).
    """
    def __init__(__self__, __name__, __opts__=None, deployment_mode=None, name=None, parameters=None, parameters_body=None, resource_group_name=None, template_body=None):
        """Create a TemplateDeployment resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not deployment_mode:
            raise TypeError('Missing required property deployment_mode')
        elif not isinstance(deployment_mode, basestring):
            raise TypeError('Expected property deployment_mode to be a basestring')
        __self__.deployment_mode = deployment_mode
        """
        Specifies the mode that is used to deploy resources. This value could be either `Incremental` or `Complete`.
        Note that you will almost *always* want this to be set to `Incremental` otherwise the deployment will destroy all infrastructure not
        specified within the template, and Terraform will not be aware of this.
        """
        __props__['deploymentMode'] = deployment_mode

        if name and not isinstance(name, basestring):
            raise TypeError('Expected property name to be a basestring')
        __self__.name = name
        """
        Specifies the name of the template deployment. Changing this forces a
        new resource to be created.
        """
        __props__['name'] = name

        if parameters and not isinstance(parameters, dict):
            raise TypeError('Expected property parameters to be a dict')
        __self__.parameters = parameters
        """
        Specifies the name and value pairs that define the deployment parameters for the template.
        """
        __props__['parameters'] = parameters

        if parameters_body and not isinstance(parameters_body, basestring):
            raise TypeError('Expected property parameters_body to be a basestring')
        __self__.parameters_body = parameters_body
        """
        Specifies a valid Azure JSON parameters file that define the deployment parameters. It can contain KeyVault references
        """
        __props__['parametersBody'] = parameters_body

        if not resource_group_name:
            raise TypeError('Missing required property resource_group_name')
        elif not isinstance(resource_group_name, basestring):
            raise TypeError('Expected property resource_group_name to be a basestring')
        __self__.resource_group_name = resource_group_name
        """
        The name of the resource group in which to
        create the template deployment.
        """
        __props__['resourceGroupName'] = resource_group_name

        if template_body and not isinstance(template_body, basestring):
            raise TypeError('Expected property template_body to be a basestring')
        __self__.template_body = template_body
        """
        Specifies the JSON definition for the template.
        """
        __props__['templateBody'] = template_body

        __self__.outputs = pulumi.runtime.UNKNOWN
        """
        A map of supported scalar output types returned from the deployment (currently, Azure Template Deployment outputs of type String, Int and Bool are supported, and are converted to strings - others will be ignored) and can be accessed using `.outputs["name"]`.
        """

        super(TemplateDeployment, __self__).__init__(
            'azure:core/templateDeployment:TemplateDeployment',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'deploymentMode' in outs:
            self.deployment_mode = outs['deploymentMode']
        if 'name' in outs:
            self.name = outs['name']
        if 'outputs' in outs:
            self.outputs = outs['outputs']
        if 'parameters' in outs:
            self.parameters = outs['parameters']
        if 'parametersBody' in outs:
            self.parameters_body = outs['parametersBody']
        if 'resourceGroupName' in outs:
            self.resource_group_name = outs['resourceGroupName']
        if 'templateBody' in outs:
            self.template_body = outs['templateBody']
