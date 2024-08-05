from . import items
from . import merchants



def init_routers(app):
    app.include_router(items.router)
    app.include_router(merchants.router)