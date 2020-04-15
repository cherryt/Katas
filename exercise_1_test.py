import pytest


from exercise_1 import Stack, PopEmptyStackException 


class TestStack:

    def test_push_once(self):
        stack = Stack()
        stack.push(1)

        assert len(stack) == 1

    def test_push_many_times(self):
        stack = self._create_stack_wth_multiple_items(1, 2)

        assert len(stack) == 2

    def _create_stack_wth_multiple_items(self, *args):
        stack = Stack()
        for item in args:
            stack.push(item)
        return stack
    
    def test_push_many_same_items(self):
        stack = self._create_stack_wth_multiple_items(1, 1)

        assert len(stack) == 2
    
    def test_pop_empty(self):
        stack = Stack()

        with pytest.raises(PopEmptyStackException):
            stack.pop()

    def test_pop_item(self):
        stack = self._create_stack_wth_multiple_items(1, 2)
        
        stack.pop()

        assert len(stack) == 1
