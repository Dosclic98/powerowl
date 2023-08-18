from abc import ABC
from typing import Union

from .bus import Bus
from .grid_edge import GridEdge
from .grid_element import GridElement
from .grid_node import GridNode


class GridAnnotator(GridElement, ABC):
    """
    A grid element that annotates an edge (e.g., a Line or Transformer) or node (i.e., Bus), and a node (i.e., Bus).
    """
    prefix: str = "grid-annotator"

    def get_bus(self) -> 'Bus':
        return self.get_property_value("bus")

    def get_associated(self) -> Union['GridNode', 'GridEdge']:
        return self.get_property_value("element")
