{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "59a1f4cd",
   "metadata": {},
   "source": [
    "## DESCRIPTION:\n",
    "This time no story, no theory. The examples below show you how to write function accum:\n",
    "```\n",
    "Examples:\n",
    "accum(\"abcd\") -> \"A-Bb-Ccc-Dddd\"\n",
    "accum(\"RqaEzty\") -> \"R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy\"\n",
    "accum(\"cwAt\") -> \"C-Ww-Aaa-Tttt\"\n",
    "The parameter of accum is a string which includes only letters from a..z and A..Z.\n",
    "```\n",
    "\n",
    "## Solution:\n",
    "```python\n",
    "def accum(s):\n",
    "    return '-'.join([s[i].upper()+ ((s[i].lower())*i) for i in range(len(s))])\n",
    "```"
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
