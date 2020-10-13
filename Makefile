SHELL := /bin/bash

GIT_TAG = $(shell git describe --tags)

ui:
	pyuic5 ui/UIDbUpdateForm.ui -o UIDbUpdateForm.py
	pyuic5 ui/UIMainWindowForm.ui -o UIMainWindowForm.py
	pyuic5 ui/UIWarning.ui -o UIWarning.py

	pyrcc5 resources.qrc -o resources_rc.py
.PHONY: ui

build:
	rm -rf ./build ./dist
	pyinstaller main.py -n OffsetCheck --windowed
	mkdir -p dist/OffsetCheck/icons
	cp -r icons/vibrator-48.png dist/OffsetCheck/icons
	#cp -r icons/ dist/OffsetCheck
	cd dist; \
	tar zcvf ../dist-out/OffsetCheck-"${GIT_TAG}".linux.tgz OffsetCheck/; \
	cd ..
	@echo "TAG: ${GIT_TAG}"
.PHONY: build

build-osx:
	@echo "TAG: ${GIT_TAG}"
	@echo "Not implemented yet"
.PHONY: build-osx