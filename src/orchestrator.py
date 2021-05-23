
def orchestrator(config, logger):
    """Orchestrator app
    """

    try:
        logger.log.info("App orchestrator execution")
        logger.log.info(f'App orchestrator arguments \'{config}\'')
    except Exception as err:
        logger.log_traceback(err)
