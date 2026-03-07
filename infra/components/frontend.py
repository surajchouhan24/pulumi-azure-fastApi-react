# from pulumi_azure_native import web

# def create_frontend(resource_group_name):
#     site = web.StaticSite(
#         "react-frontend",
#         resource_group_name=resource_group_name,
#         location="eastasia",
#         sku=web.SkuDescriptionArgs(
#             name="Free",
#             tier="Free"
#         ),
#         repository_url="https://github.com/raythurman2386/fastapi-react-starter",
#         branch="main",
#         build_properties=web.StaticSiteBuildPropertiesArgs(
#             app_location="frontend",
#             api_location="backend",
#             output_location="build"
#         )
#     )
    
#     return site
# from pulumi_azure_native import web

# def create_frontend(resource_group_name):
#     site = web.StaticSite(
#         "react-frontend",
#         resource_group_name=resource_group_name,
#         location="eastasia",  # Choose a valid region for Static Web Apps
#         sku={
#             "name": "Free",
#             "tier": "Free"
#         },
#         repository_url="https://github.com/raythurman2386/fastapi-react-starter.git",  # your repo
#         branch="main",  # your default branch
#         # Optional: you can define build properties if needed
#         build_properties=web.StaticSiteBuildPropertiesArgs(
#             app_location="/frontend",  # path inside repo to your React app
#             api_location="/backend",   # if you want Azure Functions (optional)
#             output_location="build"    # default React build folder
#         )
#     )
#     return site

from pulumi_azure_native import web

def create_frontend(resource_group_name, location):

    site = web.StaticSite(
        "react-frontend",
        resource_group_name=resource_group_name,
        location=location,

        sku=web.SkuDescriptionArgs(
            name="Free",
            tier="Free"
        ),

        repository_url="https://github.com/surajchouhan24/react-fastApi-postgres.git",
        branch="main",

        build_properties=web.StaticSiteBuildPropertiesArgs(
            app_location="/frontend",
            api_location="",
            output_location="build"
        )
    )

    return site