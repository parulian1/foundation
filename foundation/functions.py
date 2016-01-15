from PIL import ImageOps

def rescale(data, width, height, force=True):
	"""Rescale the given image, optionally cropping it to make sure the result image has the specified width and height."""
	import image as pil
	from cStringIO import StringIO
	
	max_width = width
	max_height = height

	input_file = StringIO(data)
	img = pil.open(input_file)
	if not force:
		img.thumbnail((max_width, max_height), pil.ANTIALIAS)
	else:
		img = ImageOps.fit(img, (max_width, max_height,), method=pil.ANTIALIAS)
		
	tmp = StringIO()
	img.save(tmp, 'PNG')
	tmp.seek(0)
	output_data = tmp.getvalue()
	input_file.close()
	tmp.close()
	
	return output_data