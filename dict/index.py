from .functionQuestion import *

user = {}
option = question()

while option=="I" or option=="P" or option=="E" or option=="L":
    if option=="I":
        insert(user)
    option = question()