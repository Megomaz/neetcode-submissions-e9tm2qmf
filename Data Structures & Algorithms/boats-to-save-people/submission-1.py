class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        q = deque(people)
        boats = 0

        while q:
            weight = 0
            if q and weight + q[-1] <= limit:
                weight += q.pop()

            if q and weight + q[0] <= limit:
                weight += q.popleft()

            boats += 1
        return boats