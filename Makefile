geneses.pdf: geneses.tex
	pdflatex geneses.tex

geneses.tex: genesis-blocks.csv geneses.py
	python geneses.py > geneses.tex

clean:
	rm -f geneses.tex geneses.pdf *.log *.aux *.out
