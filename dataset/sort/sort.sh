#&& rm "$f"; done sort the dataset based on the first and sixth  columns
sort -t, -k1,1n -k6,6 -s ../w1.csv > ../w1.csv.sorted 
