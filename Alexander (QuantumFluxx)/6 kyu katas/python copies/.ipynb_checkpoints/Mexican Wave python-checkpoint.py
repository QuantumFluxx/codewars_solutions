{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "ba01e463",
   "metadata": {},
   "outputs": [],
   "source": [
    "def wave(people):\n",
    "    if len(people) == 0:\n",
    "        return []\n",
    "    else:\n",
    "        people = people.lower()\n",
    "        the_waves = []\n",
    "        for e,i in enumerate(people):\n",
    "            if i == \" \":\n",
    "                continue\n",
    "            else:\n",
    "                the_waves.append(people[:e] + people[e].upper() + people[e+1:])\n",
    "        return the_waves"
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
