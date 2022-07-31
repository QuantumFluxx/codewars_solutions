{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "7a153848",
   "metadata": {},
   "outputs": [],
   "source": [
    "def scramble(s1, s2):\n",
    "    for c in set(s2):\n",
    "        if s1.count(c) < s2.count(c):\n",
    "            return False\n",
    "    return True"
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
