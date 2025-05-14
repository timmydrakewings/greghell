import pandas as pd

import mermaid as md
from mermaid.graph import Graph

render = md.Mermaid("""
flowchart TD
    A1["Coke Oven"] --> |Creosote| B1["Liquid Fueled Furnace"]
    A1 --> |Coal Coke| B2["Solid Fueled Furnace"]
    A2["Water Tank"] --> B1 & B2
    B1 & B2 --> D
""")
render