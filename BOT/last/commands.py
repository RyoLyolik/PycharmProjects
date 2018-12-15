def bt(num):
	end = ''
	num = int(num)
	num = str(num)
	num = [i for i in num]
	num = reversed(num)
	num = ''.join(num)
	cnt = 0
	for i in range(0,len(num)):


		if cnt == 3:
			end += ' '
			end += num[i]
			cnt = 0
		else:
			end+=num[i]
		cnt += 1
	end = [i for i in end]
	end = reversed(end)
	end = ''.join(end)
	return end