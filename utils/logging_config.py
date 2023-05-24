# @Author BHARATH RAM K (12053)
# @Email  bharathram.k@zohocorp.com
# @Date 12:22 PM 24/05/23 using PyCharm
import logging
import traceback

from utils.constants import INFO, EXCEPTION, DEBUG, ERROR


def log(logger: bool = False, msg: str = "", level: str = INFO):
    """
    This function helps to toggle between logging and print functions using the flag logger
    :param logger: Whether to use logging or print function.
    :param msg: Message to be displayed.
    :param exception: The given message is aException message or not.
    :param level: Info | Exception | Debug | Error level type of logging
    :return: None
    """
    logging.basicConfig(format="%(asctime)s, %(levelname)-8s [%(filename)s : %(lineno)d] - %(message)s",
                        datefmt="%Y-%m-%d %H:%M:%S",
                        level=level
                        )

    if logger:
        if level == EXCEPTION:
            logging.exception("Exception :", str(msg))
            logging.exception("Caused by :", str(traceback.format_exc()))
        elif level == INFO:
            logging.info(msg)
        elif level == DEBUG:
            logging.debug(msg)
        elif level == ERROR:
            logging.error(msg)
    else:
        print(msg)
