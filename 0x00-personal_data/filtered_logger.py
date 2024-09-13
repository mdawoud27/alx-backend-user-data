#!/usr/bin/env python3
"""Personal data Task"""
import logging
from typing import Tuple, List
import re


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Function which returns the log message obfuscated"""
    return re.sub(r'(\w+)=([^{}]+)'.format(separator),
                  lambda match: '{}={}'.format(match.group(1), redaction)
                  if match.group(1) in fields
                  else '{}={}'.format(match.group(1), match.group(2)), message)


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Init function"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """format function"""
        msg = logging.Formatter(self.FORMAT).format(record)
        return filter_datum(self.fields, self.REDACTION, msg, self.SEPARATOR)
