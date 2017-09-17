# -*- coding: utf-8 -*-

import sys
from pdfrw import PdfReader, PdfWriter


def input():
	try:
		inputs = sys.argv[1]
		pdf = PdfReader(inputs)
		return pdf
	except IndexError:
		print "Please input a pdf file"
		print "usage: process_for_printer.py <your_file.pdf>"


def main():
	pages = input().pages
	# output_even = PdfWriter().addpage([p for p in pages[0:][::2]])
	# output_odd = PdfWriter().addpage([p for p in pages[1:][::2]])
	output_even = PdfWriter()
	for p in pages[0:][::2]:
		output_even.addpage(p)

	output_odd = PdfWriter()
	for p in pages[1:][::2]:
		output_odd.addpage(p)
	inputs = sys.argv[1]
	output_even.write(inputs.replace(".pdf", "_EVEN.pdf"))
	output_odd.write(inputs.replace(".pdf", "_ODD.pdf"))

if __name__ == '__main__':
	main()