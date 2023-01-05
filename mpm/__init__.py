# create a single instance of config to be imported by all other modules
# like a Singleton...
from mpm.config import Config
config = Config()

# instantiate controller - calls the set_default_values() method
from mpm.controller import Controller
controller = Controller()

# Instantiate viewer
from mpm.view import ViewApp
ViewApp().run()

