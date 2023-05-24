# @Author BHARATH RAM K (12053)
# @Email  bharathram.k@zohocorp.com
# @Date 12:22 PM 24/05/23 using PyCharm
import logging
import traceback


def log(logger: bool = False, msg: str = "", exception: bool = False):
    """
    This function helps to toggle between logging and print functions using the flag logger
    :param logger: Whether to use logging or print function.
    :param msg: Message to be displayed.
    :param exception: The given message is aException message or not.
    :return: None
    """

    if logger:
        if exception:
            logging.exception("Exception %s :", str(msg))
            logging.exception("Caused by %s:", str(traceback.format_exc()))
        else:
            logging.info(msg)
    else:
        print(msg)
