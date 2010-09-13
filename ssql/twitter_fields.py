from datetime import datetime
from field_descriptor import FieldDescriptor
from field_descriptor import FieldType
from field_descriptor import ReturnType
from tuple_descriptor import TupleDescriptor

def twitter_user_data_extractor(field):
    def factory():
        def extract(data):
            return getattr(data[TwitterFields.USER], field)
        return extract
    return factory

def twitter_coordinate_extractor(lat_or_lng):
    def factory():
        def extract(data):
            if data["coordinates"] != None:
                coords = data["coordinates"]["coordinates"]
                latlng = (coords[1], coords[0])
                if lat_or_lng == TwitterFields.LATITUDE:
                    return latlng[1] # Note: twitter sends them backwards
                elif lat_or_lng == TwitterFields.LONGITUDE:
                    return latlng[0]
                else:
                    return None
            else:
                return None
        return extract
    return factory


class TwitterFields:
    TEXT = "text"
    USER = "user"
    SSQL_USER_ID = "user_id"
    TWITTER_USER_ID = "id"
    SCREEN_NAME = "screen_name"
    LOCATION = "location"
    LANG = "lang"
    CREATED_AT = "created_at"
    PROFILE_IMAGE_URL = "profile_image_url"
    LATITUDE = "latitude"
    LONGITUDE = "longitude"

def twitter_tuple_descriptor():
    # what they type, array of underlying fields, 
    fields = [
        FieldDescriptor(TwitterFields.TEXT, [TwitterFields.TEXT], FieldType.FIELD, ReturnType.STRING),
        FieldDescriptor(TwitterFields.LOCATION, [], FieldType.FUNCTION, ReturnType.STRING, None, twitter_user_data_extractor(TwitterFields.LOCATION)),
        FieldDescriptor(TwitterFields.LANG, [], FieldType.FUNCTION, ReturnType.STRING, None, twitter_user_data_extractor(TwitterFields.LANG)),
        FieldDescriptor(TwitterFields.PROFILE_IMAGE_URL, [], FieldType.FUNCTION, ReturnType.STRING, None, twitter_user_data_extractor(TwitterFields.PROFILE_IMAGE_URL)),
        FieldDescriptor(TwitterFields.SSQL_USER_ID, [], FieldType.FUNCTION, ReturnType.INTEGER, None, twitter_user_data_extractor(TwitterFields.TWITTER_USER_ID)),
        FieldDescriptor(TwitterFields.SCREEN_NAME, [], FieldType.FUNCTION, ReturnType.STRING, None, twitter_user_data_extractor(TwitterFields.SCREEN_NAME)),
        FieldDescriptor(TwitterFields.CREATED_AT, [TwitterFields.CREATED_AT], FieldType.FIELD, ReturnType.DATETIME),
        FieldDescriptor(TwitterFields.LATITUDE, [], FieldType.FUNCTION, ReturnType.FLOAT, None, twitter_coordinate_extractor(TwitterFields.LATITUDE)),
        FieldDescriptor(TwitterFields.LONGITUDE, [], FieldType.FUNCTION, ReturnType.FLOAT, None, twitter_coordinate_extractor(TwitterFields.LONGITUDE))
    ]
    return TupleDescriptor(fields)


