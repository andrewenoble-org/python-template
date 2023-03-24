"""YAML I/O Class."""

from typing import Dict

from yaml import dump, safe_load


class YAMLHandler:
    r"""YAML I/O Class.

    Methods
    -------
    load(yaml_path)
        Loads YAML file to Dict.
    write(yaml_dict)
        Writes Dict to YAML file.
    """

    def load(self, yaml_path: str) -> Dict:
        r"""
        Parameters
        ----------
        logger_config_path : str = "config/logger/logger.yml"
            Path to logger configuration YAML file.
        """
        with open(yaml_path) as f:
            yaml_dict = safe_load(f.read())

        return yaml_dict

    def write(self, yaml_dict: Dict, yaml_path: str) -> None:
        r"""
        Parameters
        ----------
        yaml_dict : Dict
            Dictionary to be written to YAML file.
        yaml_path : str
            Path to destination YAML file.
        """
        with open(yaml_path, "w") as f:
            # with explicit_start=True, first line of YAML file written is
            # "---", as expected by YAML linters
            stream = dump(yaml_dict, explicit_start=True, default_flow_style=False)

            # indents top-level YAML list items as expected by linter
            f.write(stream.replace("\n- ", "\n    - "))
