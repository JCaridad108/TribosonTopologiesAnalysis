#!/bin/bash

# Bash script to recieve background Monte Carlo via scp
# from the UCI HPC3 cluster

read -p "Username: " username
read -sp "Password: " password

sshpass -p $password scp $username@hpc3.rcic.uci.edu:/pub/$username/MG5_aMC_v2_9_2/2e2j1a_bkg/Events/test1/tag_1_delphes_events.root ~/Desktop/bkg_1

sshpass -p $password scp $username@hpc3.rcic.uci.edu:/pub/$username/MG5_aMC_v2_9_2/2e2j1a_bkg/Events/test1/tag_1_xs.txt ~/Desktop/bkg_1

sshpass -p $password scp $username@hpc3.rcic.uci.edu:/pub/$username/MG5_aMC_v2_9_2/2e2j1a_bkg/Events/test1/tag_2_delphes_events.root ~/Desktop/bkg_1

sshpass -p $password scp $username@hpc3.rcic.uci.edu:/pub/$username/MG5_aMC_v2_9_2/2e2j1a_bkg/Events/test1/tag_2_xs.txt ~/Desktop/bkg_1

sshpass -p $password scp $username@hpc3.rcic.uci.edu:/pub/$username/MG5_aMC_v2_9_2/2e2j1a_bkg/Events/test1/tag_3_delphes_events.root ~/Desktop/bkg_1

sshpass -p $password scp $username@hpc3.rcic.uci.edu:/pub/$username/MG5_aMC_v2_9_2/2e2j1a_bkg/Events/test1/tag_3_xs.txt ~/Desktop/bkg_1

