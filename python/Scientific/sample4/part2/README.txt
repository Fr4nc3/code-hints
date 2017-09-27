Fr4nc3

effects module implements

1) object_filter
2) shades_of_gray
3) negate_red
4) negate_green
5) negate_blue



* For the Object Filter I had the idea to have N files to clean, however, for
the limited time it was impossible to test. So, I fixed the number to 3 files.

* Also, in effects_tester can be run only with enter, without params
so fast to test.

* in effects_tester I added start_time  to calculate the execution time
of the effects.

* object_filter takes less than  2 second approx. to execute.

* shades of gray, negate_red, negate_blue and negate_green take less than a
second to execute.

* I used ''' comment ''' when # it was more than two lines.

* I used a hack trick to  create the BMP file because writing the header
make the file damaged and I couldn't fix it before of the deadline

* I added int into the create gray color because it seems (*)/3
was not an integer.

* I used 255 for the max color in the BMP file.

* I used the book example how to read a bmp file.

* I assumed 3 files in the filter because I didn't have more time to create a
better solution.

