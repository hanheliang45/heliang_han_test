
def check_gap(x1, x2, x3, x4):
	#do some basic check
	if x1 >= x2 or x3 >= x4:
		return False;

	#don't need check equal
	if x2 > x4:
		return x1 < x4;
	else:
		return x3 < x2;
		

print check_gap(1,5,2,6);
print check_gap(1,5,6,8);