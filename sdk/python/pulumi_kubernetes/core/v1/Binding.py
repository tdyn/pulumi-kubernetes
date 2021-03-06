import pulumi
import pulumi.runtime

from ... import tables

class Binding(pulumi.CustomResource):
    """
    Binding ties one object to another; for example, a pod is bound to a node by a scheduler.
    Deprecated in 1.7, please use the bindings subresource of pods instead.
    """
    def __init__(self, __name__, __opts__=None, metadata=None, target=None):
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['apiVersion'] = 'v1'
        __props__['kind'] = 'Binding'
        if not target:
            raise TypeError('Missing required property target')
        __props__['target'] = target
        __props__['metadata'] = metadata

        super(Binding, self).__init__(
            "kubernetes:core/v1:Binding",
            __name__,
            __props__,
            __opts__)

    def translate_output_property(self, prop: str) -> str:
        return tables._CASING_FORWARD_TABLE.get(prop) or prop

    def translate_input_property(self, prop: str) -> str:
        return tables._CASING_BACKWARD_TABLE.get(prop) or prop
