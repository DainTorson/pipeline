import pipeline

input_list = [(10, 3), (6, 2), (13, 6)]

pline = pipeline.Pipeline()
pline.start(4, input_list)

while(pline.is_active()):
	pline.perform_stage()
	print(pline)

print(pline.get_result())
