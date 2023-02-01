#!/bin/bash
# The above line is used to instruct the operating system to use bash as
# a command interpreter

# Activate the virtual environment
. /automation/automation_venv/bin/activate

# Set environment variables for the Oracle client
# References:
# https://docs.oracle.com/en/database/oracle/oracle-database/18/spucd/step-2-set-operating-system-environment-variables.html#GUID-ED528602-A8AC-4FCC-AA55-A36277A66A23
# https://stackoverflow.com/questions/58864378/setting-environment-variables-in-linux-using-python-for-oracle
export ORACLE_HOME=/orasrc/product/19.3
export LD_LIBRARY_PATH=$ORACLE_HOME/lib:$LD_LIBRARY_PATH

# Execute the Python googleAnalytics
python /home/ITAutomation/gawad/ci-capacity-etl/ci_capacity_etl/
