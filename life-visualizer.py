from PIL import Image, ImageFont, ImageDraw, ImageEnhance
import datetime
import time

segment = "week"
if segment == "week":
	multiplier = 1.65344e-6
	num_in_year = 52
elif segment == "month":
	multiplier = 3.80517e-7
	num_in_year = 12
elif segment == "day":
	multiplier = 1.15741e-5
	num_in_year = 365

now_s = datetime.datetime.now().timestamp()
birth_s = datetime.datetime.strptime('02.09.1992 09:38:42,76', '%d.%m.%Y %H:%M:%S,%f').timestamp()
segs_alive = (now_s - birth_s)*multiplier
print(segs_alive)

count = 0
# segs_alive = age*52
sq_size = 10
margin = 4
lifespan = 100
n = (sq_size + margin) * num_in_year + margin
m = (sq_size + margin) * lifespan + margin

def rectangle(a,b,c,d,color):
	draw = ImageDraw.Draw(image)
	draw.rectangle(((a, b), (c, d)), fill="black")
	draw.rectangle(((a+1, b+1), (c-1, d-1)), fill=color)

def year(year, count):
	for i in range(num_in_year):
		if count < segs_alive:
			color = "black"
		else:
			color = "white"
		rectangle(i*(sq_size+margin)+margin,year*(sq_size+margin)+margin,i*(sq_size+margin)+sq_size+margin,year*(sq_size+margin)+sq_size+margin,color)
		count += 1
	return count

def life(years, count):
	for i in range(years):
		count = year(i, count)

image = Image.new('RGB', (n, m), (255, 255, 255))
# rectangle(0,20,40,80)
# year(0)
life(lifespan, count)

image.save("image.png", "PNG", quality=95)




























#stop
