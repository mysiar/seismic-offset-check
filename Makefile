SHELL := /bin/bash

GIT_TAG = $(shell git describe --tags)

build:
	rm -rf ./build ./dist
	pyinstaller main.py -n OffsetCheck --windowed
	cp -r icons/ dist/OffsetCheck
	cd dist; \
	tar zcvf ../dist-out/OffsetCheck-"${GIT_TAG}".linux.tgz OffsetCheck/; \
	cd ..
.PHONY: build

var:
	echo