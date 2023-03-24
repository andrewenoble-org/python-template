"""Class to associate a pet to a sound."""

from python_template.utils.logger import Logger

_logger = Logger().get_logger()


class PetSounds:
    r"""Associate a pet to a sound.

    ...

    Attributes
    ----------
    says_str : str
        A formatted string to print out what the pet says.
    name : str
        The name of the pet.
    sound : str
        The sound that the pet makes.
    num_legs : int
        The number of legs the pet has (default 4).

    Methods
    -------
    says(sound=None)
        Prints the name of the pet and what sound it makes.

    References
    ----------
    .. [1] https://realpython.com/documenting-python-code/
    .. [2] https://numpydoc.readthedocs.io/en/latest/example.html#example
    .. [3] https://en.wikipedia.org/wiki/Pet_Sounds

    Examples
    --------
    >>> PetSounds("duck", "quack", num_legs=2).says()
    "A duck says quack"
    """

    says_str = "A {name} says {sound}"

    def __init__(self, name, sound, num_legs=4):
        r"""
        Parameters
        ----------
        name : str
            The name of the pet.
        sound : str
            The sound the pet makes.
        num_legs : int, optional
            The number of legs the pet has (default is 4).
        """
        _logger.info("Initialize attributes.")

        self.name = name
        self.sound = sound
        self.num_legs = num_legs

    def says(self, sound=None):
        r"""Prints what the pet name is and what sound it makes.

        If the argument `sound` is not passed in, the default pet
        sound is used.

        Parameters
        ----------
        sound : str, optional
            The sound the pet makes (default is None).

        Raises
        ------
        NotImplementedError
            If no sound is set for the pet or passed in as a
            parameter.
        """
        if self.sound is None and sound is None:
            raise NotImplementedError("Silent pets are not supported!")

        _logger.info("Print the pet sound.")
        out_sound = self.sound if sound is None else sound
        print(self.says_str.format(name=self.name, sound=out_sound))
