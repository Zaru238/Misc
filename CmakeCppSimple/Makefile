#! /usr/bin/make -f

.DEFAULT_GOAL := run

bin_dir := _build

program: | $(bin_dir)
	cmake -B$(bin_dir)
	make -C $(bin_dir) simple_project

$(bin_dir):
	mkdir -p $(bin_dir)

all: program

run: program
	$(bin_dir)/simple_project

clean:
	rm -rf $(bin_dir)

.PHONY: clean program testrunner all test
