#!/usr/bin/expect

# Bash script to submit SLURM batch script batch_sub.sh
# on the UCI HPC3 cluster

read -p "Username: " username
read -sp "Password: "password

spawn sshpass -p $password ssh -Y $username@hpc.oit.uci.edu

expect "$ " {send "cd MG5_aMC_v2_7_3/4e1a_bkg/"}
expect "$ " {send "./batch_sub.sh"}
expect "$ " {send "exit\r"}

/bin/bash -c "echo "yes""
