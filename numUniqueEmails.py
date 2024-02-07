"""
929. Unique Email Addresses
Every valid email consists of a local name and a domain name, separated by the '@' sign. Besides lowercase letters,
the email may contain one or more '.' Or '+'.

For example, in "alice@leetcode.com", "alice" is the local name, and "leetcode.com" is the domain name.
If you add periods '.' Between some characters in the local name part of an email address,
mail sent there will be forwarded to the same address without dots in the local name.
Note that this rule does not apply to domain names.

For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.
If you add a plus '+' in the local name, everything after the first plus sign will be ignored.
This allows certain emails to be filtered. Note that this rule does not apply to domain names.

For example, "m.y+name@email.com" will be forwarded to "my@email.com".
It is possible to use both of these rules at the same time.

Given an array of strings emails where we send one email to each (emails)[i],
return the number of different addresses that actually receive mails.
"""
from typing import List


def num_unique_emails(self, emails: List[str]) -> int:
    if not emails:
        return 0
    n = len(emails)
    addresses = []
    for i in range(n):
        # we iterate through all emails, the extract the local_name and domain_name of every one of them
        temp = emails[i].split('@')  # split function return array we 2 strings.
        local = temp[0]  # the left side is local_name
        domain = temp[1]  # the tight side is domain_name
        plus = local.find("+")  # find return the index of given char is in string if the char is missing he returns -1.
        point = local.find(".")
        if plus != -1:
            # if we found '+' in local_name so all the right chars from '+' is not relevant, and we remove them
            local = local[:plus]
        if point != -1:
            # if we found '.' in local_name, so we can remove this symbol because it is not relevant to local_name
            local = local.replace(".", "")
            # finally, we add together the local_name without all the not necessary chars.
        addresses.append(local + "@" + domain)
    # now we create a set of all the uniques emails.
    addresses = set(addresses)
    # we return the number of uniques emails.
    return len(addresses)
