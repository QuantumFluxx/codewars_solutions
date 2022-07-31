{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "80c3ce5c",
   "metadata": {},
   "outputs": [],
   "source": [
    "def calculate_total(subtotal, tax, tip):\n",
    "    return round(sum([subtotal, subtotal*tax/100, subtotal*tip/100]), 2)"
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
