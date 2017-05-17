from flask import Blueprint
routes = Blueprint('routes', __name__)

from .index import *
from .poll import *
from .vote import *
from .newuser import *
from .login import *
from .logout import *
from .newpoll import *
from .deletepoll import *
from .mypolls import *
