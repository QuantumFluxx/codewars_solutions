{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "a8cca375",
   "metadata": {},
   "outputs": [],
   "source": [
    "def add(l):\n",
    "    return [sum(l[:i+1]) for i in range(len(l))]"
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
