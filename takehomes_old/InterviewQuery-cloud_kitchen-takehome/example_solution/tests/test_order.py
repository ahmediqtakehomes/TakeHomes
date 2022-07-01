import unittest
import src
from src import Order


class OrderTestCase(unittest.TestCase):
    """" Order test cases."""

    def setUp(self):
        """ Create simple order """
        global order

        self.name = "A Calamari Nugget"
        self.temp = "Hot"
        self.decay_rate = 0.5
        self.shelf_life = 360
        data = self.create_data_from_self()
        order = Order(data)

        # Used to artifically induce age to test value computations
        self.backdate_by = 10

    def tearDown(self):
        pass

    def test_value_below_zero(self):
        order.created_at -= self.shelf_life

        self.assertLess(order.value, 0.0)

    def test_inadequate_data_on_init(self):
        data = self.create_data_from_self()
        del data["name"]
        self.assertRaises(KeyError, Order, data)

    def test_infant_value(self):
        order.created_at -= self.backdate_by
        self.assertAlmostEqual(order.infant_value, self.shelf_life, places=2)

    def test_value(self):
        """ value = ([shelf life] - [order age]) - ([overflow shelf decay]) - ([regular shelf decay]) """
        order.created_at -= self.backdate_by
        value = order.infant_value - order.order_age - order.total_decay

        self.assertAlmostEqual(order.value, value, places=2)

    def test_regular_decay(self):
        """
        Order never put on overflow shelf
            regular_decay = ([decay rate] * ([order age] - [time on overflow shelf]))
        """
        order.created_at -= self.backdate_by
        regular_decay = self.decay_rate * self.backdate_by

        self.assertAlmostEqual(order.regular_decay, regular_decay, places=2)

    def test_indefinite_overflow_decay(self):
        """
        Order is still on overflow shelf
            overflow_decay = 2 * ([decay rate] * [time on overflow shelf])
        """
        order.created_at -= self.backdate_by
        order.overflow_in = order.created_at
        overflow_decay = 2 * self.decay_rate * self.backdate_by

        self.assertAlmostEqual(order.overflow_decay, overflow_decay, places=2)

    def test_finite_overflow_decay(self):
        """
        Order has been taken off overflow shelf
            overflow_decay = 2 * ([decay rate] * [time on overflow shelf])
        """
        order.created_at -= self.backdate_by
        overflow_delta = self.backdate_by / 2
        order.overflow_in = order.created_at
        order.overflow_out = order.overflow_in + overflow_delta
        overflow_decay = 2 * (self.decay_rate * overflow_delta)

        self.assertAlmostEqual(order.overflow_decay, overflow_decay, places=2)

    def test_total_decay(self):
        """ total_decay = ([regular decay]) + ([overflow decay]) """
        total_decay = order.overflow_decay + order.regular_decay
        self.assertAlmostEqual(order.total_decay, total_decay, places=2)

    def create_data_from_self(self):
        data = {
            "name": self.name,
            "temp": self.temp,
            "decayRate": str(self.decay_rate),
            "shelfLife": str(self.shelf_life),
        }
        return data
