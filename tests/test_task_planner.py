"""
Test suite for Task Planner
"""

import pytest
from task_planner import TaskPlanner


class TestTaskPlanner:
    """Tests for TaskPlanner class"""
    
    @pytest.fixture
    def planner(self):
        """Create a planner instance for testing"""
        return TaskPlanner()
    
    def test_create_plan(self, planner):
        """Test task plan creation"""
        tasks = ["Research", "Design", "Development"]
        plan = planner.create_plan(
            tasks=tasks,
            deadline="2026-09-30",
            priority="high"
        )
        
        assert plan is not None
        assert 'tasks' in plan
        assert 'sequencing' in plan
        assert 'timeline' in plan
    
    def test_prioritize_tasks(self, planner):
        """Test task prioritization"""
        tasks = [
            "Urgent task",
            "Important task",
            "Low priority task",
            "Quick task"
        ]
        
        prioritized = planner.prioritize_tasks(tasks)
        
        assert prioritized is not None
        assert len(prioritized) == len(tasks)
    
    def test_estimate_effort(self, planner):
        """Test effort estimation"""
        task_desc = "Build a new user authentication system"
        
        estimate = planner.estimate_effort(task_desc)
        
        assert estimate is not None
        # Should contain effort metrics
        assert isinstance(estimate, (dict, str))


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
