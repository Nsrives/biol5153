#! /usr/bin/env python3
wall_time = 72

print("#!/bin/bash")

print("#SBATCH --job-name=test")
print("#SBATCH --partition condo")
print("#SBATCH --nodes=1")
print("#SBATCH --qos condo")
print("#SBATCH --tasks-per-node=16")
print('#SBATCH --time=' + (str(wall_time)) + ':00:00')
print("#SBATCH -o example_%j.out")
print("#SBATCH -e example_%j.err")
print("#SBATCH --mail-type=ALL")
print("#SBATCH --mail-user=email@uark.edu")
print("#SBATCH --constraint 'xz036'")

print("module purge")
print("module load intel/18.0.1 impi/18.0.1 mkl/18.0.1")

print("cd $SLURM_SUBMIT_DIR")

print("# job command here")
