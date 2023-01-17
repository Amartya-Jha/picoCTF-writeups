# Glory of the Garden

## Problem Statement

This [garden](https://jupiter.challenges.picoctf.org/static/d0e1ffb10fc0017c6a82c57900f3ffe3/garden.jpg) contains more than it seems.

## Type

Forensics

## Hints

1. What is a hex editor?

## Approach

1. Opened the image in a hex editor, all the static values seemed alright. Then tried changing the width of the image, but still got nothing.

2. ran `string garden.jpg | grep pico` on the image and got the flag

## Flag

picoCTF{more_than_m33ts_the_3y3eBdBd2cc}