#Question 1
import re

def is_date_format_correct(date:str)->bool:
    """
    This function takes in a date in string format
    and returns true if the date matches the format
    YYYY-MM-DD and false if it doesn't
    """
    my_format = re.compile(r'\d{4}-\d{2}-\d{2}')
    return bool(my_format.match(date))



#Question 2
import datetime

for i in range(1, 11):
    if i==6:
        continue
    else:
        print(i, end=',')



#Question 3
def compute_prev_date(dates_list:list):
    """
    """
    return [((datetime.datetime.strptime(date, "%Y-%m-%d")) -
       datetime.timedelta(days=1)).strftime("%d %b %Y") for date in dates_list]



#Question 4
import sys

def main():
    qty = None
    cost = None
    try:
        qty = fetch_quantity()
    except:
        return
        
    try:
        cost = fetch_cost()
    except Exception as e:
        print(e)
        #sys.exit(1)
        
                

def fetch_quantity():
    """
    Returns a number, any number
    """
    #...
    return ...

def fetch_cost():
    """
    Returns a number, any number
    """
    #...
    return ...

def compute_cost_per_quantity():
    qty = fetch_quantity()
    cost = fetch_cost()
    cost_per_quantity = cost/qty
    return cost_per_quantity

try:
    cost_per_quantity = compute_cost_per_quantity()
except Exception as e:
        print(e)
        #sys.exit(1)
    
a = 1 + 2 + cost_per_quantity
b = 4 + 5
print(a+b)

#Question 5
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
@api_view(['GET'])
def get_params():
    """
    """
    name = request.query_params.get('name', '')
    surname = request.query_params.get('surname', '')
    content = {
        'name': name,
        'surname': surname,
    }
    return Response(content, status=status.HTTP_200_OK)

#Question6
class TestMath:
    def _init_(self,x,y):
        self.x = x
        self.y = y

    def test_add(self):
        return self.x + self.y

    def test_subtract(self):
        return self.x - self.y
    
    def test_milutiply(self):
        return self.x * self.y
    
