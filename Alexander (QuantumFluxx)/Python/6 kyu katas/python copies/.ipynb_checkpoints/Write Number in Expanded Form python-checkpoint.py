{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "3fc879cb",
   "metadata": {},
   "outputs": [],
   "source": [
    "def expanded_form(num):\n",
    "    s = []\n",
    "    i = len(str(num)) -1\n",
    "    for n in str(num):\n",
    "        if n != \"0\":\n",
    "            s.append(n + \"0\" * i)\n",
    "        i -= 1\n",
    "    return \" + \".join(s)"
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
