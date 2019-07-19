# pdf-tabular-to-csv
Parse tables from pdf with invisible border to csv easily.

# Main goal of this script?
To parse table from the pdf having invisble border.

![table](https://user-images.githubusercontent.com/11581925/61269970-d8d4e800-a7bd-11e9-98dd-d74883ff21a1.png)

# but you can parse tables with visible border too.
you will just have to remove flavor parameter form the line 42 of the script.
# How to use this script ?
Put your pdf and this script in same folder and add page numbers in pages variable of the script. Now run the script.
after a successful execution you will have output folder in the current directory and in that output folder you will have tables according to their page number extracted in csv formats.
# What if I just want to parse only few pages/specific pages from the pdf?
Well good news is you can by simply updating pages variable to the string of your specific page numbers.
