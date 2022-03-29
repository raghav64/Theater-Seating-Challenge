# Theater-Seating-Challenge
Greedy algorithm to handle movie hall reservation requests

Running the project:
`python main.py *your_input_filepath* *your_output_filepath* `

Running the tests:
`pytest`

## Assumptions
* Reservations are assumed to be contiguous segment of seats. Each reservation would be seated together in a row. 
* The number of reservations will be less than 1000 because of xxx in Reservation ID. 
* A request cannot be fulfilled if:<br/>
                                    a) Request demands seats more than available.<br/> 
                                    b) Contiguous segment cannot be seated together. <br/> 
   In this case report *unable to seat* and move on. 
* There should not be any requests with 0 reservations.
* Prioritise seating from first row


## Algorithm
* Maintain and initialise next available seat index for each row of Theater
* Process each request
  * Scan rows from start
     * If seats can be allocated:
        * Allocate seats and update next available seats for that row with buffer constraint
    * Else:
      * Report Insufficient seats for that contiguous segment

## Roadmap & Future work
- [x] Implement greedy algorithm for contiguous segment allocation 
- [x] Implement Unit tests
- [ ] If reservations can be broken up, then can increase the optimisation by using backtracking solutions by trying all configurations
- [ ] Take into account customer's seat preference to enhance satisfaction

