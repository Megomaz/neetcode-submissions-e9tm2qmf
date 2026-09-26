from collections import defaultdict
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        size = [len(acc) - 1 for acc in accounts]
        parent = [i for i in range(len(accounts))]

        def find(node):
            while node != parent[node]:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node

        def union(n1,n2):
            p1,p2 = find(n1), find(n2)

            if p1 == p2:
                return False
            
            if size[p1] > size[p2]:
                size[p1] += size[p2]
                parent[p2] = p1
            else:
                size[p2] += size[p1]
                parent[p1] = p2

            return True

        # email -> name
        email_to_idx = defaultdict(list)
        id_to_emails = defaultdict(set)

        for idx,acc in enumerate(accounts):
            name, *emails = acc
            
            for e in emails:
                email_to_idx[e].append(idx)
        
        for e, values in email_to_idx.items():

            for i in range(1,len(values)):
                prev,curr = values[i-1], values[i]

                union(prev,curr)

        for idx, acc in enumerate(accounts):
            root = find(idx)

            for email in acc[1:]:
                id_to_emails[root].add(email)

        res = []
        for idx, emails in id_to_emails.items():
            name = accounts[idx][0]
            curr = []
            curr.append(name)
            for email in sorted(emails):
                curr.append(email)
            res.append(curr)

        return res

        