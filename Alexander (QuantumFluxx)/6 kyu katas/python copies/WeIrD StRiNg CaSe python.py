{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "d8151716",
   "metadata": {},
   "outputs": [],
   "source": [
    "def to_weird_case(string):\n",
    "    i = 0\n",
    "    result = ''\n",
    "    for c in string:\n",
    "        if(i%2==0):\n",
    "            result += c.upper()\n",
    "        else:\n",
    "            result += c.lower()\n",
    "\n",
    "        if(c==' '):  \n",
    "            i=0\n",
    "        else:\n",
    "            i+=1\n",
    "\n",
    "    return result"
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
