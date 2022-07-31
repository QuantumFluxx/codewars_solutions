{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "c030d661",
   "metadata": {},
   "outputs": [],
   "source": [
    "def pig_it(text):\n",
    "    return \" \".join([\"{}{}ay\".format(c[1:], c[0]) if c.isalpha() else c for c in text.split()])"
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
