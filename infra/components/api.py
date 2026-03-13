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
# import pulumi
# import pulumi_azure_native as azure


# class ApiService:

#     def __init__(self, name, rg, location, db_url, keyvault_uri):

#         # App Service Plan
#         plan = azure.web.AppServicePlan(
#             f"{name}-plan",
#             resource_group_name=rg,
#             location=location,
#             kind="linux",
#             reserved=True,
#             sku=azure.web.SkuDescriptionArgs(
#                 name="B1",
#                 tier="Basic"
#             )
#         )

#         # Web App (FastAPI backend)
#         app = azure.web.WebApp(
#             name,
#             resource_group_name=rg,   # ✅ fixed here
#             location=location,
#             server_farm_id=plan.id,

#             site_config=azure.web.SiteConfigArgs(
#                 linux_fx_version="PYTHON|3.10",
#                 app_settings=[
#                     azure.web.NameValuePairArgs(
#                         name="DATABASE_URL",
#                         value=db_url
#                     ),
#                     azure.web.NameValuePairArgs(
#                         name="KEYVAULT_URI",
#                         value=keyvault_uri
#                     )
#                 ]
#             )
#         )

#         # Output API URL
#         self.api_url = pulumi.Output.concat(
#             "https://",
#             app.default_host_name
#         )

# import pulumi
# import pulumi_azure_native as azure


# class ApiService:

#     def __init__(self, name, rg, location, postgres_host):

#         plan = azure.web.AppServicePlan(
#             f"{name}-plan",
#             resource_group_name=rg,
#             location=location,
#             kind="linux",
#             reserved=True,
#             sku=azure.web.SkuDescriptionArgs(
#                 name="B1",
#                 tier="Basic",
#             ),
#         )

#         app = azure.web.WebApp(
#             f"{name}-api",
#             resource_group_name=rg,
#             location=location,
#             server_farm_id=plan.id,

#             site_config=azure.web.SiteConfigArgs(
#                 linux_fx_version="DOCKER|docker.io/surajchauhan24/fastapi-backend:latest",
#                 always_on=True,

#                 app_settings=[
#                     azure.web.NameValuePairArgs(name="DB_HOST", value=postgres_host),
#                     azure.web.NameValuePairArgs(name="DB_USER", value="postgres"),
#                     azure.web.NameValuePairArgs(name="DB_PASSWORD", value="StrongPassword123!"),
#                     azure.web.NameValuePairArgs(name="DB_NAME", value="postgres"),
#                     azure.web.NameValuePairArgs(name="DB_PORT", value="5432"),
#                     azure.web.NameValuePairArgs(name="WEBSITES_PORT", value="8000"),
#                     azure.web.NameValuePairArgs(name="ENVIRONMENT", value="production"),
#                     azure.web.NameValuePairArgs(name="JWT_SIGNING_KEY", value="dummy"),
#                 ],
#             ),
#         )

#         self.api_url = pulumi.Output.concat(
#             "https://",
#             app.default_host_name
#         )

# import pulumi
# import pulumi_azure_native as azure


# class ApiService:

#     def __init__(self, name, rg, location, postgres_host, jwt_key):

#         config = pulumi.Config()
#         env = config.require("environment")

#         sku_name = "P1v3" if env == "production" else "B1"

#         plan = azure.web.AppServicePlan(
#             f"{name}-plan",
#             resource_group_name=rg,
#             location=location,
#             kind="linux",
#             reserved=True,

#             sku=azure.web.SkuDescriptionArgs(
#                 name=sku_name,
#                 tier="Basic",
#             ),
#         )

#         app = azure.web.WebApp(
#             f"{name}-api",
#             resource_group_name=rg,
#             location=location,

#             server_farm_id=plan.id,

#             identity=azure.web.ManagedServiceIdentityArgs(
#                 type="SystemAssigned"
#             ),

#             site_config=azure.web.SiteConfigArgs(

#                 linux_fx_version="DOCKER|docker.io/surajchauhan24/fastapi-backend:latest",

