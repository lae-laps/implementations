gcc=gcc -Wall -lm

main: main.c
	${gcc} -c main.c
	${gcc} -c neuralnet.c
	${gcc} -o main main.o neuralnet.o
	rm *.o

clean:
	rm -f main *.o

