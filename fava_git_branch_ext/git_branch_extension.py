"""
Show the current Git branch

Usage: 
YYYY-MM-DD custom "fava-extension" "fava_git_branch_ext"
"""

import subprocess
from fava.ext import FavaExtensionBase

class GitBranchExtension(FavaExtensionBase):
    
    report_title = "Current Branch"

    def git_branch_name(self):
        """Get the current Git branch name."""
        try:
            result = subprocess.run(
                ["git", "rev-parse", "--abbrev-ref", "HEAD"],
                cwd="/Ledger",  # Path to your git repo
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )
            if result.returncode == 0:
                return result.stdout.strip()
            else:
                return "No branch"
        except Exception as e:
            return f"Error: {str(e)}"
