# Magikarp Ground Mission

## Problem Statement

Do you know how to move between directories and read files in the shell? Start the container, `ssh` to it, and then `ls` once connected to begin. Login via `ssh` as `ctf-player` with the password, `6d448c9c`

## Type

General Skills

## Hints


## Approach

On connecting the given service, we run `ls` and see the there flag1/3 and and instructions for 2/3.
navigating to the root dir using `cd /` we get our flag 2/3 and instructions for 3/3 which is in home. Which we get by `cd ~` and our flag is complete

## Flag

picoCTF{xxsh_0ut_0f_\/\/4t3r_5190b070}