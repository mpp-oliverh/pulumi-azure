# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities

class Service(pulumi.CustomResource):
    """
    Manages an Azure Container Service Instance
    
    ~> **Note:** All arguments including the client secret will be stored in the raw state as plain-text.
    [Read more about sensitive data in state](https://www.terraform.io/docs/state/sensitive-data.html).
    
    ## Example Usage (DCOS)
    
    ```hcl
    resource "azurerm_resource_group" "test" {
      name     = "acctestRG1"
      location = "West US"
    }
    
    resource "azurerm_container_service" "test" {
      name                   = "acctestcontservice1"
      location               = "${azurerm_resource_group.test.location}"
      resource_group_name    = "${azurerm_resource_group.test.name}"
      orchestration_platform = "DCOS"
    
      master_profile {
        count      = 1
        dns_prefix = "acctestmaster1"
      }
    
      linux_profile {
        admin_username = "acctestuser1"
    
        ssh_key {
          key_data = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCqaZoyiz1qbdOQ8xEf6uEu1cCwYowo5FHtsBhqLoDnnp7KUTEBN+L2NxRIfQ781rxV6Iq5jSav6b2Q8z5KiseOlvKA/RF2wqU0UPYqQviQhLmW6THTpmrv/YkUCuzxDpsH7DUDhZcwySLKVVe0Qm3+5N2Ta6UYH3lsDf9R9wTP2K/+vAnflKebuypNlmocIvakFWoZda18FOmsOoIVXQ8HWFNCuw9ZCunMSN62QGamCe3dL5cXlkgHYv7ekJE15IA9aOJcM7e90oeTqo+7HTcWfdu0qQqPWY5ujyMw/llas8tsXY85LFqRnr3gJ02bAscjc477+X+j/gkpFoN1QEmt terraform@demo.tld"
        }
      }
    
      agent_pool_profile {
        name       = "default"
        count      = 1
        dns_prefix = "acctestagent1"
        vm_size    = "Standard_F2"
      }
    
      diagnostics_profile {
        enabled = false
      }
    
      tags {
        Environment = "Production"
      }
    }
    ```
    """
    def __init__(__self__, __name__, __opts__=None, agent_pool_profile=None, diagnostics_profile=None, linux_profile=None, location=None, master_profile=None, name=None, orchestration_platform=None, resource_group_name=None, service_principal=None, tags=None):
        """Create a Service resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not agent_pool_profile:
            raise TypeError('Missing required property agent_pool_profile')
        elif not isinstance(agent_pool_profile, dict):
            raise TypeError('Expected property agent_pool_profile to be a dict')
        __self__.agent_pool_profile = agent_pool_profile
        """
        One or more Agent Pool Profile's block as documented below.
        """
        __props__['agentPoolProfile'] = agent_pool_profile

        if not diagnostics_profile:
            raise TypeError('Missing required property diagnostics_profile')
        elif not isinstance(diagnostics_profile, dict):
            raise TypeError('Expected property diagnostics_profile to be a dict')
        __self__.diagnostics_profile = diagnostics_profile
        """
        A VM Diagnostics Profile block as documented below.
        """
        __props__['diagnosticsProfile'] = diagnostics_profile

        if not linux_profile:
            raise TypeError('Missing required property linux_profile')
        elif not isinstance(linux_profile, dict):
            raise TypeError('Expected property linux_profile to be a dict')
        __self__.linux_profile = linux_profile
        """
        A Linux Profile block as documented below.
        """
        __props__['linuxProfile'] = linux_profile

        if not location:
            raise TypeError('Missing required property location')
        elif not isinstance(location, basestring):
            raise TypeError('Expected property location to be a basestring')
        __self__.location = location
        """
        The location where the Container Service instance should be created. Changing this forces a new resource to be created.
        """
        __props__['location'] = location

        if not master_profile:
            raise TypeError('Missing required property master_profile')
        elif not isinstance(master_profile, dict):
            raise TypeError('Expected property master_profile to be a dict')
        __self__.master_profile = master_profile
        """
        A Master Profile block as documented below.
        """
        __props__['masterProfile'] = master_profile

        if name and not isinstance(name, basestring):
            raise TypeError('Expected property name to be a basestring')
        __self__.name = name
        """
        Unique name of the agent pool profile in the context of the subscription and resource group.
        """
        __props__['name'] = name

        if not orchestration_platform:
            raise TypeError('Missing required property orchestration_platform')
        elif not isinstance(orchestration_platform, basestring):
            raise TypeError('Expected property orchestration_platform to be a basestring')
        __self__.orchestration_platform = orchestration_platform
        """
        Specifies the Container Orchestration Platform to use. Currently can be either `DCOS`, `Kubernetes` or `Swarm`. Changing this forces a new resource to be created.
        """
        __props__['orchestrationPlatform'] = orchestration_platform

        if not resource_group_name:
            raise TypeError('Missing required property resource_group_name')
        elif not isinstance(resource_group_name, basestring):
            raise TypeError('Expected property resource_group_name to be a basestring')
        __self__.resource_group_name = resource_group_name
        """
        Specifies the resource group where the resource exists. Changing this forces a new resource to be created.
        """
        __props__['resourceGroupName'] = resource_group_name

        if service_principal and not isinstance(service_principal, dict):
            raise TypeError('Expected property service_principal to be a dict')
        __self__.service_principal = service_principal
        """
        A Service Principal block as documented below.
        """
        __props__['servicePrincipal'] = service_principal

        if tags and not isinstance(tags, dict):
            raise TypeError('Expected property tags to be a dict')
        __self__.tags = tags
        """
        A mapping of tags to assign to the resource.
        """
        __props__['tags'] = tags

        super(Service, __self__).__init__(
            'azure:containerservice/service:Service',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'agentPoolProfile' in outs:
            self.agent_pool_profile = outs['agentPoolProfile']
        if 'diagnosticsProfile' in outs:
            self.diagnostics_profile = outs['diagnosticsProfile']
        if 'linuxProfile' in outs:
            self.linux_profile = outs['linuxProfile']
        if 'location' in outs:
            self.location = outs['location']
        if 'masterProfile' in outs:
            self.master_profile = outs['masterProfile']
        if 'name' in outs:
            self.name = outs['name']
        if 'orchestrationPlatform' in outs:
            self.orchestration_platform = outs['orchestrationPlatform']
        if 'resourceGroupName' in outs:
            self.resource_group_name = outs['resourceGroupName']
        if 'servicePrincipal' in outs:
            self.service_principal = outs['servicePrincipal']
        if 'tags' in outs:
            self.tags = outs['tags']
