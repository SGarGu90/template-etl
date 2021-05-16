
def orchestrator(args, logger):
    """Orchestrator app
    """

    try:
        logger.log.info("App orchestrator execution\n")
        logger.log.info("App orchestrator arguments {0} \n".format(args))
    except Exception as err:
        logger.log_traceback(err)
