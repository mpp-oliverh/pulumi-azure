// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package notificationhub

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Gets information about the specified Notification Hub Namespace.
func LookupNamespace(ctx *pulumi.Context, args *GetNamespaceArgs) (*GetNamespaceResult, error) {
	inputs := make(map[string]interface{})
	if args != nil {
		inputs["name"] = args.Name
		inputs["resourceGroupName"] = args.ResourceGroupName
	}
	outputs, err := ctx.Invoke("azure:notificationhub/getNamespace:getNamespace", inputs)
	if err != nil {
		return nil, err
	}
	return &GetNamespaceResult{
		Enabled: outputs["enabled"],
		Location: outputs["location"],
		NamespaceType: outputs["namespaceType"],
		ServicebusEndpoint: outputs["servicebusEndpoint"],
		Sku: outputs["sku"],
		Id: outputs["id"],
	}, nil
}

// A collection of arguments for invoking getNamespace.
type GetNamespaceArgs struct {
	// Specifies the Name of the Notification Hub Namespace.
	Name interface{}
	// Specifies the Name of the Resource Group within which the Notification Hub exists.
	ResourceGroupName interface{}
}

// A collection of values returned by getNamespace.
type GetNamespaceResult struct {
	// Is this Notification Hub Namespace enabled?
	Enabled interface{}
	// The Azure Region in which this Notification Hub Namespace exists.
	Location interface{}
	// The Type of Namespace, such as `Messaging` or `NotificationHub`.
	NamespaceType interface{}
	ServicebusEndpoint interface{}
	// A `sku` block as defined below.
	Sku interface{}
	// id is the provider-assigned unique ID for this managed resource.
	Id interface{}
}
