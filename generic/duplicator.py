
# Duplicator : given a shape in the matrix constant, defined in b&w as 1 being white and 0 being black, it prints out that shape, that shape made of smaller shapes which are the same, etc ...
# Note: the size of the matrix is not predefined - you can make it as big or small as you want

h = 2 # Number of elements it produces

matrix = [
        [0, 0, 0, 1, 0, 0, 0], 
        [0, 0, 1, 1, 1, 0, 0], 
        [0, 1, 0, 1, 0, 1, 0], 
        [1, 1, 1, 1, 1, 1, 1], 
        [0, 1, 0, 1, 0, 1, 0], 
        [0, 0, 1, 1, 1, 0, 0], 
        [0, 0, 0, 1, 0, 0, 0], 
    ]

block = "#"
empty_block = " "

b_block = ""
b_empty_block = ""

r = 1
q = 1

def set(text):
    global q
    global r
    global b_block
    global b_empty_block
    print("."+text)
    b_block += text
    b_block += "\n"
    b_empty_block += " " * len(text)
    b_empty_block += "\n"
    r += 1

def switch_new_blocks():
    global q
    global r
    global block
    global b_block
    global empty_block
    global b_empty_block
    block = b_block
    empty_block = b_empty_block
    b_block = ""
    b_empty_block = ""
    q = r
    r = 1

for i in range(h):
    print()
    print()
    for row in matrix:
        for n in range(q):
            out = ""
            for col in row:
                if col == 1: 
                    s = block
                else:
                    s = empty_block
                out += s.split('\n')[n]
                out += " "
            set(out)
    switch_new_blocks()

'''
                                                 Example
.      #       
.    # # #     
.  #   #   #   
.# # # # # # # 
.  #   #   #   
.    # # #     
.      #       
.
.                                                   #                                                     
.                                                 # # #                                                   
.                                               #   #   #                                                 
.                                             # # # # # # #                                               
.                                               #   #   #                                                 
.                                                 # # #                                                   
.                                                   #                                                     
.       
.                                    #              #              #                                      
.                                  # # #          # # #          # # #                                    
.                                #   #   #      #   #   #      #   #   #                                  
.                              # # # # # # #  # # # # # # #  # # # # # # #                                
.                                #   #   #      #   #   #      #   #   #                                  
.                                  # # #          # # #          # # #                                    
.                                    #              #              #                                      
.       
.                     #                             #                             #                       
.                   # # #                         # # #                         # # #                     
.                 #   #   #                     #   #   #                     #   #   #                   
.               # # # # # # #                 # # # # # # #                 # # # # # # #                 
.                 #   #   #                     #   #   #                     #   #   #                   
.                   # # #                         # # #                         # # #                     
.                     #                             #                             #                       
.       
.      #              #              #              #              #              #              #        
.    # # #          # # #          # # #          # # #          # # #          # # #          # # #      
.  #   #   #      #   #   #      #   #   #      #   #   #      #   #   #      #   #   #      #   #   #    
.# # # # # # #  # # # # # # #  # # # # # # #  # # # # # # #  # # # # # # #  # # # # # # #  # # # # # # #  
.  #   #   #      #   #   #      #   #   #      #   #   #      #   #   #      #   #   #      #   #   #    
.    # # #          # # #          # # #          # # #          # # #          # # #          # # #      
.      #              #              #              #              #              #              #        
.       
.                     #                             #                             #                       
.                   # # #                         # # #                         # # #                     
.                 #   #   #                     #   #   #                     #   #   #                   
.               # # # # # # #                 # # # # # # #                 # # # # # # #                 
.                 #   #   #                     #   #   #                     #   #   #                   
.                   # # #                         # # #                         # # #                     
.                     #                             #                             #                       
.       
.                                    #              #              #                                      
.                                  # # #          # # #          # # #                                    
.                                #   #   #      #   #   #      #   #   #                                  
.                              # # # # # # #  # # # # # # #  # # # # # # #                                
.                                #   #   #      #   #   #      #   #   #                                  
.                                  # # #          # # #          # # #                                    
.                                    #              #              #                                      
.       
.                                                   #                                                     
.                                                 # # #                                                   
.                                               #   #   #                                                 
.                                             # # # # # # #                                               
.                                               #   #   #                                                 
.                                                 # # #                                                   
.                                                   #                                                     
.       
'''
