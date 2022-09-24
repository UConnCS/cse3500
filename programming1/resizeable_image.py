import imagematrix

class ResizeableImage(imagematrix.ImageMatrix):
    def best_seam(self, dp=True):
        if dp == True:
            return self.dp_seam()
        else:
            return self.naive_seam()

    def dp_seam(self):
        coord = []
        dp = [[0 for i in range(self.width)] for j in range(self.height)]

        for i in range(self.height):
            for j in range(self.width):
                if i == 0:
                    dp[i][j] = self.energy(j, i)
                else:
                    if j == 0:
                        dp[i][j] = min(dp[i-1][j], dp[i-1][j+1]
                                       ) + self.energy(j, i)
                    elif j == self.width - 1:
                        dp[i][j] = min(dp[i-1][j-1], dp[i-1]
                                       [j]) + self.energy(j, i)
                    else:
                        dp[i][j] = min(dp[i-1][j-1], dp[i-1][j],
                                       dp[i-1][j+1]) + self.energy(j, i)
        
        min_val = min(dp[self.height-1])
        min_index = dp[self.height-1].index(min_val)
        coord.append((min_index, self.height-1))

        for i in range(self.height-2, -1, -1):
            if min_index == 0:
                if dp[i][min_index] < dp[i][min_index+1]:
                    coord.append((min_index, i))
                else:
                    min_index += 1
                    coord.append((min_index, i))
            elif min_index == self.width - 1:
                if dp[i][min_index] < dp[i][min_index-1]:
                    coord.append((min_index, i))
                else:
                    min_index -= 1
                    coord.append((min_index, i))
            else:
                if dp[i][min_index] < dp[i][min_index-1] and dp[i][min_index] < dp[i][min_index+1]:
                    coord.append((min_index, i))
                elif dp[i][min_index-1] < dp[i][min_index+1]:
                    min_index -= 1
                    coord.append((min_index, i))
                else:
                    min_index += 1
                    coord.append((min_index, i))
        return coord

    def naive_seam(self):
        coord = []
        min_val = float('inf')

        for i in range(self.width):
            val = self.energy(i, 0)
            if val < min_val:
                min_val = val
                min_index = i
        
        coord.append((min_index, 0))
        
        for i in range(1, self.height):
            if min_index == 0:
                if self.energy(min_index, i) < self.energy(min_index+1, i):
                    coord.append((min_index, i))
                else:
                    min_index += 1
                    coord.append((min_index, i))
            elif min_index == self.width - 1:
                if self.energy(min_index, i) < self.energy(min_index-1, i):
                    coord.append((min_index, i))
                else:
                    min_index -= 1
                    coord.append((min_index, i))
            else:
                if self.energy(min_index, i) < self.energy(min_index-1, i) and self.energy(min_index, i) < self.energy(min_index+1, i):
                    coord.append((min_index, i))
                elif self.energy(min_index-1, i) < self.energy(min_index+1, i):
                    min_index -= 1
                    coord.append((min_index, i))
                else:
                    min_index += 1
                    coord.append((min_index, i))

        return coord

    def remove_best_seam(self):
        self.remove_seam(self.best_seam())