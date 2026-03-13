# from pulumi_azure_native import network

# def create_network(resource_group_name):

#     vnet = network.VirtualNetwork(
#         "app-vnet",
#         resource_group_name=resource_group_name,
#         address_space={
#             "address_prefixes": ["10.0.0.0/16"],
#         }
#     )

#     subnet = network.Subnet(
#         "app-subnet",
#         resource_group_name=resource_group_name,
#         virtual_network_name=vnet.name,
#         address_prefix="10.0.1.0/24"
#     )

#     return vnet, subnet

# from pulumi_azure_native import network

# def create_network(resource_group_name, location):

#     vnet = network.VirtualNetwork(
#         "app-vnet",
#         resource_group_name=resource_group_name,
#         location=location,
#         address_space={
#             "address_prefixes": ["10.0.0.0/16"],
#         }
#     )

#     subnet = network.Subnet(
#         "app-subnet",
#         resource_group_name=resource_group_name,
#         virtual_network_name=vnet.name,
#         address_prefix="10.0.1.0/24"
#     )

#     return vnet, subnet

# import pulumi_azure_native as azure


# class Network:

#     def __init__(self, name, rg, location):

#         vnet = azure.network.VirtualNetwork(
#             f"{name}-vnet",
#             resource_group_name=rg,
#             location=location,
#             address_space=azure.network.AddressSpaceArgs(
#                 address_prefixes=["10.0.0.0/16"]
#             ),
#         )

#         subnet = azure.network.Subnet(
#             f"{name}-subnet",
#             resource_group_name=rg,
#             virtual_network_name=vnet.name,
#             address_prefix="10.0.1.0/24",
#         )

#         self.subnet_id = subnet.id


# import pulumi_azure_native as azure


# class Network:
#     def __init__(self, name, rg, location, private_dns_zone_name=None):
#         # Virtual network
#         vnet = azure.network.VirtualNetwork(
#             f"{name}-vnet",
#             resource_group_name=rg,
#             location=location,
#             address_space=azure.network.AddressSpaceArgs(
#                 address_prefixes=["10.0.0.0/16"]
#             )
#         )

#         # Subnet for App Service / DB
#         subnet = azure.network.Subnet(
#             f"{name}-subnet",
#             resource_group_name=rg,
#             virtual_network_name=vnet.name,
#             address_prefix="10.0.1.0/24",
#             delegations=[azure.network.DelegationArgs(
#                 name="db-delegation",
#                 service_name="Microsoft.DBforPostgreSQL/flexibleServers"
#             )],
#         )

#         self.vnet_id = vnet.id
#         self.subnet_id = subnet.id

#         # Optional Private DNS
#         if private_dns_zone_name:
#             dns_zone = azure.network.PrivateZone(
#                 f"{name}-dns",
#                 resource_group_name=rg,
#                 location="global",
#                 zone_name=private_dns_zone_name
#             )
#             self.dns_zone_id = dns_zone.id
#         else:
#             self.dns_zone_id = None

# network.py
# import pulumi_azure_native as azure
# from pulumi_azure_native import privatedns

# class Network:
#     def __init__(self, name, rg, location):
#         # Virtual network
#         vnet = azure.network.VirtualNetwork(
#             f"{name}-vnet",
#             resource_group_name=rg,
#             location=location,
#             address_space=azure.network.AddressSpaceArgs(
#                 address_prefixes=["10.0.0.0/16"]
#             )
#         )

#         # Subnet for App Service / DB
#         subnet = azure.network.Subnet(
#             f"{name}-subnet",
#             resource_group_name=rg,
#             virtual_network_name=vnet.name,
#             address_prefix="10.0.1.0/24",
#             delegations=[azure.network.DelegationArgs(
#                 name="db-delegation",
#                 service_name="Microsoft.DBforPostgreSQL/flexibleServers"
#             )],
#         )

#         self.vnet_id = vnet.id
#         self.subnet_id = subnet.id

#         # Private DNS zone for Flexible PostgreSQL
#         dns_zone = privatedns.PrivateZone(
#             f"{name}-dns",
#             resource_group_name=rg,
#             location="global",
#             private_zone_name="privatelink.postgres.database.azure.com"  # correct parameter
#         )
#         self.dns_zone_id = dns_zone.id


import pulumi_azure_native as azure
from pulumi_azure_native import privatedns


class Network:
    def __init__(self, name, rg, location):

        # Virtual Network
        vnet = azure.network.VirtualNetwork(
            f"{name}-vnet",
            resource_group_name=rg,
            location=location,
            address_space=azure.network.AddressSpaceArgs(
                address_prefixes=["10.0.0.0/16"]
            )
        )

        # App Service subnet
        app_subnet = azure.network.Subnet(
            f"{name}-app-subnet",
            resource_group_name=rg,
            virtual_network_name=vnet.name,
            address_prefix="10.0.1.0/24",
            delegations=[
                azure.network.DelegationArgs(
                    name="appserviceDelegation",
                    service_name="Microsoft.Web/serverFarms"
                )
            ],
        )

        # PostgreSQL subnet
        db_subnet = azure.network.Subnet(
            f"{name}-db-subnet",
            resource_group_name=rg,
            virtual_network_name=vnet.name,
            address_prefix="10.0.2.0/24",
            delegations=[
                azure.network.DelegationArgs(
                    name="postgresDelegation",
                    service_name="Microsoft.DBforPostgreSQL/flexibleServers"
                )
            ],
        )

        # Private DNS zone for PostgreSQL
        dns_zone = privatedns.PrivateZone(
            f"{name}-pg-dns",
            resource_group_name=rg,
            location="global",
            private_zone_name="privatelink.postgres.database.azure.com",
        )

        # Export outputs
        self.vnet_id = vnet.id
        self.app_subnet_id = app_subnet.id
        self.db_subnet_id = db_subnet.id
        self.dns_zone_id = dns_zone.id