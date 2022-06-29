from mpm.config import Config

config = Config()

from mpm.main import MainApp
from mpm.controller import set_default_values

set_default_values()
MainApp().run()

