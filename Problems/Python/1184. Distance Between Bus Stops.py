def distanceBetweenBusStops(
    self, distance: list[int], start: int, destination: int
) -> int:
    if start > destination:
        start, destination = destination, start
    from_left = sum(distance[start:destination])
    from_right = sum(distance[destination:] + distance[:start])
    return from_left if from_left < from_right else from_right


def distanceBetweenBusStops(
    self, distance: list[int], start: int, destination: int
) -> int:
    a = min(start, destination)
    b = max(start, destination)
    c = sum(distance[a:b])
    return min(c, sum(distance) - c)


# print(distanceBetweenBusStops(0, [1, 2, 3, 4], 0, 3))
# start > destination
# print(distanceBetweenBusStops(0, [1, 2, 3, 4], 3, 0))
# print(distanceBetweenBusStops(0, [1, 2, 3, 4], 0, 1))
# print(distanceBetweenBusStops(0, [1, 2, 3, 4], 0, 2))
print(distanceBetweenBusStops(0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0, 6))
# print(distanceBetweenBusStops(0, [7, 10, 1, 12, 11, 14, 5, 0], 7, 2))
# print(
#     distanceBetweenBusStops(0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1, 8)
# )
