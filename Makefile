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

ui:
	pyuic5 ui/UIDbUpdateForm.ui -o UIDbUpdateForm.py
	pyuic5 ui/UIMainWindowForm.ui -o UIMainWindowForm.py

	pyrcc5 resources.qrc -o resources_rc.py
.PHONY: ui