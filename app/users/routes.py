from ..common.router import Router
from .service import get_users, post_users

__router = Router()

__router.get('', get_users)

__router.post('', post_users)

UserRouter = __router._routes