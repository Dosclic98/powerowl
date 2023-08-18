import dataclasses

from .substation import Substation


@dataclasses.dataclass(eq=False, kw_only=True)
class JunctionBox(Substation):
    pass
