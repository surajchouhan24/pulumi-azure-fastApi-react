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

# import pulumi
# import pulumi_azure_native as azure

# class Postgres:
#     def __init__(self, name, rg, location, subnet_id):

#         password = "StrongPassword123!"

#         server = azure.dbforpostgresql.Server(
#             name,
#             resource_group_name=rg,
#             location=location,
#             administrator_login="postgres",
#             administrator_login_password=password,
#             version="14",
#             sku=azure.dbforpostgresql.SkuArgs(
#                 name="Standard_B1ms",
#                 tier="Burstable",
#             ),
#             storage=azure.dbforpostgresql.StorageArgs(
#                 storage_size_gb=32
#             ),
#         )

#         # allow Azure services
#         azure.dbforpostgresql.FirewallRule(
#             f"{name}-allow-azure",
#             resource_group_name=rg,
#             server_name=server.name,
#             start_ip_address="0.0.0.0",
#             end_ip_address="0.0.0.0",
#         )

#         self.host = server.fully_qualified_domain_name
#         self.password = password

# import pulumi
# import pulumi_azure_native as azure


# class Postgres:

#     def __init__(self, name, rg, location, subnet_id, password):

#         server = azure.dbforpostgresql.Server(
#             name,

#             resource_group_name=rg,
#             location=location,

#             administrator_login="postgres",
#             administrator_login_password=password,

#             version="15",

#             sku=azure.dbforpostgresql.SkuArgs(
#                 name="Standard_B1ms",
#                 tier="Burstable",
#             ),
#         )

#         database = azure.dbforpostgresql.Database(
#             f"{name}-db",

#             resource_group_name=rg,
#             server_name=server.name,

#             charset="UTF8",
#             collation="en_US.UTF8",
#         )

#         azure.dbforpostgresql.FirewallRule(
#             f"{name}-allow-azure",

#             resource_group_name=rg,
#             server_name=server.name,

#             start_ip_address="0.0.0.0",
#             end_ip_address="0.0.0.0",
#         )

#         self.host = server.fully_qualified_domain_name


# import pulumi
# import pulumi_azure_native as azure


# class Postgres:

#     def __init__(self, name, rg, location, subnet_id, password_secret):

#         # Flexible server
#         server = azure.dbforpostgresql.Server(
#             name,
#             resource_group_name=rg,
#             location=location,
#             administrator_login="postgres",
#             administrator_login_password=password_secret,
#             version="15",
#             sku=azure.dbforpostgresql.SkuArgs(
#                 name="Standard_B1ms",
#                 tier="Burstable",
#             ),
#         )

#         # Database
#         database = azure.dbforpostgresql.Database(
#             f"{name}-db",
#             resource_group_name=rg,
#             server_name=server.name,
#             charset="UTF8",
#             collation="en_US.UTF8",
#         )

#         # Firewall rule to allow Azure services
#         azure.dbforpostgresql.FirewallRule(
#             f"{name}-allow-azure",
#             resource_group_name=rg,
#             server_name=server.name,
#             start_ip_address="0.0.0.0",
#             end_ip_address="0.0.0.0"
#         )

#         self.host = server.fully_qualified_domain_name
#         self.database_name = database.name


# import pulumi
# import pulumi_azure_native as azure

# class Postgres:

#     def __init__(self, name, rg, location, subnet_id, vnet_id, password_secret):
#         stack = pulumi.get_stack()
#         admin_user = "pgadmin"
#         database_name = "appdb"

#         # ------------------------
#         # Private DNS Zone for PostgreSQL
#         # ------------------------
#         dns_zone = azure.privatedns.PrivateZone(
#             f"{name}-pg-dns",
#             resource_group_name=rg,
#             private_zone_name="privatelink.postgres.database.azure.com",
#             location="global"
#         )

#         # ------------------------
#         # Link VNet to DNS Zone
#         # ------------------------
#         azure.privatedns.VirtualNetworkLink(
#             f"{name}-dns-link",
#             resource_group_name=rg,
#             private_zone_name=dns_zone.name,
#             location="global",
#             virtual_network=azure.privatedns.SubResourceArgs(
#                 id=vnet_id
#             ),
#             registration_enabled=False
#         )

