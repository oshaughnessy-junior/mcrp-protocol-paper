# Manuscript rendering

`build_submission.py` invokes Pandoc with the repository bibliography, then the
Typst Python package. It writes a Typst source next to the requested PDF. The
review1587 edition was rendered with Pandoc3.9.0.2 and Typst0.15.0, then inspected
as page images. Fonts and tool versions can affect pagination and output bytes.

```sh
python3 scripts/build_submission.py --output output/verification-lifecycle.pdf
```

Install Pandoc and the Typst Python package in an appropriate environment first.
The script does not install dependencies, read credentials or publish files.
Its table widths are specific to this manuscript and must be visually rechecked
when the document structure changes. Code is MIT licensed (LICENSE).
