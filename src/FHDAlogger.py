from dotenv import load_dotenv
import logging, datetime, os

def initiateLogger(origin, level):
    '''Initiate a logger with given logging level and logging origin

    Args:
        origin: from which source this logger is from (for determining logging file name)
        level: the level of the logger, options are [INFO, DEBUG, WARNING, ERROR, CRITICAL]
    Raises:
        KeyError: The level parameter is not valid
    Returns:
        the logger object

    '''

    try:
        load_dotenv()
        root_name = os.getenv('log_path')
        if root_name == None: ##when env variable is undefined we print it to stdout
            logInfo = str(datetime.datetime.now()).replace(' ', '_').replace(':', '')[:17] + origin
            print("log: {0}".format(logInfo))
        else:
            logging.basicConfig(filename = root_name +
                    str(datetime.datetime.now()).replace(' ', '_').replace(':', '')[:17] + origin + '.log',
                    level=level,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    except:
        raise KeyError("Invalid logger level")
    return logging.getLogger(__name__)
