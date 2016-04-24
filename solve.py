#!/usr/bin/env python2.7
import sys
import subprocess
import os
import glob
import ktest
import shlex
import json
import binascii

debug = False

def run_klee(files):
    bc_cmd  = ["clang", "-emit-llvm", "-g", "-c","-o", "target.bc"]
    bc_cmd += files

    exe_cmd  = ["clang", "-L%s"%os.getenv("KLEE_LIB"), "-o", "target"]
    exe_cmd += files
    exe_cmd += ["-lkleeRuntest"]
    try:
        subprocess.check_call(bc_cmd)
        subprocess.check_call(exe_cmd)
    except subprocess.CalledProcessError:
        return
    out = subprocess.check_output(["klee", "target.bc"])
    sys.stderr.write(out)

def get_sym(name):
    case = ktest.KTest.fromfile(name)
    objects = case.objects
    d = {}
    for name, value in objects:
        d[name] = binascii.hexlify(value)
    return d

def replay(name):
    cmd = ["env", "KTEST_FILE=\"%s\"" % name, "./target"]
    cmd = "env KTEST_FILE=\"%s\" ./target" % name
    p = subprocess.Popen(shlex.split(cmd))
    ret = p.wait()
    return ret

if __name__ == '__main__':
    run_klee(sys.argv[1:])
    out = []
    for name in sorted(glob.glob("klee-last/test*.ktest")):
        sym = get_sym(name)
        ret = replay(name)
        out.append({'sym': sym, 'ret': ret})
    print json.dumps(out, indent=4)

