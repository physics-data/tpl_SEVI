.PHONY: all

all: VelocityImage_1.h5 VelocityImage_2.h5 VelocityImage_3.h5 VelocityImage_4.h5

VelocityImage_%.h5:
	@echo python sevi_simulate.py $* $@

.PHONY: clean

clean:
	rm -rf *.h5 *.png *.gif

# Delete partial files when the processes are killed.
.DELETE_ON_ERROR:
# Keep intermediate files around
.SECONDARY:
