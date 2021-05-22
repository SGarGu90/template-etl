
def orchestrator(config, logger):
    """Orchestrator app
    """

    try:
        logger.log.info("App orchestrator execution\n")
        logger.log.info(f'App orchestrator arguments \'{config}\' \n')
    except Exception as err:
        logger.log_traceback(err)
