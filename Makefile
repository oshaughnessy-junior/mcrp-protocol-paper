PANDOC ?= pandoc

.PHONY: all pdf clean

all: pdf

pdf: output/pdf/position-paper.pdf

output/pdf/position-paper.pdf: paper/position-paper.md paper/metadata.yaml paper/refs.bib
	mkdir -p output/pdf
	$(PANDOC) paper/position-paper.md \
		--metadata-file=paper/metadata.yaml \
		--bibliography=paper/refs.bib \
		--citeproc \
		--pdf-engine=pdflatex \
		-o $@

clean:
	trash output/pdf
