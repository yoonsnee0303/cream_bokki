from selenium import webdriver

# initialize the web driver
driver = webdriver.Chrome()

# navigate to the webpage with the image
driver.get('https://www.example.com')

# locate the image element
image_element = driver.find_element_by_xpath('//img')

image_element.ex

# get the location and size of the image element
location = image_element.execute_script('return arguments[0].getBoundingClientRect().top;', img)
size = image_element.size

# calculate the coordinates of the image
x = location['x']
y = location['y']
width = size['width']
height = size['height']
x2 = x + width
y2 = y + height

# print the coordinates of the image
print(f"The coordinates of the image are ({x}, {y}) - ({x2}, {y2})")
