todo = ["eat", "sleep", "repeat"]
progress = ["", "", ""]
done = ["", "", ""]

progress[1] = todo[1]
todo[1] = ""

print("TODO", todo)
print("PROGRESS", progress)
print("DONE", done)

done[0] = progress[1]
progress[1] = ""

print("TODO", todo)
print("PROGRESS", progress)
print("DONE", done)