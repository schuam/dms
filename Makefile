# -----------------------------------------------------------------------------
# The install target is supposed to install copy all scripts into:
# /usr/local/msssc/ and make links to all the scripts in /usr/local/bin/.
# The idea behind it is, that I want to easily be able to see where the
# installed scripts in /usr/local/bin/ come from.
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# variables/constants
# -----------------------------------------------------------------------------

INSTALL_DIR_BASE = /usr/local
INSTALL_DIR_SCRIPTS = $(INSTALL_DIR_BASE)/dms
INSTALL_DIR_BIN = $(INSTALL_DIR_BASE)/bin

SRC_DIR_BASE = ./src

SRC_DIR_BASH = $(SRC_DIR_BASE)/bash
SCRIPTS_BASH = $(wildcard $(SRC_DIR_BASH)/*.sh)

SRC_DIR_PYTHON = $(SRC_DIR_BASE)/python
SCRIPTS_PYTHON = $(wildcard $(SRC_DIR_PYTHON)/*.py)

INSTALLED_SCRIPTS = $(patsubst $(SRC_DIR_BASH)/%.sh, $(INSTALL_DIR_SCRIPTS)/%.sh, $(SCRIPTS_BASH))
INSTALLED_SCRIPTS += $(patsubst $(SRC_DIR_PYTHON)/%.py, $(INSTALL_DIR_SCRIPTS)/%.py, $(SCRIPTS_PYTHON))

SYM_LINKS_BASH = $(patsubst $(SRC_DIR_BASH)/%.sh, $(INSTALL_DIR_BIN)/$(basename %.sh), $(SCRIPTS_BASH))
SYM_LINKS_PYTHON = $(patsubst $(SRC_DIR_PYTHON)/%.py, $(INSTALL_DIR_BIN)/$(basename %.py), $(SCRIPTS_PYTHON))


# -----------------------------------------------------------------------------
# targets
# -----------------------------------------------------------------------------

# Print available targets
.PHONY: help
help: Makefile
	@echo ""
	@echo "The following targets exists:"
	@sed -n "s/^## //p" $<


## install:            Install all scripts and make links
.PHONY: install
install: install_scripts links


## install_scripts:    Install all scripts
.PHONY: install_scripts
install_scripts: $(INSTALLED_SCRIPTS)


# '$(INSTALL_DIR_SCRIPTS/%.sh' matches the items in '$(INSTALLED_SCRIPTS)'
$(INSTALL_DIR_SCRIPTS)/%.sh: $(SRC_DIR_BASH)/%.sh | $(INSTALL_DIR_SCRIPTS)
	cp $< $@


# '$(INSTALL_DIR_SCRIPTS/%.py' matches the items in '$(INSTALLED_SCRIPTS)'
$(INSTALL_DIR_SCRIPTS)/%.py: $(SRC_DIR_PYTHON)/%.py | $(INSTALL_DIR_SCRIPTS)
	cp $< $@


# Installation directory for the scripts
$(INSTALL_DIR_SCRIPTS):
	mkdir -p $@


# Installation directory for the links
$(INSTALL_DIR_BIN):
	mkdir -p $@


## links:              Create links in INSTALL_DIR_BIN directory
.PHONY: links
links: $(SYM_LINKS_BASH) $(SYM_LINKS_PYTHON)


# Creates a link for every installed bash script.
$(SYM_LINKS_BASH): $(INSTALLED_SCRIPTS) | $(INSTALL_DIR_BIN)
	ln -sf $(INSTALL_DIR_SCRIPTS)/$(basename $(notdir $@)).sh $@


# Creates a link for every installed python script.
$(SYM_LINKS_PYTHON): $(INSTALLED_SCRIPTS) | $(INSTALL_DIR_BIN)
	ln -sf $(INSTALL_DIR_SCRIPTS)/$(basename $(notdir $@)).py $@


## uninstall:          Deletes installed scripts.
.PHONY: uninstall
uninstall:
	rm -rf $(INSTALL_DIR_SCRIPTS)
	rm -f $(SYM_LINKS_BASH)
	rm -f $(SYM_LINKS_PYTHON)


# -----------------------------------------------------------------------------
# debug target
# -----------------------------------------------------------------------------

.PHONY: variables
variables:
	@echo INSTALL_DIR_BASE: $(INSTALL_DIR_BASE)
	@echo INSTALL_DIR_SCRIPTS: $(INSTALL_DIR_SCRIPTS)
	@echo INSTALL_DIR_BIN: $(INSTALL_DIR_BIN)
	@echo
	@echo SRC_DIR_BASE: $(SRC_DIR_BASE)
	@echo SRC_DIR_BASH: $(SRC_DIR_BASH)
	@echo SRC_DIR_PYTHON: $(SRC_DIR_PYTHON)
	@echo
	@echo SCRIPTS_BASH: $(SCRIPTS_BASH)
	@echo SCRIPTS_PYTHON: $(SCRIPTS_PYTHON)
	@echo
	@echo INSTALLED_SCRIPTS: $(INSTALLED_SCRIPTS)
	@echo
	@echo SYM_LINKS: $(SYM_LINKS)
