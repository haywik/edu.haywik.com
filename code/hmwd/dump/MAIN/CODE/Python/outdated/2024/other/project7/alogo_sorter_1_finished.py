#9/7/2024 start  11/7/2024 finish					# the comments may not corrilate to location where its placed.
import random

data = [4,5,1,2,4,5,3,3,2,1,1,1,1,4,4,4,4,5,5,5,6,6,8,8,5,5444,3,3,1,2,0,33,5555555]
def begin_pro():
		
	random_data = input("Generate random data?: Y, N:").lower()	
	if random_data == "y":
		RD_amount = int(input("How many digits of random data would you like?:"))
		
		RD_max_digit = int(input("How big can the random numbers go?:"))
																		
																									#Data to stort, anything that is not a numbe will hold its postion in the list
		for i in range(RD_amount):												#adds random data to the list 
			x = random.randint(1,RD_max_digit)
			data.append(x)
		
	print("Random data:",data)
	
	sort(data)										#displayes the data

def sort(list):	
	input("Press enter to start list")
	cu = len(list)
	while True:
		prev_list = list.copy()
		loop = 0
		for i in range(cu):
			current = 0 + loop		#current number in the list
			next = 1 + loop			#next number in the list
			old_list = list.copy()
			try:													# try is used for when a pecice of data is not in the lists paramters usch as a = [1,4,5]  a[4] does not exist it would then move on
				if list[current] > list[next]:	#asks if the current number if bigger or smaller then the one on its right next one if true it flips them by saving the prevoius lists numbers					
					list[current] = old_list[next]		# change the inequilty to make it > acesding < descending           	
					list[next] = old_list[current]	
			except:
				pass						
			loop = loop + 1
		if list == prev_list:																#only presents list if changed and wont reapet the same list over and over
			print("Current State:",list)
			break
																	#used to move the program onto the next current number to sort with the next			
def count(list):
	c = 0
	for i in list:
		c = c + 1
	return c



while True:
	input("Start?")
	begin_pro()
