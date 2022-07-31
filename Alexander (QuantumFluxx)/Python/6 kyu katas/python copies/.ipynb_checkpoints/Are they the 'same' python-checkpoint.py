{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "5f572c38",
   "metadata": {},
   "outputs": [],
   "source": [
    "def comp(array1, array2):\n",
    "    if array1 is None or array2 is None:\n",
    "        return False\n",
    "    return sorted([num**2 for num in array1]) == sorted(array2)"
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
