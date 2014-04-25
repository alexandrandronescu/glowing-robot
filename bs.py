''' Five implementations of binary search problem. '''

def iterative_bs(search_item, data):
	data_len = len(data)
	start_index = 0
	stop_index = data_len-1

	while start_index<=stop_index:
		index = start_index + (stop_index-start_index)/2

		if data[index]==search_item:
			return index
		elif search_item<data[index]:
			stop_index = index-1
		elif search_item>data[index]:
			start_index = index+1
		else:
			return -1
	return -1

def temp_bs(start_index, stop_index, search_item, data):
	if start_index>stop_index:
		return -1

	index = start_index + (stop_index-start_index)/2

	if search_item == data[index]:
		return index
	elif search_item < data[index]:
		return temp_bs(start_index, index-1, search_item, data)
	elif search_item > data[index]:
		return temp_bs(index+1, stop_index, search_item, data)
	else:
		return -1

def recursive_bs(search_item, data):
	return temp_bs(0, len(data)-1, search_item, data)


def main():
	test_bs(iterative_bs)
	test_bs(recursive_bs)

def test_bs(bs):
	assert -1 == bs(3, [])
	assert -1 == bs(3, [1])
	assert 0 == bs(1, [1])
	
	assert 0 == bs(1, [1, 3, 5])
	assert 1 == bs(3, [1, 3, 5])
	assert 2 == bs(5, [1, 3, 5])
	assert -1 == bs(0, [1, 3, 5])
	assert -1 == bs(2, [1, 3, 5])
	assert -1 == bs(4, [1, 3, 5])
	assert -1 == bs(6, [1, 3, 5])
	
	assert 0 == bs(1, [1, 3, 5, 7])
	assert 1 == bs(3, [1, 3, 5, 7])
	assert 2 == bs(5, [1, 3, 5, 7])
	assert 3 == bs(7, [1, 3, 5, 7])
	assert -1 == bs(0, [1, 3, 5, 7])
	assert -1 == bs(2, [1, 3, 5, 7])
	assert -1 == bs(4, [1, 3, 5, 7])
	assert -1 == bs(6, [1, 3, 5, 7])
	assert -1 == bs(8, [1, 3, 5, 7])

if __name__ == "__main__":
    main()


