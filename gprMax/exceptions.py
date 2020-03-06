# Copyright (C) 2015-2020: The University of Edinburgh
#                 Authors: Craig Warren and Antonis Giannopoulos
#
# This file is part of gprMax.
#
# gprMax is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# gprMax is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with gprMax.  If not, see <http://www.gnu.org/licenses/>.

import logging

from colorama import init
from colorama import Fore
init()

logger = logging.getLogger(__name__)


class GeneralError(ValueError):
    """Handles general errors. Subclasses the ValueError class."""
    def __init__(self, message, *args):
        self.message = message
        super(GeneralError, self).__init__(message, *args)
        logger.exception(Fore.RED)


class CmdInputError(Exception):
    """Handles errors in user specified commands. Subclasses the ValueError
        class.
    """
    pass
    # def __init__(self, message, *args):
    #     self.message = message
    #     super(CmdInputError, self).__init__(message, *args)
    #     logger.exception(Fore.RED)
