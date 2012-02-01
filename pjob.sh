#!/bin/sh

WDIR=$1
ENV_SCRIPT=$2
REDIR=$3

POINT_FILE=$4

cd $WDIR
POINT=$(awk -v L=$SGE_TASK_ID 'NR==L' $POINT_FILE) 
source $ENV_SCRIPT
./job.py $WDIR $ENV_SCRIPT $REDIR $POINT >& $REDIR
