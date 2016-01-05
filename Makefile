geneses.pdf: geneses.tex
	pdflatex geneses.tex

geneses.tex: genesis-blocks.csv geneses.py
	python geneses.py > geneses.tex

clean:
	rm -f geneses.tex geneses.pdf *.log *.aux *.out

pod: geneses.pdf
	pdftk A=blank.pdf B=geneses.pdf \
		cat B A A A A A A \
		output geneses-pod.pdf
