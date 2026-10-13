

class VisionObject:

    def __init__(self, coordinates, dimensions):
        self.__coordinates = coordinates # [x,y]
        self.__dimensions = dimensions # [width, height]

    def get_coordinates(self):
        """coordinates from top left corner"""

        return self.__coordinates

    def get_dimensions(self):
        return self.__dimensions
    
class VPerson(VisionObject):

    def __init__(self,coordinates, dimensions, track_id):
        super().__init__(coordinates, dimensions)
        self.__track_id = track_id

    def get_track_id(self):
        return self.__track_id

class VStaff(VPerson):

    def __init__(self, coordinates, dimensions, track_id, staff_id):
        super().__init__(coordinates, dimensions, track_id)
        self.__staff_id = staff_id

    def get_staff_id(self):
        return self.__staff_id


class VTable(VisionObject):

    def __init__(self, coordinates, dimensions, table_id, occupants=None):
        super().__init__(coordinates, dimensions)
        self.__occupants = tuple(occupants or [])
        self.__table_id = table_id

    def is_occupied(self):
        """return boolean based on whether table is classified as occupied or not in this specific snapshot"""
        return len(self.__occupants) > 0

    def get_occupants(self):
        """returns a tuple of track IDs"""
        return self.__occupants

    def get_id(self):
        return self.__table_id

class Scene:

    def __init__(self,zone_id, timestamp, detected_objects):
        self.__detected_objects = tuple(detected_objects)
        self.__timestamp = timestamp
        self.__zone_id = zone_id

    def get_objects(self):
        """returns a list of all detected Object class instances in this snapshot"""
        return self.__detected_objects

    def get_persons(self):
        """returns a list of only detected Person class instances in this snapshot"""
        pass

    def get_tables(self):
            """returns a list of only detected Table class instances in this snapshot"""
            pass

    def get_timestamp(self):
        """return camera capture time in float timestamp format"""
        return self.__timestamp

    def get_zone_id(self):
        return self.__zone_id
        