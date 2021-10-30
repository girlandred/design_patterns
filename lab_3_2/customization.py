from __future__ import annotations

from abc import ABC


class Customization(ABC):
    """
        Represents abstract class Customization

        ...

        Attributes
        ----------
        extraMilk : float
            extra milk.
        sugar : float
            sugar.
        mugSize : float
            size of mug.
    """

    def __init__(self, extraMilk: float, sugar: float, mugSize: float):
        self.extraMilk = extraMilk
        self.sugar = sugar
        self.mugSize = mugSize
