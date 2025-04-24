## Exercise 8: Dictionary learning and source separation
This repository contains the Python scripts compiled to address problem 5 from Exercise 8: ICA as source separation on audio, for the DTU Fall 2024 course 02741: Machine learning for signal processing.

## Project Contributers
<ul>
  <li>Tommy Sonne Alstrøm (course responsible) + staff</li>
  <li>Enrico Leonardi (student - 222721)</li>
</ul>

## Abstract:
In this problem we worked on a set of mixed audio recordings which have been created using instantaneous mixing. The audio file contains two channels. Two Python scripts are included:
<ol type="I">
  <li>Main script, loading the audio files and calling the ICA function</li>
  <li>ICA function definition and model's weights update implementation</li>
</ol>

## Data
The employed scripts have been primarily developed by the course staff. The students were called to individually complete a few significant lines of code as a last step, in order to apply the formulas discussed in class.

## Goal
The Exercise belongs to week 8 class, focused on dictionary learning and source separation. Specifically, several dictionary learning-based algorithms have been discussed, while only Independent Component Analysis being applied in the exercise. The objective of the exercise has been understanding the derivation behind ICA, and applying the algorithm as a source separation technique. The course provided us students with knowledge of:
<ol type="a">
  <li>Fundamental and widely applied signal processing methods;</li>
  <li>Matlab or Python as a tool for the development of signal processing algorithms;</li>
  <li>how to derive and construct a modern signal processing system based on machine learning.</li>
</ol>

## Usage
The suggested means of usage of the provided material is running the main Python ```ex8_5.py``` script. By loading the mixture_instantaneous.wav audio file, two audio files (```ica_source_1.wav``` and ```ica_source_2.wav```) will be produced, demonstrating how ICA model is effective within separation of sources that are statistically independent.

## Conclusion
Machine learning is becoming an indispensable tool for communication engineers. However, as the field of machine learning is broad, identifying a set of relevant tools for solving a specific set of problems may be challenging. <br/><br/> Specifically for this assignment, machine learning ICA model have been implemented. Moreover, it has been successfully shown how a set of mixed audio recordings - created using instantaneous mixing - can be split into its statistically independent audio sources.
