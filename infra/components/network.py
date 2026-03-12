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


import pulumi_azure_native as azure


class Network:
    def __init__(self, name, rg, location, private_dns_zone_name=None):
        # Virtual network
        vnet = azure.network.VirtualNetwork(
            f"{name}-vnet",
            resource_group_name=rg,
            location=location,
            address_space=azure.network.AddressSpaceArgs(
                address_prefixes=["10.0.0.0/16"]
            )
        )

        # Subnet for App Service / DB
        subnet = azure.network.Subnet(
            f"{name}-subnet",
            resource_group_name=rg,
            virtual_network_name=vnet.name,
            address_prefix="10.0.1.0/24",
            delegations=[azure.network.DelegationArgs(
                name="db-delegation",
                service_name="Microsoft.DBforPostgreSQL/flexibleServers"
            )],
        )

        self.vnet_id = vnet.id
        self.subnet_id = subnet.id

        # Optional Private DNS
        if private_dns_zone_name:
            dns_zone = azure.network.PrivateZone(
                f"{name}-dns",
                resource_group_name=rg,
                location="global",
                zone_name=private_dns_zone_name
            )
            self.dns_zone_id = dns_zone.id
        else:
            self.dns_zone_id = None