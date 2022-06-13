"""queuing system, initial classes."""


class Passenger:
    """
    Used to store and manage information
    related to airline passenger.

    Attributes:
    -----------
        idNum: int
            id number
        arrivalTime: int
            arriving time
    """

    def __init__(self, idNum, arrivalTime):
        """Creates passenger object."""
        self._idNum = idNum
        self._arrivalTime = arrivalTime

    def idNum(self):
        """Gets passenger`s id number."""
        return self._idNum

    def timeArrived(self):
        """Gets passenger`s arrival time."""
        return self._arrivalTime


class TicketAgent:
    """
    Used to store and manage information
    related to airline ticket agent.

    Attributes:
    -----------
        idNum: int
            id number
        passenger: None|Passenger
            passenger, default to None
        stopTime: -1|int
            finished time, default to -1
    """

    def __init__(self, idNum):
        """Creates ticket agent object."""
        self._idNum = idNum
        self._passenger = None
        self._stopTime = -1

    def idNum(self):
        """Gets ticket agent`s id number."""
        return self._idNum

    def isFree(self):
        """Determines if ticket agent is free to assist passenger."""
        return self._passenger is None

    def isFinished(self, curTime):
        """Determines if ticket agent has finished helping passenger."""
        return self._passenger is not None and self._stopTime == curTime

    def startService(self, passenger, stopTime):
        """Indicates ticket agent has begun assisting passenger."""
        self._passenger = passenger
        self._stopTime = stopTime

    def stopService(self):
        """Indicates ticket agent has finished helping passenger."""
        thePassenger = self._passenger
        self._passenger = None
        return thePassenger
