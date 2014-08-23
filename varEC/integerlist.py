""" This functions help to interpreting a list of integers. """


class IntegerList(list):
    def __init__(self, arg):
        super().__init__(arg)
        assert all(isinstance(i, int) for i in self), \
            "All of the items must be integer."
        self.intervals = self.make_intervals()

    def make_intervals(self):
        """   Sort the list (of integers) and returns the intervals as a
        pair of integers. E.g. when the list=[1, 5, 6, 7],  it gives
        [(1, 1), (5, 7)].
        """
        if not self:
            return []
        intervals = []
        self.sort()
        index_of_the_first = 0
        for i in range(len(self) - 1):  # i: indexes from zero to len(self)
            if self[i] + 1 == self[i+1] or self[i] == self[i+1]:
                continue
            # elif self[i] == self[i+1]:
            #     not_uniq.append(  (self.count(self[i]), self[i])  )
            else:
                intervals.append((self[index_of_the_first], self[i]))
                index_of_the_first = i + 1
        # And now the last element:
        last_index = len(self) - 1
        intervals.append((self[index_of_the_first], self[last_index]))
        return intervals

    def __str__(self):
        """docstring for __str__"""
        if self.intervals is None:
            self.make_intervals()
        return " ".join(self.interval_to_string(i) for i in self.intervals)

    @staticmethod
    def interval_to_string(interval):
        if interval[0] == interval[1]:
            return "{interval[0]}".format(interval=interval)
        else:
            return "{interval[0]}..{interval[0]}".format(interval=interval)


def uniq(ordered_list):
    """Returns with the list, but all the items will exists one times."""
    list = ordered_list[:]
    previous_item = list[0]
    for item in list[1:]:
        if item == previous_item:
            list.remove(item)
        previous_item = item
    return list


def _uniq_test():
    """prints [1,2,3,5,"a",9]"""

    L = [1, 1, 1, 1, 1, 2, 3, 3, 3, 5, "a", "a",  9, 9, 9, 9, 9, 9, 9, 9]
    print(uniq(L))


def search_not_uniq(list):
    """Searches all the not uniq items in
    the 'list', and returns whith a list of pairs.
    e.g. (3, 15) means 15 is three times."""

    not_uniq = {}
    for i in set(list):
        count = list.count(i)
        if count != 1:
            not_uniq[i] = count
    return not_uniq


def print_not_uniq(list, mesg="{multiplicity} times: {item}"):
    """ Writes the not uniq items of the 'list' with multiplicity."""

    not_uniq = search_not_uniq(list)
    for item, multiplicity in not_uniq.items():
        print(mesg.format(**locals()))
    return len(not_uniq)

if __name__ == '__main__':
    list_ = [1, 1, 1, 1, 1, 2, 3, 3, 3, 5, "a", "a",  9, 9, 9, 9, 9, 9, 9, 9]
    print(print_not_uniq(list_))
    print_not_uniq(list_, "{item} ({multiplicity} darab)")
