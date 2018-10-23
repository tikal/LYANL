from insertion_sort import InsertionSort


class SortTestSuite:

    def sort(self, to_sort):
        raise NotImplementedError

    def test_when_empty_list(self):
        assert self.sort([]) == []

    def test_when_one_element(self):
        assert self.sort([-1]) == [-1]

    def test_when_less_trival_case(self):
        assert self.sort([
            2, 8, 4, 6, 4, 23, 90, 5, 78, 23, 89, -1
        ]) == [
            -1, 2, 4, 4, 5, 6, 8, 23, 23, 78, 89, 90
        ]


class TestInsertionSort(SortTestSuite):

    sort = InsertionSort().sort

