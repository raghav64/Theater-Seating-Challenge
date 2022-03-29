import sys


class TheaterSeating:
    def __init__(self, reservations, rows=10, cols=20):
        self.rows = rows
        self.cols = cols
        self.seats = []
        self.allocations = []
        self.requests = reservations
        self.next_available = [0 for _ in range(rows)]

    def allocate_seating(self):  # Allocates the seats greedily according to the requests
        for seats_requested in self.requests:
            request_accepted = False
            for i in range(self.rows):
                first_available = self.next_available[i]
                if first_available + seats_requested <= self.cols:
                    self.next_available[i] += seats_requested + 3
                    self.allocations.append((i, first_available, seats_requested))
                    request_accepted = True
                    break
            if not request_accepted:
                self.allocations.append(())

    def generate_seats(self):  # Generates the seating plan from the allocations
        for data in self.allocations:
            if len(data):
                row_character = chr(ord('A') + data[0])
                first_available = data[1]
                seats_requested = data[2]
                res = [row_character + str(i + 1) for i in range(first_available, first_available + seats_requested)]
                self.seats.append(res)
            else:
                self.seats.append([])  # If request cannot be fulfilled then output unfulfilled

    def generate_seating_plan(self):
        self.allocate_seating()
        self.generate_seats()

    def print_seats(self):
        for reservations in self.seats:
            for x in reservations:
                print(x, end=" ")
            print()


def file_check(file_path):
    try:
        open(file_path, "r")
        return 1
    except IOError:
        return 0


def read_input(file_name):
    if not file_check(file_name):
        raise FileNotFoundError('Input reservation file not found')

    with open(file_name, mode='r') as f:
        input = map(lambda s: int(s.split()[1]), f.read().splitlines())
    return list(input)


def write_output(seating_order, output_file):
    processed_output = []
    for i, seats in enumerate(seating_order):
        r_no = str(i + 1).zfill(3)
        s = 'Request cannot be fulfilled' if len(seats) == 0 else ','.join(seats)
        processed_output.append(f'R{r_no} {s}\n')

    with open(output_file, mode='w') as f:
        f.writelines(processed_output)


if __name__ == "__main__":
    input_filepath = sys.argv[1]
    output_filepath = sys.argv[2]

    requests = read_input(input_filepath)

    obj = TheaterSeating(requests, 10, 20)

    # obj.print_seats()
    obj.generate_seating_plan()
    write_output(obj.seats, output_filepath)
