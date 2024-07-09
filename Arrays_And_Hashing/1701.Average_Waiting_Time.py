class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        customer_awaited_times = 0
        next_idle_time = 0
        for arrival, awaiting_time in customers:
            waited_until_idle = next_idle_time - arrival if arrival < next_idle_time else 0
            start_proccessing = max(arrival, next_idle_time)
            finished = start_proccessing + awaiting_time
            customer_awaited_times += waited_until_idle + (finished - start_proccessing) 
            next_idle_time = finished

        return customer_awaited_times / len(customers)
