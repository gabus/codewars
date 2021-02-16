# https://www.codewars.com/kata/554e4a2f232cdd87d9000038/train/python

"""
Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions" for the development and functioning of living organisms.
If you want to know more http://en.wikipedia.org/wiki/DNA
In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". You have function with one side of
the DNA (string, except for Haskell); you need to get the other complementary side. DNA strand is never empty or there is no DNA at all (again, except for Haskell).
More similar exercise are found here http://rosalind.info/problems/list-view/ (source)
"""


def DNA_strand(dna: str) -> str:
    for index, _ in enumerate(dna):
        if dna[index] == 'A': dna[index] = 'T'
        if dna[index] == 'T': dna[index] = 'A'
        if dna[index] == 'C': dna[index] = 'G'
        if dna[index] == 'G': dna[index] = 'C'


print('Success' if DNA_strand('AAAA') == 'TTTT' else 'Failed')
