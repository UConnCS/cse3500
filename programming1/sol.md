## Questions

### What is the recurrence relation for the Seam Carving Horizontal algorithm?

The recurrence relation can be modelled as follows:

$$
\begin{align}
F(i, j) &= min\left(F(i - 1, j - 1), F(i - 1, j), F(i - 1, j + 1)\right) + e(i, j) \\
F(i, 0) &= min\left(F(i - 1, 0), F(i - 1, 1)\right) + e(i, 0) \\
F(i, n - 1) &= min\left(F(i - 1, n - 1), F(i - 1, n - 2)\right) + e(i, n - 1)
\end{align}
$$

where $F(i, j)$ is the minimum energy of the seam at pixel $(i, j)$ and $e(i, j)$ is the energy of pixel $(i, j)$.

### What is the recurrence relation for the Seam Carving Vertical algorithm?

The recurrence relation can be modelled as follows:

$$
\begin{align}
F(i, j) &= min\left(F(i - 1, j - 1), F(i, j - 1), F(i + 1, j - 1)\right) + e(i, j) \\
F(0, j) &= min\left(F(0, j - 1), F(1, j - 1)\right) + e(0, j) \\
F(m - 1, j) &= min\left(F(m - 1, j - 1), F(m - 2, j - 1)\right) + e(m - 1, j)
\end{align}
$$

where $F(i, j)$ is the minimum energy of the seam at pixel $(i, j)$ and $e(i, j)$ is the energy of pixel $(i, j)$.

### How does the Seam Carving algorithm find the seam?

The Seam Carving algorithm finds the seam by starting at the pixel with the minimum energy in the last row of the energy matrix and then backtracking to the first row of the energy matrix by choosing the pixel with the minimum energy that is adjacent to the current pixel.

### How does the Seam Carving algorithm remove the seam?

The Seam Carving algorithm removes the seam by shifting all the pixels to the right of the seam to the left by one pixel.

### How does the