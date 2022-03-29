from main import TheaterSeating


def test_no_reservations():
    obj = TheaterSeating([])
    obj.generate_seating_plan()
    assert obj.seats == []


def test_single_reservations():
    obj = TheaterSeating([1])
    obj.generate_seating_plan()
    assert obj.seats == [["A1"]]


def test_exceeding_reservations():
    obj = TheaterSeating([21])
    obj.generate_seating_plan()
    assert obj.seats == [[]]


def test_first_row_utilisation():
    obj = TheaterSeating([2, 16, 1])
    obj.generate_seating_plan()
    assert obj.seats[2] == ["A6"]


def test_full_row_utilisation():
    obj = TheaterSeating([20])
    obj.generate_seating_plan()
    for x in obj.seats[0]:
        assert x[0] == 'A'


def test_skipping_exceeding_requests():
    obj = TheaterSeating([20, 21, 1])
    obj.generate_seating_plan()
    assert [] in obj.seats
    assert obj.seats[2] == ["B1"]
