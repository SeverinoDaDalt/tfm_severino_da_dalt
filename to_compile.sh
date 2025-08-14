pdflatex -output-directory out authorfile
biber -output-directory out authorfile
pdflatex -output-directory out authorfile  # Yep, run it twice