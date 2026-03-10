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
    def __init__(self, name, rg, location, subnet_id):

        password = "StrongPassword123!"

        server = azure.dbforpostgresql.Server(
            name,
            resource_group_name=rg,
            location=location,
            administrator_login="postgres",
            administrator_login_password=password,
            version="14",
            sku=azure.dbforpostgresql.SkuArgs(
                name="Standard_B1ms",
                tier="Burstable",
            ),
            storage=azure.dbforpostgresql.StorageArgs(
                storage_size_gb=32
            ),
        )

        # allow Azure services
        azure.dbforpostgresql.FirewallRule(
            f"{name}-allow-azure",
            resource_group_name=rg,
            server_name=server.name,
            start_ip_address="0.0.0.0",
            end_ip_address="0.0.0.0",
        )

        self.host = server.fully_qualified_domain_name
        self.password = password