#         # ------------------------
#         # PostgreSQL Server
#         # ------------------------
#         server = azure.dbforpostgresql.Server(
#             f"{name}-pg",
#             resource_group_name=rg,
#             location=location,
#             administrator_login=admin_user,
#             administrator_login_password=password_secret,
#             version="15",
#             sku=azure.dbforpostgresql.SkuArgs(
#                 name="Standard_B1ms" if stack != "production" else "Standard_D2s_v3",
#                 tier="Burstable" if stack != "production" else "GeneralPurpose",
#             ),
#             # storage=dbforpostgresql.StorageArgs(
#             #     storage_size_gb=32
#             # ),
#             # storage_profile=azure.dbforpostgresql.StorageProfileArgs(
#             #     storage_mb=32768 if stack != "production" else 131072,
#             #     backup_retention_days=7,
#             #     geo_redundant_backup="Disabled"
#             # ),
#             # Fallback for dev/test if FlexibleServer is not available:
#             public_network_access="Enabled"
#         )

#         # ------------------------
#         # Database
#         # ------------------------
#         database = azure.dbforpostgresql.Database(
#             f"{name}-db",
#             resource_group_name=rg,
#             server_name=server.name,
#             charset="UTF8",
#             collation="en_US.UTF8"
#         )

#         # ------------------------
#         # Firewall rule to allow Azure services
#         # ------------------------
#         azure.dbforpostgresql.FirewallRule(
#             f"{name}-allow-azure",
#             resource_group_name=rg,
#             server_name=server.name,
#             start_ip_address="0.0.0.0",
#             end_ip_address="0.0.0.0"
#         )

#         # Outputs
#         self.host = server.fully_qualified_domain_name
#         self.database_name = database.name
# import pulumi
# import pulumi_azure_native as azure
# from pulumi_azure_native.dbforpostgresql import HighAvailabilityArgs, StorageArgs, BackupArgs, SkuArgs

# class Postgres:
#     def __init__(self, name, rg, location, subnet_id, vnet_id, password_secret, private_dns_zone_id=None):
#         """
#         Create an Azure PostgreSQL Flexible Server with a database.
#         Includes:
#             - Firewall rule to allow Azure services
#             - 32GB storage, 7-day backups
#             - Disabled high availability for dev/test
#         """
#         stack = pulumi.get_stack()
#         admin_user = "pgadmin"

#         # PostgreSQL Flexible Server
#         server = azure.dbforpostgresql.Server(
#             f"{name}-pg",
#             resource_group_name=rg,
#             location=location,
#             administrator_login=admin_user,
#             administrator_login_password=password_secret,
#             version="15",
#             sku=SkuArgs(
#                 name="Standard_B1ms",
#                 tier="Burstable"
#             ),
#             storage=StorageArgs(
#                 storage_size_gb=32
#             ),
#             backup=BackupArgs(
#                 backup_retention_days=7
#             ),
#             high_availability=HighAvailabilityArgs(
#                 mode="Disabled"
#             ),
#             network=azure.dbforpostgresql.NetworkArgs(
#                 delegated_subnet_resource_id=subnet_id,
#                 private_dns_zone_arm_resource_id=private_dns_zone_id
#             ),
#             # public_network_access="Enabled"  # allow access from Azure services
#         )

#         # Firewall rule: allow Azure services
#         azure.dbforpostgresql.FirewallRule(
#             f"{name}-allow-azure",
#             resource_group_name=rg,
#             server_name=server.name,
#             start_ip_address="0.0.0.0",
#             end_ip_address="0.0.0.0"
#         )

#         # Database
#         database = azure.dbforpostgresql.Database(
#             f"{name}-db",
#             resource_group_name=rg,
#             server_name=server.name,
#             charset="UTF8",
#             collation="en_US.UTF8"
#         )

#         # Outputs
#         self.host = server.fully_qualified_domain_name
#         self.database_name = database.name


# postgres.py
# import pulumi_azure_native as azure
# from pulumi_azure_native.dbforpostgresql import HighAvailabilityArgs, StorageArgs, BackupArgs, SkuArgs

# class Postgres:
#     def __init__(self, name, rg, location, subnet_id, vnet_id, password_secret, private_dns_zone_id):
#         admin_user = "pgadmin"

#         server = azure.dbforpostgresql.Server(
#             f"{name}-pg",
#             resource_group_name=rg,
#             location=location,
#             administrator_login=admin_user,
#             administrator_login_password=password_secret,
#             version="15",
#             sku=SkuArgs(name="Standard_B1ms", tier="Burstable"),
#             storage=StorageArgs(storage_size_gb=32),
#             backup=BackupArgs(backup_retention_days=7),
#             high_availability=HighAvailabilityArgs(mode="Disabled"),
#             network=azure.dbforpostgresql.NetworkArgs(
#                 delegated_subnet_resource_id=subnet_id,
#                 private_dns_zone_arm_resource_id=private_dns_zone_id  # <-- required
#             ),
#             public_network_access="Enabled"
#         )

