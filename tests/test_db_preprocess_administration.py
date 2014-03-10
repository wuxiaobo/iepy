from unittest import TestCase

from iepy.models import PreProcessSteps
from factories import IEDocFactory


class TestDocumentsPreprocessMetadata(TestCase):

    def test_preprocess_steps(self):
        self.assertEqual(
            [p.name for p in PreProcessSteps],
            ['tokenization', 'segmentation', 'tagging', 'nerc'])

    def test_just_created_document_has_no_preprocess_done(self):
        doc = IEDocFactory()
        for step in PreProcessSteps:
            self.assertFalse(doc.was_preprocess_done(step))

    def test_get_preprocess_result_when_not_done_gives_nothing(self):
        doc = IEDocFactory()
        for step in PreProcessSteps:
            self.assertIsNone(doc.get_preprocess_result(step))

    def test_setting_tokenization_result_can_be_later_retrieved(self):
        doc = IEDocFactory()
        pathetic_tkns = doc.text.split()
        step = PreProcessSteps.tokenization
        doc.set_preprocess_result(step, pathetic_tkns)
        self.assertTrue(doc.was_preprocess_done(step))
        self.assertEqual(doc.get_preprocess_result(step), pathetic_tkns)

    def test_setting_segmentation_result_can_be_later_retrieved(self):
        doc = IEDocFactory(text='Some sentence. And some other. Indeed!')
        pathetic_segments = map(lambda s: s.strip(), doc.text.split('.'))
        step = PreProcessSteps.segmentation
        doc.set_preprocess_result(step, pathetic_segments)
        self.assertTrue(doc.was_preprocess_done(step))
        self.assertEqual(doc.get_preprocess_result(step), pathetic_segments)

    def test_setting_tagging_result_can_be_later_retrieved(self):
        doc = IEDocFactory(text='Some sentence. And some other. Indeed!')
        pathetic_tags = ['NN' for token in doc.text.split()]
        step = PreProcessSteps.tagging
        doc.set_preprocess_result(step, pathetic_tags)
        self.assertTrue(doc.was_preprocess_done(step))
        self.assertEqual(doc.get_preprocess_result(step), pathetic_tags)


class TestDocumentsFiltersForPreprocess(TestCase):

    def test_raw_documents_are_filtered(self):
        doc1 = IEDocFactory(text='')
        doc2 = IEDocFactory(text='')
        doc3 = IEDocFactory(text='')
        doc1.save()


    def get_documents_lacking_preprocess(self):
        pass
