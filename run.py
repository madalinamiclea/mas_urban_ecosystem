from core.model import UrbanModel
from mesa.datacollection import DataCollector
import pandas as pd
import os

# Create model instance
model = UrbanModel()

# Initialize data collector with correct attribute names
model.datacollector = DataCollector(
    model_reporters={
        "Residents Low Energy": lambda m: len([a for a in m.schedule.agents 
                                             if "resident" in a.unique_id and a.current_energy < 2.0]),
        "Pollution": lambda m: next((a.total_pollution for a in m.schedule.agents 
                                   if a.unique_id == "environment"), 0),
        "Energy Distributed": lambda m: next((a.energy_distributed for a in m.schedule.agents 
                                            if a.unique_id == "energy"), 0),
        "Sales": lambda m: next((a.sales for a in m.schedule.agents 
                               if a.unique_id == "commercial"), 0)
    }
)

# Run simulation
print("Starting simulation...")
for i in range(100):
    model.step()
    if i % 10 == 0:  # Print progress every 10 steps
        print(f"Step {i}/100")

# Create reports directory if it doesn't exist
os.makedirs("reports", exist_ok=True)

# Collect and save results
results = pd.DataFrame(model.datacollector.model_vars)
results.to_csv("reports/simulation_logs.csv", index=False)
print("Simulation complete. Results saved to reports/simulation_logs.csv")