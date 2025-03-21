# -*- coding:utf-8 -*-
"""
作者：Zhakx
日期：2025年03月21日
"""
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)  # 行数（长度）
        cols = len(obstacleGrid[0]) # 列数（宽度）
        matrix = [[0] * cols for _ in range(rows)]
        for i in range(cols):
            if obstacleGrid[0][i]:
                break
            else:
                matrix[0][i] = 1
        for j in range(rows):
            if obstacleGrid[j][0]:
                break
            else:
                matrix[j][0] = 1
        for q in range(1, rows):
            for k in range(1, cols):
                if obstacleGrid[q][k]:
                    matrix[q][k] = 0
                else:
                    matrix[q][k] = matrix[q - 1][k] + matrix[q][k - 1]
        return matrix[rows - 1][cols - 1]

# 初始化：如果第一行的某个地方有障碍，那第一行后面的格子全是0，第一列同理
# 递推公式：如果某个位置有障碍，那这个位置直接设置为0，如果没障碍，那么这一个格子的值的递推关系和62题一样