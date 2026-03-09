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

        # App Settings (DB + JWT + ENV)
        app_settings = [
            azure.web.NameValuePairArgs(name="DATABASE_URL", value=db_url),
            azure.web.NameValuePairArgs(name="ENVIRONMENT", value="production"),
            azure.web.NameValuePairArgs(name="KEYVAULT_URI", value=keyvault_uri),
            # Inject secrets from KeyVault
            # For example, if you have JWT_SECRET
            azure.web.NameValuePairArgs(name="JWT_KEY", value=pulumi.Config().get_secret("jwtKey") or pulumi.Output.secret("dev-jwt-secret"))
        ]

        # Web App
        app = azure.web.WebApp(
            name,
            resource_group_name=rg,
            location=location,
            server_farm_id=plan.id,
            site_config=azure.web.SiteConfigArgs(
                linux_fx_version="PYTHON|3.12",  # Use latest supported Python
                app_settings=app_settings,
                always_on=True
            ),
            https_only=True
        )

        # 🔹 Startup command: Gunicorn + Uvicorn
        # Replace `app.main:app` with your FastAPI ASGI app path
        app_identity = azure.web.WebAppApplicationSettings(
            name=name,
            resource_group_name=rg,
            properties={"startupCommand": "gunicorn -w 4 -k uvicorn.workers.UvicornWorker app.main:app --bind 0.0.0.0:8000"}
        )

        # API URL output
        self.api_url = pulumi.Output.concat("https://", app.default_host_name)