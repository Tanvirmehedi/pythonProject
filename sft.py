import math


class Stone_measurement:
    def __init__(self, height, length, width):
        self.height = height
        self.length = length
        self.width = width

    def Convert_inch(self):

        if isinstance(self.height and self.length and self.width, float):
            conv_length_srt = str(self.length)
            conv_height_str = str(self.height)
            conv_width_str = str(self.width)
            text = conv_height_str.split('.'), conv_length_srt.split(
                '.'), conv_width_str.split('.')
            for item in text:
                result = int(item[1])/12
        return "%.2f" % result


stone_input = Stone_measurement(float(input("Input Height : ")), float(
    input("Input Length : ")), float(input("Input Width : ")))

print(stone_input.Convert_inch())
