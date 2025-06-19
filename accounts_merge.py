# https://leetcode.com/problems/accounts-merge

from collections import defaultdict
from typing import List


class UnionFind(object):
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, current):
        if self.parent[current] != current:
            self.parent = self.find(self.parent[current])

        return self.parent

    def union(self, a, b):
        parent_a, parent_b = self.find(a), self.find(b)
        if parent_a == parent_b:
            return False

        if self.rank[parent_a] > self.rank[parent_b]:
            self.parent[parent_b] = parent_a
            self.rank[parent_a] += self.rank[parent_b]
        else:
            self.parent[parent_a] = parent_b
            self.rank[parent_b] += self.rank[parent_a]

        return True


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        email_to_account = {}

        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in email_to_account:
                    uf.union(i, email_to_account[email])
                else:
                    email_to_account[email] = i

        email_groups = defaultdict(list)
        for email, i in email_to_account.items():
            leader = uf.find(i)
            email_groups[leader].append(email)

        res = []
        for index, emails in email_groups.items():
            r = [accounts[index][0]]
            r += sorted(emails)
            res.append(r)

        return res


if __name__ == '__main__':
    sol = Solution()
    accounts = [["John", "johnsmith@mail.com", "john_newyork@mail.com"],
                ["John", "johnsmith@mail.com", "john00@mail.com"], ["Mary", "mary@mail.com"],
                ["John", "johnnybravo@mail.com"]]
    accounts = sol.accountsMerge(accounts)
    print(accounts)
