from mesa import Model
from mesa.space import MultiGrid
from mesa.time import RandomActivation
from mesa import DataCollector

from agents.resident import ResidentAgent
from agents.transport import TransportAgent
from agents.energy import EnergyAgent
from agents.environment import EnvironmentalAgent
from agents.commercial import CommercialAgent

class UrbanModel(Model):
    def __init__(self, width=20, height=20, num_residents=30):
        super().__init__()
        self.grid = MultiGrid(width, height, torus=True)
        self.schedule = RandomActivation(self)
        self.running = True
        self.messages = []  # Message queue

        # Initialize data collector
        self.datacollector = DataCollector(
            model_reporters={
                "Residents Low Energy": lambda m: len([a for a in m.schedule.agents 
                                                     if "resident" in a.unique_id and hasattr(a, 'current_energy') and a.current_energy < 2.0]),
                "Pollution": lambda m: next((a.total_pollution for a in m.schedule.agents 
                                          if a.unique_id == "environment"), 0),
                "Energy Distributed": lambda m: next((a.energy_distributed for a in m.schedule.agents 
                                                   if a.unique_id == "energy"), 0),
                "Sales": lambda m: next((a.sales for a in m.schedule.agents 
                                      if a.unique_id == "commercial"), 0)
            }
        )

        # Create agents
        self.init_agents(width, height, num_residents)

    def send_message(self, sender, receiver, msg_type, content):
        """Send a message between agents"""
        self.messages.append({
            "from": sender,
            "to": receiver,
            "type": msg_type,
            "content": content
        })

    def get_messages_for(self, receiver_id):
        """Get all messages for a specific receiver"""
        return [msg for msg in self.messages if msg["to"] == receiver_id]

    def init_agents(self, width, height, num_residents):
        # Create resident agents
        for i in range(num_residents):
            agent = ResidentAgent(f"resident_{i}", self)
            self.schedule.add(agent)
            x = self.random.randrange(width)
            y = self.random.randrange(height)
            self.grid.place_agent(agent, (x, y))

        # Create single instances of service agents
        transport = TransportAgent("transport", self)
        self.schedule.add(transport)
        self.grid.place_agent(transport, (width // 2, height // 2))

        energy = EnergyAgent("energy", self)
        self.schedule.add(energy)
        self.grid.place_agent(energy, (width // 4, height // 4))

        environment = EnvironmentalAgent("environment", self)
        self.schedule.add(environment)
        self.grid.place_agent(environment, (width - 2, height - 2))

        commercial = CommercialAgent("commercial", self)
        self.schedule.add(commercial)
        self.grid.place_agent(commercial, (width // 3, height // 3))

    def step(self):
        """Execute one step of the model"""
        self.messages = []  # Clear messages from previous step
        self.schedule.step()
        self.datacollector.collect(self)