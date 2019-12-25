class Solution:
    """
    @param gas: An array of integers
    @param cost: An array of integers
    @return: An integer
    """
    def canCompleteCircuit(self, gas, cost):
        if not gas or not cost:
            return -1
        gas_recorded = 0
        gas_amount = 0
        pos = 0
        for i in range(len(gas)):
            gas_amount += gas[i] - cost[i]
            gas_recorded += gas[i] - cost[i]
            if gas_amount < 0:
                pos = i + 1
                gas_amount = 0
        if gas_recorded >= 0:
            return pos
        return -1