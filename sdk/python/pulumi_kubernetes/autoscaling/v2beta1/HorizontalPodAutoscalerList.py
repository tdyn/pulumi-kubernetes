import pulumi
import pulumi.runtime

from ... import tables

class HorizontalPodAutoscalerList(pulumi.CustomResource):
    """
    HorizontalPodAutoscaler is a list of horizontal pod autoscaler objects.
    """
    def __init__(self, __name__, __opts__=None, items=None, metadata=None):
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['apiVersion'] = 'autoscaling/v2beta1'
        __props__['kind'] = 'HorizontalPodAutoscalerList'
        if not items:
            raise TypeError('Missing required property items')
        __props__['items'] = items
        __props__['metadata'] = metadata

        super(HorizontalPodAutoscalerList, self).__init__(
            "kubernetes:autoscaling/v2beta1:HorizontalPodAutoscalerList",
            __name__,
            __props__,
            __opts__)

    def translate_output_property(self, prop: str) -> str:
        return tables._CASING_FORWARD_TABLE.get(prop) or prop

    def translate_input_property(self, prop: str) -> str:
        return tables._CASING_BACKWARD_TABLE.get(prop) or prop
