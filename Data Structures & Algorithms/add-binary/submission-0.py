class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = []
        lista = list(a)
        listb = list(b)
        if len(lista) < len(listb):
            lista, listb = listb, lista

        carry = 0
        while lista:
            digita = lista.pop()
            digitb = listb.pop() if listb else 0
            digit = int(digita) + int(digitb) + carry
            carry = digit // 2
            digit %= 2
            ans.append(str(digit))

        if carry:
            ans.append(str(carry))

        return "".join(ans[::-1])