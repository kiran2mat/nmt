{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Makefile\n",
    "\n",
    "EXECUTABLE := __init__\n",
    "\n",
    "SOURCES := *.py\n",
    "\n",
    "EXT := py\n",
    "CC := python\n",
    "\n",
    "0:\n",
    "\t$(CC) $(SOURCES) \n",
    "\t$(CC) $(EXECUTABLE).$(EXT) 0\n",
    "\n",
    "1:\n",
    "\t$(CC) $(SOURCES) \n",
    "\t$(CC) $(EXECUTABLE).$(EXT) 1\n",
    "\n",
    "realclean:\n",
    "\tfind . -type f -name \"*.pyc\" -exec rm '{}' \\;\n",
    "\n",
    "# this line required by make - don't delete"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
