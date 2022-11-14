from .routes import router
from fastapi import FastAPI, APIRouter
from fastapi.responses import ORJSONResponse
from src.core.settings import settings
from src.routes import router
from src import __version__


def get_application():
    application = FastAPI(
        version=__version__,
        docs_url=f"{settings.BASE_PATH}/docs",
        redoc_url=f"{settings.BASE_PATH}/redoc",
        openapi_url=f"{settings.BASE_PATH}/openapi.json",
    )

    # application.add_event_handler(
    #     "startup",
    #     events.on_event(application, dynatrace.dynatrace_start, setup_database()),
    # )

    application.include_router(router, prefix=f"{settings.BASE_PATH}")
    return application


app = get_application()
