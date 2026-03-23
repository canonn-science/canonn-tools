#!/usr/bin/bash

function symbol(){
	value=$(tr "[/]" "[."] <<<$1 | cut -d"." -f2)
	echo  $value
}

for inner in symbols/[0-9].png symbols/[0-9][0-9].png ;  do
	for outer in symbols/[0-9][A-Z].png ; do
		inner_id=$(symbol $inner)
		outer_id=$(symbol $outer)
		echo $outer_id-$inner_id.gif
		convert -page 128x128+0+0 symbols/core.png -page 128x128+0+0 symbols/$inner_id.png -page 128x128+0+0 symbols/$outer_id.png +level-colors orange,black -background none -flatten composite_gifs/$outer_id-$inner_id.gif
		convert -page 128x128+0+0 symbols/core.png -page 128x128+0+0 symbols/$inner_id.png -page 128x128+0+0 symbols/$outer_id.png  -background none -flatten composite/$outer_id-$inner_id.png
	done
done


