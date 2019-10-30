# sort the dataset based on the first and sixth  columns

split -b250M ../small.csv chunk
for f in chunk*; do sort -t, --parallel=4 -k1,1n -k6,6 -s "$f" > "$f".sorted && rm "$f"; done
sort -T temp/ --parallel=4 -mo ../w1_sorted.csv -k1,1 -k6,6 --stable chunk*.sorted
rm chunk*
