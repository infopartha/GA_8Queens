import unittest
import nQueens_GA as nQueen


class test_NQueens_GA(unittest.TestCase):
    
    test_qn = nQueen.NQueens_GA(8, False)
    
    def test_init_population(self):
        self.test_qn.init_population()
        self.assertLessEqual(len(self.test_qn.population), 100)
        self.test_qn.init_population(200)
        self.assertLessEqual(len(self.test_qn.population), 200)
    
    def test_fitness_score(self):
        self.assertEqual(self.test_qn.fitness_score([3, 4, 7, 1, 6, 5, 0, 2]), (0.90625, [7, 7, 7, 8, 7, 7, 8, 7]))
        self.assertEqual(self.test_qn.fitness_score([2, 0, 6, 4, 7, 1, 3, 5]), (1, [8, 8, 8, 8, 8, 8, 8, 8]))
    
    def test_goal_check(self):
        self.assertEqual(self.test_qn.goal_check([3, 4, 7, 1, 6, 5, 0, 2]), False)
        self.assertEqual(self.test_qn.goal_check([2, 0, 6, 4, 7, 1, 3, 5]), True)
    
    def test_crossover(self):
        self.assertEqual(self.test_qn.crossover([6, 2, 5, 1, 4, 7, 0, 3], [4, 6, 7, 3, 1, 0, 2, 5]), [4, 2, 5, 1, 4, 7, 2, 3])
        self.assertEqual(self.test_qn.crossover([1, 7, 3, 6, 4, 2, 0, 5], [4, 0, 5, 6, 2, 7, 3, 1]), [4, 0, 3, 6, 2, 7, 0, 5])
    
    def test_mutate(self):
        self.assertEqual(self.test_qn.mutate([4, 2, 5, 1, 4, 7, 2, 3]), [6, 0, 5, 1, 4, 7, 2, 3])
        self.assertEqual(self.test_qn.mutate([4, 4, 7, 6, 1, 3, 5, 0]), [2, 4, 7, 6, 1, 3, 5, 0])
    
if __name__ == '__main__':
    unittest.main()