from contextlib import redirect_stdout
from io import StringIO

from python_template.pet_sounds import PetSounds
from python_template.utils.logger import Logger

EXPECTED_RESULT = "A cat says meow\n"


_logger = Logger().get_logger()


def test_pet_sound():
    with StringIO() as buf, redirect_stdout(buf):
        PetSounds("cat", "meow").says()
        result = buf.getvalue()

    assert result == EXPECTED_RESULT

    _logger.info("Tested.")
