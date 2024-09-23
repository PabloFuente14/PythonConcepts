import datetime as dt
import json
import logging
from typing import override

LOG_RECORD_BUILTIN_ATTRS = {
        "args",
    "asctime",
    "created",
    "exc_info",
    "exc_text",
    "filename",
    "funcName",
    "levelname",
    "levelno",
    "lineno",
    "module",
    "msecs",
    "message",
    "msg",
    "name",
    "pathname",
    "process",
    "processName",
    "relativeCreated",
    "stack_info",
    "thread",
    "threadName",
    "taskName",
    "extra",
}


class MyJSONFormatter(logging.Formatter):
    #if the formatting keys are not passd, the formatter has no info
    def __init__(self, *, fmt_keys: dict[str, str] | None = None):
        super().__init__() 
        self.fmt_keys = fmt_keys if fmt_keys is not None else {}

    @override #the parent method
    def format(self, record: logging.LogRecord) -> str:
        message = self._prepare_log_dict(record)
        return json.dumps(message, default=str)

    def _prepare_log_dict(self, record:logging.LogRecord):
        always_fields = {
            "message": record.getMessage(), ##getting the message from the LogRecord object
            "timestamp": dt.datetime.fromtimestamp( ##convertinr
                record.created, tz=dt.timezone.utc
            ).isoformat(),
        }
        if record.exc_info is not None: #tuple containin exception rised during logging process
            always_fields["exc_info"] = self.formatException(record.exc_info) #formatting exception
            
        if record.stack_info is not None: #this attb contains the sequence of function calls
            always_fields["stack_info"] = self.formatStack(record.stack_info)
            
        message = { ##adding to log message other standards passed on the fmt_keys
            key: msg_val
            if (msg_val := always_fields.pop(val, None)) is not None #assings to msg_val the value of the always_field element, returns None if there's nothing
            else getattr(record, val) #finds fot the vaule at LogRecord istance
            for key, val in self.fmt_keys.items()
        }
        message.update(always_fields)

        for key, val in record.__dict__.items(): 
            if key not in LOG_RECORD_BUILTIN_ATTRS: #if key is not a standard key, is an extra and added to message
                message[key] = val ## getting the extra

        return message


