import unittest, time, functions
from solution import solve


class ScoreListTest(unittest.TestCase):

    def test_time_len(self):
        dur = int(round(time.time() * 1000))

        solve()
        print("hello\n")

        dur = int(round(time.time() * 1000)) - dur
        self.assertEqual(True, dur < 500, '\nابتدا باید تردهای مربوط به هر تابع را start و join کنید و سپس به سراغ تردهای مربوط به تابع بعدی بروید.')