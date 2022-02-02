class CountCards:
	def __init__(self,running_count=0,true_count=0):
		self.running_count = running_count
		self.true_count = true_count

	def update_true_count(self, num_of_deck_r):
		self.true_count = self.running_count/num_of_deck_r

	def reset(self):
		self.running_count = 0
		self.true_count = 0

if __name__ == "__main__":
	c = CountCards(true_count=14)

	print(c.true_count)