import pipeline
import filereader

reader = filereader.FileReader()
reader.set_file("input_data.txt")
input_list = reader.read()

pline = pipeline.Pipeline()
pline.start(4, 6, input_list)

while pline.is_active():
	pline.perform_stage()
	if pline.is_active():
		print(pline)

print(pline.get_result())
