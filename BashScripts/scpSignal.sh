#!/bin/bash

# Bash script to recieve background Monte Carlo via scp
# from the UCI HPC3 cluster

read -p "Username: " username
read -sp "Password: " password

sshpass -p $password scp $username@hpc3.rcic.uci.edu:/pub/$username/MG5_aMC_v2_9_2/1a4jet_sig/Events/signal1/tag_1_delphes_events.root ~/Desktop/sig
sshpass -p $password scp $username@hpc3.rcic.uci.edu:/pub/$username/MG5_aMC_v2_9_2/1a4jet_sig/Events/signal1/tag_1_xs.txt ~/Desktop/sig

sshpass -p $password scp $username@hpc3.rcic.uci.edu:/pub/$username/MG5_aMC_v2_9_2/1a4jet_sig/Events/signal1/tag_2_delphes_events.root ~/Desktop/sig
sshpass -p $password scp $username@hpc3.rcic.uci.edu:/pub/$username/MG5_aMC_v2_9_2/1a4jet_sig/Events/signal1/tag_2_xs.txt ~/Desktop/sig

sshpass -p $password scp $username@hpc3.rcic.uci.edu:/pub/$username/MG5_aMC_v2_9_2/1a4jet_sig/Events/signal1/tag_3_delphes_events.root ~/Desktop/sig
sshpass -p $password scp $username@hpc3.rcic.uci.edu:/pub/$username/MG5_aMC_v2_9_2/1a4jet_sig/Events/signal1/tag_3_xs.txt ~/Desktop/sig

sshpass -p $password scp $username@hpc3.rcic.uci.edu:/pub/$username/MG5_aMC_v2_9_2/1a4jet_sig/Events/signal1/tag_4_delphes_events.root ~/Desktop/sig
sshpass -p $password scp $username@hpc3.rcic.uci.edu:/pub/$username/MG5_aMC_v2_9_2/1a4jet_sig/Events/signal1/tag_4_xs.txt ~/Desktop/sig
