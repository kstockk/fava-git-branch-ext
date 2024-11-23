"""
Show the current Git branch

Usage: 
YYYY-MM-DD custom "fava-extension" "fava_git_branch_ext"
"""

import os
import subprocess
from fava.ext import FavaExtensionBase

LEDGER_DATA_DIR = os.environ.get('LEDGER_DATA_DIR', '/Ledger')

class GitBranchExtension(FavaExtensionBase):

    report_title = "Source Control"

    def _run_git_command(self, command):
        try:
            result = subprocess.run(
                command,
                cwd=LEDGER_DATA_DIR,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )
            if result.returncode == 0:
                return result.stdout.strip()
            return f"Error: {result.stderr.strip()}"
        except Exception as e:
            return f"Error: {str(e)}"

    def git_branch_name(self):
        return self._run_git_command(["git", "rev-parse", "--abbrev-ref", "HEAD"])

    def get_git_graph(self):
        return self._run_git_command(["git", "log", "--graph", "--oneline", "--all", "--decorate"])

    def get_git_status(self):
        return self._run_git_command(["git", "status"])
