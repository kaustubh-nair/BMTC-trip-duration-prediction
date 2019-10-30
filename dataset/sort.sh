## split the file into 100M pieces named fileChunkNNNN
split -b100M small.csv fileChunk
## Sort each of the pieces and delete the unsorted one
for f in fileChunk*; do sort "$f" > "$f".sorted && rm "$f"; done
## merge the sorted files    
sort -T /some_dir/ --parallel=4 -muo file_sort.csv -k 1,3 fileChunk*.sorted