#                 always_on=True,

#                 app_settings=[

#                     azure.web.NameValuePairArgs(
#                         name="DATABASE_URL",
#                         value=pulumi.Output.concat(
#                             "postgresql://postgres:",
#                             "password",
#                             "@",
#                             postgres_host,
#                             ":5432/appdb"
#                         )
#                     ),

#                     azure.web.NameValuePairArgs(
#                         name="JWT_SIGNING_KEY",
#                         value=jwt_key
#                     ),

#                     azure.web.NameValuePairArgs(
#                         name="ENVIRONMENT",
#                         value=env
#                     ),

#                     azure.web.NameValuePairArgs(
#                         name="WEBSITES_PORT",
#                         value="8000"
#                     ),
#                 ],
#             ),
#         )

#         self.api_url = pulumi.Output.concat(
#             "https://",
#             app.default_host_name
#         )

# import pulumi
# import pulumi_azure_native as azure


# class ApiService:

#     def __init__(self, name, rg, location, postgres_host, postgres_password, db_name, jwt_key):

#         config = pulumi.Config()
#         env = config.require("environment")

#         sku_name = "P1v3" if env == "production" else "B1"

#         # App Service Plan
#         plan = azure.web.AppServicePlan(
#             f"{name}-plan",
#             resource_group_name=rg,
#             location=location,
#             kind="linux",
#             reserved=True,
#             sku=azure.web.SkuDescriptionArgs(
#                 name=sku_name,
#                 tier="Basic",
#             ),
#         )

#         # Web App
#         app = azure.web.WebApp(
#             f"{name}-api",
#             resource_group_name=rg,
#             location=location,
#             server_farm_id=plan.id,
#             identity=azure.web.ManagedServiceIdentityArgs(
#                 type="SystemAssigned"
#             ),
#             site_config=azure.web.SiteConfigArgs(
#                 linux_fx_version="DOCKER|docker.io/surajchauhan24/fastapi-backend:latest",
#                 always_on=True,
#                 app_settings=[
#                     azure.web.NameValuePairArgs(
#                         name="DATABASE_URL",
#                         value=pulumi.Output.concat(
#                             "postgresql://postgres:",
#                             postgres_password,
#                             "@",
#                             postgres_host,
#                             ":5432/",
#                             db_name
#                         )
#                     ),
#                     azure.web.NameValuePairArgs(
#                         name="JWT_SIGNING_KEY",
#                         value=jwt_key
#                     ),
#                     azure.web.NameValuePairArgs(
#                         name="ENVIRONMENT",
#                         value=env
#                     ),
#                     azure.web.NameValuePairArgs(
#                         name="WEBSITES_PORT",
#                         value="8000"
#                     ),
#                 ],
#             ),
#         )

#         self.api_url = pulumi.Output.concat("https://", app.default_host_name)

# import pulumi
# import pulumi_azure_native as azure

# class ApiService:
#     def __init__(self, name, rg, location, postgres_host, postgres_password, db_name, jwt_key):
#         env = pulumi.Config().require("environment")
#         sku_name = "P1v3" if env == "production" else "B1"

#         plan = azure.web.AppServicePlan(
#             f"{name}-plan",
#             resource_group_name=rg,
#             location=location,
#             kind="linux",
#             reserved=True,
#             sku=azure.web.SkuDescriptionArgs(name=sku_name, tier="Basic")
#         )

#         app = azure.web.WebApp(
#             f"{name}-api",
#             resource_group_name=rg,
#             location=location,
#             server_farm_id=plan.id,
#             identity=azure.web.ManagedServiceIdentityArgs(type="SystemAssigned"),
#             site_config=azure.web.SiteConfigArgs(
#                 linux_fx_version="DOCKER|docker.io/surajchauhan24/fastapi-backend:latest",
#                 always_on=True,
#                 app_settings=[
#                     azure.web.NameValuePairArgs(
#                         name="DATABASE_URL",
#                         value=pulumi.Output.concat(
#                             "postgresql://postgres:",
#                             postgres_password,
#                             "@",
#                             postgres_host,
#                             ":5432/",
#                             db_name
#                         )
#                     ),
#                     azure.web.NameValuePairArgs(name="JWT_SIGNING_KEY", value=jwt_key),
#                     azure.web.NameValuePairArgs(name="ENVIRONMENT", value=env),
#                     azure.web.NameValuePairArgs(name="WEBSITES_PORT", value="8000"),
#                 ]
#             )
#         )

