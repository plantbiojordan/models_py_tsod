# Optional

# Changes names of jpg images to 0001.jpg, 0002.jpg, 0003.jpg, etc.

# Can be changed to rename XML files as well BUT (!!!!!!) I can't guarantee 
#   your images and XML files will still match unfortunately.
#   I haven't tried that yet myself.

n=1
for i in /path/jpg_raw/*.jpg; do
	new=$(printf "%04d.jpg" "$n")
	mv -i -- "$i" "$new"
	let n=n+1
done
