import csv


class CsvUtils(object):
    """
    CsvUtils class :

    In charge of every interaction with the csv file.
    """

    FILE_EXTENSION = ".csv"

    def __init__(self, file_name):

        if file_name is None:
            raise Exception("You didn't put any valid file name.")

        self.file_name = file_name

        # Append '.csv' file extension if it is not present in the *file_name*
        if self.FILE_EXTENSION not in file_name:
            self.file_name = "{}.csv".format(file_name)

    def read_file(self):
        """
        :returns: All data from the selected csv file
        """
        with open(self.file_name) as file:
            read_csv = csv.reader(file, delimiter=',')

            fetched = []
            for row in read_csv:
                fetched.append(row)
            return fetched

    def get_data(self, row_index, column_index):
        """
        :param row_index: Accepts the row number to fetch
        :param column_index: Accepts the column number to fetch
        :return: Returns the result in string form
        """
        return self.read_file()[row_index][column_index]
