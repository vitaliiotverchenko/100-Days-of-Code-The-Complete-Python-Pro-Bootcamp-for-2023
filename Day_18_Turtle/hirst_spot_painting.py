import colorgram

# Extract 6 colors from an image.
colors = colorgram.extract("C:\\Users\\38096\\Desktop\\100DaysOfCodeChallenge\\100-Days-of-Code-The-Complete-Python-Pro-Bootcamp-for-2023\\Day_18_Turtle\\hirst_spot_paint.jpg", 30)

rgb_colors = [colors[i].rgb[0:3] for i in range(len(colors))]
# colorgram.extract returns Color objects, which let you access
# RGB, HSL, and what proportion of the image was that color.

first_color = colors[0]
rgb = first_color.rgb # e.g. (255, 151, 210)
hsl = first_color.hsl # e.g. (230, 255, 203)
proportion  = first_color.proportion # e.g. 0.34

# RGB and HSL are named tuples, so values can be accessed as properties.
# These all work just as well:
red = rgb[0]
red = rgb.r
saturation = hsl[1]
saturation = hsl.s