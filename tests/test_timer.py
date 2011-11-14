
import common
import unittest

import pyuv


class TimerTest(common.UVTestCase):

    def test_timer1(self):
        self.timer_cb_called = 0
        def timer_cb(timer, data):
            self.timer_cb_called += 1
            timer.stop()
            timer.close()
        loop = pyuv.Loop.default_loop()
        timer = pyuv.Timer(loop)
        timer.start(timer_cb, 1, 0)
        loop.run()
        self.assertEqual(self.timer_cb_called, 1)

    def test_timer_never(self):
        self.timer_cb_called = 0
        def timer_cb(timer, data):
            self.timer_cb_called += 1
            timer.stop()
            timer.close()
        loop = pyuv.Loop.default_loop()
        timer = pyuv.Timer(loop)
        timer.start(timer_cb, 1, 0)
        timer.close()
        loop.run()
        self.assertEqual(self.timer_cb_called, 0)

    def test_timer_ref1(self):
        self.timer_cb_called = 0
        def timer_cb(timer, data):
            self.timer_cb_called += 1
            timer.stop()
            timer.close()
        loop = pyuv.Loop.default_loop()
        timer = pyuv.Timer(loop)
        loop.unref()
        loop.run()
        # When timer is destroyed it will unref the loop again, so loop.run() would block next time
        loop.ref()
        self.assertEqual(self.timer_cb_called, 0)

    def test_timer_ref2(self):
        self.timer_cb_called = 0
        def timer_cb(timer, data):
            self.timer_cb_called += 1
            timer.stop()
            timer.close()
        loop = pyuv.Loop.default_loop()
        timer = pyuv.Timer(loop)
        timer.start(timer_cb, 1, 0)
        loop.unref()
        loop.run()
        # When timer is destroyed it will unref the loop again, so loop.run() would block next time
        loop.ref()
        self.assertEqual(self.timer_cb_called, 0)


if __name__ == '__main__':
    unittest.main()
