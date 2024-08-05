from . import items
from . import merchants
from . import wallets


def init_routers(app):
    app.include_router(items.router)
    app.include_router(merchants.router)
    app.include_router(wallets.router)