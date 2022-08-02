#===============================================================================
# Copyright 2021 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#===============================================================================

import re
import sys
import subprocess
from datetime import datetime
from subprocess import Popen, PIPE
from utils import make_report
import argparse
import os

try:
    import daal4py
except:
    raise Exception('daal4py is not installed')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Script to make scikit-learn conformance report'
                                     'based on tests for different device types')
    parser.add_argument('-d', '--device', type=str, help='device name', choices=['host', 'cpu', 'gpu'])
    parser.add_argument('-f', '--consider_fails',
                        help='Exclude failed tests from conformance calculation', action="store_true")
    args = parser.parse_args()

    os.environ['SKLEARNEX_VERBOSE'] = 'INFO'

    algs_filename = "algorithms.txt"
    report_filename = f"report_{args.device}.html"

    with open(algs_filename, "r") as file_algs:
        algs = file_algs.read().split("\n")
    algs.remove("")

    print("Confromance testing start")
    for alg_name in algs:
        if code := subprocess.call(
            ["./download_tests.sh", "--alg-name", f"{alg_name}"]
        ):
            raise Exception('Error while copying test files')
        print(alg_name)

        with open(f"_log_{alg_name}.txt", "w") as alg_log:
            subprocess.call(
                [
                    "python",
                    "-m",
                    "sklearnex",
                    "run_tests_with_context.py",
                    f"-a{alg_name}",
                    f"-d{args.device}",
                ],
                stdout=alg_log,
            )

    make_report(algs_filename=algs_filename,
                report_filename = report_filename,
                device=args.device,
                consider_fails=args.consider_fails)
