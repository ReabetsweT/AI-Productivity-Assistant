"""
Test suite for Meeting Summarizer
"""

import pytest
from meeting_summarizer import MeetingSummarizer


class TestMeetingSummarizer:
    """Tests for MeetingSummarizer class"""
    
    @pytest.fixture
    def summarizer(self):
        """Create a summarizer instance for testing"""
        return MeetingSummarizer()
    
    @pytest.fixture
    def sample_transcript(self):
        """Sample meeting transcript"""
        return """
        Manager: Welcome everyone to the Q3 review.
        Developer 1: We completed the API development.
        Developer 2: Frontend is almost done.
        Manager: Great! Let's schedule testing for next week.
        QA Lead: I'll coordinate the testing schedule.
        """
    
    def test_summarize(self, summarizer, sample_transcript):
        """Test meeting summarization"""
        summary = summarizer.summarize(sample_transcript)
        
        assert summary is not None
        assert 'summary' in summary
        assert 'key_points' in summary
        assert 'action_items' in summary
    
    def test_extract_action_items(self, summarizer, sample_transcript):
        """Test action item extraction"""
        action_items = summarizer.extract_action_items(sample_transcript)
        
        assert action_items is not None
        assert isinstance(action_items, (list, dict))
    
    def test_generate_meeting_minutes(self, summarizer, sample_transcript):
        """Test meeting minutes generation"""
        attendees = ["Manager", "Developer 1", "Developer 2", "QA Lead"]
        minutes = summarizer.generate_meeting_minutes(sample_transcript, attendees)
        
        assert minutes is not None
        # Minutes should contain attendee information
        assert any(attendee in str(minutes).lower() for attendee in [a.lower() for a in attendees])


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
