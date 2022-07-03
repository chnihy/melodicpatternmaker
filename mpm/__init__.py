#__init__.py

from mpm.config import Config

config = Config()

from mpm.view import ViewApp
from mpm.controller import set_default_values

set_default_values()
ViewApp().run()

