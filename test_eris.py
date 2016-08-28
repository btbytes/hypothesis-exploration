import unittest
from hypothesis import given
from hypothesis import strategies as st

class TestEris(unittest.TestCase):
    "Comparing the syntax and implementation of features with Eris"

    @given(st.integers(), st.integers())
    def test_sum_is_commutative(self, first, second):
        x = first + second
        y = second + first
        self.assertEqual(x, y, "Sum between %d and %d should be commutative" % (first, second))

    @given(st.lists(st.integers()))
    def test_reversing_twice_gives_same_list(self, xs):
        ys = list(xs)
        ys.reverse()
        ys.reverse()
        self.assertEqual(xs, ys)

    @given(st.integers().filter(lambda x: x > 42))
    def test_filtering(self, x):
        self.assertGreater(x, 42)

    @given(st.integers().map(lambda x: x * 2))
    def test_mapping(self, x):
        self.assertEqual(x % 2, 0)

    @given(st.lists(st.integers(), min_size=4, max_size=4).flatmap(
        lambda xs: st.tuples(st.just(xs), st.sampled_from(xs))
    ))
    def test_list_and_element_from_it(self, pair):
        (generated_list, element) = pair
        self.assertIn(element, generated_list)
