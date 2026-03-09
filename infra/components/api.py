# from pulumi_azure_native import web

# def create_api(resource_group_name):

#     plan = web.AppServicePlan(
#         "fastapi-plan",
#         resource_group_name=resource_group_name,
#         sku={
#             "name": "B1",
#             "tier": "Basic"
#         },
#         kind="linux",
#         reserved=True
#     )

#     app = web.WebApp(
#         "fastapi-backend",
#         resource_group_name=resource_group_name,
#         server_farm_id=plan.id,
#         site_config={
#             "linux_fx_version": "PYTHON|3.10"
#         }
#     )

#     return app

# from pulumi_azure_native import web

# def create_api(resource_group_name, location):

#     plan = web.AppServicePlan(
#         "fastapi-plan",
#         resource_group_name=resource_group_name,
#         location=location,
#         sku={
#             "name": "B1",
#             "tier": "Basic"
#         },
#         kind="linux",
#         reserved=True
#     )

#     app = web.WebApp(
#         "fastapi-backend",
#         resource_group_name=resource_group_name,
#         location=location,
#         server_farm_id=plan.id,
#         site_config={
#             "linux_fx_version": "PYTHON|3.10"
#         }
#     )

#     return app
import pulumi
import pulumi_azure_native as azure


class ApiService:

    def __init__(self, name, rg, location, db_url, keyvault_uri):

        # App Service Plan
        plan = azure.web.AppServicePlan(
            f"{name}-plan",
            resource_group_name=rg,
            location=location,
            kind="linux",
            reserved=True,
            sku=azure.web.SkuDescriptionArgs(
                name="B1",
                tier="Basic"
            )
        )

        # Web App (FastAPI backend)
        app = azure.web.WebApp(
            name,
            resource_group_name=rg,   # ✅ fixed here
            location=location,
            server_farm_id=plan.id,

            site_config=azure.web.SiteConfigArgs(
                linux_fx_version="PYTHON|3.10",
                app_settings=[
                    azure.web.NameValuePairArgs(
                        name="DATABASE_URL",
                        value=db_url
                    ),
                    azure.web.NameValuePairArgs(
                        name="KEYVAULT_URI",
                        value=keyvault_uri
                    )
                ]
            )
        )

        # Output API URL
        self.api_url = pulumi.Output.concat(
            "https://",
            app.default_host_name
        )