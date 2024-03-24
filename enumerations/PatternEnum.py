from enum import Enum


class PatternEnum(Enum):
    CHINESE = "[\u4e00-\u9fa5]+"
    DIGIT = "[0-9]+"
