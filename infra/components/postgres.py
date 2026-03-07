from pulumi_azure_native import dbforpostgresql


def create_postgres(resource_group_name, location):

    server = dbforpostgresql.Server(
        "fastapi-postgres",

        resource_group_name=resource_group_name,
        location=location,

        administrator_login="pgadmin",
        administrator_login_password="StrongPassword123!",

        version="14",
            storage={
            "storage_size_gb": 32
        },

        sku={
            "name": "Standard_B1ms",
            "tier": "Burstable"
        }
    )

    return server
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