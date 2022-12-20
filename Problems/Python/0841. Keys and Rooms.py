from typing import List


class Solution:
    """
    Intuition:
        This problem actually ask us if we can travers all graph.
        Here rooms are like graph nodes and keys are like edges.

    Solution: (DFS)

        1.  Create a "visited" set where we will track
            the rooms we have visited.

        2.  Starting from 0th room, we will take the
            key for nxt room, make it visited and go
            to the room if it is not visited.

        3.  Continue the 2nd step until we can reach
            our gained rooms.

        4.  Return true if the visited room and the rooms
            have same length, else false.

    Complexity:
        Time:   O(n+m) where n is number of room
                and m is number of keys.
        Space:  O(n) where n is size of visited room.
    """

    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = {0}

        def dfs(room: int):
            for nxt_room in rooms[room]:
                if nxt_room not in visited:
                    visited.add(nxt_room)
                    dfs(nxt_room)

        dfs(0)

        return len(visited) == len(rooms)


obj = Solution()

print(obj.canVisitAllRooms(([[1], [2], [3], []])))
