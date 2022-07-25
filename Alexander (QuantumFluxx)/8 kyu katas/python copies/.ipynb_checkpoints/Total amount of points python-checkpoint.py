{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "5d239f56",
   "metadata": {},
   "outputs": [],
   "source": [
    "def points(games):\n",
    "    result = 0\n",
    "    for item in games:\n",
    "        result += 3 if item[0] > item[2] else 0     \n",
    "        result += 1 if item[0] == item[2] else 0\n",
    "    return result"
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
