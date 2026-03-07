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

from pulumi_azure_native import network

def create_network(resource_group_name, location):

    vnet = network.VirtualNetwork(
        "app-vnet",
        resource_group_name=resource_group_name,
        location=location,
        address_space={
            "address_prefixes": ["10.0.0.0/16"],
        }
    )

    subnet = network.Subnet(
        "app-subnet",
        resource_group_name=resource_group_name,
        virtual_network_name=vnet.name,
        address_prefix="10.0.1.0/24"
    )

    return vnet, subnet