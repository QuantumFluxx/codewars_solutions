{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "ed1c8fea",
   "metadata": {},
   "source": [
    "## DESCRIPTION:\n",
    "There is a bus moving in the city, and it takes and drop some people in each bus stop.\n",
    "\n",
    "You are provided with a list (or array) of integer pairs. Elements of each pair represent number of people get into bus (The first item) and number of people get off the bus (The second item) in a bus stop.\n",
    "\n",
    "Your task is to return number of people who are still in the bus after the last bus station (after the last array). Even though it is the last bus stop, the bus is not empty and some people are still in the bus, and they are probably sleeping there :D\n",
    "\n",
    "Take a look on the test cases.\n",
    "\n",
    "Please keep in mind that the test cases ensure that the number of people in the bus is always >= 0. So the return integer can't be negative.\n",
    "\n",
    "The second value in the first integer array is 0, since the bus is empty in the first bus stop.\n",
    "\n",
    "## Solution:\n",
    "```python\n",
    "def number(bus_stops):\n",
    "    return sum([stop[0] - stop[1] for stop in bus_stops])\n",
    "```"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
