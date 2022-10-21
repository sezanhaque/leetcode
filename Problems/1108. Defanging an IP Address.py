class Solution:
    def defangIPaddr(self, address: str) -> str:
        idx = 0
        while idx < len(address):
            if address[idx] == ".":
                address = address[:idx] + "[.]" + address[idx + 1 :]
                idx += 2
            idx += 1
        return address

    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")


print(Solution.defangIPaddr(0, "1.1.1.1"))
print(Solution.defangIPaddr(0, "255.100.50.0"))
