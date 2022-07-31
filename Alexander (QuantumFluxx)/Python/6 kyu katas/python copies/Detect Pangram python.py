{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "767db734",
   "metadata": {},
   "outputs": [],
   "source": [
    "import string\n",
    "\n",
    "def is_pangram(s):\n",
    "    s = s.lower()\n",
    "    for char in 'abcdefghijklmnopqrstuvwxyz':\n",
    "        if char not in s:\n",
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
