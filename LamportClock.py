class LamportsClock:
	def  __init__(self, process_id):
    	self.process_id = process_id
    	self.clock = 0

	def tick(self):
    	#Increment the clock on internal events.
    	self.clock += 1
    	print(f"Process {self.process_id} tick: {self.clock}")

	def send_event(self):
    	#Simulate sending a message with the current clock value.
    	self.clock += 1
    	print(f"Process {self.process_id} sends event with clock {self.clock}")
    	return self.clock

	def receive_event(self, received_clock):
    	"""
    	Simulate receiving a message and updating the clock.
    	The clock is updated to the maximum of the current clock or received clock + 1.
    	"""
    	self.clock = max(self.clock, received_clock) + 1
    	print(f"Process {self.process_id} receives event and updates clock to {self.clock}")


if __name__ == "__main__":
	# Create two processes
	process_A = LamportsClock(process_id="A")
	process_B = LamportsClock(process_id="B")

	# Simulate events in Process A
	process_A.tick()  # Internal event in A
	sent_clock = process_A.send_event()  # A sends a message

	# Simulate events in Process B
	process_B.tick()  # Internal event in B
	process_B.receive_event(sent_clock)  # B receives the message from A

	# Another event in Process A
	process_A.tick()

	# B sends a message to A
	sent_clock = process_B.send_event()
	process_A.receive_event(sent_clock)  # A receives the message from B
