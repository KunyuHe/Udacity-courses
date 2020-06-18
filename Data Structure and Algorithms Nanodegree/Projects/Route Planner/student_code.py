import heapq
import math
from typing import Tuple, Type, List, Dict, Union

from helpers import Map


def dist(start: Tuple[float, float], end: Tuple[float, float]) -> float:
    """Returns the euclidean distance between two coordinates."""
    return math.hypot(end[0] - start[0], end[1] - start[1])


def best_route(prev_curr: Dict[int, int],
               start: int, goal: int) -> Union[List[int], None]:
    """
    Find the best path with minimum cost backwards.

    :param prev_curr: Mapping previous intersection indices to current.
    :param start: index of the starting intersection
    :param goal: index of the target intersection
    :return: representing the best route from `start` to `goal`
    """
    node = goal
    path = []

    if node not in prev_curr:
        return

    while node != start:
        path.append(node)
        node = prev_curr[node]

    path.append(start)
    return path[::-1]


def shortest_path(M: Type[Map], start: int, goal: int) -> Union[
    List[int], None]:
    """
    Given the map and the start, end intersection index, find the best route
    with minimum total distance from `start` to `goal`.

    :param M: Map. The `intersections` attribute contains a mapping from
        intersection index (int) to its coordinates ([int, int]). The `roads`
        attribute maps the intersection index (int, as array index)
        to its connected intersections ([int]) and is a list of lists.
    :param start: index of the starting intersection.
    :param goal: index of the target intersection.
    :return: representing the best route from `start` to `goal`.
    """
    prev_curr, cost_so_far = {start: None}, {start: 0}
    # Use heap for faster lookup
    frontier = [(0, start)]

    while len(frontier) > 0:
        _, curr = heapq.heappop(frontier)
        if curr == goal:
            break

        for neighbor in M.roads[curr]:
            cost = dist(M.intersections[curr], M.intersections[neighbor])
            new_cost = cost_so_far.get(curr, 0) + cost
            # Admissible heuristic
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                prev_curr[neighbor] = curr
                cost_so_far[neighbor] = new_cost
                heapq.heappush(frontier, (new_cost, neighbor))

    return best_route(prev_curr, start, goal)
