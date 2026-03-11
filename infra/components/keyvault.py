# from pulumi_azure_native import keyvault
# from pulumi_azure_native import authorization


# def create_keyvault(resource_group_name, location):

#     client_config = authorization.get_client_config()

#     vault = keyvault.Vault(
#         "app-keyvault",
#         resource_group_name=resource_group_name,
#         location=location,

#         properties=keyvault.VaultPropertiesArgs(
#             tenant_id=client_config.tenant_id,

#             sku=keyvault.SkuArgs(
#                 family="A",
#                 name="standard"
#             ),

#             access_policies=[],
#             enable_soft_delete=True
#         )
#     )

#     return vault

import pulumi
import pulumi_azure_native as azure


class KeyVault:

    def __init__(self, name, resource_group_name, location):

        config = pulumi.Config()

        # Get stack name
        stack = pulumi.get_stack()

        # Azure tenant
        client_config = azure.authorization.get_client_config()
        
        # Azure KeyVault name rules:
        # 3–24 chars, alphanumeric + hyphen, globally unique
        vault_name = f"{name}-{stack}".replace("-", "")[:24].lower()

        vault = azure.keyvault.Vault(
            name,
            vault_name=vault_name,
            resource_group_name=resource_group_name,
            location=location,
            properties=azure.keyvault.VaultPropertiesArgs(
                tenant_id=client_config.tenant_id,

                sku=azure.keyvault.SkuArgs(
                    family="A",
                    name="standard",
                ),

                access_policies=[],
                enable_rbac_authorization=True
            ),
        )

        # Pulumi secrets
        db_password = config.require_secret("dbPassword")
        jwt_key = config.get_secret("jwtKey") or pulumi.Output.secret("dev-jwt-secret")

        # Store DB password
        db_secret = azure.keyvault.Secret(
            "db-password",
            resource_group_name=resource_group_name,
            vault_name=vault_name,
            properties=azure.keyvault.SecretPropertiesArgs(
                value=db_password
            ),
            opts=pulumi.ResourceOptions(depends_on=[vault])
        )

        # Store JWT key
        jwt_secret = azure.keyvault.Secret(
            "jwt-signing-key",
            resource_group_name=resource_group_name,
            vault_name=vault_name,
            properties=azure.keyvault.SecretPropertiesArgs(
                value=jwt_key
            ),
            opts=pulumi.ResourceOptions(depends_on=[vault])
        )

        # Outputs
        self.vault_uri = vault.properties.vault_uri
        self.db_secret_name = db_secret.name
        self.jwt_secret_name = jwt_secret.name