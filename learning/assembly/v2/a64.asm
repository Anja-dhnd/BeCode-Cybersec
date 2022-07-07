bits 64

section .data
   message db 'Hello World', 10

section .text
   global _start
   _start:
    ; write the msg:
        mov rax, 1
        mov rdi, 1
        mov rsi, message
        mov rdx, 13+1
        syscall ; syscall calls the kernel and clean registers
    ; allows to exit:
        mov rax, 60 ;accumulator
        mov rdi, 0
        syscall

