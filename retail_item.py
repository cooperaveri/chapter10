{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "eda450ad-5be5-4679-b160-f5fbb800aced",
   "metadata": {},
   "outputs": [],
   "source": [
    "class retailitem:\n",
    "    def __init__(self, description, units_in_inventory, price):\n",
    "        self.description = description\n",
    "        self.units_in_inventory = units_in_inventory\n",
    "        self.price = price\n",
    "\n",
    "    def get_description(self):\n",
    "        return self.description\n",
    "\n",
    "    def get_units_in_inventory(self):\n",
    "        return self.units_in_inventory\n",
    "\n",
    "    def get_price(self):\n",
    "        return self.price\n",
    "\n",
    "    def set_description(self, description):\n",
    "        self.description = description\n",
    "\n",
    "    def set_units_in_inventory(self, units_in_inventory):\n",
    "        self.units_in_inventory = units_in_inventory\n",
    "\n",
    "    def set_price(self, price):\n",
    "        self.price = price\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "477f3820-ea1d-4d1a-a4bd-13d58afd41a6",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "anaconda-2022.05-py39",
   "language": "python",
   "name": "conda-env-anaconda-2022.05-py39-py"
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
