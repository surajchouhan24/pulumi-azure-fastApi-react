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

from pulumi_azure_native import web

def create_api(resource_group_name, location):

    plan = web.AppServicePlan(
        "fastapi-plan",
        resource_group_name=resource_group_name,
        location=location,
        sku={
            "name": "B1",
            "tier": "Basic"
        },
        kind="linux",
        reserved=True
    )

    app = web.WebApp(
        "fastapi-backend",
        resource_group_name=resource_group_name,
        location=location,
        server_farm_id=plan.id,
        site_config={
            "linux_fx_version": "PYTHON|3.10"
        }
    )

    return app