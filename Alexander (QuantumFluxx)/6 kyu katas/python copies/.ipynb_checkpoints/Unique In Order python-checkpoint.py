{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "2efb8aec",
   "metadata": {},
   "outputs": [],
   "source": [
    "def unique_in_order(iterable):\n",
    "    chars = []\n",
    "    for i in range(len(iterable)):\n",
    "        if i == 0 or iterable[i] != iterable[i-1]:\n",
    "            chars.append(iterable[i])\n",
    "    return chars"
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
