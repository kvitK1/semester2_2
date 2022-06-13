"""queuing system."""

import random
from arrays import Array
from llistqueue import Queue
from simpeople import TicketAgent, Passenger

class TicketCounterSimulation:
    """
    Implementation of the main simulation class.
    """

    def __init__(self, numAgents, numMinutes, betweenTime, serviceTime):
        """Create a simulation object."""
        self._arriveProb = 1.0 / betweenTime
        self._serviceTime = serviceTime
        self._numMinutes = numMinutes
        self._passengerQ = Queue()
        self._theAgents = Array(numAgents)
        for i in range(numAgents):
            self._theAgents[i] = TicketAgent(i+1)
        self._totalWaitTime = 0
        self._numPassengers = 0

    def run(self):
        """Run the simulation using the parameters supplied earlier."""
        for curTime in range(self._numMinutes + 1) :
            self._handleArrival(curTime)
            self._handleBeginService(curTime)
            self._handleEndService(curTime)

    def _handleArrival(self, curTime):
        """rule1"""
        bol = self.check_arrival()
        if bol:
            self._numPassengers += 1
            passenger = Passenger(self._numPassengers, curTime)
            print(f"Time {curTime}: Passenger {passenger.idNum()} arrived.")
            self._passengerQ.enqueue(passenger)

    def check_arrival(self):
        """Helper function to check probability of customer arrival."""
        num = random.random()
        return num <= self._arriveProb

    def _handleBeginService(self, curTime):
        """rule2"""
        for agent in self._theAgents:
            if agent.isFree() and not self._passengerQ.isEmpty():
                passenger = self._passengerQ.dequeue()
                agent.startService(passenger, curTime+self._serviceTime)
                self._totalWaitTime += curTime - passenger.timeArrived()
                print(f"Time {curTime}: Agent {agent.idNum()} started serving\
passenger {passenger.idNum()}")

    def _handleEndService(self, curTime):
        """rule3"""
        for agent in self._theAgents:
            if agent.isFinished(curTime):
                passenger = agent.stopService()
                print(f"Time {curTime}: Agent {agent.idNum()}\
stopped serving passenger {passenger.idNum()}")

    def printResults(self):
        """Print the simulation results."""
        numServed = self._numPassengers - len(self._passengerQ)
        avgWait = float(self._totalWaitTime)/numServed
        print("")
        print("Number of passengers served = ", numServed)
        print(f"Number of passengers remaining in line = {len(self._passengerQ)}")
        print("The average wait time was %4.2f minutes." % avgWait)

def driver():
    """Driver function."""
    agents = int(input("Enter number of agents: "))
    minutes = int(input("Enter number of minutes: "))
    beetwentime = int(input("Enter average amount of time between passengers` arrival: "))
    servicetime = int(input("Enter average amount of time to serve a transaction: "))
    tickets_queue = TicketCounterSimulation(agents, minutes, beetwentime, servicetime)
    # random.seed(4500)
    tickets_queue.run()
    tickets_queue.printResults()

if __name__ == "__main__":
    driver()
