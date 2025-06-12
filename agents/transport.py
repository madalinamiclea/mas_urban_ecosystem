from mesa import Agent

class TransportAgent(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.max_capacity = 10
        self.current_requests = []
        self.pollution_level = 0.0

    def step(self):
        self.current_requests = []
        
        #Processing transport requests
        messages = self.model.get_messages_for(self.unique_id)
        for msg in messages:
            if msg["type"] == "transport_request":
                if len(self.current_requests) < self.max_capacity:
                    self.current_requests.append(msg)
                    self.handle_transport_request(msg)

        #Generating pollution based on activity
        self.pollution_level = len(self.current_requests) * 0.8
        if self.pollution_level > 0:
            self.model.send_message(
                sender=self.unique_id,
                receiver="environment",
                msg_type="pollution_report",
                content=self.pollution_level
            )

    def handle_transport_request(self, request):
        self.model.send_message(
            sender=self.unique_id,
            receiver=request["content"]["from"],
            msg_type="transport_confirmation",
            content=True
        )