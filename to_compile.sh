pdflatex -output-directory out thesis
biber -output-directory out thesis
pdflatex -output-directory out thesis  # Yep, run it twice