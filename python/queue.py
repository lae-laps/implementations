# Simple implementation of a queue just for learning / understanding purposes
# code is not optimized and should not be used as a real data structure

n_max = 10

front = 0
back = 0
queue = []

# initialize the queue to 0
for i in range(n_max):
	queue.append(0)

# definitions

# add to the top of the queue
def enqueue(element):
	global front
	if front > n_max:
		print("queue full")
	queue[front] = element
	front += 1

# remove from the bottom of the queue
def dequeue():
	global back
	if front - back < 1:
		print("no elements left") 

	ret = queue[back]
	back += 1
	return ret

# display the queue
def display():
    print(" | ", end='')
    for i in range(back, front):
        print( "%02d" % (queue[i],), end=' | ')
    print()

# display the queue with empty slots included - usefull to visualize memory layout
def display_center():
    print(" | ", end='')
    for i in range(back):
        print("   | ", end='')
    for i in range(back, n_max):
        if queue[i] == 0:
            print("   | ", end='')
        else:
            print( "%02d" % (queue[i],), end=' | ')
    print()

# shorthand definition to change between the two display modes easily
def a():
    exec("display_center()")

# example data manipulation

enqueue(10)
a()
enqueue(20)
a()
enqueue(15)
a()
dequeue()
a()
enqueue(2)
a()
enqueue(4)
a()
dequeue()
a()
enqueue(9)
a()

