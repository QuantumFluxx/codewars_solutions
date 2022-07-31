{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "278c7df3",
   "metadata": {},
   "source": [
    "## DESCRIPTION:\n",
    "Usually when you buy something, you're asked whether your credit card number, phone number or answer to your most secret question is still correct. However, since someone could look over your shoulder, you don't want that shown on your screen. Instead, we mask it.\n",
    "\n",
    "Your task is to write a function maskify, which changes all but the last four characters into '#'.\n",
    "```\n",
    "Examples\n",
    "\"4556364607935616\" --> \"############5616\"\n",
    "     \"64607935616\" -->      \"#######5616\"\n",
    "               \"1\" -->                \"1\"\n",
    "                \"\" -->                 \"\"\n",
    "\n",
    "// \"What was the name of your first pet?\"\n",
    "\n",
    "\"Skippy\" --> \"##ippy\"\n",
    "\n",
    "\"Nananananananananananananananana Batman!\"\n",
    "-->\n",
    "\"####################################man!\"\n",
    "```\n",
    "\n",
    "## Solution:\n",
    "```python\n",
    "def maskify(cc):\n",
    "    return \"#\"*(len(cc)-4) + cc[-4:]\n",
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
