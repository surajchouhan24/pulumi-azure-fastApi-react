from pulumi_azure_native import keyvault
from pulumi_azure_native import authorization


def create_keyvault(resource_group_name, location):

    client_config = authorization.get_client_config()

    vault = keyvault.Vault(
        "app-keyvault",
        resource_group_name=resource_group_name,
        location=location,

        properties=keyvault.VaultPropertiesArgs(
            tenant_id=client_config.tenant_id,

            sku=keyvault.SkuArgs(
                family="A",
                name="standard"
            ),

            access_policies=[],
            enable_soft_delete=True
        )
    )

    return vault