{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "c39ce179",
   "metadata": {},
   "source": [
    "## DESCRIPTION:\n",
    "There is a queue for the self-checkout tills at the supermarket. Your task is write a function to calculate the total time required for all the customers to check out!\n",
    "\n",
    "input\n",
    "\n",
    "customers: an array of positive integers representing the queue. Each integer represents a customer, and its value is the amount of time they require to check out.\n",
    "\n",
    "n: a positive integer, the number of checkout tills.\n",
    "\n",
    "output\n",
    "\n",
    "The function should return an integer, the total time required.\n",
    "\n",
    "\n",
    "## Solution:\n",
    "```python\n",
    "def queue_time(customers, n):\n",
    "    l=[0]*n\n",
    "    for i in customers:\n",
    "        l[l.index(min(l))]+=i\n",
    "    return max(l)\n",
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
