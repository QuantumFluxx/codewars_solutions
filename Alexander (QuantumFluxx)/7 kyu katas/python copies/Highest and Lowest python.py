{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "96a6c089",
   "metadata": {},
   "outputs": [],
   "source": [
    "def high_and_low(numbers):\n",
    "    nums = [int(i) for i in numbers.split()]\n",
    "    return \" \".join([str(max(nums)), str(min(nums))])"
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
