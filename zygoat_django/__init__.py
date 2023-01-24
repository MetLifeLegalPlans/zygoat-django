from importlib_metadata import version
from .exceptions import MissingEnvironmentError  # noqa

__version__ = version("zygoat_django")
