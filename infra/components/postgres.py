# from pulumi_azure_native import dbforpostgresql


# def create_postgres(resource_group_name, location):

#     server = dbforpostgresql.Server(
#         "fastapi-postgres",

#         resource_group_name=resource_group_name,
#         location=location,

#         administrator_login="pgadmin",
#         administrator_login_password="StrongPassword123!",

#         version="14",
#             storage={
#             "storage_size_gb": 32
#         },

#         sku={
#             "name": "Standard_B1ms",
#             "tier": "Burstable"
#         }
#     )

#     return server
# from pulumi_azure_native import dbforpostgresql

# def create_postgres(resource_group_name, ):

#     server = dbforpostgresql.FlexibleServer(
#         "fastapi-postgres",

#         resource_group_name=resource_group_name,
#         location=location,

#         administrator_login="pgadmin",
#         administrator_login_password="StrongPassword123!",

#         version="14",

#         sku=dbforpostgresql.SkuArgs(
#             name="Standard_B1ms",
#             tier="Burstable"
#         ),

#         storage=dbforpostgresql.StorageArgs(
#             storage_size_gb=32
#         )
#     )

#     return server
import pulumi
import pulumi_azure_native as azure

class Postgres:

    def __init__(self, name, rg, location, subnet_id, keyvault_uri):

        password = pulumi.Config().require_secret("dbPassword")

        server = azure.dbforpostgresql.Server(
            name,
            resource_group_name=rg,
            location=location,

            administrator_login="postgres",
            administrator_login_password=password,

            version="14",

            sku=azure.dbforpostgresql.SkuArgs(
                name="Standard_B1ms",
                tier="Burstable"
            ),

            storage=azure.dbforpostgresql.StorageArgs(
                storage_size_gb=32
            )
        )

        self.host = server.fully_qualified_domain_name

        self.db_url = pulumi.Output.concat(
            "postgresql+asyncpg://postgres:",
            password,
            "@",
            server.fully_qualified_domain_name,
            ":5432/postgres"
        )