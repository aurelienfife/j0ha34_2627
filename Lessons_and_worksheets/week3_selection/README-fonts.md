# Building the OpenDyslexic handouts

Keep both `.tex` files alongside the `fonts` directory. Run `pdflatex week3_theory.tex` or `pdflatex week3_exercises.tex` from this directory, twice. No system font installation or shell-escape option is required.

Body text uses the outlines of OpenDyslexic Regular, Bold, Italic and BoldItalic; code uses OpenDyslexic Mono Regular. Code emphasis uses colour rather than a substituted bold font. The layout uses 12-point body text, increased line spacing, left alignment and no automatic prose hyphenation.

The bundled Type 1 fonts were converted from the locally installed OpenDyslexic OpenType fonts with LCDF Typetools for pdfTeX compatibility. Their internal font names are changed to HandoutAccessible to distinguish these format conversions from the original fonts and respect reserved font names. The letter shapes have not been redesigned. Original author attribution and licence information are included in `fonts/*-LICENSE.txt`.

Keep the font-support files with the sources when sharing or uploading to a LaTeX editor. The existing PDFs are not replaced by these source changes; compile the sources to produce the new layout.