#         self.api_url = pulumi.Output.concat("https://", app.default_host_name)

# import pulumi
# import pulumi_azure_native as azure


# class ApiService:

#     def __init__(self, name, rg, location, postgres_host, postgres_password, db_name, jwt_key):

#         config = pulumi.Config()
#         env = config.require("environment")

#         # Production vs Dev plan
#         if env == "production":
#             sku_name = "P1v3"
#             sku_tier = "PremiumV3"
#         else:
#             sku_name = "B1"
#             sku_tier = "Basic"

#         # App Service Plan
#         plan = azure.web.AppServicePlan(
#             f"{name}-plan",
#             resource_group_name=rg,
#             location=location,
#             kind="linux",
#             reserved=True,  # required for Linux containers
#             sku=azure.web.SkuDescriptionArgs(
#                 name=sku_name,
#                 tier=sku_tier,
#             ),
#         )

#         # Azure Postgres requires username format:
#         # user@servername
#         # Azure Postgres requires username@servername
#         db_user = postgres_host.apply(
#             lambda host: f"postgres@{host.split('.')[0]}"
#         )

#         # database_url = pulumi.Output.concat(
#         #     "postgresql://",
#         #     db_user,
#         #     ":",
#         #     postgres_password,
#         #     "@",
#         #     postgres_host,
#         #     ":5432/",
#         #     db_name,
#         # )
        
#         database_url = pulumi.Output.concat(
#             "postgresql+asyncpg://postgres:",
#             postgres_password,
#             "@",
#             postgres_host,
#             ":5432/",
#             db_name,
#             "?sslmode=require"
#         )

#         # Web App
#         app = azure.web.WebApp(
#             f"{name}-api",
#             resource_group_name=rg,
#             location=location,
#             server_farm_id=plan.id,

#             identity=azure.web.ManagedServiceIdentityArgs(
#                 type="SystemAssigned"
#             ),

#             site_config=azure.web.SiteConfigArgs(
#                 linux_fx_version="DOCKER|docker.io/surajchauhan24/fastapi-backend:latest",

#                 always_on=True,
                
#                 app_settings=[

#                     azure.web.NameValuePairArgs(
#                         name="DB_HOST",
#                         value=postgres_host
#                     ),

#                     azure.web.NameValuePairArgs(
#                         name="DB_PORT",
#                         value="5432"
#                     ),

#                     azure.web.NameValuePairArgs(
#                         name="DB_NAME",
#                         value=db_name
#                     ),

#                     azure.web.NameValuePairArgs(
#                         name="DB_USER",
#                         value="postgres"
#                     ),

#                     azure.web.NameValuePairArgs(
#                         name="DB_PASSWORD",
#                         value=postgres_password
#                     ),

#                     azure.web.NameValuePairArgs(
#                         name="ENVIRONMENT",
#                         value=env
#                     ),

#                     azure.web.NameValuePairArgs(
#                         name="JWT_SIGNING_KEY",
#                         value=jwt_key
#                     ),

#                     azure.web.NameValuePairArgs(
#                         name="WEBSITES_PORT",
#                         value="8000"
#                     ),

#                 ]

#                 # app_settings=[

#                 #     # Database connection
#                 #     azure.web.NameValuePairArgs(
#                 #         name="DATABASE_URL",
#                 #         value=database_url
#                 #     ),

#                 #     # JWT
#                 #     azure.web.NameValuePairArgs(
#                 #         name="JWT_SIGNING_KEY",
#                 #         value=jwt_key
#                 #     ),

