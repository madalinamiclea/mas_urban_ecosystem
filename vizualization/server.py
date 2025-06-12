import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from mesa.visualization.modules import CanvasGrid, ChartModule
from mesa.visualization.ModularVisualization import ModularServer
from core.model import UrbanModel

def agent_portrayal(agent):
    portrayal = {"Shape": "circle", "Filled": "true", "r": 0.8, "Layer": 0}

    if agent is None:
        return None

    if "resident" in agent.unique_id:
        portrayal["Color"] = "red" if agent.current_energy < 2.0 else "blue"
        portrayal["r"] = 0.6
        portrayal["Layer"] = 1
    elif agent.unique_id == "transport":
        portrayal["Color"] = "green"
        portrayal["r"] = 1.2
        portrayal["Layer"] = 2
    elif agent.unique_id == "energy":
        portrayal["Color"] = "yellow"
        portrayal["r"] = 1.0
        portrayal["Layer"] = 2
    elif agent.unique_id == "environment":
        portrayal["Color"] = "brown"
        portrayal["r"] = 1.0
        portrayal["Layer"] = 0
    elif agent.unique_id == "commercial":
        portrayal["Color"] = "orange"
        portrayal["r"] = 1.0
        portrayal["Layer"] = 1

    return portrayal

# Create visualization elements
grid = CanvasGrid(agent_portrayal, 20, 20, 500, 500)

charts = [
    ChartModule(
        [
            {"Label": "Residents Low Energy", "Color": "Red"},
            {"Label": "Pollution", "Color": "Black"}
        ],
        data_collector_name="datacollector"
    ),
    ChartModule(
        [
            {"Label": "Energy Distributed", "Color": "Yellow"},
            {"Label": "Sales", "Color": "Orange"}
        ],
        data_collector_name="datacollector"
    )
]

# Create and launch server
server = ModularServer(
    UrbanModel,
    [grid] + charts,
    "Smart Urban Ecosystem Simulation",
    {"width": 20, "height": 20, "num_residents": 30}
)

server.port = 8521

if __name__ == "__main__":
    server.launch()