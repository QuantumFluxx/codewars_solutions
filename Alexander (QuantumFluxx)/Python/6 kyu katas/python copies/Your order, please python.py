{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "e80b0d70",
   "metadata": {},
   "outputs": [],
   "source": [
    "def order(sentence):\n",
    "    words = []\n",
    "    for i in range(1, 10):\n",
    "        for word in sentence.split(' '):\n",
    "            if str(i) in word:\n",
    "                words.append(word)\n",
    "    return ' '.join(words)"
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
