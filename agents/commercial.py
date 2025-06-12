from mesa import Agent

class CommercialAgent(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.inventory = 100
        self.sales = 0
        self.max_inventory = 150

    def step(self):
        #Here are processed the sales for residents
        for agent in self.model.schedule.agents:
            if "resident" in agent.unique_id and self.inventory > 0:
                if self.random.random() < 0.2:  # 20% chance of purchase
                    quantity = self.random.randint(1, 5)
                    if self.inventory >= quantity:
                        self.inventory -= quantity
                        self.sales += quantity

        #Restocking if necesary
        if self.inventory < 50:
            restock = self.max_inventory - self.inventory
            self.inventory += restock