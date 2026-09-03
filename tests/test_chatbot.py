"""
Test suite for Chatbot
"""

import pytest
from chatbot import ProductivityChatbot


class TestProductivityChatbot:
    """Tests for ProductivityChatbot class"""
    
    @pytest.fixture
    def chatbot(self):
        """Create a chatbot instance for testing"""
        return ProductivityChatbot()
    
    def test_chat_response(self, chatbot):
        """Test basic chatbot response"""
        response = chatbot.chat("What can you help me with?")
        
        assert response is not None
        assert isinstance(response, str)
        assert len(response) > 0
    
    def test_conversation_history(self, chatbot):
        """Test conversation history tracking"""
        chatbot.chat("First message")
        chatbot.chat("Second message")
        
        history = chatbot.get_conversation_history()
        
        assert len(history) >= 4  # 2 user messages + 2 bot responses
        assert history[0]['role'] == 'user'
        assert history[1]['role'] == 'assistant'
    
    def test_reset_conversation(self, chatbot):
        """Test conversation reset"""
        chatbot.chat("Test message")
        assert len(chatbot.get_conversation_history()) > 0
        
        chatbot.reset_conversation()
        
        assert len(chatbot.get_conversation_history()) == 0
    
    def test_context_aware_response(self, chatbot):
        """Test context-aware response generation"""
        response = chatbot.chat(
            "Help me plan my day",
            context="I have 3 meetings and 2 projects to work on"
        )
        
        assert response is not None
        # Response should be aware of context
        assert isinstance(response, str)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
