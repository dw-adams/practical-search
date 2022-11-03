from typing import Dict, Any

from .node import Node
from .nst2 import HistoryDist, NestingLevel, NestedBelief
from .nst2 import NestedSearchTree as NestedSearchTree2

SEARCH_TREES: Dict[str, Any] = {
    'NST2': NestedSearchTree2,
    **{
        c.__name__: c for c in [
            NestedSearchTree2,
        ]
    }
}
