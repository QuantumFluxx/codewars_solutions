{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "069c3b91",
   "metadata": {},
   "source": [
    "## DESCRIPTION:\n",
    "Clock shows h hours, m minutes and s seconds after midnight.\n",
    "\n",
    "Your task is to write a function which returns the time since midnight in milliseconds.\n",
    "```\n",
    "Example:\n",
    "h = 0\n",
    "m = 1\n",
    "s = 1\n",
    "\n",
    "result = 61000\n",
    "```\n",
    "## Solution:\n",
    "```python\n",
    "def past(h, m, s):\n",
    "    return (3600*h + 60*m + s) * 1000\n",
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
