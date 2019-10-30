split -b250M ../w1.csv fileChunk
for f in fileChunk*; do sort -t, --parallel=4 -k1,1n -k6,6 -s "$f" > "$f".sorted && rm "$f"; done
sort -T temp/ --parallel=4 -mo w1_sorted.csv -k1,1 -k6,6 --stable fileChunk*.sorted
rm fileChunk*
