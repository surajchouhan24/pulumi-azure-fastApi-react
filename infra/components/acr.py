import pulumi
import pulumi_azure_native as azure


class ContainerRegistry:

    def __init__(self, name, rg, location):

        acr = azure.containerregistry.Registry(
            f"{name}acr",
            resource_group_name=rg,
            location=location,

            sku=azure.containerregistry.SkuArgs(
                name="Basic"
            ),

            admin_user_enabled=False
        )

        self.registry = acr
        self.login_server = acr.login_server