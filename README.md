# VigenereFreidmanAttack
A python implementation of the Freidman attack on the vignere cipher.
The default keylength is set to 36.

The program will:
1. Clean & normalize the cipher text.
2. Split the ciphertext into n streams.
3. Perform chi-square analysis on each possible caesar shift for every stream.
4. Return the most probable plaintext, by reassemebling shifted streams that posses the most english-like letter frequency.

Limitations:
Requires knowledge of a probable keylength.
Cipher texts of small size or very large keylength will not reliably be vulnerable to statistical analysis.

More information:
https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher
https://en.wikipedia.org/wiki/Chi-squared_test


