#!/usr/bin/env python3

import atheris
import sys
import os
import numpy as np

with atheris.instrument_imports():
    from zeus.moves import DifferentialMove
    

def TestOneInput(input):
    fdp = atheris.FuzzedDataProvider(input)
    try:
        move = DifferentialMove()
        nwalkers = fdp.ConsumeIntInRange(1, 4096)
        ndim = fdp.ConsumeIntInRange(1, 4096)
        X = np.array([[fdp.ConsumeIntInRange(1, 4096) for _ in range(ndim)] for _ in range(nwalkers // 2)])
        mu = fdp.ConsumeFloat()
        
        directions, tune = move.get_direction(X, mu)
    except Exception:
        return
    
def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()
    

if __name__ == "__main__":
    main()