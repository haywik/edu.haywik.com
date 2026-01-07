; NASM assembly code for Windows
; Assemble with: nasm -f win32 ai.asm -o ai.obj
; Link with: link /entry:start /subsystem:console ai.obj kernel32.lib

section .data
    ; Messages
    prompt db "Enter a number (0-9): ", 0
    output1 db "You entered a small number.", 0
    output2 db "You entered a medium number.", 0
    output3 db "You entered a large number.", 0
    invalid db "Invalid input!", 0

section .bss
    input resb 1

section .text
    global _start

extern _GetStdHandle@4
extern _WriteConsoleA@20
extern _ReadConsoleA@20
extern _ExitProcess@4

_start:
    ; Get handle to stdout
    push -11            ; STD_OUTPUT_HANDLE
    call _GetStdHandle@4
    mov ebx, eax        ; Save stdout handle in ebx

    ; Write prompt to console
    push 0              ; lpReserved
    push 0              ; lpNumberOfCharsWritten
    push 21             ; nNumberOfCharsToWrite (length of prompt)
    push prompt         ; lpBuffer
    push ebx            ; hConsoleOutput (stdout handle)
    call _WriteConsoleA@20

    ; Get handle to stdin
    push -10            ; STD_INPUT_HANDLE
    call _GetStdHandle@4
    mov ecx, eax        ; Save stdin handle in ecx

    ; Read input from console
    push 0              ; lpReserved
    push 0              ; lpNumberOfCharsRead
    push 1              ; nNumberOfCharsToRead (read 1 byte)
    push input          ; lpBuffer
    push ecx            ; hConsoleInput (stdin handle)
    call _ReadConsoleA@20

    ; Convert ASCII to integer
    movzx eax, byte [input]
    sub eax, '0'

    ; Decision making
    cmp eax, 3
    jl .small
    cmp eax, 6
    jl .medium
    cmp eax, 9
    jle .large
    jmp .invalid

.small:
    ; Print small number message
    push 0
    push 0
    push 25             ; Length of output1
    push output1
    push ebx
    call _WriteConsoleA@20
    jmp .exit

.medium:
    ; Print medium number message
    push 0
    push 0
    push 26             ; Length of output2
    push output2
    push ebx
    call _WriteConsoleA@20
    jmp .exit

.large:
    ; Print large number message
    push 0
    push 0
    push 25             ; Length of output3
    push output3
    push ebx
    call _WriteConsoleA@20
    jmp .exit

.invalid:
    ; Print invalid input message
    push 0
    push 0
    push 14             ; Length of invalid
    push invalid
    push ebx
    call _WriteConsoleA@20

.exit:
    ; Exit program
    push 0
    call _ExitProcess@4