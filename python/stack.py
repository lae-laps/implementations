#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This is an implementation of a stack in python using a class as a type
# To use it create a new stack object and you can just push or pop data onto it

import os

class Stack:
    def __init__(self, wordsize):
        self.data = []
        self.stack_pointer = 0
        self.wordsize = wordsize
        
    def push(self, value):
        if isinstance(value, str):
            # emulate stack truncating by asuming each character uses up 8 bits (unaccurate)
            max_bytes = self.wordsize / 8
            value = value[0 : max_bytes]
        else:
            pass

        self.data.append(value)
        self.stack_pointer += 1
        
    def pop(self):
        ret = self.data.pop(len(self.data) - 1)
        if self.stack_pointer < 0:
            self.stack_pointer -= 1
        return ret
        
    def check(self) -> bool: 
        if self.stack_pointer > 0:
            return self.stack_pointer
        else:
            return False
            
    def print_stack(self):
        #for _ in range(len(str(element)) + 4):
        max = 0
        
        for element in self.data:
            if isinstance(element, int) or isinstance(element, float):
                #length = (element.bit_length() + 7) // 8
                length = len(str(element))
            else:
                length = len(element)
            if length > max:
                max = length
                
            separator = '       ' + '-' * (max + 4)

        for i in range(0, self.stack_pointer):
            if i == 0:
                print(f"{separator}\n{hex(i):6s} | {self.data[i]:{max}} |\n{separator}")
            else:
                print(f"{hex(i):6s} | {self.data[i]:{max}} |\n{separator}")


# testing the stack

if __name__ == "__main__":
    try:
        s = Stack(64)

        #s.push(1234)
        #s.push("dsjf")
        #s.pop()
        #s.print_stack()
        #print(s.check())

        # dynamic testing
        os.system("clear")
        while True:
            s.print_stack()
            exp = input(">> ")
            try:
                exec(exp)
            except:
                pass
            os.system("clear")

    except KeyboardInterrupt:
        print("exiting...")
        exit(0)
