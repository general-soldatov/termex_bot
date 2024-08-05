import logging

class ErrorLogFilters(logging.Filter):
    def filter(self, record):
        return record.levelname == 'ERROR'

class DebugWarningLogFilter(logging.Filter):
    def filter(self, record):
        return record.levelname in ('DEBUG', 'WARNING', 'INFO')

class CriticalLogFilter(logging.Filter):
    def filter(self, record):
        return record.levelname == 'CRITICAL'