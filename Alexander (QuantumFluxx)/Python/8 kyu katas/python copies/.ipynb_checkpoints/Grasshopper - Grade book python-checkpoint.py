{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "db9f5b6b",
   "metadata": {},
   "outputs": [],
   "source": [
    "def get_grade(s1, s2, s3):\n",
    "    mean = sum([s1,s2,s3])/3\n",
    "    if mean>=90: return 'A'\n",
    "    if mean>=80: return 'B'\n",
    "    if mean>=70: return 'C'\n",
    "    if mean>=60: return 'D'\n",
    "    return 'F'"
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
