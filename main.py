from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.application.container import ApplicationContainer
from src.core.config.settings import SETTINGS
from src.infrastructure.container import InfrastructureContainer
from src.web_api.controllers import delivery_person_controller, package_controller, route_controller


def create_app():
    app = FastAPI(
        title='Logistic Microservice API',
        description='FastAPI - Logistic Microservice',
        version='1.0.0',
        docs_url='/docs',
        redoc_url='/redoc',
        root_path="/api"
    )
    config_modules(app)
    config_middleware(app)
    app.get("/", tags=["Status"])(check_status)
    return app


def config_modules(app: FastAPI) -> None:
    infra_container = InfrastructureContainer()
    app_container = ApplicationContainer()
    app_container.infrastructure.override(infra_container)

    app_container.wire(modules=[
        delivery_person_controller,
        package_controller,
        route_controller
    ])

    app.include_router(delivery_person_controller.router)
    app.include_router(package_controller.router)
    app.include_router(route_controller.router)


def config_middleware(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=SETTINGS.ALLOWED_HOSTS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


def check_status():
    response = {
        'detail': 'Logistic Microservice is running successfully.'
    }
    return response


app = create_app()
