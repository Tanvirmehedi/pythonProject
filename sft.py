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
            num = 1
            for item in text:
                division_result = int(item[1])/12
                division_result_formation = "%.2f" % division_result
                result_str = str(division_result_formation)
                explode = result_str.split('.')
                join_num = f"{item[0]}.{explode[1]}"
                conv_float2num = float(join_num)
                num = num*conv_float2num
                formate_num ="%.2f"%num
            return f"\nThe result is {formate_num} feet\n"


stone_input = Stone_measurement(float(input("Input Height : ")), float(
    input("Input Length : ")), float(input("Input Width : ")))

print(stone_input.Convert_inch())
