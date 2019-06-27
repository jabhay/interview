from address import Address
import pytest


@pytest.mark.parametrize(
    ("unit_type, unit_number, street_number_1, street_name, street_type, street_suffix, locality, state, postcode, "
     "expected_value"),
    [
        (None, None, '1', 'SMITH', 'ST', None, 'KAMBAH', 'ACT', '2902', '1 SMITH ST, KAMBAH ACT 2902'),
        ('UNIT', '10', '1', 'SMITH', 'ST', None, 'KAMBAH', 'ACT', '2902', 'UNIT 10 1 SMITH ST, KAMBAH ACT 2902'),
        (None, '10', '1', 'SMITH', 'ST', None, 'KAMBAH', 'ACT', '2902', '10/1 SMITH ST, KAMBAH ACT 2902'),
        (None, None, '1', 'SMITH', 'ST', 'SOUTH', 'KAMBAH', 'ACT', '2902', '1 SMITH ST SOUTH, KAMBAH ACT 2902'),
    ]
)
def test_get_full_address(
        unit_type, unit_number, street_number_1, street_name, street_type, street_suffix, locality, state, postcode,
        expected_value
):
    address: Address = Address(
        street_number_1=street_number_1, street_name=street_name, street_type=street_type, street_suffix=street_suffix,
        locality=locality, state=state, postcode=postcode, unit_type=unit_type, unit_number=unit_number
    )
    assert expected_value == address.get_full_address()
