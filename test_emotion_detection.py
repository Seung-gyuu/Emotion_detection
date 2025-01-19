import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detection(self):

        r_1 = emotion_detector("I am glad this happened")
        self.assertEqual(r_1['dominant_emotion'], "joy")

        r_2 = emotion_detector("I am really mad about this")
        self.assertEqual(r_2['dominant_emotion'], "anger")

        r_3 = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(r_3['dominant_emotion'], "disgust")

        r_4 = emotion_detector("I am so sad about this")
        self.assertEqual(r_4['dominant_emotion'], "sadness")

        r_5 = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(r_5['dominant_emotion'], "fear")


unittest.main()
