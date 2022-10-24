class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        uniqueEmails = set()
        for email in emails:
            # Find "@"
            localName, domainName = email.split("@")

            # Find + index
            localName = localName.split("+")[0]

            # Replace "."
            localName = localName.replace(".", "")

            # Join
            email = localName + "@" + domainName

            uniqueEmails.add(email)

        return len(uniqueEmails)


print(
    Solution.numUniqueEmails(
        0,
        [
            "test.email+alex@leetcode.com",
            "test.e.mail+bob.cathy@leetcode.com",
            "testemail+david@lee.tcode.com",
        ],
    )
)
