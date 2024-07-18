"""
framework file
    usage example:
        import common.framework as fw
        fw.{constant}
        fw.log(message='bla', payload={'foo': 'bar'}, severity=logging.ERROR)
"""

from common._framework.constants import *
import common._framework.initialization as _init
from common._framework.gcp_logging import Logger
from common._framework.json_fixer import to_jsonable_dict

log = Logger()
