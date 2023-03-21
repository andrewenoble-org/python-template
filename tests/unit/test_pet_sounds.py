from contextlib import redirect_stdout
from io import StringIO
from logging import getLogger
from logging.config import dictConfig

from yaml import safe_load

from python_template.pet_sounds import PetSounds

EXPECTED_RESULT = "A cat says meow\n"


with open("/home/project/config/logger/logger.yaml") as f:
    config = safe_load(f.read())
    dictConfig(config)
    _logger = getLogger()


def test_pet_sound():
    with StringIO() as buf, redirect_stdout(buf):
        PetSounds("cat", "meow").says()
        result = buf.getvalue()

    assert result == EXPECTED_RESULT

    _logger.info("Tested.")
