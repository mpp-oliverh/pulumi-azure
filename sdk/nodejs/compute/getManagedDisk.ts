// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Use this data source to access the properties of an existing Azure Managed Disk.
 */
export function getManagedDisk(args: GetManagedDiskArgs, opts?: pulumi.InvokeOptions): Promise<GetManagedDiskResult> {
    return pulumi.runtime.invoke("azure:compute/getManagedDisk:getManagedDisk", {
        "name": args.name,
        "resourceGroupName": args.resourceGroupName,
        "tags": args.tags,
        "zones": args.zones,
    }, opts);
}

/**
 * A collection of arguments for invoking getManagedDisk.
 */
export interface GetManagedDiskArgs {
    /**
     * Specifies the name of the Managed Disk.
     */
    readonly name: string;
    /**
     * Specifies the name of the resource group.
     */
    readonly resourceGroupName: string;
    readonly tags?: {[key: string]: any};
    readonly zones?: string[];
}

/**
 * A collection of values returned by getManagedDisk.
 */
export interface GetManagedDiskResult {
    /**
     * The size of the managed disk in gigabytes.
     */
    readonly diskSizeGb: number;
    /**
     * The operating system for managed disk. Valid values are `Linux` or `Windows`
     */
    readonly osType: string;
    /**
     * ID of an existing managed disk that the current resource was created from.
     */
    readonly sourceResourceId: string;
    /**
     * The source URI for the managed disk
     */
    readonly sourceUri: string;
    /**
     * The storage account type for the managed disk.
     */
    readonly storageAccountType: string;
    /**
     * A mapping of tags assigned to the resource.
     */
    readonly tags: {[key: string]: any};
    /**
     * (Optional) A collection containing the availability zone the managed disk is allocated in.
     */
    readonly zones: string[];
    /**
     * id is the provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
}
