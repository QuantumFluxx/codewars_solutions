{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "a9ef75ba",
   "metadata": {},
   "outputs": [],
   "source": [
    "def likes(names):\n",
    "    l = len(names)\n",
    "    if l == 0: return 'no one likes this'\n",
    "    if l == 1: return '{} likes this'.format(names[0])\n",
    "    if l == 2: return '{} and {} like this'.format(names[0], names[1])\n",
    "    if l == 3: return '{}, {} and {} like this'.format(names[0], names[1], names[2])\n",
    "    return '{}, {} and {} others like this'.format(names[0], names[1], len(names)-2)"
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
