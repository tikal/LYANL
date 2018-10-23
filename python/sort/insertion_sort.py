class InsertionSort:

    def sort(self, to_sort):
        for index in range(0, len(to_sort) - 1):
            for new_index in range(index + 1, 0, -1):
                right_item = to_sort[new_index]
                left_item = to_sort[new_index - 1]
                if left_item > right_item:
                    to_sort[new_index - 1] = right_item
                    to_sort[new_index] = left_item
                else:
                    break
        return to_sort

