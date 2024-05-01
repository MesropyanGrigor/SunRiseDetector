import logging
import sys

logger = logging.getLogger("SUN RISE")
logging.basicConfig(level=logging.INFO)

def sig_term_handler(signal_num: int, current_stack_frame):
    logger.error(
        "There is some connection issue",
    )

    sys.exit(1)

def sig_abort_handler(signal_num: int, current_stack_frame):
    logger.error(
        "Could not fetch sun rise info",
    )

    sys.exit(1)
