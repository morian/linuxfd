## Specific tools used in this Makefile.
DEBUILD         ?= /usr/bin/debuild
MKDIR           ?= /bin/mkdir
PYTHON          ?= /usr/bin/python
RPMBUILD        ?= /usr/bin/rpmbuild
TAR             ?= /bin/tar


## Environment for package buildings.
PACKAGE_NAME    := python-linuxfd
PACKAGE_SOURCES := source/ COPYING MANIFEST.in README.md setup.py

RPM_BUILD_DIR   := $(CURDIR)/_build
RPM_SOURCE_DIR  := $(RPM_BUILD_DIR)/SOURCES
RPM_TARBALL     := $(RPM_SOURCE_DIR)/$(PACKAGE_NAME).tar.xz
RPM_SPEC_FILE   := $(CURDIR)/centos/$(PACKAGE_NAME).spec
RPM_SOURCES     := $(RPM_TARBALL) $(RPM_SPEC_FILE)


PHONY += all
all: sdist

PHONY += sdist
sdist:
	$(PYTHON) setup.py sdist

PHONY += rpm
rpm: $(RPM_SOURCES)
	$(RPMBUILD) -ba --define "%_topdir $(RPM_BUILD_DIR)" $(RPM_SPEC_FILE)

PHONY += deb
deb:
	$(DEBUILD) -i -us -uc -b

PHONY += clean
clean:
	$(RM) --recursive "$(RPM_BUILD_DIR)"
	$(RM) --recursive dist/ build/


$(RPM_SOURCE_DIR):
	$(MKDIR) --parents "$@"

$(RPM_TARBALL): $(PACKAGE_SOURCES) | $(RPM_SOURCE_DIR)
	$(TAR) --create --xz --file="$(RPM_TARBALL)"         \
	       --transform='flags=r;s,^,$(PACKAGE_NAME)/,'   \
	       $(PACKAGE_SOURCES)

.PHONY: $(PHONY)
