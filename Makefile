# Makefile for Anatomy of Breakthroughs LaTeX Book
# Usage: make [all|clean|pdf|view]

LATEX = pdflatex -interaction=nonstopmode -shell-escape
BIBTEX = bibtex
MAIN = main

# Default target
all: pdf

# Build PDF (requires 3 passes for TOC, refs, bibliography)
pdf: $(MAIN).pdf

$(MAIN).pdf: $(MAIN).tex chapters/*.tex references.bib
	-$(LATEX) $(MAIN).tex
	-$(BIBTEX) $(MAIN)
	-$(LATEX) $(MAIN).tex
	-$(LATEX) $(MAIN).tex
	@echo "Build complete. Pages: $$(pdfinfo $(MAIN).pdf 2>/dev/null | grep Pages | awk '{print $$2}')"

# Quick build (2 passes, no bibliography)
quick: $(MAIN).tex chapters/*.tex
	$(LATEX) $(MAIN).tex
	$(LATEX) $(MAIN).tex

# View PDF (macOS)
view: $(MAIN).pdf
	open $(MAIN).pdf

# View PDF (Linux)
view-linux: $(MAIN).pdf
	xdg-open $(MAIN).pdf

# Clean auxiliary files
clean:
	rm -f *.aux *.log *.out *.toc *.lof *.lot *.fls *.fdb_latexmk *.bbl *.blg *.idx *.ilg *.ind
	rm -f chapters/*.aux chapters/*.log chapters/*.out

# Deep clean (including PDF)
distclean: clean
	rm -f $(MAIN).pdf

# Check for common LaTeX issues
check: $(MAIN).pdf
	@echo "=== Checking for undefined references ==="
	@grep -i "reference.*undefined" $(MAIN).log || echo "None found"
	@echo "=== Checking for undefined citations ==="
	@grep -i "citation.*undefined" $(MAIN).log || echo "None found"
	@echo "=== Checking for overfull boxes (>100pt) ==="
	@grep "Overfull.*hbox ([0-9]\\{3,\\}" $(MAIN).log || echo "None found"
	@echo "=== Checking for underfull boxes (badness 10000) ==="
	@grep "Underfull.*vbox (badness 10000)" $(MAIN).log || echo "None found"
	@echo "=== Page count ==="
	@pdfinfo $(MAIN).pdf 2>/dev/null | grep Pages

# Count words (approximate)
wordcount:
	@detex $(MAIN).tex | wc -w

# Spell check (requires aspell)
spell:
	@for f in $(MAIN).tex chapters/*.tex; do \
		echo "Checking $$f..."; \
		aspell -t -c $$f; \
	done

# List all chapters
list-chapters:
	@ls chapters/*.tex | sed 's/chapters\///; s/.tex//'

.PHONY: all pdf quick view view-linux clean distclean check wordcount spell list-chapters