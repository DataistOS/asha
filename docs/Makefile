# Variables for Sphinx build
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = build

.PHONY: help Makefile build-all

# Standard Sphinx target
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

# Build HTML and EPUB, PDF process is commented out to prevent errors
build-all:
	@echo "--- Generating HTML, EPUB, and PDF (PDF currently disabled) ---"
	rm -rf $(BUILDDIR)/*
	$(SPHINXBUILD) -b html "$(SOURCEDIR)" "$(BUILDDIR)/html"
	$(SPHINXBUILD) -b epub "$(SOURCEDIR)" "$(BUILDDIR)/epub"
	
	# PDF build process is commented out:
	# $(SPHINXBUILD) -b latex "$(SOURCEDIR)" "$(BUILDDIR)/latex"
	# @echo "--- Compiling LaTeX to PDF ---"
	# cd "$(BUILDDIR)/latex" && xelatex -interaction=nonstopmode *.tex && xelatex -interaction=nonstopmode *.tex
	
	@echo "ALL BUILDS COMPLETED SUCCESSFULLY!"