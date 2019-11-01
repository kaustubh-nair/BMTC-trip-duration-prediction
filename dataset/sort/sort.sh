# sort the dataset based on the first and sixth  columns
sort -T temp/ -o ../small_sor.csv -s -k1,1n -k6.9,6.10n -k6.12,6.13n -k6.15,6.16n -k6.18,6.19n  ../small.csv
