"""Init and utils."""
from zope.i18nmessageid import MessageFactory

import logging


PACKAGE_NAME = "pssa2023"

_ = MessageFactory("pssa2023")

logger = logging.getLogger("pssa2023")
