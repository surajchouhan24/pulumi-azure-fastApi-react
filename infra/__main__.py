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
# import pulumi
# from pulumi_azure_native import resources

# from components.network import create_network
# from components.postgres import create_postgres
# from components.api import create_api
# from components.frontend import create_frontend
# from components.keyvault import create_keyvault

# env = pulumi.get_stack()
# location = "eastasia"

# # Resource Group
# resource_group = resources.ResourceGroup(
#     f"fastapi-react-{env}-rg",
#     location=location
# )

# # Network
# vnet, subnet = create_network(resource_group.name, location)

# # Key Vault
# keyvault = create_keyvault(resource_group.name, location)

# # PostgreSQL
# postgres = create_postgres(resource_group.name, location)

# # Backend API
# api = create_api(resource_group.name, location)

# # Frontend
# frontend = create_frontend(resource_group.name, location)

# # Outputs
# pulumi.export("resourceGroupName", resource_group.name)
# pulumi.export("frontendUrl", frontend.default_hostname)
# pulumi.export("apiUrl", api.default_host_name)
# pulumi.export("postgresHost", postgres.fully_qualified_domain_name)

# import pulumi
# import pulumi_azure_native as azure

# from components.network import Network
# from components.postgres import Postgres
# from components.api import ApiService
# from components.frontend import Frontend


# config = pulumi.Config()
# env = config.require("environment")
# location = config.get("location") or "centralindia"


# resource_group = azure.resources.ResourceGroup(
#     f"myapp-{env}-rg",
#     location=location
# )


# network = Network(
#     f"myapp-{env}-network",
#     resource_group.name,
#     location
# )


# postgres = Postgres(
#     f"myapp-{env}-db",
#     resource_group.name,
#     location,
#     network.subnet_id
# )


# api = ApiService(
#     f"myapp-{env}-api",
#     resource_group.name,
#     location,
#     postgres.host
# )


# frontend = Frontend(
#     f"myapp-{env}-frontend",
#     resource_group.name,
#     location,
#     api.api_url
# )


# pulumi.export("frontendUrl", frontend.url)
# pulumi.export("staticWebAppToken", frontend.token)
# pulumi.export("apiUrl", api.api_url)
# pulumi.export("postgresHost", postgres.host)
# pulumi.export("resourceGroupName", resource_group.name)





# import pulumi
# import pulumi_azure_native as azure

# from components.network import Network
# from components.postgres import Postgres
# from components.api import ApiService
# from components.frontend import Frontend
# from components.keyvault import KeyVault


# config = pulumi.Config()

# env = config.require("environment")
# location = config.get("location") or "centralindia"


# # -------------------------------------------------------
# # Resource Group
# # -------------------------------------------------------

# resource_group = azure.resources.ResourceGroup(
#     f"myapp-{env}-rg",
#     location=location
# )


# # -------------------------------------------------------
# # Network
# # -------------------------------------------------------

# network = Network(
#     f"myapp-{env}-network",
#     resource_group.name,
#     location
# )


# # -------------------------------------------------------
# # Key Vault
# # -------------------------------------------------------

# keyvault = KeyVault(
#     f"myapp-{env}-kv",
#     resource_group.name,
#     location
# )


# # -------------------------------------------------------
# # PostgreSQL Flexible Server
# # -------------------------------------------------------

# postgres = Postgres(
#     f"myapp-{env}-db",
#     resource_group.name,
#     location,
#     network.subnet_id,
#     keyvault.db_password
# )


# # -------------------------------------------------------
# # FastAPI Backend
# # -------------------------------------------------------

# api = ApiService(
#     f"myapp-{env}-api",
#     resource_group.name,
#     location,
#     postgres.host,
#     keyvault.jwt_key
# )


# # -------------------------------------------------------
# # React Frontend
# # -------------------------------------------------------

# frontend = Frontend(
#     f"myapp-{env}-frontend",
#     resource_group.name,
#     location,
#     api.api_url
# )


# # -------------------------------------------------------
# # Outputs
# # -------------------------------------------------------

# pulumi.export("frontendUrl", frontend.url)
# pulumi.export("apiUrl", api.api_url)
# pulumi.export("postgresHost", postgres.host)
# pulumi.export("resourceGroupName", resource_group.name)
# pulumi.export("keyVaultUri", keyvault.vault_uri)
# pulumi.export("staticWebAppToken", frontend.token)

# import pulumi
# import pulumi_azure_native as azure

# from components.network import Network
# from components.postgres import Postgres
# from components.api import ApiService
# from components.frontend import Frontend
# from components.keyvault import KeyVault

# config = pulumi.Config()
# env = config.require("environment")
# location = config.get("location") or "centralindia"

# # ------------------------
# # Resource Group
# # ------------------------
# resource_group = azure.resources.ResourceGroup(
#     f"myapp-{env}-rg",
#     location=location
# )

# # ------------------------
# # Network
# # ------------------------
# network = Network(
#     f"myapp-{env}-network",
#     resource_group.name,
#     location
# )

# # ------------------------
# # Key Vault
# # ------------------------
# keyvault = KeyVault(
#     f"myapp-{env}-kv",
#     resource_group.name,
#     location
# )

# # ------------------------
# # PostgreSQL Flexible Server
# # ------------------------
# postgres = Postgres(
#     f"myapp-{env}-db",
#     resource_group.name,
#     location,
#     network.subnet_id,
#     keyvault.db_password  # pass Pulumi secret directly
# )

