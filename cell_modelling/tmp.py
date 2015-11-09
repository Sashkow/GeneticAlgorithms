import tempfile

with tempfile.NamedTemporaryFile(mode="wb") as jpg:
	jpg.write(b"Hello World!")
	print jpg.name
	from PIL import Image
	img = Image.open(jpg.name)
	img.show()
