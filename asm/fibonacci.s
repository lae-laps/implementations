# Simple ASM program to calculate a Fibonacci number sequence
#
#VARIABLES:
# %eax -> a
# %ebx -> b
# %ecx -> c

.section .data
	list:
		.long 1, 1

.section .text
.globl _start
_start:
	movl $1, %eax
	movl $1, %ebx
loop_1:
	movl %eax, list(,%edi,4)
	add %eax, %ebx
	movl %eax, %ecx
loop_2:
	jmp display
	# print %ecx
	movl %ebx, %eax
	movl %ecx, %ebx
	jmp loop_1

display:
	movl $4, eax
	movl $1, ebx
	# mov content to %ecx - content is already in ecx so no move needed
	movl $4, %edx		# move content length to edx
	int 0x80
	movl $1, %eax
	movl $0, ebx
	int 0x80
	jmp loop_2

exit:
	movl $1, %eax
	int $0x80
