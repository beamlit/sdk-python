Module blaxel.models.function_spec
==================================

Classes
-------

`FunctionSpec(configurations: blaxel.types.Unset | ForwardRef('CoreSpecConfigurations') = <blaxel.types.Unset object>, enabled: blaxel.types.Unset | bool = <blaxel.types.Unset object>, flavors: blaxel.types.Unset | list['Flavor'] = <blaxel.types.Unset object>, integration_connections: blaxel.types.Unset | list[str] = <blaxel.types.Unset object>, pod_template: blaxel.types.Unset | ForwardRef('PodTemplateSpec') = <blaxel.types.Unset object>, policies: blaxel.types.Unset | list[str] = <blaxel.types.Unset object>, private_clusters: blaxel.types.Unset | ForwardRef('ModelPrivateCluster') = <blaxel.types.Unset object>, revision: blaxel.types.Unset | ForwardRef('RevisionConfiguration') = <blaxel.types.Unset object>, runtime: blaxel.types.Unset | ForwardRef('Runtime') = <blaxel.types.Unset object>, sandbox: blaxel.types.Unset | bool = <blaxel.types.Unset object>, serverless_config: blaxel.types.Unset | ForwardRef('ServerlessConfig') = <blaxel.types.Unset object>, description: blaxel.types.Unset | str = <blaxel.types.Unset object>, kit: blaxel.types.Unset | list['FunctionKit'] = <blaxel.types.Unset object>, schema: blaxel.types.Unset | ForwardRef('FunctionSchema') = <blaxel.types.Unset object>)`
:   Function specification
    
    Attributes:
        configurations (Union[Unset, CoreSpecConfigurations]): Optional configurations for the object
        enabled (Union[Unset, bool]): Enable or disable the agent
        flavors (Union[Unset, list['Flavor']]): Types of hardware available for deployments
        integration_connections (Union[Unset, list[str]]):
        pod_template (Union[Unset, PodTemplateSpec]): Pod template specification
        policies (Union[Unset, list[str]]):
        private_clusters (Union[Unset, ModelPrivateCluster]): Private cluster where the model deployment is deployed
        revision (Union[Unset, RevisionConfiguration]): Revision configuration
        runtime (Union[Unset, Runtime]): Set of configurations for a deployment
        sandbox (Union[Unset, bool]): Sandbox mode
        serverless_config (Union[Unset, ServerlessConfig]): Configuration for a serverless deployment
        description (Union[Unset, str]): Function description, very important for the agent function to work with an LLM
        kit (Union[Unset, list['FunctionKit']]): Function kits
        schema (Union[Unset, FunctionSchema]): Function schema
    
    Method generated by attrs for class FunctionSpec.

    ### Static methods

    `from_dict(src_dict: dict[str, typing.Any]) ‑> ~T`
    :

    ### Instance variables

    `additional_keys: list[str]`
    :

    `additional_properties`
    :

    `configurations`
    :

    `description`
    :

    `enabled`
    :

    `flavors`
    :

    `integration_connections`
    :

    `kit`
    :

    `pod_template`
    :

    `policies`
    :

    `private_clusters`
    :

    `revision`
    :

    `runtime`
    :

    `sandbox`
    :

    `schema`
    :

    `serverless_config`
    :

    ### Methods

    `to_dict(self) ‑> dict[str, typing.Any]`
    :