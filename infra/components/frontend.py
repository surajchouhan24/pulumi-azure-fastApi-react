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

# from pulumi_azure_native import web

# def create_frontend(resource_group_name, location):

#     site = web.StaticSite(
#         "react-frontend",
#         resource_group_name=resource_group_name,
#         location=location,

#         sku=web.SkuDescriptionArgs(
#             name="Free",
#             tier="Free"
#         ),

#         repository_url="https://github.com/surajchouhan24/react-fastApi-postgres.git",
#         branch="main",

#         build_properties=web.StaticSiteBuildPropertiesArgs(
#             app_location="/frontend",
#             api_location="",
#             output_location="build"
#         )
#     )

#     return site

# import pulumi_azure_native as azure

# class Frontend:

#     def __init__(self, name, rg, location, api_url):

#         swa = azure.web.StaticSite(
#             name,
#             resource_group_name=rg,
#             location=location,
#             sku=azure.web.SkuDescriptionArgs(
#                 name="Free",
#                 tier="Free"
#             ),
#             repository_url="https://github.com/surajchouhan24/pulumi-azure-fastApi-react.git",
#             branch="main",
            
#         )

#         self.url = swa.default_hostname

# import pulumi
# import pulumi_azure_native as azure


# class Frontend:

#     def __init__(self, name, rg, location):

#         swa = azure.web.StaticSite(
#             f"{name}-frontend",
#             resource_group_name=rg,
#             location=location,

#             sku=azure.web.SkuDescriptionArgs(
#                 name="Free",
#                 tier="Free"
#             ),

#             repository_url="https://github.com/surajchouhan24/pulumi-azure-fastApi-react.git",

#             branch="main",

#             build_properties=azure.web.StaticSiteBuildPropertiesArgs(
#                 app_location="fastapi-react-starter/frontend",
#                 api_location="",
#                 app_artifact_location="dist",
#                 app_build_command="npm run build"
#             )
#         )

#         self.url = pulumi.Output.concat(
#             "https://",
#             swa.default_hostname
#         )

import pulumi
import pulumi_azure_native as azure


class Frontend:

    def __init__(self, name, rg, location, api_url):

        swa = azure.web.StaticSite(
            f"{name}-frontend",
            resource_group_name=rg,
            location=location,

            sku=azure.web.SkuDescriptionArgs(
                name="Free",
                tier="Free"
            ),

            repository_url="https://github.com/surajchouhan24/pulumi-azure-fastApi-react.git",
            branch="main",

            build_properties=azure.web.StaticSiteBuildPropertiesArgs(
                app_location="fastapi-react-starter/frontend",
                api_location="",
                app_artifact_location="dist",
                app_build_command="npm run build",

                # # inject env variable into frontend build
                # environment_variables={
                #     "VITE_API_URL": api_url
                # }
            )
        )

        self.url = pulumi.Output.concat(
            "https://",
            swa.default_hostname
        )