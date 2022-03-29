# Theater-Seating-Challenge
Greedy algorithm to handle movie hall reservation requests

Running the project:
`python main.py *your_input_filepath* *your_output_filepath* `

Running the tests:
`pytest`

## Assumptions
* Reservations are assumed to be contiguous segment of seats. Each reservation would be seated together in a row. 
* The number of reservations will be less than 1000 because of xxx in Reservation ID. 
* A request cannot be fulfilled if: a) Request demands seats more than available. 
                                    b) Contiguous segment cannot be seated together. 
   In this case skip that request and move on. 
* There should not be any requests with 0 reservations. 


## Algorithm
* Maintain and initialise next available seat index for each row of Theater
* Process each request
  * Scan rows from start
     * If seats can be allocated:
        * Allocate seats and update next available seats for that row with buffer constraint
    * Else:
      * Report Insufficient seats for that contiguous segment

