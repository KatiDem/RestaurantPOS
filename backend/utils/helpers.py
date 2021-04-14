from django.core.validators import RegexValidator

rtmp_regex = RegexValidator(
    regex=r'rtmp[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
    message="Rtmp url not a valid")


def modify_input_for_multiple_files(property_id, image):
    dict = {}
    dict['property_id'] = property_id
    dict['image'] = image
    return dict
