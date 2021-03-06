# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
import platform

__author__ = 'Microsoft Corp. <ptvshelp@microsoft.com>'
__version__ = '1.0.0'

# UserAgent string sample: 'Azure-Storage/0.37.0-0.38.0 (Python CPython 3.4.2; Windows 8)'
# First version(0.37.0) is the common package, and the second version(0.38.0) is the service package
USER_AGENT_STRING_PREFIX = 'Azure-Storage/{}-'.format(__version__)
USER_AGENT_STRING_SUFFIX = '(Python {} {}; {} {})'.format(platform.python_implementation(),
                                                          platform.python_version(), platform.system(),
                                                          platform.release())

# default values for common package, in case it is used directly
DEFAULT_X_MS_VERSION = '2017-04-17'
DEFAULT_USER_AGENT_STRING = '{}None {}'.format(USER_AGENT_STRING_PREFIX, USER_AGENT_STRING_SUFFIX)

# Live ServiceClient URLs
SERVICE_HOST_BASE = 'core.windows.net'
DEFAULT_PROTOCOL = 'https'

# Development ServiceClient URLs
DEV_BLOB_HOST = '127.0.0.1:10000'
DEV_QUEUE_HOST = '127.0.0.1:10001'

# Default credentials for Development Storage Service
DEV_ACCOUNT_NAME = 'devstoreaccount1'
DEV_ACCOUNT_SECONDARY_NAME = 'devstoreaccount1-secondary'
DEV_ACCOUNT_KEY = 'Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw=='

# Socket timeout in seconds
DEFAULT_SOCKET_TIMEOUT = 20

# Encryption constants
_ENCRYPTION_PROTOCOL_V1 = '1.0'
