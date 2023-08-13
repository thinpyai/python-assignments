def calculate_cheapest(route_cost: list, start: int, dest: int) -> int:
    """
    Calculate the cheapest cost to target destination.
    (start)
         1
      0 ---> 1
      ^      | 2
    4 |      v
      3 <--- 2 (dest)
          3
    route_cost : cost in direction of 0 ~ end e.g., 1,2,3,4.
    start : starting point e.g., 0.
    dest : ending point e.g., 2.
    """
    full_route_cost = 0
    for i in route_cost:
        full_route_cost += i 
    
    clockwise_cost = 0
    for i in range(start, dest):
        clockwise_cost += route_cost[i]

    counterclockwise_cost = full_route_cost-clockwise_cost

    # return the cheapest cost (clockwise or counterclockwise)
    return min(clockwise_cost, counterclockwise_cost)

    
if __name__ == "__main__":
    k = [1,2,3,4]
    n=0
    b=1
    result = calculate_cheapest(k,n,b)
    print(result) # expect 1


