class Contract():
    def __init__(self, type_object, total_value, number_participants, consortium_status):
        self.__type_object = type_object
        self.__total_value = total_value
        self.__number_participants = number_participants
        self.__consortium_status = consortium_status

    @property
    def type_object(self):
        return self.__type_object

    @type_object.setter
    def type_object(self, type_object):
        self.__type_object = type_object

    @property
    def total_value(self):
        return self.__total_value

    @total_value.setter
    def total_value(self, total_value):
        self.__total_value = total_value

    @property
    def number_participants(self):
        return self.__number_participants

    @number_participants.setter
    def number_participants(self, number_participants):
        self.__number_participants = number_participants

    @property
    def consortium_status(self):
        return self.__consortium_status

    @consortium_status.setter
    def consortium_status(self, consortium_status):
        self.__consortium_status = consortium_status
