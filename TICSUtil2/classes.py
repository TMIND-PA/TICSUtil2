import os, sys
from loguru import logger
import __main__

# stdout unbuffering
# sys.stdout = os.fdopen(sys.stdout.fileno(), "w", buffering=1)
# sys.stderr = os.fdopen(sys.stderr.fileno(), "w", buffering=1)


class TICSLogger:
    def __init__(
        self,
        filename=None,
        dir=None,
        max_num="10",
        colorize=True,
        file_level="debug",
        console_level="debug",
        msg_col_len=80,
    ):

        if filename is None:
            full_path = __main__.__file__
            script_name = os.path.basename(os.path.realpath(full_path))
            # print(f"{script_name = }")
            filename = script_name[:-3]

        if dir is None:
            full_path = __main__.__file__
            dir = os.path.dirname(os.path.realpath(full_path))

        if not os.path.exists(dir):
            os.makedirs(dir, exist_ok=True)

        if file_level is not None:
            file_level = file_level.upper()

        if console_level is not None:
            console_level = console_level.upper()

        # Setup loguru logger to TICS formatting
        logger.remove()  # Remove default logger
        fmt = f"<green>{{time:YYYY-MM-DD HH:mm:ss.SSS}}</green> | <level>{{level: <8}}</level> | <level>{{message: <{msg_col_len}}}</level> | <cyan>{{function}}</cyan>:<cyan>{{line}}</cyan>"

        # Configure console logger
        if console_level is not None:
            logger.add(
                sys.stderr,
                level=console_level,
                format=fmt,
                colorize=colorize,
                enqueue=True,
                backtrace=False,
                diagnose=True,
            )
            logger.bind(msg_col_len=msg_col_len)

        # Configure file logger
        if file_level is not None:
            full_path = __main__.__file__
            script_name = os.path.basename(os.path.realpath(full_path))
            log_file_name = os.path.join(dir, filename)
            logger.add(
                log_file_name + "_{time:YYYYMMDD}.log",
                level=file_level,
                format=fmt,
                rotation="00:00",
                enqueue=True,
                backtrace=False,
                diagnose=True,
            )

    def get_log(self):
        return logger
