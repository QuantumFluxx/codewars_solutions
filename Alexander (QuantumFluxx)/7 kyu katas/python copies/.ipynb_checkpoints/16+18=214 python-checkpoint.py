{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "4c731120",
   "metadata": {},
   "outputs": [],
   "source": [
    "def add(num1, num2):\n",
    "    num1, num2 = str(num1), str(num2)\n",
    "    padding = len(num1) if len(num1) > len(num2) else len(num2)\n",
    "    num1, num2 = num1.zfill(padding), num2.zfill(padding)\n",
    "    num1, num2 = num1[::-1], num2[::-1]\n",
    "    return int(''.join([str(int(i) + int(j)) for i, j in zip(num1, num2)][::-1]))"
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