#         # Firewall rule: allow Azure services
#         azure.dbforpostgresql.FirewallRule(
#             f"{name}-allow-azure",
#             resource_group_name=rg,
#             server_name=server.name,
#             start_ip_address="0.0.0.0",
#             end_ip_address="0.0.0.0"
#         )

#         # Database
#         database = azure.dbforpostgresql.Database(
#             f"{name}-db",
#             resource_group_name=rg,
#             server_name=server.name,
#             charset="UTF8",
#             collation="en_US.UTF8"
#         )

#         self.host = server.fully_qualified_domain_name
#         self.database_name = database.name
# import pulumi_azure_native as azure
# from pulumi_azure_native.dbforpostgresql import HighAvailabilityArgs, StorageArgs, BackupArgs, SkuArgs, NetworkArgs

# class Postgres:
#     def __init__(self, name, rg, location, subnet_id, private_dns_zone_id, password_secret):
#         admin_user = "pgadmin"

#         # PostgreSQL Flexible Server
#         # server = azure.dbforpostgresql.Server(
#         #     f"{name}-pg",
#         #     resource_group_name=rg,
#         #     location=location,
#         #     administrator_login=admin_user,
#         #     administrator_login_password=password_secret,
#         #     version="15",
#         #     sku=SkuArgs(
#         #         name="Standard_B1ms",
#         #         tier="Burstable"
#         #     ),
#         #     storage=StorageArgs(
#         #         storage_size_gb=32
#         #     ),
#         #     backup=BackupArgs(
#         #         backup_retention_days=7
#         #     ),
#         #     high_availability=HighAvailabilityArgs(
#         #         mode="Disabled"
#         #     ),
#         #     network=NetworkArgs(
#         #         delegated_subnet_resource_id=subnet_id,
#         #         private_dns_zone_arm_resource_id=private_dns_zone_id  # use argument here
#         #     ),
#         # )
#         server = azure.dbforpostgresql.Server(
#             f"{name}-pg",
#             resource_group_name=rg,
#             location=location,
#             administrator_login=admin_user,
#             administrator_login_password=password_secret,
#             version="15",
#             sku=SkuArgs(name="Standard_B1ms", tier="Burstable"),
#             storage=StorageArgs(storage_size_gb=32),
#             backup=BackupArgs(backup_retention_days=7),
#             high_availability=HighAvailabilityArgs(mode="Disabled"),
#             ssl_enforcement="Enabled"
#             # public_network_access="Enabled"  # <- remove network block entirely
#         )

#         # Firewall rule: allow Azure services
#         azure.dbforpostgresql.FirewallRule(
#             f"{name}-allow-azure",
#             resource_group_name=rg,
#             server_name=server.name,
#             start_ip_address="0.0.0.0",
#             end_ip_address="0.0.0.0"
#         )

#         # Database
#         database = azure.dbforpostgresql.Database(
#             f"{name}-db",
#             resource_group_name=rg,
#             server_name=server.name,
#             charset="UTF8",
#             collation="en_US.UTF8"
#         )

#         # Outputs
#         self.host = server.fully_qualified_domain_name
#         self.database_name = database.name


import pulumi_azure_native as azure
from pulumi_azure_native.dbforpostgresql import (
    HighAvailabilityArgs,
    StorageArgs,
    BackupArgs,
    SkuArgs,
    NetworkArgs,
)


class Postgres:
    def __init__(self, name, rg, location, subnet_id, private_dns_zone_id, password_secret):

        admin_user = "pgadmin"
        database_name = "appdb"

        # PostgreSQL Flexible Server
        server = azure.dbforpostgresql.Server(
            f"{name}-pg",
            resource_group_name=rg,
            location=location,

            administrator_login=admin_user,
            administrator_login_password=password_secret,

            version="15",

            sku=SkuArgs(
                name="Standard_B1ms",
                tier="Burstable",
            ),

            storage=StorageArgs(
                storage_size_gb=32
            ),

            backup=BackupArgs(
                backup_retention_days=7
            ),

            high_availability=HighAvailabilityArgs(
                mode="Disabled"
            ),

            # 🔑 Private networking
            network=NetworkArgs(
                delegated_subnet_resource_id=subnet_id,
                private_dns_zone_arm_resource_id=private_dns_zone_id,
            ),

            # disable public internet access
            # public_network_access="Disabled",
        )

        # Database
        database = azure.dbforpostgresql.Database(
            f"{name}-db",
            resource_group_name=rg,
            server_name=server.name,
            database_name=database_name,
            charset="UTF8",
            collation="en_US.UTF8",
        )

        # Outputs
        self.host = server.fully_qualified_domain_name
        self.database_name = database.name