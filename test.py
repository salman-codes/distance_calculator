from util import calculate_distance


def test_distance_calculator(source_coordinates):
    test_cases = [
        ((51.897970, -8.470610), 219),
        ((53.29388889, -6.136026), 9),
        ((53.270580, -9.065248), 186),
        ((53.215830, -6.666940), 30),
        ((54.000000, -6.416666), 74)
    ]
    for coordinates, expected_dist in test_cases:
        temp = calculate_distance(
            source_coordinates=source_coordinates,
            destination_coordinates={'latitude': coordinates[0], 'longitude': coordinates[1]}
        )
        assert int(temp) == expected_dist