# # ------------------------
# # FastAPI Backend
# # ------------------------
# api = ApiService(
#     f"myapp-{env}-api",
#     resource_group.name,
#     location,
#     postgres.host,
#     keyvault.db_password,   # use secret here
#     postgres.database_name, # DB name
#     keyvault.jwt_key
# )

# # ------------------------
# # React Frontend
# # ------------------------
# frontend = Frontend(
#     f"myapp-{env}-frontend",
#     resource_group.name,
#     location,
#     api.api_url
# )

# # ------------------------
# # Outputs
# # ------------------------
# pulumi.export("frontendUrl", frontend.url)
# pulumi.export("apiUrl", api.api_url)
# pulumi.export("postgresHost", postgres.host)
# pulumi.export("postgresDb", postgres.database_name)
# pulumi.export("resourceGroupName", resource_group.name)
# pulumi.export("keyVaultUri", keyvault.vault_uri)
# pulumi.export("staticWebAppToken", frontend.token)

# import pulumi
# import pulumi_azure_native as azure

# from components.network import Network
# from components.keyvault import KeyVault
# from components.postgres import Postgres
# from components.api import ApiService
# from components.frontend import Frontend

# config = pulumi.Config()
# env = config.require("environment")
# location = config.get("location") or "centralindia"

# # Resource Group
# rg = azure.resources.ResourceGroup(f"myapp-{env}-rg", location=location)

# # Network + Private DNS for Postgres
# network = Network(f"myapp-{env}-network", rg.name, location)

# # Key Vault
# keyvault = KeyVault(f"myapp-{env}-kv", rg.name, location)

# # PostgreSQL server
# postgres = Postgres(
#     f"myapp-{env}-db",
#     rg.name,
#     location,
#     network.subnet_id,
#     network.dns_zone_id,  # pass PrivateZone id
#     keyvault.db_password
# )

# # FastAPI backend
# api = ApiService(f"myapp-{env}-api", rg.name, location,
#                  postgres.host,
#                  keyvault.db_password,
#                  postgres.database_name,
#                  keyvault.jwt_key)

# # React frontend
# frontend = Frontend(f"myapp-{env}-frontend", rg.name, location, api.api_url)

# # Pulumi outputs
# pulumi.export("frontendUrl", frontend.url)
# pulumi.export("apiUrl", api.api_url)
# pulumi.export("postgresHost", postgres.host)
# pulumi.export("postgresDb", postgres.database_name)
# pulumi.export("resourceGroupName", rg.name)
# pulumi.export("keyVaultUri", keyvault.vault_uri)
# pulumi.export("staticWebAppToken", frontend.token)

import pulumi
import pulumi_azure_native as azure

from components.acr import ContainerRegistry
from components.network import Network
from components.keyvault import KeyVault
from components.postgres import Postgres
from components.api import ApiService
from components.frontend import Frontend

# Pulumi config
config = pulumi.Config()
location = config.get("location") or "centralindia"

# Environment
stack = pulumi.get_stack()

project = "myapp"
name_prefix = f"{project}-{stack}"

# Resource Group
rg = azure.resources.ResourceGroup(
    f"{name_prefix}-rg",
    location=location
)

# Container Registry
acr = ContainerRegistry(
    name_prefix.replace("-", ""),
    rg.name,
    location
)

# Network
network = Network(
    name_prefix,
    rg.name,
    location
)

# Key Vault
keyvault = KeyVault(
    name_prefix,
    rg.name,
    location
)

# PostgreSQL
postgres = Postgres(
    name_prefix,
    rg.name,
    location,
    network.db_subnet_id,
    network.dns_zone_id,
    keyvault.db_password,
    network.dns_link
)

# Frontend (React)
frontend = Frontend(
    name_prefix,
    rg.name,
    location
)

# API (FastAPI backend)
api = ApiService(
    name_prefix,
    rg.name,
    location,
    postgres.host,
    network.app_subnet_id,
    keyvault.db_password_secret_uri,
    keyvault.jwt_secret_uri,
    frontend.hostname,
    acr.login_server
)

# Key Vault access for API identity
azure.authorization.RoleAssignment(
    f"{name_prefix}-kv-access",
    scope=keyvault.vault.id,

    role_definition_id="/providers/Microsoft.Authorization/roleDefinitions/4633458b-17de-408a-b874-0445c86b69e6",

    principal_id=api.identity_principal_id,
    principal_type="ServicePrincipal",
)

# ACR Pull role for API identity
azure.authorization.RoleAssignment(
    f"{name_prefix}-acr-pull",
    scope=acr.registry.id,

    role_definition_id="/providers/Microsoft.Authorization/roleDefinitions/7f951dda-4ed3-4680-a7ca-43fe172d538d",

    principal_id=api.identity_principal_id,
    principal_type="ServicePrincipal",
)

# Pulumi Outputs
pulumi.export("environment", stack)
pulumi.export("frontendUrl", frontend.url)
pulumi.export("apiUrl", api.api_url)
pulumi.export("postgresHost", postgres.host)
pulumi.export("resourceGroupName", rg.name)
pulumi.export("keyVaultUri", keyvault.vault_uri)
pulumi.export("staticWebAppToken", frontend.deployment_token)
pulumi.export("acrLoginServer", acr.login_server)