from mesa import Agent

class EnvironmentalAgent(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.total_pollution = 0.0
        self.warning_threshold = 10.0
        self.critical_threshold = 20.0

    def step(self):
        #Calculating total polution from all agents
        new_pollution = 0.0
        for agent in self.model.schedule.agents:
            if hasattr(agent, 'pollution_level'):
                new_pollution += agent.pollution_level

        #Updating total pollution with decay
        self.total_pollution = (self.total_pollution * 0.9) + new_pollution