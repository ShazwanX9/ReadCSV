"""
Working with CSV files

>> foo = ReadCSV(filename, primary_key)
>> print(foo)

[ { primarykey[row]: { [ col[row] for col in row ] } } for row in len(foo) ]
"""

################## MODULES ##################
import csv

################## CODE ##################

class ReadCSV:
    """
    Load the CSV file to a list of dictionary
    Working with the CSV data
    Save/Overwrite the CSV data
    PS: Not as smart as Panda, this reads everything as string
    """

    def __init__(self, filename, primary_key):
        """
        Initialize Object
        :param filename:       string      CSV filename
        :param primary_key:    string      CSV Unique key
        :return: self
        """
        self.CSVFILE     = filename
        self.PRIMARY_KEY = primary_key
        self.item_dict = {}
        self._item_dict_keys = [] # minimize the call of item_dict.keys()

        with open(filename, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in list(csv_reader):
                self + row

    def __repr__(self):
        """
        print(self)
        :param:     None
        :return:    dict    info when print
        """
        return str(self.item_dict)

    def __add__(self, item):
        """
        Let object comunicate directly to item_dict
        :refer self.add_item():
        :param *args:      dict     Arguments to receive
        :return:    None
        """
        self.item_dict[item[self.PRIMARY_KEY]] = item
        self._item_dict_keys.append(item[self.PRIMARY_KEY])

    def __getitem__(self, *args):
        """
        Let object comunicate directly to item_dict
        :refer self.get_item():
        :param *args:      tuple     Arguments to receive
        :return:    Object
        """
        if isinstance(*args, str):
            return self.item_dict[str(*args)]
        keys = list(*args)
        return [self.item_dict[key] for key in keys]

    def __len__(self):
        """
        len(self)
        :param:     None
        :return:    int    dict key lenght
        """
        return len(self._item_dict_keys)

    def __iter__(self):
        """
        To iterate using loops
        :param:     none
        :return:    self
        """
        self._count = 0
        return self.item_dict

    def __next__(self):
        """
        To iterate using loops
        :param:     none
        :return:    object
        """
        if self._count < len(self.item_dict):
            temp = self._item_dict_keys[self._count]
            self._count += 1
            return temp
        else:
            raise StopIteration

    def add_item(self, item):
        """
        Add item to registry
        :param item:    object      Item's detail
        :return:        None
        """
        self.item_dict[item[self.PRIMARY_KEY]] = item

    def get_item(self, item):
        """
        get object details match the item
        :param:     None
        :return:    object details
        """
        return self.item_dict[item]
    
    def isExist(self, item):
        """
        check object existance match the item
        :param:     None
        :return:    boolean     is exist
        """
        return item and item in self._item_dict_keys

    def keys(self):
        """
        get dictionary keys
        :param:     None
        :return:    list     dictionary keys
        """
        return self._item_dict_keys

    def values(self):
        """
        get dictionary values
        :param:     None
        :return:    list     dictionary values
        """
        return self.item_dict.values()

    def items(self):
        """
        get dictionary items
        :param:     None
        :return:    list     dictionary items
        """
        return self.item_dict.items()

    def overwrite_csv(self, filename=None, data=None):
        """
        Overwrite csv file
        :param filename:     string         CSV filename
        :param data:         dictionary     CSV data
        :return: None
        """
        if not filename: filename = self.CSVFILE
        if not data: data = self.item_dict

        field=list(data.values())
        with open(filename, mode='w') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=field[0].keys())
            writer.writeheader()
            for row in field:
                writer.writerow(row)
        return

    def change_info(self, ref_key, ref_key_val, new_key, new_key_val):
        """
        Overwrite csv file
        :param ref_key:         string      Keyname to refer
        :param ref_key_val:     string      Unique value
        :param new_key:         string      Keyname to change
        :param new_key_val:     string      New value
        :return: None
        """
        for row in self.values():
            if row[ref_key] == ref_key_val:
                row[new_key] = new_key_val
                return
        else: 
            raise AttributeError("Key not found!")

# Print Documentation if run directly
if __name__ == "__main__":
    print(__doc__)