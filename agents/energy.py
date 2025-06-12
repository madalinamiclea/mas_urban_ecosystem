from mesa import Agent
import random

class EnergyAgent(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.energy_capacity = 100.0
        self.current_energy = self.energy_capacity
        self.energy_distributed = 0.0
        self.pollution_factor = 0.2

    def step(self):
        self.energy_distributed = 0.0
        messages = self.model.schedule.agents
        for agent in messages:
            if hasattr(agent, 'current_energy') and agent.current_energy < 2.0:
                self.distribute_energy(agent)
        
        self.generate_energy()

    def distribute_energy(self, agent):
        energy_needed = 5.0 - agent.current_energy
        if self.current_energy >= energy_needed:
            self.current_energy -= energy_needed
            agent.current_energy += energy_needed
            self.energy_distributed += energy_needed

    def generate_energy(self):
        generation = random.uniform(5.0, 10.0)
        self.current_energy = min(self.current_energy + generation, self.energy_capacity)