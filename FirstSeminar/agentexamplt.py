import matplotlib.pyplot as plt

class agent:
	state = 1
	action  = 0
	rewardsum = 0
	reward = 0
	recordreward = []
	
	def take_action(self,a):
		self.action = a
		
	def act(self):
		if self.state==1 and self.action ==1 :
			self.state=1
			self.reward = 10
			self.rewardsum = self.rewardsum + self.reward
			self.action = 0
		elif self.state==1 and self.action ==2 :
			self.state=2
			self.reward = -10
			self.rewardsum = self.rewardsum + self.reward
			self.action = 0
		elif self.state==2 and self.action ==1 :
			self.state=1
			self.reward = 40
			self.rewardsum = self.rewardsum + self.reward
			self.action = 0
		elif self.state==2 and self.action ==2 :
			self.state=2
			self.reward = 10
			self.rewardsum = self.rewardsum + self.reward
			self.action = 0
			
	def display(self):
		output = "###the agent is in state %d, last reward is %d, the accumulative reward is %d" %(self.state,self.reward,self.rewardsum)
		print(output)
		
	def exploration(self):
		agent1.display()

		a = input("please take an action : ")
		
		
		while a != -1:
			
				agent1.take_action(a)
				agent1.act()
				agent1.display()
				
				self.recordreward.append(agent1.rewardsum)
				
				a = input("please take an action : ")
		plt.plot(self.recordreward)
		plt.show()
  
		
temp = 1
agent1 = agent()
agent1.exploration()

while(temp !=0):
    temp = input(" terminal or continun or new? 0 or 1 or 2 : ")

    if temp == 1 :
        agent1.exploration()
    if temp == 2:
        agent1 = agent()
        agent1.exploration()

		


		
			
	
		
	
	
