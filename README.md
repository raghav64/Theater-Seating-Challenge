# Theater-Seating-Challenge
Greedy algorithm to handle movie hall reservation requests


## Assumptions
-> Reservations are assumed to be contiguous segment of seats. Each reservation would be seated together in a row. 
-> The number of reservations will be less than 1000 because of xxx in Reservation ID. 
-> A request cannot be fulfilled if: a) Request demands seats more than available. 
                                     b) Contiguous segment cannot be seated together. 
   In this case skip that request and move on. 
-> No requests with 0 reservations. 

## Algorithm