#                 #     # Environment
#                 #     azure.web.NameValuePairArgs(
#                 #         name="ENVIRONMENT",
#                 #         value=env
#                 #     ),

#                 #     # Required for container apps
#                 #     azure.web.NameValuePairArgs(
#                 #         name="WEBSITES_PORT",
#                 #         value="8000"
#                 #     ),

#                 #     # Prevent Azure storage mount issues
#                 #     azure.web.NameValuePairArgs(
#                 #         name="WEBSITES_ENABLE_APP_SERVICE_STORAGE",
#                 #         value="false"
#                 #     ),

#                 #     # Faster container startup
#                 #     azure.web.NameValuePairArgs(
#                 #         name="DOCKER_ENABLE_CI",
#                 #         value="true"
#                 #     ),
#                 # ],
#             ),

#             https_only=True,
#         )

#         self.api_url = pulumi.Output.concat(
#             "https://",
#             app.default_host_name
#         )

import pulumi
import pulumi_azure_native as azure


class ApiService:

    def __init__(
        self,
        name,
        rg,
        location,
        postgres_host,
        app_subnet_id,
        db_password_secret_uri,
        jwt_secret_uri,
        frontend_host,
    ):

        stack = pulumi.get_stack()
        config = pulumi.Config()

        backend_image = config.require("backendImage")

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

        # Web App
        app = azure.web.WebApp(
            f"{name}-api",
            resource_group_name=rg,
            location=location,

            server_farm_id=plan.id,

            identity=azure.web.ManagedServiceIdentityArgs(
                type="SystemAssigned"
            ),

            # VNet integration
            virtual_network_subnet_id=app_subnet_id,

            site_config=azure.web.SiteConfigArgs(

                linux_fx_version=pulumi.Output.concat(
                    "DOCKER|",
                    backend_image
                ),

                always_on=True,
                # cors=azure.web.CorsSettingsArgs(
                #     allowed_origins=[frontend_host],  # Use full URL including https://
                #     support_credentials=True
                # ),

                cors=azure.web.CorsSettingsArgs(
                    allowed_origins=[
                        pulumi.Output.concat("https://", frontend_host)
                    ],
                    support_credentials=True
                ),
                

                app_settings=[

                    # Database
                    azure.web.NameValuePairArgs(
                        name="DB_HOST",
                        value=postgres_host
                    ),

                    azure.web.NameValuePairArgs(
                        name="DB_USER",
                        value="pgadmin"
                    ),

                    azure.web.NameValuePairArgs(
                        name="DB_PASSWORD",
                        value=pulumi.Output.concat(
                            "@Microsoft.KeyVault(SecretUri=",
                            db_password_secret_uri,
                            ")"
                        )
                    ),

                    azure.web.NameValuePairArgs(
                        name="DB_NAME",
                        value="appdb"
                    ),

                    azure.web.NameValuePairArgs(
                        name="DB_PORT",
                        value="5432"
                    ),

                    # JWT Secret
                    azure.web.NameValuePairArgs(
                        name="JWT_SIGNING_KEY",
                        value=pulumi.Output.concat(
                            "@Microsoft.KeyVault(SecretUri=",
                            jwt_secret_uri,
                            ")"
                        )
                    ),

                    # Azure networking
                    azure.web.NameValuePairArgs(
                        name="WEBSITE_VNET_ROUTE_ALL",
                        value="1"
                    ),

                    azure.web.NameValuePairArgs(
                        name="WEBSITES_PORT",
                        value="8000"
                    ),
                    azure.web.NameValuePairArgs(
                        name="CORS_ORIGINS",
                        value="https://wonderful-water-020621800.1.azurestaticapps.net,http://localhost:5173"
                    ),      

                    azure.web.NameValuePairArgs(
                        name="ENVIRONMENT",
                        value=stack
                    ),
                ]
            ),

            https_only=True
        )

        self.api_url = pulumi.Output.concat(
            "https://",
            app.default_host_name
        )

        self.identity_principal_id = app.identity.apply(
            lambda i: i.principal_id
        )