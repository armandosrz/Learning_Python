import operator, math, random, copy, sys, os.path, bisect

class Queue:
	"""Queue is an abstract class/interface. There are three types:
		Stack(): A Last In First Out Queue.
		FIFOQueue(): A First In First Out Queue.
		PriorityQueue(order, f): Queue in sorted order (default min-first).
	Each type supports the following methods and functions:
		q.append(item)  -- add an item to the queue
		q.extend(items) -- equivalent to: for item in items: q.append(item)
		q.pop()         -- return the top item from the queue
		len(q)          -- number of items in q (also q.__len())
		item in q       -- does q contain item?
	Note that isinstance(Stack(), Queue) is false, because we implement stacks
	as lists.  If Python ever gets interfaces, Queue will be an interface."""

	def __init__(self):
		abstract

	def extend(self, items):
		for item in items: self.append(item)

class PriorityQueue(Queue):
	"""A queue in which the minimum (or maximum) element (as determined by f and
	order) is returned first. If order is min, the item with minimum f(x) is
	returned first; if order is max, then it is the item with maximum f(x).
	Also supports dict-like lookup."""
	def __init__(self, order=min, f=lambda x: x):
		update(self, A=[], order=order, f=f)
	def enqueue(self, item):
		bisect.insort(self.A, (self.f(item), item))
	def __len__(self):
		return len(self.A)
	def dequeue(self):
		if self.order == min:
			return self.A.pop(0)[1]
		else:
			return self.A.pop()[1]
	def __contains__(self, item):
		return some(lambda (_, x): x == item, self.A)
	def __getitem__(self, key):
		for _, item in self.A:
			if item == key:
				return item
	def __delitem__(self, key):
		for i, (value, item) in enumerate(self.A):
			if item == key:
				self.A.pop(i)
				return

def update(x, **entries):
	"""Update a dict; or an object with slots; according to entries.
	>>> update({'a': 1}, a=10, b=20)
	{'a': 10, 'b': 20}
	>>> update(Struct(a=1), a=10, b=20)
	Struct(a=10, b=20)
	"""
	if isinstance(x, dict):
		x.update(entries)
	else:
		x.__dict__.update(entries)
	return x

def some(predicate, seq):
	"""If some element x of seq satisfies predicate(x), return predicate(x).
	>>> some(callable, [min, 3])
	1
	>>> some(callable, [2, 3])
	0
	"""
	for x in seq:
		px = predicate(x)
		if  px: return px
	return False

class test():
	def __init__(self, frecuency, name):
		self.frecuency = frecuency
		self.name = name
	def __cmp__(self, other):
		return cmp(self.frecuency, other.frecuency)
	def __eq__(self, other):
		if (self.name == other.name):
			return True
		else:
			return False


pq = PriorityQueue()

alan = test(45, "Albert")

pq.enqueue(test(8, "ALAN"))
pq.enqueue(test(4, "Tom"))
pq.enqueue(alan)

allon = test(12, "Albert")

if (pq.__contains__(allon)):
	if pq.__getitem__(allon).frecuency > allon.frecuency:
		pq.__delitem__(allon)
		pq.enqueue(allon)

"""
a = pq.__getitem__(alan)
pq.__delitem__(alan)
print str(a.frecuency) + " " + a.name
a.frecuency = 5
pq.enqueue(a)
"""
while pq:
	next_level = pq.dequeue()
	print str(next_level.frecuency) + " " + next_level.name
