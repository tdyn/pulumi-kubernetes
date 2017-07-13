// *** WARNING: this file was generated by the Lumi Terraform Bridge (TFGEN) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as lumi from "@lumi/lumi";

export class Namespace extends lumi.NamedResource implements NamespaceArgs {
    public readonly capacity?: number;
    public readonly defaultPrimaryConnectionString?: string;
    public readonly defaultPrimaryKey?: string;
    public readonly defaultSecondaryConnectionString?: string;
    public readonly defaultSecondaryKey?: string;
    public readonly location: string;
    public readonly _name: string;
    public readonly resourceGroupName: string;
    public readonly sku: string;
    public readonly tags?: {[key: string]: any};

    constructor(name: string, args: NamespaceArgs) {
        super(name);
        this.capacity = args.capacity;
        this.defaultPrimaryConnectionString = args.defaultPrimaryConnectionString;
        this.defaultPrimaryKey = args.defaultPrimaryKey;
        this.defaultSecondaryConnectionString = args.defaultSecondaryConnectionString;
        this.defaultSecondaryKey = args.defaultSecondaryKey;
        this.location = args.location;
        this._name = args._name;
        this.resourceGroupName = args.resourceGroupName;
        this.sku = args.sku;
        this.tags = args.tags;
    }
}

export interface NamespaceArgs {
    readonly capacity?: number;
    readonly defaultPrimaryConnectionString?: string;
    readonly defaultPrimaryKey?: string;
    readonly defaultSecondaryConnectionString?: string;
    readonly defaultSecondaryKey?: string;
    readonly location: string;
    readonly _name: string;
    readonly resourceGroupName: string;
    readonly sku: string;
    readonly tags?: {[key: string]: any};
}
