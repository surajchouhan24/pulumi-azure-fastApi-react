# """An Azure RM Python Pulumi program"""

# import pulumi
# from pulumi_azure_native import storage
# from pulumi_azure_native import resources

# # Create an Azure Resource Group
# resource_group = resources.ResourceGroup("resource_group")

# # Create an Azure Storage Account
# account = storage.StorageAccount(
#     "sa",
#     resource_group_name=resource_group.name,
#     sku={
#         "name": storage.SkuName.STANDARD_LRS,
#     },
#     kind=storage.Kind.STORAGE_V2,
# )

# # Export the storage account name
# pulumi.export("storage_account_name", account.name)

# import pulumi
# from pulumi_azure_native import resources
# from components.network import create_network
# from components.postgres import create_postgres
# from components.api import create_api
# from components.frontend import create_frontend

# config = pulumi.Config()

# env = pulumi.get_stack()

# resource_group = resources.ResourceGroup(
#     f"fastapi-react-{env}-rg"
# )

# pulumi.export("resourceGroupName", resource_group.name)



# import pulumi
# from pulumi_azure_native import resources

# from components.network import create_network
# from components.postgres import create_postgres
# from components.api import create_api
# from components.frontend import create_frontend

# env = pulumi.get_stack()

# # Resource Group
# resource_group = resources.ResourceGroup(
#     f"fastapi-react-{env}-rg"
# )

# # Network
# vnet, subnet = create_network(resource_group.name)

# # Postgres
# postgres = create_postgres(resource_group.name)

# # Backend
# api = create_api(resource_group.name)

# # Frontend
# frontend = create_frontend(resource_group.name)

# pulumi.export("resourceGroupName", resource_group.name)
# # pulumi.export("frontend_url", frontend.default_host_name)
import pulumi
from pulumi_azure_native import resources

from components.network import create_network
from components.postgres import create_postgres
from components.api import create_api
from components.frontend import create_frontend
from components.keyvault import create_keyvault

env = pulumi.get_stack()
location = "eastasia"

# Resource Group
resource_group = resources.ResourceGroup(
    f"fastapi-react-{env}-rg",
    location=location
)

# Network
vnet, subnet = create_network(resource_group.name, location)

# Key Vault
keyvault = create_keyvault(resource_group.name, location)

# PostgreSQL
postgres = create_postgres(resource_group.name, location)

# Backend API
api = create_api(resource_group.name, location)

# Frontend
frontend = create_frontend(resource_group.name, location)

# Outputs
pulumi.export("resourceGroupName", resource_group.name)
pulumi.export("frontendUrl", frontend.default_hostname)
pulumi.export("apiUrl", api.default_host_name)
pulumi.export("postgresHost", postgres.fully_qualified_domain_name)