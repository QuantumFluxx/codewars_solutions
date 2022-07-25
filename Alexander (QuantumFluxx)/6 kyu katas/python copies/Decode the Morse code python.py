{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "7099a072",
   "metadata": {},
   "outputs": [],
   "source": [
    "def decodeMorse(morse_code):\n",
    "    message = \"\".join([MORSE_CODE[i] if i in MORSE_CODE else \" \" for i in morse_code.split(\" \")])\n",
    "    return message.replace(\"  \", \" \").strip()"
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
