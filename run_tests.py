# ============================================================
# run_tests.py - Test Runner Script
# ============================================================
import os
import sys
import subprocess
import argparse
from datetime import datetime


def run_tests(args):

    print("=" * 70)

    print("ENTERPRISE SELENIUM PYTHON AUTOMATION FRAMEWORK")

    print(
        f"Execution Started: "
        f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    )

    print(f"Environment : {args.env}")

    print(f"Browser     : {args.browser}")

    print(f"Suite       : {args.suite}")

    print(f"Headless    : {args.headless}")

    print("=" * 70)

    cmd = ["pytest"]

    cmd.extend(["-v", "--tb=short"])

    cmd.extend([f"--browser={args.browser}"])

    cmd.extend([f"--env={args.env}"])

    cmd.extend([f"--headless={args.headless}"])

    if args.suite == "smoke":

        cmd.extend(["-m", "smoke"])

    elif args.suite == "regression":

        cmd.extend(["-m", "regression"])

    elif args.suite == "sanity":

        cmd.extend(["-m", "sanity"])

    elif args.suite == "e2e":

        cmd.extend(["-m", "e2e"])

    elif args.suite == "login":

        cmd.extend(["tests/login/"])

    elif args.suite == "product":

        cmd.extend(["tests/product/"])

    elif args.suite == "cart":

        cmd.extend(["tests/cart/"])

    elif args.suite == "checkout":

        cmd.extend(["tests/checkout/"])

    elif args.suite == "contact":

        cmd.extend(["tests/contact/"])

    if args.parallel:

        cmd.extend(["-n", str(args.workers)])

    cmd.extend([
        "--html=reports/report.html",
        "--self-contained-html"
    ])

    cmd.extend([
        "--alluredir=allure-results"
    ])

    if args.retries > 0:

        cmd.extend([
            f"--reruns={args.retries}"
        ])

    print("\nExecuting Command:\n")

    print(" ".join(cmd))

    print("\n" + "=" * 70)

    result = subprocess.run(
        cmd,
        cwd=os.path.dirname(__file__)
    )

    print("=" * 70)

    print(
        f"Execution Finished: "
        f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    )

    print(f"Exit Code: {result.returncode}")

    print("=" * 70)

    return result.returncode


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Run Automation Tests"
    )

    parser.add_argument(
        "--browser",
        default="chrome",
        choices=["chrome", "firefox", "edge"],
        help="Browser to run tests"
    )

    parser.add_argument(
        "--env",
        default="qa",
        choices=["qa", "staging", "production"],
        help="Environment to execute tests"
    )

    parser.add_argument(
        "--suite",
        default="all",
        choices=[
            "all",
            "smoke",
            "regression",
            "sanity",
            "e2e",
            "login",
            "product",
            "cart",
            "checkout",
            "contact"
        ],
        help="Test suite to execute"
    )

    parser.add_argument(
        "--headless",
        default="false",
        choices=["true", "false"],
        help="Run browser in headless mode"
    )

    parser.add_argument(
        "--parallel",
        action="store_true",
        help="Enable parallel execution"
    )

    parser.add_argument(
        "--workers",
        default=3,
        type=int,
        help="Number of parallel workers"
    )

    parser.add_argument(
        "--retries",
        default=1,
        type=int,
        help="Retry failed tests"
    )

    args = parser.parse_args()

    exit_code = run_tests(args)

    sys.exit(exit_code)