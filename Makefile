.PHONY: all

all: VelocityImage.h5
# ET-1
VelocityImage.h5:
	python src/sevi_simulate.py -o $@
VelocityImage.pdf: VelocityImage.h5
	python src/read_sim_data.py -i $^ -o $@
# ET-2
SingleGain.h5:
	python src/single_mcp.py -o $@
SingleGain.pdf: SingleGain.h5
	python src/read_single_mcp.py -i $^ -o $@
DualGain.h5: SingleGain.h5
	python src/dual_mcp.py -o $@
DualGain.pdf: DualGain.h5
	python src/read_dual_mcp.py -i $^ -o $@
# ET-3
CCDImage.h5: DualGain.h5
	python src/ccd.py -i $^ -o $@
CCDImage.pdf: VelocityImage.h5 CCDImage.h5
	python src/read_ccd.py -i $^ -o $@

.PHONY: clean

clean:
	rm -rf *.h5 *.png *.gif

# Delete partial files when the processes are killed.
.DELETE_ON_ERROR:
# Keep intermediate files around
.SECONDARY:
