"""
TODO: Fix bug where street_suffix is between street_name and street_type
TODO: You realise you don’t need street_type
TODO: You need to add handling of level numbers - level details come after unit details. Level number is optional e.g., GROUND FLOOR 1 SMITH ST, KAMBAH ACT 2902
TODO: Add handling of post office boxes (e.g., postal_delivery_type: PO BOX, postal_delivery_id: 10, expected: PO BOX 10, KAMBAH ACT 2902)
"""

class Address:

    _unit_type: str = None
    _unit_number: str = None
    _street_number_1: str = None
    _street_name: str = None
    _street_type: str = None
    _street_suffix: str = None
    _locality: str = None
    _state: str = None
    _postcode: str = None

    def __init__(
            self, street_number_1: str, street_name: str, street_type: str, street_suffix: str, locality: str,
            state: str, postcode: str, unit_type: str, unit_number: str
    ):
        self._unit_type = unit_type
        self._unit_number = unit_number
        self._street_number_1 = street_number_1
        self._street_name = street_name
        self._street_type = street_type
        self._street_suffix = street_suffix
        self._locality = locality
        self._state = state
        self._postcode = postcode

    def get_full_address(self) -> str:
        """
        Returns a joined full address string representing this address using the format:
        <st_num_1> <st_name> <st_type>, <locality> <state> <postcode>

        :return: address joining all fields together
        """
        result: str = ''
        street_number: str = None
        if self._unit_number and self._unit_type:
            street_number = ' '.join([self._unit_type, self._unit_number]) + ' '
        elif self._unit_number:
            street_number = self._unit_number + '/'
        else:
            street_number = ''
        street_number += self._street_number_1
        street: str = ' '.join(x for x in [self._street_name, self._street_suffix, self._street_type] if x)
        location: str = ' '.join([self._locality, self._state, self._postcode])
        result = ' '.join([street_number, street + ',', location])
        return result