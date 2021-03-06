// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Use this data source to access the properties of an Azure resource group.
 */
export function getResourceGroup(args: GetResourceGroupArgs, opts?: pulumi.InvokeOptions): Promise<GetResourceGroupResult> {
    return pulumi.runtime.invoke("azure:core/getResourceGroup:getResourceGroup", {
        "name": args.name,
    }, opts);
}

/**
 * A collection of arguments for invoking getResourceGroup.
 */
export interface GetResourceGroupArgs {
    /**
     * Specifies the name of the resource group.
     */
    readonly name: string;
}

/**
 * A collection of values returned by getResourceGroup.
 */
export interface GetResourceGroupResult {
    /**
     * The location of the resource group.
     */
    readonly location: string;
    /**
     * A mapping of tags assigned to the resource group.
     */
    readonly tags: {[key: string]: any};
    /**
     * id is the provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
}
