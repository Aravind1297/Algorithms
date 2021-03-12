#import time   
#start = time.process_time()

def fractional_knapsack(W,s_weight,s_value,sorted_ratio):
	A = [0] * len(s_weight)    #list which should hold the weight of the most valuable materials/things.
	v = 0                      # This variable will be updated with the value of the most valuable
	i = 0                      # iterator (will be increased by 1)
	for weigh in s_weight:    
		if W == 0:
			return "{:.4f}".format(v),A
		a = min(weigh,W)
		v = v + a * sorted_ratio[i]
		weigh = weigh - a
		A[i] = A[i] + a
		W = W - a
		i+=1
	return "{:.4f}".format(v),A
	

if __name__ == '__main__':
	n,W = map(int,input().split())
	valueweight_list = []
	vw_ratio =[]
	for x in range(n):
		(value,weight) = map(int,input().split())
		valueweight_list.append((value,weight))
		vw_ratio.append(value/weight)
	valueweight_dict = dict(zip(vw_ratio,valueweight_list)) #created a dictionary containing the value weight ratio as key and value weight tuple as value
	sorted_dict = dict(sorted(valueweight_dict.items(), key = lambda t: t[0], reverse = True)) #sorting the dictionary by key in descending order
	sorted_vw = list(sorted_dict.values())
	s_value,s_weight = zip(*sorted_vw)
	s_value = list(s_value)             
	s_weight = list(s_weight)
	sorted_ratio = list(sorted_dict.keys())
	print(fractional_knapsack(W,s_weight,s_value,sorted_ratio))

	#end = time.process_time()
	#print(end -start)
