from mesa import Agent
import random

class ResidentAgent(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.current_energy = random.uniform(2.0, 5.0)
        self.needs_transport = False
        self.destination = None

    def step(self):
        #Daily energy consumption
        consumption = random.uniform(0.5, 1.5)
        self.current_energy -= consumption

        #Requesting energy if its below threshold
        if self.current_energy < 2.0:
            self.model.send_message(
                sender=self.unique_id,
                receiver="energy",
                msg_type="energy_request",
                content=3.0
            )

        #Random transport needs
        if random.random() < 0.3:
            self.needs_transport = True
            width = self.model.grid.width
            height = self.model.grid.height
            self.destination = (self.random.randrange(width), self.random.randrange(height))
            self.model.send_message(
                sender=self.unique_id,
                receiver="transport",
                msg_type="transport_request",
                content={"from": self.unique_id, "to": self.destination}
            )

        #Random purchase decisions
        if random.random() < 0.2:
            quantity = random.randint(1, 5)
            self.model.send_message(
                sender=self.unique_id,
                receiver="commercial",
                msg_type="purchase_request",
                content=quantity
            )

        # Processing received messages
        messages = self.model.get_messages_for(self.unique_id)
        for msg in messages:
            if msg["type"] == "transport_confirmation" and self.destination:
                self.model.grid.move_agent(self, self.destination)
                self.needs_transport = False
                self.destination = None

            elif msg["type"] == "energy_delivery":
                received_energy = msg["content"]
                self.current_energy += received_energy

            elif msg["type"] == "purchase_confirmation":
                status = msg["content"]["status"]
                qty = msg["content"]["quantity"]
                if status == "success":
                    print(f"{self.unique_id} bought {qty} units.")
                else:
                    print(f"{self.unique_id} couldn't buy: insufficient stock.")