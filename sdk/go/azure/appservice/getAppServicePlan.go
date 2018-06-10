// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package appservice

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Use this data source to obtain information about an App Service Plan (formerly known as a `Server Farm`).
func LookupppServicePlan(ctx *pulumi.Context, args *GetAppServicePlanArgs) (*GetAppServicePlanResult, error) {
	inputs := make(map[string]interface{})
	if args != nil {
		inputs["name"] = args.Name
		inputs["resourceGroupName"] = args.ResourceGroupName
	}
	outputs, err := ctx.Invoke("azure:appservice/getAppServicePlan:getAppServicePlan", inputs)
	if err != nil {
		return nil, err
	}
	ret := GetAppServicePlanResult{}
	if v, ok := outputs["kind"]; ok {
		ret.Kind = v
	}
	if v, ok := outputs["location"]; ok {
		ret.Location = v
	}
	if v, ok := outputs["maximumNumberOfWorkers"]; ok {
		ret.MaximumNumberOfWorkers = v
	}
	if v, ok := outputs["properties"]; ok {
		ret.Properties = v
	}
	if v, ok := outputs["sku"]; ok {
		ret.Sku = v
	}
	if v, ok := outputs["tags"]; ok {
		ret.Tags = v
	}
	return &ret, nil
}

// A collection of arguments for invoking getAppServicePlan.
type GetAppServicePlanArgs struct {
	// The name of the App Service Plan.
	Name interface{}
	// The Name of the Resource Group where the App Service Plan exists.
	ResourceGroupName interface{}
}

// A collection of values returned by getAppServicePlan.
type GetAppServicePlanResult struct {
	// The Operating System type of the App Service Plan
	Kind interface{}
	// The Azure location where the App Service Plan exists
	Location interface{}
	// Maximum number of instances that can be assigned to this App Service plan.
	MaximumNumberOfWorkers interface{}
	// A `properties` block as documented below.
	Properties interface{}
	// A `sku` block as documented below.
	Sku interface{}
	// A mapping of tags assigned to the resource.
	Tags interface{}
}