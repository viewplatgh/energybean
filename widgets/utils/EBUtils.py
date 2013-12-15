from exceptions import ValueError

class EBUtils(object):
    """Some utilities for common stuff"""
    
    @staticmethod
    def parse_int(val):
        try:
            rslt = int(val)
        except ValueError:
            rslt = 0
        return rslt
    
    @staticmethod
    def parse_float(val):
        try:
            rslt = float(val)
        except ValueError:
            rslt = 0
        return rslt


