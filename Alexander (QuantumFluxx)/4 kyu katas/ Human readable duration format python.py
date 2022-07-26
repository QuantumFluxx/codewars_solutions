{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "6aa42d95",
   "metadata": {},
   "outputs": [],
   "source": [
    "def format_duration(seconds):\n",
    "    words = [\"year\", \"day\", \"hour\", \"minute\", \"second\"]\n",
    "    \n",
    "    if not seconds:\n",
    "        return \"now\"\n",
    "    else:\n",
    "        m, s = divmod(seconds, 60)\n",
    "        h, m = divmod(m, 60)\n",
    "        d, h = divmod(h, 24)\n",
    "        y, d = divmod(d, 365)\n",
    "        \n",
    "        time = [y, d, h, m, s]\n",
    "        \n",
    "        duration = []\n",
    "        \n",
    "        for x, i in enumerate(time):\n",
    "            if i == 1:\n",
    "                duration.append(f\"{i} {words[x]}\")\n",
    "            elif i > 1:\n",
    "                duration.append(f\"{i} {words[x]}s\")\n",
    "        \n",
    "        if len(duration) == 1:\n",
    "            return duration[0]\n",
    "        elif len(duration) == 2:\n",
    "            return f\"{duration[0]} and {duration[1]}\"\n",
    "        else:\n",
    "            return \", \".join(duration[:-1]) + \" and \" + duration[-1]"
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
