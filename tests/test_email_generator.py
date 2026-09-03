"""
Test suite for Email Generator
"""

import pytest
from email_generator import EmailGenerator


class TestEmailGenerator:
    """Tests for EmailGenerator class"""
    
    @pytest.fixture
    def generator(self):
        """Create a generator instance for testing"""
        return EmailGenerator()
    
    def test_create_email(self, generator):
        """Test basic email creation"""
        email = generator.create_email(
            recipient="test@example.com",
            subject="Test Subject",
            context="Test context"
        )
        assert email is not None
        assert "test@example.com" in email or "Test Subject" in email
    
    def test_create_email_with_tone(self, generator):
        """Test email creation with different tones"""
        tones = ["professional", "casual", "formal"]
        for tone in tones:
            email = generator.create_email(
                recipient="user@example.com",
                subject="Subject",
                context="Context",
                tone=tone
            )
            assert email is not None
    
    def test_email_contains_recipient(self, generator):
        """Test that email contains recipient information"""
        email = generator.create_email(
            recipient="John Doe",
            subject="Meeting",
            context="Discuss project"
        )
        assert "John" in email or "recipient" in email.lower()


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
