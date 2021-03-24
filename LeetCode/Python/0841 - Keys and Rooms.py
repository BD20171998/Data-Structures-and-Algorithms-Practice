'''
841. Keys and Rooms
https://leetcode.com/problems/keys-and-rooms/submissions/
'''


def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
    opened = set()
    queue = [0]

    while(queue):
        room = queue.pop()
        opened.add(room)
        for i in range(len(rooms[room])):
            if rooms[room][i] not in queue and rooms[room][i] not in opened:
                queue.append(rooms[room][i])

    if len(opened) == len(rooms):
        return True
    else:
        return False
