"""
Implement LRU cache by a double linked list and a map
When insert new key-value entry:
		if the cache has reached its capacity, 
				remove the tail of the list, at the same time delete key->node from map
				then append new node in the head, while inserting key->node into the map
		if hasn't reached its capacity,
				append new node in the head directly, while inserting key->node into the map
				
when get value by key:
		if key don't exist in cache
			return None;
		if key exist in cache
			return value, at the same time move the node to the head
			
offer two main method : get, put
"""
class Node:
	def __init__(self, key, value):
		self.next = None;
		self.pre = None;
		self.key = key;
		self.value = value;


class LRU_Cache(object):

	def __init__(self, capacity):
		self.num = 0;
		self.capacity = capacity;
		self.head = None;
		self.tail = None;
		
		# store key -> node in the double linked list by key.
		self.key_node = {};

	"""
	if key doesn't exist, return None;
	"""
	def get(self, key):
		if self.capacity == 0:
			return None;
		if self.key_node.has_key(key):
			node = self.key_node[key];
			self.__move_to_head(node);
			return node.value;
		else:
			return None;

	def put(self, key, value):
		if self.key_node.has_key(key):
			node = self.key_node[key];
			node.value = value;
			self.__move_to_head(node);
		else:
			node = Node(key, value);
			#may be a little inefficient, but be more readable
			#in order to resue the method of "move_to_head"
			if self.num >= self.capacity:
				self.__replace_last(node);
				self.__move_to_head(node);
			else:
				self.__append_last(node);
				self.__move_to_head(node);
		#self.debug();

	def debug(self):
		node = self.head;
		while node != None:
			print node.key,
			node = node.next;
		print "head:"+str(self.head.key)+" tail:"+str(self.tail.key);


	def __move_to_head(self, node):
		if node == self.head:
			return;
		pre_node = node.pre;
		pre_node.next = node.next;
		if node.next == None:
			self.tail = pre_node;
		else:
			node.next.pre = pre_node;
		node.pre = None;
		node.next = self.head;
		self.head.pre = node;
		self.head = node;

	def __replace_last(self, node):
		node.pre = self.tail.pre;
		if self.tail.pre != None:
			self.tail.pre.next = node;
		else:
			self.head = node;
		del self.key_node[self.tail.key];
		self.tail = node;
		self.key_node[self.tail.key] = self.tail;

	def __append_last(self, node):
		self.key_node[node.key] = node;
		self.num += 1; 
		if self.head == None:
			self.head = node;
			self.tail = node;
			return;
		self.tail.next = node;
		node.pre = self.tail;
		self.tail = node;
		

cache = LRU_Cache(3);
cache.put(1,1);
cache.put(2,2);
cache.put(3,3);
print cache.get(4);
print cache.get(2);
print cache.get(3);
cache.debug();
cache.put(4,4);
print cache.get(1);
cache.debug();
