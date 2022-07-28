{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "a63fd4e3",
   "metadata": {},
   "source": [
    "## DESCRIPTION:\n",
    "Given a 2D ( nested ) list ( array, vector, .. ) of size m * n, your task is to find the sum of the minimum values in each row.\n",
    "\n",
    "For Example:\n",
    "```\n",
    "[ [ 1, 2, 3, 4, 5 ]        #  minimum value of row is 1\n",
    ", [ 5, 6, 7, 8, 9 ]        #  minimum value of row is 5\n",
    ", [ 20, 21, 34, 56, 100 ]  #  minimum value of row is 20\n",
    "]\n",
    "```\n",
    "So the function should return 26 because the sum of the minimums is 1 + 5 + 20 = 26.\n",
    "\n",
    "Note: You will always be given a non-empty list containing positive values.\n",
    "\n",
    "## Solution:\n",
    "```python\n",
    "def sum_of_minimums(numbers):\n",
    "    return sum(map(min, numbers))\n",
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
