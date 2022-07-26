{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "0e8d3b86",
   "metadata": {},
   "outputs": [],
   "source": [
    "def fibonacci(n: int) -> int:\n",
    "    a, b = 0, 1\n",
    "    for i in range(n):\n",
    "        a, b = b, a + b\n",
    "    return a"
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
