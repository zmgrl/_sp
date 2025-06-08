        .global mult3

        .text
mult3:
        mov     %rdi, %rax                # result (rax) initially holds x
        imul   %rsi, %rax                # if so, set result to y
        imul   %rdx, %rax                # if so, set result to z
        ret                               # the max will be in eax