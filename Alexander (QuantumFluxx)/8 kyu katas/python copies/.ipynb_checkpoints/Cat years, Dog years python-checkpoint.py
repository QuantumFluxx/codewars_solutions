{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "44b95ae1",
   "metadata": {},
   "outputs": [],
   "source": [
    "def human_years_cat_years_dog_years(n):\n",
    "    cat_years = 15 + (9 * (n > 1)) + (4 * (n - 2) * (n > 2))\n",
    "    dog_years = 15 + (9 * (n > 1)) + (5 * (n - 2) * (n > 2))\n",
    "    return [n, cat_years, dog_years]"
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
