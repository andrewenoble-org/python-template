from io import StringIO
from contextlib import redirect_stdout

from python_template.pet_sounds import PetSound

EXPECTED_RESULT = "A duck says quack\n"


def test_pet_sound():
    with StringIO() as buf, redirect_stdout(buf):
        PetSound("duck", "quack", num_legs=2).says()
        result = buf.getvalue()

    assert result == EXPECTED_RESULT