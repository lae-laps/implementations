[0x00001149]> pdf
            ; DATA XREF from dbg._start @ 0x1068(r)
┌ 110: int main (int argc, char **argv, char **envp);
│           ; var signed int64_t var_4h @ rbp-0x4
│           ; var int64_t var_8h @ rbp-0x8
│           ; var int64_t var_ch @ rbp-0xc
│           0x00001149      55             push rbp
│           0x0000114a      4889e5         mov rbp, rsp
│           0x0000114d      4883ec10       sub rsp, 0x10
│           0x00001151      488d05ac0e00.  lea rax, str.Fibbonacci_numbers ; 0x2004 ; "Fibbonacci numbers"
│           0x00001158      4889c7         mov rdi, rax                ; const char *s
│           0x0000115b      e8d0feffff     call sym.imp.puts           ; int puts(const char *s)
│           0x00001160      c745f4010000.  mov dword [var_ch], 1
│           0x00001167      c745f8010000.  mov dword [var_8h], 1
│           0x0000116e      c745fc010000.  mov dword [var_4h], 1
│       ┌─< 0x00001175      eb30           jmp 0x11a7
│       │   ; CODE XREF from main @ 0x11ae(x)
│      ┌──> 0x00001177      8b55f4         mov edx, dword [var_ch]
│      ╎│   0x0000117a      8b45f8         mov eax, dword [var_8h]
│      ╎│   0x0000117d      01d0           add eax, edx
│      ╎│   0x0000117f      8945fc         mov dword [var_4h], eax
│      ╎│   0x00001182      8b45fc         mov eax, dword [var_4h]
│      ╎│   0x00001185      89c6           mov esi, eax
│      ╎│   0x00001187      488d05890e00.  lea rax, [0x00002017]       ; "%d\n"
│      ╎│   0x0000118e      4889c7         mov rdi, rax                ; const char *format
│      ╎│   0x00001191      b800000000     mov eax, 0
│      ╎│   0x00001196      e8a5feffff     call sym.imp.printf         ; int printf(const char *format)
│      ╎│   0x0000119b      8b45f8         mov eax, dword [var_8h]
│      ╎│   0x0000119e      8945f4         mov dword [var_ch], eax
│      ╎│   0x000011a1      8b45fc         mov eax, dword [var_4h]
│      ╎│   0x000011a4      8945f8         mov dword [var_8h], eax
│      ╎│   ; CODE XREF from main @ 0x1175(x)
│      ╎└─> 0x000011a7      817dfc40420f.  cmp dword [var_4h], 0xf4240 ; '@B\x0f'
│      └──< 0x000011ae      7ec7           jle 0x1177
│           0x000011b0      b800000000     mov eax, 0
│           0x000011b5      c9             leave
└           0x000011b6      c3             ret
[0x00001149]> 
