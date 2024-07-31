# Comprehensive Python Projects README

## Table of Contents

1. [Merge Sort and Inversion Counting Script](#merge-sort-and-inversion-counting-script)
2. [Maximum Number Finder Script](#maximum-number-finder-script)
3. [YouTube Playlist Manager](#youtube-playlist-manager)
4. [Movie Studio Release Schedule Manager](#movie-studio-release-schedule-manager)

## Merge Sort and Inversion Counting Script

### Overview

This script demonstrates an efficient algorithm for counting the number of inversions in an array using a modified version of the merge sort algorithm. An inversion in an array `A` is a pair of indices `(i, j)` such that `i < j` and `A[i] > A[j]`.

### Features

- Utilizes a divide-and-conquer strategy to efficiently sort an array.
- Counts the number of inversions during the merge process.
- Reads arrays of integers from a text file and prints both the array and the count of inversions.

### Usage

Prepare the input file `"Counting_Inversions_input.txt"` with arrays of integers, one array per line. Run the script to read each line, identify the maximum number in the array using the custom algorithm, and print both the array and the found maximum number.

## Maximum Number Finder Script

### Overview

This Python script finds the maximum number in a given array of integers without using built-in Python functions for finding the maximum value. It employs a custom algorithm inspired by binary search principles.

### Features

- Implements a unique algorithm to identify the maximum number in an array.
- Reads input arrays from a file named `"find_largest_number_input.txt"`, where each line contains a separate array of integers.

### Usage

Prepare the input file `"find_largest_number_input.txt"` with arrays of integers, one array per line. Run the script to read each line, identify the maximum number in the array using the custom algorithm, and print both the array and the found maximum number.

## YouTube Playlist Manager

### Overview

This Python script simulates a simplified version of a playlist manager for a hypothetical music streaming platform, akin to YouTube. It allows users to manage playlists, shuffle songs, shorten playlists, and view playlist previews.

### Features

- User authentication system that checks for a username and password match.
- Playlist management features including viewing, shuffling, and shortening playlists.
- Dynamic playlist display showing up to 5 videos at a time, with an option to view more.

### Usage

Run the script and follow the interactive prompts to log in, view playlists, shuffle them, shorten them, or exit the application.

## Movie Studio Release Schedule Manager

### Overview

This script simulates a movie studio release schedule manager. It allows users to manage movies, including adding new movies, scheduling premieres, postponing releases, and viewing summaries of the release schedule.

### Features

- Object-oriented design with classes representing movies, dates, and the release schedule.
- Interactive interface for managing the release schedule, with prompts guiding actions.
- Custom error handling for scenarios where a movie cannot be found or postponed.

### Usage

Run the script and follow the interactive prompts to add movies, schedule premieres, postpone releases, view summaries, or finish managing the schedule.

---
