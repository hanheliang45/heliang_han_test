"""
parse input
@return (isvalid, is_negative, start position of number, position of point)
"""
def parse_str(str):
	#only one point symbol is acceptable
	has_point = False;
	point_pos = len(str);
	number_start_pos = 0;
	is_negative = False;
	for i in range(0, len(str)):
		if 0 == i and ('-' == str[0] or '+' == str[0]):
			number_start_pos = 1;
			if '-' == str[0]:
				is_negative = True;
			continue;
		if str[i] >= '0' and str[i] <= '9':
			continue;
		if (not has_point) and '.' == str[i]:
			has_point = True;
			point_pos = i;
			continue;
		return (False, is_negative, number_start_pos, point_pos);
	return (True, is_negative, number_start_pos, point_pos);


"""
get the integer of input
"""
def get_integer(str, parse_result):
	i = parse_result[2];
	num = 0;
	while i < parse_result[3]:
		num = num*10 + int(str[i]);
		i += 1;
	return num;



"""

Lib method is here:

@return int
if str1 > str2 return 1;
if str1 == str2 return 0;
if str1 < str2 return -1;
if str1 or str2 is invalid return -2;
"""
def compare_str(str1, str2):
	parse_result1 = parse_str(str1);
	parse_result2 = parse_str(str2);

	#check valid -2;
	if not (parse_result1[0] and parse_result2[0]):
		return -2;
	
	#check signal
	is_negative_str1 = parse_result1[1];
	is_negative_str2 = parse_result2[1];
	if is_negative_str1^is_negative_str2:
		if is_negative_str1:
			return -1;
		if is_negative_str2:
			return 1;
			
	#compare absolute value of integer part
	num_integer_part_1 = get_integer(str1, parse_result1);
	num_integer_part_2 = get_integer(str2, parse_result2);
	if num_integer_part_1 != num_integer_part_2:
		return 1 if is_negative_str1 ^ (num_integer_part_1 > num_integer_part_2) else -1;
	
	#compare absolute value of decimal
	idx_decimal_1 = parse_result1[3]+1;
	idx_decimal_2 = parse_result2[3]+1;
	while idx_decimal_1<len(str1) and idx_decimal_2<len(str2):
		if str1[idx_decimal_1] != str2[idx_decimal_2]:
			return 1 if is_negative_str1 ^ (str1[idx_decimal_1] > str2[idx_decimal_2]) else -1;
		idx_decimal_1 += 1;
		idx_decimal_2 += 1;
	if idx_decimal_2==len(str2) and idx_decimal_1<len(str1):
		return -1 if is_negative_str1 else 1;
	if idx_decimal_2<len(str2) and idx_decimal_1==len(str1):
		return 1 if is_negative_str1 else -1;
	
	#same
	return 0;
	

print compare_str("-1.1", "0.1.3");
print compare_str("-1.1", "0");
print compare_str("23.4511", "-1000.00");
print compare_str("4.00", "6.00");
print compare_str("-23.4511", "-23.4");
print compare_str("-23.4511", "-23.4512");
print compare_str("-23.4511", "-23.4511");
print compare_str("23.4511", "23.4512");
print compare_str("23.4511", "23.4511");