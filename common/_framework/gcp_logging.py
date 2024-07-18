import logging
import traceback
from typing import Dict, Any, Optional
import sys
import json
from time import time

from .constants import GcpLoggerFormat
from .json_fixer import to_jsonable_dict


def create_logger(name: str) -> logging.Logger:
    formatter = logging.Formatter(GcpLoggerFormat.LOGGER_FORMAT)
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)
    return logger


class Logger:
    def __init__(self, name: Optional[str] = None):
        self._logger = None
        self.name = None
        self.set_name(name if name is not None else f'{GcpLoggerFormat.UNNAMED}_{time()}')

    def set_name(self, name: str):
        self.name = name
        self._logger = create_logger(self.name)

    @staticmethod
    def create_error_payload(error: Exception) -> Dict[str, Any]:
        payload = \
            {
                'error': type(error),
                'args': error.args,
                'traceback': traceback.format_exc(),
            }
        return payload

    def _log(self, message: str, payload: Optional[Dict[str, Any]] = None, severity: int = logging.INFO):
        if payload is None:
            payload = {}
        message = GcpLoggerFormat.LOGGER_NAME_FORMAT.format(self.name, message)
        extra = {'payload': json.dumps(to_jsonable_dict(payload), default=lambda x: f'{x}')}
        if (severity == logging.INFO):
            self._logger.info(msg=message, extra=extra)
        elif severity == logging.ERROR:
            self._logger.error(msg=message, extra=extra)
            # print(payload['traceback'])
            # if __debug__:
            #     raise Exception(payload.get('traceback'))
        elif (severity == logging.DEBUG):
            self._logger.debug(msg=message, extra=extra)
        elif (severity == logging.WARNING):
            self._logger.warning(msg=message, extra=extra)

    def __call__(self, message: str, payload: Optional[Dict[str, Any]] = None, severity: int = logging.INFO):
        return self._log(message=message, payload=payload, severity=severity)
