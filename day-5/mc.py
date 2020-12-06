num_columns = 1
while num_columns < 15:
	space = 0
	while space < 7:
		buffer_room = 0
		while buffer_room < 7:
			total = 2*buffer_room + num_columns*4 + (num_columns-1)*space
			if total == 76:
				print("columns:",num_columns, "space",space, "buffer",buffer_room, total)
			buffer_room +=1
		space += 1
	num_columns += 1


x = 2 + 4 + 4 + 4 + 4 + 4 + 4 + 4 + 4 +4 + 4+ 4 + 4 + 4 + 4 + 4 + 4 + 4 + 4 + 4 + 2
print(x)