"""Configureable Logger Class."""

from logging import Logger as LoggingLoggerClass
from logging import getLogger
from logging.config import dictConfig

from python_template.utils.yaml_handler import YAMLHandler


class Logger:
    r"""Configureable Logger Class.

    Methods
    -------
    get_logger
        Get logger configured according to :code:`logger_config_path` YAML file.
    """

    def get_logger(
        self,
        logger_config_path: str = "config/logger/logger.yml",
    ) -> LoggingLoggerClass:
        r"""
        Parameters
        ----------
        logger_config_path : str = "config/logger/logger.yml"
            Path to logger configuration YAML file.
        """
        # configure logger
        logger_config_dict = YAMLHandler().load(logger_config_path)
        dictConfig(logger_config_dict)

        return getLogger()
