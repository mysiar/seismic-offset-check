SHELL := /bin/bash

build:
	rm -rf ./build ./dist
	pyinstaller main.py -n OffsetCheck --windowed
	cp -r icons/ dist/OffsetCheck
	cd dist; \
	tar zcvf ../dist-out/OffsetCheck-linux.tgz OffsetCheck/; \
	cd ..
.PHONY: build
